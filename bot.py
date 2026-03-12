import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import requests
import sqlite3

# --- SOZLAMALAR ---
TOKEN = 'SIZNING_BOT_TOKENINGIZNI_SHU_YERGA_YOZING'
ADMIN_ID = 123456789  # O'zingizning Telegram ID raqamingiz
SMM_API_KEY = "SIZNING_SMM_API_KALITINGIZ"
SMM_API_URL = "https://u6182.xvest4.ru/api/"

bot = telebot.TeleBot(TOKEN)

# --- MA'LUMOTLAR BAZASI (SQLite) ---
conn = sqlite3.connect('bot.db', check_same_thread=False)
cursor = conn.cursor()

# Foydalanuvchilar jadvali
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (user_id INTEGER PRIMARY KEY, balance REAL DEFAULT 0, ref_count INTEGER DEFAULT 0)''')
# Sozlamalar jadvali (Narxlar, hamyonlar uchun)
cursor.execute('''CREATE TABLE IF NOT EXISTS settings
                  (key TEXT PRIMARY KEY, value TEXT)''')
conn.commit()

# Standart sozlamalarni bazaga yozish
def init_settings():
    default_settings = {
        "ref_narx": "100", "arzon_narx": "3", "tezkor_narx": "5",
        "click_hamyon": "Kiritilmagan", "qiwi_hamyon": "Kiritilmagan"
    }
    for k, v in default_settings.items():
        cursor.execute("INSERT OR IGNORE INTO settings (key, value) VALUES (?, ?)", (k, v))
    conn.commit()

init_settings()

def get_setting(key):
    cursor.execute("SELECT value FROM settings WHERE key=?", (key,))
    res = cursor.fetchone()
    return res[0] if res else None

# Foydalanuvchini bazaga qoshish yoki olish
def get_user(user_id):
    cursor.execute("SELECT balance, ref_count FROM users WHERE user_id=?", (user_id,))
    user = cursor.fetchone()
    if not user:
        cursor.execute("INSERT INTO users (user_id) VALUES (?)", (user_id,))
        conn.commit()
        return (0, 0)
    return user

# --- TUGMALAR ---
def main_menu(user_id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(KeyboardButton("➕ Buyurtma berish"))
    markup.add(KeyboardButton("💵 Pul ishlash"), KeyboardButton("👔 Kabinet"))
    markup.add(KeyboardButton("📊 Buyurtmani kuzatish"))
    if user_id == ADMIN_ID:
        markup.add(KeyboardButton("👨🏻‍💻 Boshqaruv paneli"))
    return markup

cancel_markup = ReplyKeyboardMarkup(resize_keyboard=True)
cancel_markup.add(KeyboardButton("⬅️ Orqaga"))

# --- ASOSIY FUNKSIYALAR ---

@bot.message_handler(commands=['start'])
def start_command(message):
    user_id = message.from_user.id
    args = message.text.split()
    
    # Referal tizimi
    cursor.execute("SELECT user_id FROM users WHERE user_id=?", (user_id,))
    if not cursor.fetchone():
        if len(args) > 1 and args[1].isdigit():
            inviter_id = int(args[1])
            if inviter_id != user_id:
                ref_narx = float(get_setting('ref_narx'))
                cursor.execute("UPDATE users SET balance = balance + ?, ref_count = ref_count + 1 WHERE user_id=?", (ref_narx, inviter_id))
                conn.commit()
                bot.send_message(inviter_id, f"📳 Sizda yangi taklif mavjud va sizga {ref_narx} UZS berildi!")
        
        cursor.execute("INSERT INTO users (user_id) VALUES (?)", (user_id,))
        conn.commit()

    text = (f"<b>✋ Assalomu alaykum, {message.from_user.first_name}!</b>\n\n"
            "🚀 Biz sizga Telegram xizmatlarini taklif etamiz!\n"
            "🔽 Davom etish uchun quyidagi tugmalardan birini tanlang:")
    bot.send_message(message.chat.id, text, parse_mode="HTML", reply_markup=main_menu(user_id))

@bot.message_handler(func=lambda m: m.text == "⬅️ Orqaga")
def back_btn(message):
    bot.send_message(message.chat.id, "🖥 Asosiy menyuga qaytdingiz", reply_markup=main_menu(message.from_user.id))

@bot.message_handler(func=lambda m: m.text == "👔 Kabinet")
def cabinet(message):
    user_id = message.from_user.id
    balance, ref_count = get_user(user_id)
    text = (f"<b>🔑 Sizning ID raqamingiz:</b> <code>{user_id}</code>\n\n"
            f"<b>💵 Umumiy balansingiz:</b> {int(balance)} UZS\n"
            f"<b>👥 Takliflaringiz:</b> {ref_count} ta\n"
            "Statusingiz: Oddiy")
    
    inline_markup = InlineKeyboardMarkup()
    inline_markup.add(InlineKeyboardButton("💳 Pul kiritish", callback_data="buy"))
    bot.send_message(message.chat.id, text, parse_mode="HTML", reply_markup=inline_markup)

@bot.message_handler(func=lambda m: m.text == "💵 Pul ishlash")
def earn_money(message):
    inline_markup = InlineKeyboardMarkup()
    inline_markup.add(InlineKeyboardButton("🖇 Takliflar (Referal)", callback_data="ref"))
    bot.send_message(message.chat.id, "<b>Quyidagilardan birini tanlang ⤵️</b>", parse_mode="HTML", reply_markup=inline_markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    user_id = call.from_user.id
    if call.data == "buy":
        inline_markup = InlineKeyboardMarkup()
        inline_markup.add(InlineKeyboardButton("💳 Click", callback_data="card"),
                          InlineKeyboardButton("🥝 Qiwi", callback_data="qiwi"))
        bot.edit_message_text("<b>To'lov tizimini tanlang:</b>", call.message.chat.id, call.message.message_id, parse_mode="HTML", reply_markup=inline_markup)
    
    elif call.data == "card":
        click_hamyon = get_setting('click_hamyon')
        bot.edit_message_text(f"<b>⬇️ Karta raqamiga to'lov qiling va adminga yozing\n\n💳 Karta:</b> <code>{click_hamyon}</code>",
                              call.message.chat.id, call.message.message_id, parse_mode="HTML")
        
    elif call.data == "ref":
        bot_info = bot.get_me()
        ref_link = f"https://t.me/{bot_info.username}?start={user_id}"
        text = (f"*✅ Telegram sahifalarga obunachi qo'shish\n"
                f"👇 Hoziroq sinab ko'ring! Linkni bosing!*\n\n👉🏻 {ref_link}")
        bot.send_message(call.message.chat.id, text, parse_mode="Markdown")

# --- NAKRUTKA (API YUBORISH) QISMI ---
@bot.message_handler(func=lambda m: m.text == "➕ Buyurtma berish")
def order_menu(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("Arzon Obunachi"), KeyboardButton("Tezkor Obunachi"))
    markup.add(KeyboardButton("⬅️ Orqaga"))
    msg = bot.send_message(message.chat.id, "<b>Buyurtma turini tanlang:</b>", parse_mode="HTML", reply_markup=markup)
    bot.register_next_step_handler(msg, process_service_choice)

def process_service_choice(message):
    if message.text == "⬅️ Orqaga":
        return back_btn(message)
    
    if message.text == "Arzon Obunachi":
        service_id = 1
        narx = float(get_setting('arzon_narx'))
    elif message.text == "Tezkor Obunachi":
        service_id = 2
        narx = float(get_setting('tezkor_narx'))
    else:
        return bot.send_message(message.chat.id, "Noto'g'ri tanlov.", reply_markup=main_menu(message.from_user.id))

    msg = bot.send_message(message.chat.id, "<b>🔗 Kanalingiz manzilini yuboring:\nNamuna: https://t.me/kanal_linki</b>", parse_mode="HTML", reply_markup=cancel_markup)
    bot.register_next_step_handler(msg, process_link, service_id, narx)

def process_link(message, service_id, narx):
    if message.text == "⬅️ Orqaga":
        return back_btn(message)
    link = message.text
    msg = bot.send_message(message.chat.id, "<b>Qancha obunachi qo'shmoqchisiz? (Faqat raqam yozing)</b>", parse_mode="HTML")
    bot.register_next_step_handler(msg, process_quantity, service_id, narx, link)

def process_quantity(message, service_id, narx, link):
    if message.text == "⬅️ Orqaga":
        return back_btn(message)
    
    if not message.text.isdigit():
        msg = bot.send_message(message.chat.id, "<b>Iltimos, faqat raqam kiriting!</b>", parse_mode="HTML")
        return bot.register_next_step_handler(msg, process_quantity, service_id, narx, link)

    quantity = int(message.text)
    total_price = quantity * narx
    user_id = message.from_user.id
    balance = get_user(user_id)[0]

    if balance < total_price:
        bot.send_message(message.chat.id, f"❌ <b>Hisobingizda mablag' yetarli emas!</b>\nKerakli summa: {total_price} UZS", parse_mode="HTML", reply_markup=main_menu(user_id))
        return

    # Balansdan yechish
    cursor.execute("UPDATE users SET balance = balance - ? WHERE user_id=?", (total_price, user_id))
    conn.commit()

    # API ga yuborish
    try:
        api_req = requests.get(f"{SMM_API_URL}?kalit={SMM_API_KEY}&act=obunachi&id={service_id}&manzil={link}&miqdor={quantity}").json()
        if "order" in api_req:
            order_id = api_req["order"]
            bot.send_message(message.chat.id, f"✅ <b>Buyurtma qabul qilindi!</b>\n\nBuyurtma ID si: <code>{order_id}</code>\nNarxi: {total_price} UZS", parse_mode="HTML", reply_markup=main_menu(user_id))
        else:
            # Xatolik bolsa pulni qaytarish
            cursor.execute("UPDATE users SET balance = balance + ? WHERE user_id=?", (total_price, user_id))
            conn.commit()
            bot.send_message(message.chat.id, "❌ API da xatolik yuz berdi. Pul hisobingizga qaytarildi.", reply_markup=main_menu(user_id))
    except Exception as e:
         bot.send_message(message.chat.id, "❌ Server bilan ulanishda xatolik.", reply_markup=main_menu(user_id))


# --- ADMIN PANEL ---
@bot.message_handler(func=lambda m: m.text == "👨🏻‍💻 Boshqaruv paneli" and m.from_user.id == ADMIN_ID)
def admin_panel(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("➕ Pul berish"), KeyboardButton("➖ Pul ayirish"))
    markup.add(KeyboardButton("📊 Statistika"))
    markup.add(KeyboardButton("⬅️ Orqaga"))
    bot.send_message(message.chat.id, "<b>Xush kelibsiz, Admin!</b>", parse_mode="HTML", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "📊 Statistika" and m.from_user.id == ADMIN_ID)
def statistics(message):
    cursor.execute("SELECT COUNT(user_id) FROM users")
    total_users = cursor.fetchone()[0]
    
    # API Balansni tekshirish
    try:
        api_balance = requests.get(f"{SMM_API_URL}?kalit={SMM_API_KEY}&act=hisob").json()
        smm_bal = api_balance.get("hisob", "Noma'lum")
    except:
        smm_bal = "Xatolik"

    text = f"📊 <b>Botdagi jami a'zolar:</b> {total_users} ta\n💰 <b>SMM API Balans:</b> {smm_bal} USD"
    bot.send_message(message.chat.id, text, parse_mode="HTML")

print("Bot ishga tushdi...")
bot.infinity_polling()
