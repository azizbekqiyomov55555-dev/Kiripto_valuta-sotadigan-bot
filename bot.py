#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Kod Amirov Bekjan tomonidan tarqatildi | Python versiyasi

import os
import re
import json
import time
import random
import requests
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ===================== SOZLAMALAR =====================
BOT_TOKEN = "8527362840:AAEHwbiUGYLPbnWBY-b8nfmhLYeajxPL744"  # Bot tokenini kiriting
ADMIN_ID = "8537782289"  # Admin ID raqami

DATA_DIR = "scsmm"
STEP_DIR = "scsmmbot"
USERS_FILE = "scsmm.bot"
BAN_FILE = "scsmm.ban"
# ======================================================

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(STEP_DIR, exist_ok=True)
os.makedirs("number", exist_ok=True)

def _touch(path, default=""):
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            f.write(default)

_touch(USERS_FILE)
_touch(BAN_FILE)
_touch(f"{DATA_DIR}/kamissiya.txt", "sumOut")
_touch(f"{DATA_DIR}/supportuser.txt", "off")
_touch(f"{DATA_DIR}/minimal.sum", "2")
_touch(f"{DATA_DIR}/valbot.txt", "RUB")
_touch(f"{DATA_DIR}/summa.text", "0")
_touch(f"{DATA_DIR}/referal.sum", "0")
_touch(f"{DATA_DIR}/holat.txt", "✅")
_touch(f"{DATA_DIR}/paytoken.txt", "")
_touch(f"{DATA_DIR}/par.txt", "")
_touch(f"{DATA_DIR}/tolovtt.txt", "")
_touch(f"{DATA_DIR}/qollanma.txt", "")
_touch(f"{DATA_DIR}/kanal.txt", "")


# ===================== API YORDAMCHILARI =====================
def api(method, data=None):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/{method}"
    try:
        resp = requests.post(url, data=data or {}, timeout=30)
        return resp.json()
    except Exception as e:
        logger.error(f"API xato: {e}")
        return {}

def send(chat_id, text, parse_mode="html", reply_markup=None, **kwargs):
    d = {"chat_id": chat_id, "text": text, "parse_mode": parse_mode}
    if reply_markup:
        d["reply_markup"] = json.dumps(reply_markup) if isinstance(reply_markup, dict) else reply_markup
    d.update(kwargs)
    return api("sendMessage", d)

def edit(chat_id, message_id, text, parse_mode="html", reply_markup=None):
    d = {"chat_id": chat_id, "message_id": message_id, "text": text, "parse_mode": parse_mode}
    if reply_markup:
        d["reply_markup"] = json.dumps(reply_markup) if isinstance(reply_markup, dict) else reply_markup
    return api("editMessageText", d)

def delete(chat_id, message_id):
    return api("deleteMessage", {"chat_id": chat_id, "message_id": message_id})

def answer_cb(cb_id, text="", show_alert=False):
    return api("answerCallbackQuery", {"callback_query_id": cb_id, "text": text, "show_alert": show_alert})

def typing(chat_id):
    api("sendChatAction", {"chat_id": chat_id, "action": "typing"})

def forward(chat_id, from_chat_id, message_id):
    return api("forwardMessage", {"chat_id": chat_id, "from_chat_id": from_chat_id, "message_id": message_id})


# ===================== FAYL OPERATSIYALARI =====================
def read(path, default=""):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except:
        return default

def write(path, value):
    with open(path, "w", encoding="utf-8") as f:
        f.write(str(value))

def append_file(path, value):
    with open(path, "a", encoding="utf-8") as f:
        f.write(value)

def remove(path):
    try:
        os.remove(path)
    except:
        pass


# ===================== FOYDALANUVCHI MA'LUMOTLARI =====================
def get_step(uid):
    return read(f"{STEP_DIR}/{uid}.step", "")

def set_step(uid, val):
    write(f"{STEP_DIR}/{uid}.step", val)

def clear_step(uid):
    remove(f"{STEP_DIR}/{uid}.step")

def get_balance(uid):
    return float(read(f"{DATA_DIR}/{uid}.pul", "0") or "0")

def set_balance(uid, val):
    write(f"{DATA_DIR}/{uid}.pul", str(val))

def get_referal(uid):
    return read(f"{DATA_DIR}/{uid}.referal", "0")

def is_banned(uid):
    return read(f"{DATA_DIR}/{uid}.ban", "") == "ban"

def ban_user(uid, reason=""):
    write(f"{DATA_DIR}/{uid}.ban", "ban")
    if reason:
        write(f"{DATA_DIR}/{uid}.sabab", reason)
    # Qora ro'yxatga qo'shish
    banned = read(BAN_FILE)
    lines = [l for l in banned.split("\n") if l.strip()]
    if str(uid) not in lines:
        append_file(BAN_FILE, f"\n{uid}")

def unban_user(uid):
    remove(f"{DATA_DIR}/{uid}.ban")

def add_stat(uid):
    users = read(USERS_FILE)
    lines = [l for l in users.split("\n") if l.strip()]
    if str(uid) not in lines:
        append_file(USERS_FILE, f"\n{uid}")

def get_users():
    return [l for l in read(USERS_FILE).split("\n") if l.strip()]

def get_contact(uid):
    return read(f"{DATA_DIR}/{uid}.contact", "")

def has_contact(uid):
    return bool(get_contact(uid))


# ===================== KLAVIATURA UCHUN YORDAMCHILAR =====================
def menu_kb():
    return {
        "resize_keyboard": True,
        "keyboard": [
            [{"text": "♻️ Pul ishlash"}],
            [{"text": "💰 Hisobim"}, {"text": "📩 Murojaat uchun"}],
            [{"text": "📝 To'lovlar tarixi"}],
            [{"text": "📊 Hisobot"}, {"text": "🗒 Qo'llanma"}],
        ]
    }

def panel_kb():
    return {
        "resize_keyboard": True,
        "keyboard": [
            [{"text": "📨 Xabarnoma"}],
            [{"text": "🛠 Sozlamalar"}, {"text": "💰 Hisob olib tashlash"}],
            [{"text": "💳 Hisob tekshirish"}, {"text": "💰 Hisob toʻldirish"}],
            [{"text": "👥 Referal narxini o'zgartirish"}, {"text": "📤 Minimal yechish"}],
            [{"text": "✅ Bandan olish"}, {"text": "🚫 Ban berish"}],
            [{"text": "⬅️ Ortga"}],
        ]
    }

def settings_kb():
    return {
        "resize_keyboard": True,
        "keyboard": [
            [{"text": "📤 Majburiy kanal"}, {"text": "📝 To'lovlar kanali"}],
            [{"text": "📩 Murojaat user"}, {"text": "🗒 Qo'llanma matn"}],
            [{"text": "💱 Bot valyutasi"}, {"text": "🛠 Bot holati"}],
            [{"text": "📝 Payeer parametrlari"}],
            [{"text": "↩ ortga"}],
        ]
    }

def back_kb():
    return {
        "resize_keyboard": True,
        "one_time_keyboard": True,
        "keyboard": [[{"text": "⬅️ Ortga"}]]
    }

def ortga_kb():
    return {
        "resize_keyboard": True,
        "keyboard": [[{"text": "↩ ortga"}]]
    }


# ===================== ASOSIY FUNKSIYALAR =====================
def check_join(uid):
    """Majburiy kanallarni tekshirish"""
    kanal = read(f"{DATA_DIR}/kanal.txt", "").strip()
    if not kanal:
        return True
    channels = [c.strip() for c in kanal.split("\n") if c.strip()]
    for ch in channels:
        username = ch.lstrip("@")
        try:
            r = api("getChatMember", {"chat_id": f"@{username}", "user_id": uid})
            status = r.get("result", {}).get("status", "left")
            if status not in ("creator", "administrator", "member"):
                return False
        except:
            return False
    return True

def check_phone(uid):
    """Telefon raqam tekshirish"""
    return has_contact(uid)

def get_bot_username():
    r = api("getMe")
    return r.get("result", {}).get("username", "")

def send_join_request(uid, firstname):
    """Kanalga obuna bo'lishni so'rash"""
    kanal = read(f"{DATA_DIR}/kanal.txt", "").strip()
    if not kanal:
        return True
    channels = [c.strip() for c in kanal.split("\n") if c.strip()]
    keyboard = []
    all_joined = True
    for i, ch in enumerate(channels):
        username = ch.lstrip("@")
        try:
            r = api("getChatMember", {"chat_id": f"@{username}", "user_id": uid})
            status = r.get("result", {}).get("status", "left")
            name_r = api("getChat", {"chat_id": f"@{username}"})
            name = name_r.get("result", {}).get("title", username)
            keyboard.append([{"text": f" {name}", "url": f"https://t.me/{username}"}])
            if status not in ("creator", "administrator", "member"):
                all_joined = False
        except:
            all_joined = False
            keyboard.append([{"text": ch, "url": f"https://t.me/{ch.lstrip('@')}"}])

    if not all_joined:
        keyboard.append([{"text": "✅ Tekshirish", "callback_data": "result"}])
        send(uid,
             "<b>Assalomu Alaykum, botdan to`liq foydalanish uchun quydagi kanallarga obuna bo`ling, Obunangizni tasdiqlash uchun ( ✅ Tekshirish )! tugmasini bosing.</b>",
             reply_markup={"inline_keyboard": keyboard})
        return False
    return True

def request_contact(uid):
    """Telefon raqam so'rash"""
    set_step(uid, "request_contact")
    send(uid,
         "<b>Hurmatli foydalanuvchi!</b>\n<b>Pul ishlash ishonchli bo'lishi uchun, pastdagi «📲 Telefon raqamni yuborish» tugmasini bosing:</b>",
         reply_markup={
             "resize_keyboard": True, "one_time_keyboard": True,
             "keyboard": [[{"text": "📲 Telefon raqamni yuborish", "request_contact": True}]]
         })


# ===================== ADMIN KOMANDALAR TEKSHIRUVI =====================
ADMIN_CMDS = [
    "📨 Xabarnoma", "🛠 Sozlamalar", "💰 Hisob olib tashlash", "💳 Hisob tekshirish",
    "✅ Bandan olish", "🚫 Ban berish", "💰 Hisob toʻldirish", "⬅️ Ortga",
    "👥 Referal narxini o'zgartirish", "📤 Minimal yechish", "📤 Majburiy kanal",
    "📝 To'lovlar kanali", "📩 Murojaat user", "🗒 Qo'llanma matn",
    "💱 Bot valyutasi", "📝 To'lovlar tarix", "🛠 Bot holati", "📝 Payeer parametrlari",
    "↩ ortga", "📝  O`zgartirish"
]


# ===================== MESSAGE HANDLER =====================
def handle_message(update):
    msg = update.get("message", {})
    if not msg:
        return

    chat_id = str(msg.get("chat", {}).get("id", ""))
    from_id = str(msg.get("from", {}).get("id", ""))
    text = msg.get("text", "") or ""
    firstname = msg.get("from", {}).get("first_name", "")
    username = msg.get("from", {}).get("username", "")
    message_id = msg.get("message_id")
    contact = msg.get("contact")

    if not chat_id:
        return

    # Standart o'zgaruvchilar
    holat = read(f"{DATA_DIR}/holat.txt", "✅").strip()
    valbot = read(f"{DATA_DIR}/valbot.txt", "RUB").strip()
    minimalsumma = read(f"{DATA_DIR}/minimal.sum", "2").strip()
    referalsum = read(f"{DATA_DIR}/referal.sum", "0").strip()
    supportuser = read(f"{DATA_DIR}/supportuser.txt", "off").strip()
    tolovtt = read(f"{DATA_DIR}/tolovtt.txt", "").strip()
    qollanma = read(f"{DATA_DIR}/qollanma.txt", "").strip()
    jami = read(f"{DATA_DIR}/summa.text", "0").strip()
    paytoken = read(f"{DATA_DIR}/paytoken.txt", "").strip()
    paykamissiya = read(f"{DATA_DIR}/kamissiya.txt", "sumOut").strip()
    par = read(f"{DATA_DIR}/par.txt", "").strip()
    kanal = read(f"{DATA_DIR}/kanal.txt", "").strip()
    step = get_step(chat_id)
    banned = is_banned(chat_id)
    sum_val = get_balance(chat_id)
    referal = get_referal(chat_id)

    # Faylarni boshlash
    _touch(f"{DATA_DIR}/{chat_id}.referal", "0")
    _touch(f"{DATA_DIR}/{chat_id}.pul", "0")
    _touch(f"{DATA_DIR}/{chat_id}.sabab", "Botdan faqat O'zbekiston fuqarolari foydalanishi mumkin!")

    # Bot holati tekshirish
    if text and holat == "❌" and chat_id != ADMIN_ID:
        send(chat_id, "⛔️ <b>Bot vaqtinchalik o'chirilgan!</b>\n\n<i>Birozdan so`ng qayta /start bosing.</i>")
        return

    # Ban tekshirish
    if banned:
        delete(chat_id, message_id)
        send(chat_id, "<b>Hurmatli foydalanuvchi!</b>\n<b>Siz botdan banlangansiz. Shuning uchun botni ishlata olmaysiz!</b>",
             reply_markup={"inline_keyboard": [[{"text": "📃 Batafsil maʼlumot", "callback_data": "sabab"}]]})
        return

    # Kontakt yuborish holati
    if step == "request_contact" and contact:
        phone = str(contact.get("phone_number", "")).replace("+", "")
        contact_uid = str(contact.get("user_id", ""))

        if check_join(from_id):
            if len(phone) == 12 and phone.startswith("998"):
                if contact_uid == chat_id:
                    add_stat(from_id)
                    u_name = f"@{username}" if username else firstname

                    # Referal bonus
                    if os.path.exists(f"{DATA_DIR}/{from_id}.referalid"):
                        ref_id = read(f"{DATA_DIR}/{from_id}.referalid")
                        channel_s = read(f"{DATA_DIR}/{from_id}.channel", "")
                        login_s = read(f"{DATA_DIR}/{from_id}.login", "")
                        if channel_s == "true" and login_s == "false":
                            if check_join(ref_id):
                                write(f"{DATA_DIR}/{from_id}.login", "true")
                                ref_bal = get_balance(ref_id)
                                bonus = float(referalsum or "0")
                                set_balance(ref_id, ref_bal + bonus)
                                fn = firstname.replace("<","").replace(">","").replace("/","")
                                send(ref_id,
                                     f"<b>👏 Tabriklaymiz! Sizni referalingiz</b> <a href='tg://user?id={from_id}'>{fn}</a> <b>botimizdan ro'yxatdan o'tdi va sizga {referalsum}-{valbot} taqdim etildi.</b>",
                                     reply_markup=menu_kb())

                    reply_r = send(from_id, "<b>Bosh menyu</b>", reply_markup=menu_kb())
                    reply_mid = reply_r.get("result", {}).get("message_id")
                    botname = get_bot_username()
                    send(from_id, "",
                         reply_markup={"inline_keyboard": [[{"text": "↗️ Doʻstlarga yuborish", "switch_inline_query": from_id}]]},
                         reply_to_message_id=reply_mid)
                    clear_step(chat_id)
                    write(f"{DATA_DIR}/{chat_id}.contact", phone)
                else:
                    send(chat_id, "<b>Faqat o'zingizni kontaktingizni yuboring:</b>",
                         reply_markup={"resize_keyboard": True, "one_time_keyboard": True,
                                       "keyboard": [[{"text": "📲 Telefon raqamni yuborish", "request_contact": True}]]})
            else:
                ban_user(chat_id)
                send(chat_id, "<b>Kechirasiz! Botdan faqat O'zbekiston fuqarolari foydalanishi mumkin!</b>",
                     reply_markup={"remove_keyboard": True})
                clear_step(chat_id)
        return

    # ==================== ADMIN KOMANDALAR ====================

    if text == "/admin" and chat_id == ADMIN_ID:
        typing(chat_id)
        send(chat_id, "<b>Salom, Siz bot administratorisiz. Kerakli boʻlimni tanlang:</b>", reply_markup=panel_kb())
        return

    if text == "↩ ortga" and chat_id == ADMIN_ID:
        typing(chat_id)
        send(chat_id, "Panel", reply_markup=panel_kb())
        return

    if text == "🛠 Sozlamalar" and chat_id == ADMIN_ID:
        typing(chat_id)
        send(chat_id, "<b>Kerakli boʻlimni tanlang:</b>", reply_markup=settings_kb())
        return

    if text == "📨 Xabarnoma" and chat_id == ADMIN_ID:
        send(chat_id, "<b>Yuboriladigan xabar turini tanlang;</b>",
             reply_markup={"inline_keyboard": [
                 [{"text": "Oddiy xabar", "callback_data": "send"}, {"text": "Forward xabar", "callback_data": "forsend"}],
                 [{"text": "Foydalanuvchiga xabar", "callback_data": "user"}]
             ]})
        return

    if text == "↩Back" and chat_id == ADMIN_ID:
        typing(chat_id)
        send(chat_id, "<b>Kerakli boʻlimni tanlang:</b>", reply_markup=settings_kb())
        return

    # Step: user (foydalanuvchiga xabar ID)
    if step == "user" and chat_id == ADMIN_ID:
        if text == "↩ ortga":
            clear_step(chat_id)
        elif text.isdigit():
            write(f"{STEP_DIR}/xbr.txt", text)
            send(chat_id, "<b>Xabaringizni kiriting:</b>")
            set_step(chat_id, "xabar")
        else:
            send(chat_id, "<b>Faqat raqamlardan foydalaning!</b>")
        return

    # Step: xabar (foydalanuvchiga xabar matni)
    if step == "xabar" and chat_id == ADMIN_ID:
        if text == "↩ ortga":
            clear_step(chat_id)
        else:
            saved = read(f"{STEP_DIR}/xbr.txt", "")
            send(saved, text, disable_web_page_preview=True)
            send(chat_id, "<b>Xabaringiz yuborildi ✅</b>", reply_markup=panel_kb())
            clear_step(chat_id)
            remove(f"{STEP_DIR}/xbr.txt")
        return

    # Step: users (hammaga xabar)
    if step == "users" and chat_id == ADMIN_ID:
        users = get_users()
        ok = False
        for uid in users:
            r = send(uid, text, disable_web_page_preview=True)
            if r.get("ok"):
                ok = True
        if ok:
            send(chat_id, "<b>Hammaga yuborildi ✅</b>", reply_markup=panel_kb())
        clear_step(chat_id)
        return

    # Step: forusers (hammaga forward)
    if step == "forusers" and chat_id == ADMIN_ID:
        if text == "↩ ortga":
            clear_step(chat_id)
            return
        users = get_users()
        ok = False
        for uid in users:
            r = forward(uid, chat_id, message_id)
            if r.get("ok"):
                ok = True
        if ok:
            send(chat_id, "<b>Hammaga yuborildi ✅</b>", reply_markup=panel_kb())
        clear_step(chat_id)
        return

    if text == "🛠 Bot holati" and chat_id == ADMIN_ID:
        send(chat_id, f"<b>Hozirgi holat:</b> {holat}",
             reply_markup={"inline_keyboard": [
                 [{"text": "✅", "callback_data": "holat-✅"}, {"text": "❌", "callback_data": "holat-❌"}],
                 [{"text": "Yopish", "callback_data": "qayt"}]
             ]})
        return

    if text == "📝 Payeer parametrlari" and chat_id == ADMIN_ID:
        if not paytoken:
            send(chat_id, "❌ <b>To'lov uchun token mavjud emas!</b>\n\n▶ Iltimos, tokenni kiriting:",
                 reply_markup={"inline_keyboard": [[{"text": "▶ Token kiritish", "callback_data": "uptoken"}]]})
        else:
            try:
                kurs_r = requests.get(f"https://scsmm.uz/pay/?key={paytoken}&action=kurs", timeout=10).json()
                usd_k = kurs_r.get("USD", "N/A")
                rub_k = kurs_r.get("RUB", "N/A")
                bal_r = requests.get(f"https://scsmm.uz/pay?key={paytoken}&action=balance", timeout=10).json()
                balans = bal_r.get("balance", "?")
                valyuta = bal_r.get("currency", "?")
                kimdan = "Foydalanuvchidan" if paykamissiya == "sum" else "Admin"
                send(chat_id,
                     f"💰 <b>Hisobda: {balans} {valyuta}\n\nTo'lov kursi:\nUSD-{usd_k}\nRUB-{rub_k}\n\n🔑 Joriy token:</b> {paytoken}\n\n<b>Kamissiya kimdan olinadi: {paykamissiya} ({kimdan})</b>",
                     reply_markup={"inline_keyboard": [
                         [{"text": "♻ Token yangilash", "callback_data": "uptoken"}],
                         [{"text": "✅ Kamissiyani sozlash", "callback_data": "kamissiya"}]
                     ]})
            except:
                send(chat_id, "⚠ <b>Balansni olishda xatolik yuz berdi.</b>",
                     reply_markup={"inline_keyboard": [[{"text": "♻ Token yangilash", "callback_data": "uptoken"}]]})
        return

    if step == "uptoken" and chat_id == ADMIN_ID:
        typing(chat_id)
        write(f"{DATA_DIR}/paytoken.txt", text)
        send(chat_id, f"✅ {text}-saqlandi")
        clear_step(chat_id)
        return

    if text == "📝 To'lovlar kanali" and chat_id == ADMIN_ID:
        kanallar = read(f"{DATA_DIR}/tolovtt.txt", "")
        send(chat_id, f"Hozirgi o'rnatilgan kanal:\n{kanallar}",
             reply_markup={"resize_keyboard": True,
                           "keyboard": [[{"text": "📝 Kanal o'zgartirish"}], [{"text": "↩Back"}]]})
        return

    if text == "📝 Kanal o'zgartirish" and chat_id == ADMIN_ID:
        send(chat_id, "Kanalni ulamasangiz bot to'lov tizizmlari ishlamaydi!\nKanal manzilini kiriting: Namuna - @your_channel_username")
        set_step(chat_id, "kanal_add")
        return

    if step == "kanal_add" and chat_id == ADMIN_ID:
        typing(chat_id)
        if "@" in text:
            uname = text.lstrip("@")
            try:
                ci = requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/getChat?chat_id=@{uname}", timeout=10).json()
                if ci.get("ok") and ci.get("result", {}).get("type") in ("channel", "supergroup"):
                    bot_info = api("getMe")
                    bot_id = bot_info.get("result", {}).get("id")
                    cm = requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/getChatMember?chat_id=@{uname}&user_id={bot_id}", timeout=10).json()
                    if cm.get("ok") and cm.get("result", {}).get("status") in ("administrator", "creator"):
                        send(chat_id, "✅ Muvaffaqiyatli saqlandi!")
                        write(f"{DATA_DIR}/tolovtt.txt", text)
                        clear_step(chat_id)
                    else:
                        send(chat_id, "⚠️ Xato: Bot ushbu kanal yoki guruhda admin emas.")
                else:
                    send(chat_id, "⚠️ Xato: Kiritilgan username kanal yoki guruh emas.")
            except:
                send(chat_id, "⚠️ Xato: Kanal tekshirishda muammo yuz berdi.")
        else:
            send(chat_id, "⚠️ Xato: Iltimos, kanal yoki guruh username'ini to'g'ri kiriting.")
        return

    if text == "📤 Majburiy kanal" and chat_id == ADMIN_ID:
        send(chat_id, "<b>Majburiy obunalarni sozlash bo'limidasiz:</b>",
             reply_markup={"inline_keyboard": [
                 [{"text": "➕ Qo'shish", "callback_data": "qoshish"}],
                 [{"text": "📑 Ro'yxat", "callback_data": "royxat"}, {"text": "🗑 O'chirish", "callback_data": "ochirish"}]
             ]})
        return

    if step == "qo'shish" and chat_id == ADMIN_ID:
        if text == "↩ ortga":
            clear_step(chat_id)
        elif "@" in text:
            if not kanal:
                write(f"{DATA_DIR}/kanal.txt", text)
            else:
                append_file(f"{DATA_DIR}/kanal.txt", f"\n{text}")
            send(chat_id, f"<b>{text} - kanal qo'shildi!</b>", reply_markup=panel_kb())
            clear_step(chat_id)
        else:
            send(chat_id, "<b>Kanalingiz useri yuboring:\n\nNamuna:</b> @ByKons")
        return

    if text == "📩 Murojaat user" and chat_id == ADMIN_ID:
        manzil = read(f"{DATA_DIR}/supportuser.txt", "off")
        send(chat_id, f"Murojat etish uchun Manzillar:\n {manzil}",
             reply_markup={"resize_keyboard": True,
                           "keyboard": [[{"text": "⬅ O`zgartirish"}], [{"text": "↩Back"}]]})
        return

    if text == "⬅ O`zgartirish" and chat_id == ADMIN_ID:
        send(chat_id, "*Murojaat etish uchun usernamengizni @ belgisisiz yuboring*\n\nMurojaatni yopib qoyish uchun { off } sozini kiriting.", parse_mode="markdown")
        set_step(chat_id, "00")
        return

    if step == "00" and chat_id == ADMIN_ID:
        typing(chat_id)
        write(f"{DATA_DIR}/supportuser.txt", text)
        send(chat_id, f"✅  @{text}-Saqlandi")
        clear_step(chat_id)
        return

    if text == "🗒 Qo'llanma matn" and chat_id == ADMIN_ID:
        qollat = read(f"{DATA_DIR}/qollanma.txt", "")
        send(chat_id, f"Matn:\n {qollat}",
             reply_markup={"resize_keyboard": True,
                           "keyboard": [[{"text": "🗒 O`zgartirish"}], [{"text": "↩Back"}]]})
        return

    if text == "🗒 O`zgartirish" and chat_id == ADMIN_ID:
        send(chat_id, "*Qo`llanma uchun matn kiriting*", parse_mode="markdown")
        set_step(chat_id, "qollanma")
        return

    if step == "qollanma" and chat_id == ADMIN_ID:
        typing(chat_id)
        write(f"{DATA_DIR}/qollanma.txt", text)
        send(chat_id, "✅ Saqlandi")
        clear_step(chat_id)
        return

    if text == "💱 Bot valyutasi" and chat_id == ADMIN_ID:
        send(chat_id, f"Bot valyutasi: {valbot}",
             reply_markup={"resize_keyboard": True,
                           "keyboard": [[{"text": "💱 O`zgartirish"}], [{"text": "↩ ortga"}]]})
        return

    if text == "💱 O`zgartirish" and chat_id == ADMIN_ID:
        send(chat_id, "*Bot to'lov tizimi valyutasini tanlang*", parse_mode="markdown",
             reply_markup={"inline_keyboard": [
                 [{"text": "USD", "callback_data": "val-USD"}],
                 [{"text": "RUB", "callback_data": "val-RUB"}],
                 [{"text": "↩ Back", "callback_data": "qayt"}]
             ]})
        return

    if text == "💳 Hisob tekshirish" and chat_id == ADMIN_ID:
        typing(chat_id)
        set_step(chat_id, "result")
        send(chat_id, "<b>Foydalanuvchini ID raqamini kiriting:</b>", reply_markup=panel_kb())
        return

    if step == "result" and chat_id == ADMIN_ID:
        typing(chat_id)
        if text not in ADMIN_CMDS:
            s = get_balance(text)
            r = get_referal(text)
            rq = get_contact(text)
            send(chat_id,
                 f"<b>Foydalanuvchi hisobi:</b> <code>{s}</code>\n<b>Foydalanuvchi referali:</b> <code>{r}</code>\n<b>Foydalanuvchi raqami:</b> <code>{rq}</code>",
                 reply_markup=panel_kb())
            clear_step(chat_id)
        return

    if text == "💰 Hisob olib tashlash" and chat_id == ADMIN_ID:
        typing(chat_id)
        set_step(chat_id, "coinm")
        send(chat_id, "<b>Foydalanuvchi hisobini necha pul olmoqchisiz</b>", reply_markup=panel_kb())
        return

    if step == "coinm" and chat_id == ADMIN_ID:
        if text not in ADMIN_CMDS:
            write(f"{DATA_DIR}/{chat_id}.coinm", text)
            set_step(chat_id, "paym")
            send(chat_id, "<b>Foydalanuvchi ID raqamini kiriting:</b>", reply_markup=panel_kb())
        return

    if step == "paym" and chat_id == ADMIN_ID:
        if text not in ADMIN_CMDS:
            summa = float(read(f"{DATA_DIR}/{chat_id}.coinm", "0") or 0)
            s = get_balance(text)
            jami_new = s - summa
            set_balance(text, jami_new)
            send(text, f"💰 Hisobingiz: {summa} olib tashlandi!\nHozirgi hisobingiz: {jami_new}")
            send(chat_id, "<b>Foydalanuvchi balansidan olib tashlandi!</b>", reply_markup=panel_kb())
            clear_step(chat_id)
        return

    if text == "💰 Hisob toʻldirish" and chat_id == ADMIN_ID:
        typing(chat_id)
        set_step(chat_id, "coin")
        send(chat_id, "<b>Foydalanuvchi hisobini necha pulga toʻldirmoqchisiz:</b>", reply_markup=panel_kb())
        return

    if step == "coin" and chat_id == ADMIN_ID:
        if text not in ADMIN_CMDS:
            write(f"{DATA_DIR}/{chat_id}.coin", text)
            set_step(chat_id, "pay")
            send(chat_id, "<b>Foydalanuvchi ID raqamini kiriting:</b>", reply_markup=panel_kb())
        return

    if step == "pay" and chat_id == ADMIN_ID:
        if text not in ADMIN_CMDS:
            summa = float(read(f"{DATA_DIR}/{chat_id}.coin", "0") or 0)
            s = get_balance(text)
            jami_new = s + summa
            set_balance(text, jami_new)
            send(text, f"💰 Hisobingiz: {summa} {valbot}ga to'ldirildi!\nHozirgi hisobingiz: {jami_new}")
            send(chat_id, "<b>Foydalanuvchi balansi toʻldirildi!</b>", reply_markup=panel_kb())
            clear_step(chat_id)
        return

    if text == "👥 Referal narxini o'zgartirish" and chat_id == ADMIN_ID:
        mref = read(f"{DATA_DIR}/referal.sum", "0")
        send(chat_id, f"1-referal narxi:\n {mref}-{valbot}",
             reply_markup={"resize_keyboard": True,
                           "keyboard": [[{"text": "👥 O`zgartirish"}], [{"text": "↩ ortga"}]]})
        return

    if text == "👥 O`zgartirish" and chat_id == ADMIN_ID:
        typing(chat_id)
        set_step(chat_id, "referal")
        send(chat_id, "<b>Referal narxini kiriting:</b>", reply_markup=panel_kb())
        return

    if step == "referal" and chat_id == ADMIN_ID:
        typing(chat_id)
        if text.replace(".", "").isdigit():
            write(f"{DATA_DIR}/referal.sum", text)
            send(chat_id, f"<b>Referal taklif qilish narxi: {text} {valbot}ga o'zgardi!</b>", reply_markup=panel_kb())
            clear_step(chat_id)
        else:
            send(chat_id, "Raqamlardan foydalaning.", reply_markup=panel_kb())
        return

    if text == "✅ Bandan olish" and chat_id == ADMIN_ID:
        set_step(chat_id, "unban")
        send(chat_id, "<b>Foydalanuvchini ID raqamini kiriting:</b>", reply_markup=panel_kb())
        return

    if step == "unban" and chat_id == ADMIN_ID:
        if text not in ADMIN_CMDS:
            unban_user(text)
            send(chat_id, f"<a href='tg://user?id={text}'>Foydalanuvchi</a> <b>bandan olindi!</b>", reply_markup=panel_kb())
            clear_step(chat_id)
        return

    if text == "🚫 Ban berish" and chat_id == ADMIN_ID:
        set_step(chat_id, "sabab")
        send(chat_id, "<b>Foydalanuvchini nima sababdan ban qilmoqchisiz:</b>", reply_markup=panel_kb())
        return

    if step == "sabab" and chat_id == ADMIN_ID:
        write(f"{DATA_DIR}/{chat_id}.sabab", text)
        send(chat_id, "<b>Foydalanuvchini ID raqamini kiriting:</b>", reply_markup=panel_kb())
        set_step(chat_id, "ban")
        return

    if step == "ban" and chat_id == ADMIN_ID:
        if text not in ADMIN_CMDS:
            sabab = read(f"{DATA_DIR}/{chat_id}.sabab", "")
            ban_user(text, sabab)
            send(chat_id, f"<a href='tg://user?id={text}'>Foydalanuvchi</a> <b>banlandi!</b>", reply_markup=panel_kb())
            clear_step(chat_id)
            send(text, "<b>Hurmatli foydalanuvchi!</b>\n<b>Siz botdan banlandingiz.</b>",
                 reply_markup={"inline_keyboard": [[{"text": "📃 Batafsil maʼlumot", "callback_data": "sabab"}]]})
        return

    if text == "📤 Minimal yechish" and chat_id == ADMIN_ID:
        mmin = read(f"{DATA_DIR}/minimal.sum", "2")
        send(chat_id, f"Minimal pul yechish narxi:\n {mmin}-{valbot}",
             reply_markup={"resize_keyboard": True,
                           "keyboard": [[{"text": "📤 O`zgartirish"}], [{"text": "↩ ortga"}]]})
        return

    if text == "📤 O`zgartirish" and chat_id == ADMIN_ID:
        typing(chat_id)
        set_step(chat_id, "minimalsumma")
        send(chat_id, "<b>Minimal pul yechish narxini kiriting:\nmin 2-RUB\nmin 0.1-USD</b>", reply_markup=panel_kb())
        return

    if step == "minimalsumma" and chat_id == ADMIN_ID:
        if text not in ADMIN_CMDS:
            write(f"{DATA_DIR}/minimal.sum", text)
            send(chat_id, f"<b>Minimal pul yechish narxi: {text} {valbot}ga o'zgardi!</b>", reply_markup=panel_kb())
            clear_step(chat_id)
        return

    # ==================== FOYDALANUVCHI KOMANDALAR ====================

    # /start
    if text.startswith("/start"):
        parts = text.split()
        ref_id = parts[1] if len(parts) > 1 else None

        if not check_join(from_id):
            send_join_request(from_id, firstname)
            if ref_id and ref_id != chat_id:
                write(f"{DATA_DIR}/{from_id}.referalid", ref_id)
                write(f"{DATA_DIR}/{from_id}.channel", "false")
                write(f"{DATA_DIR}/{from_id}.login", "false")
            return

        if not check_phone(from_id):
            request_contact(from_id)
            if ref_id and ref_id != chat_id:
                write(f"{DATA_DIR}/{from_id}.referalid", ref_id)
                write(f"{DATA_DIR}/{from_id}.channel", "false")
                write(f"{DATA_DIR}/{from_id}.login", "false")
            return

        add_stat(from_id)
        u_name = f"@{username}" if username else firstname
        botname = get_bot_username()

        # Referal tekshirish
        if ref_id and ref_id != chat_id:
            users_list = get_users()
            if chat_id not in users_list:
                append_file(USERS_FILE, f"\n{chat_id}")
            if not any(chat_id == u for u in users_list):
                write(f"{DATA_DIR}/{from_id}.referalid", ref_id)
                write(f"{DATA_DIR}/{from_id}.channel", "false")
                write(f"{DATA_DIR}/{from_id}.login", "false")
                send(ref_id,
                     f"<b>👏 Tabriklaymiz! Siz referalingiz</b> <a href='tg://user?id={chat_id}'>foydalanuvchi</a><b>ni botga taklif qildingiz!</b>")
            else:
                send(chat_id,
                     "<b>Hurmatli foydalanuvchi!</b>\n<b>Siz referalingiz referal bo'la olmaysiz!</b>",
                     reply_to_message_id=message_id)

        reply_r = send(from_id, "<b>Bosh menyu</b>", reply_markup=menu_kb())
        reply_mid = reply_r.get("result", {}).get("message_id")
        send(from_id, "",
             reply_markup={"inline_keyboard": [[{"text": "↗️ Doʻstlarga yuborish", "switch_inline_query": from_id}]]},
             reply_to_message_id=reply_mid)
        return

    # Pul ishlash
    if text == "♻️ Pul ishlash" and not banned:
        if not check_join(from_id):
            send_join_request(from_id, firstname)
            return
        if not check_phone(from_id):
            request_contact(from_id)
            return
        botname = get_bot_username()
        u_name = f"@{username}" if username else firstname
        send(chat_id,
             f"<b>Hurmatli {firstname} botimizdan pul ishlash uchun pastdagi referal havolani do'stlaringizga ulashing va pul ishlang!\n\n1-referal {referalsum}-{valbot}</b>\n\n<i>Taklif havolangiz👇</i>\n\nhttps://t.me/{botname}?start={chat_id}",
             disable_web_page_preview=True,
             reply_markup={"inline_keyboard": [[{"text": "💰Pul ishlashni boshlash", "switch_inline_query": chat_id}]]})
        return

    # Hisobim
    if text == "💰 Hisobim" and not banned:
        if not check_join(from_id):
            send_join_request(from_id, firstname)
            return
        if not check_phone(from_id):
            request_contact(from_id)
            return
        send(chat_id,
             f"<b>Sizning balansingiz:</b> {sum_val}-<b>{valbot}</b>\n<b>🗣 Siz botga taklif qilgan a'zolar soni:</b> {referal}-<b>ta</b>\n<b>💵 Bot toʻlab bergan jami summa:</b> {jami}-{valbot}\n<b>🎈 Pul yechib olish uchun minimal summa:</b> {minimalsumma}-<b>{valbot}</b>",
             reply_markup={"inline_keyboard": [[{"text": "Pul yechish", "callback_data": "production"}]]})
        return

    # Hisobot
    if text == "📊 Hisobot" and not banned:
        if not check_join(from_id):
            send_join_request(from_id, firstname)
            return
        if not check_phone(from_id):
            request_contact(from_id)
            return
        all_users = get_users()
        member = len(all_users)
        ban_users = [l for l in read(BAN_FILE).split("\n") if l.strip()]
        banmember = len(ban_users)
        send(chat_id,
             f"<b>Botdagi a'zolar soni:</b> {member}-<b>ta</b>\n<b>Botdan ban olganlar:</b> {banmember}-<b>ta</b>\n<b>Bot to'lab bergan jami summa:</b> {jami}-<b>{valbot}</b>",
             reply_markup={"inline_keyboard": [[{"text": "♻️ Yangilash", "callback_data": "upgrade"}]]})
        return

    # Qo'llanma
    if text == "🗒 Qo'llanma" and not banned:
        if not check_join(from_id):
            send_join_request(from_id, firstname)
            return
        if not check_phone(from_id):
            request_contact(from_id)
            return
        if qollanma:
            send(chat_id, f"<b>{qollanma}</b>")
        else:
            send(chat_id, "<b>Qo`llanma bot adminstratori tamonidan kiritilmagan.</b>")
        return

    # To'lovlar tarixi
    if text == "📝 To'lovlar tarixi" and not banned:
        if not check_join(from_id):
            send_join_request(from_id, firstname)
            return
        if not check_phone(from_id):
            request_contact(from_id)
            return
        if tolovtt:
            kanal_u = tolovtt.lstrip("@")
            send(chat_id,
                 f"<b>✅ Botimiz to'lovlar kanaliga obuna bo'lishingiz mumkin. </b>\n\n<i>Quyidagi kanal orqali to'lovlar tarixini kuzatib boring👇</i>\n\n@{kanal_u}",
                 reply_markup={"inline_keyboard": [[{"text": "Kanalga kirish 🧾", "url": f"https://t.me/{kanal_u}"}]]})
        else:
            send(chat_id, "<b>To'lov manitoringi bot adminstratori tomonidan o'chirilgan.</b>")
        return

    # Murojaat uchun
    if text == "📩 Murojaat uchun" and not banned:
        if not check_join(from_id):
            send_join_request(from_id, firstname)
            return
        if not check_phone(from_id):
            request_contact(from_id)
            return
        if supportuser and supportuser != "off":
            send(chat_id, f"<b>Murojaat uchun: @{supportuser}</b>",
                 reply_markup={"inline_keyboard": [[{"text": "Murojaat etish", "url": f"https://t.me/{supportuser}"}]]})
        else:
            send(chat_id, "<b>Murojaat etish bot adminstratori tamonidan o`chirilgan.</b>")
        return

    # Ortga
    if text == "⬅️ Ortga" and not banned:
        if not check_join(from_id):
            send_join_request(from_id, firstname)
            return
        if not check_phone(from_id):
            request_contact(from_id)
            return
        add_stat(chat_id)
        send(chat_id, "<b>Kerakli boʻlimni tanlang</b> 👇", reply_markup=menu_kb())
        clear_step(chat_id)
        return

    # Step: wallet-XXX (hamyon raqami kiritish)
    if step.startswith("wallet-"):
        wallet_type = step.split("-", 1)[1]
        if text == "⬅️ Ortga":
            clear_step(chat_id)
        elif re.match(r'^P\d+$', text):
            send(chat_id, "Qancha miqdorda pul yechib olmoqchisiz?",
                 reply_markup={"resize_keyboard": True,
                               "keyboard": [[{"text": str(int(sum_val))}], [{"text": "⬅️ Ortga"}]]})
            set_step(chat_id, f"miqdor-{wallet_type}-{text}")
        else:
            send(chat_id, "❌ To'lov raqami noto'g'ri kiritildi!\n\nTo'g'ri namuna: <code>P123456789</code>",
                 reply_markup={"resize_keyboard": True, "keyboard": [[{"text": "⬅️ Ortga"}]]})
        return

    # Step: miqdor-XXX-RAQAM (miqdor kiritish)
    if step.startswith("miqdor-"):
        parts = step.split("-")
        wallet_type = parts[1] if len(parts) > 1 else ""
        wallet_num = parts[2] if len(parts) > 2 else ""

        if text == "⬅️ Ortga":
            clear_step(chat_id)
            return

        try:
            amount = float(text)
        except:
            send(chat_id, "Iltimos, to'g'ri summa kiriting.")
            return

        if amount >= float(minimalsumma or 2):
            hisob = get_balance(chat_id)
            if hisob >= amount:
                botname = get_bot_username()
                paytoken2 = read(f"{DATA_DIR}/paytoken.txt", "").strip()
                url = f"https://scsmm.uz/pay/?key={paytoken2}&payment_type=payeer&action=transfer&account={wallet_num}&currency={valbot}&transfer_type={paykamissiya}&amount={int(amount)}&comment={botname}"
                try:
                    resp = requests.get(url, timeout=15).json()
                    if resp.get("status") == "success":
                        send(ADMIN_ID,
                             f"*💳 Foydalanuvchi puli toʻlab berildi!*\n\n👤 *Foydalanuvchi*: [{chat_id}](tg://user?id={chat_id})\n💰 *To'lov miqdori:* `{int(amount)}` *{valbot}*\n\n✅ *Muvaffaqiyatli oʻtkazildi!*",
                             parse_mode="markdown")
                        jami2 = float(read(f"{DATA_DIR}/summa.text", "0") or 0) + amount
                        write(f"{DATA_DIR}/summa.text", str(jami2))
                        new_bal = hisob - amount
                        set_balance(chat_id, new_bal)
                        send(chat_id, "<b>Pul bir necha soniyada hisobingizga tushadi! 🎉\n\n💸 Sizning pulingiz muvaffaqiyatli o'tkazildi!</b>",
                             reply_markup=menu_kb())
                    else:
                        send(chat_id, "⚠ <b>Xatolik yuz berdi: Pul o'tkazishda muammo bor. Iltimos, qayta urinib ko'ring.</b>")
                        send(ADMIN_ID, f"⚠ <b>Foydalanuvchi pul yechisda muammo bo'ldi: {resp}</b>")
                except Exception as e:
                    send(chat_id, "⚠ <b>Xatolik yuz berdi.</b>")
                clear_step(chat_id)
            else:
                send(chat_id, f"💵 Sizning hisobingizda siz yechib olmoqchi bo'lgan pul mavjud emas!\nSiz faqat {hisob} {valbot}-pulni yechib olishingiz mumkin!")
        else:
            send(chat_id, f"Minimal pul yechish miqdori: {minimalsumma}-{valbot}")
        return


# ===================== CALLBACK HANDLER =====================
def handle_callback(update):
    cb = update.get("callback_query", {})
    if not cb:
        return

    cb_id = cb.get("id")
    data = cb.get("data", "")
    chat_id = str(cb.get("message", {}).get("chat", {}).get("id", ""))
    from_id = str(cb.get("from", {}).get("id", ""))
    msg_id = cb.get("message", {}).get("message_id")
    first_name = cb.get("from", {}).get("first_name", "")
    username = cb.get("from", {}).get("username", "")
    banned_cb = is_banned(from_id)

    holat = read(f"{DATA_DIR}/holat.txt", "✅").strip()
    valbot = read(f"{DATA_DIR}/valbot.txt", "RUB").strip()
    minimalsumma = read(f"{DATA_DIR}/minimal.sum", "2").strip()
    referalsum = read(f"{DATA_DIR}/referal.sum", "0").strip()
    tolovtt = read(f"{DATA_DIR}/tolovtt.txt", "").strip()
    par = read(f"{DATA_DIR}/par.txt", "").strip()
    jami = read(f"{DATA_DIR}/summa.text", "0").strip()
    sum_val = get_balance(from_id)
    referal = get_referal(from_id)

    if holat == "❌" and from_id != ADMIN_ID:
        answer_cb(cb_id, "⛔️ Bot vaqtinchalik o'chirilgan!\n\nBirozdan so`ng qayta /start bosing.", True)
        return

    if banned_cb:
        delete(chat_id, msg_id)
        send(chat_id, "<b>Hurmatli foydalanuvchi!</b>\n<b>Siz botdan banlangansiz.</b>",
             reply_markup={"inline_keyboard": [[{"text": "📃 Batafsil maʼlumot", "callback_data": "sabab"}]]})
        return

    if data == "sabab":
        sabab = read(f"{DATA_DIR}/{from_id}.sabab", "")
        answer_cb(cb_id, sabab, True)
        return

    if data == "result":
        delete(chat_id, msg_id)
        add_stat(from_id)
        if check_join(from_id):
            if check_phone(from_id):
                u = f"@{username}" if username else first_name
                reply_r = send(from_id, "<b>Bosh menyu</b>", reply_markup=menu_kb())
                reply_mid = reply_r.get("result", {}).get("message_id")
                send(from_id, "",
                     reply_markup={"inline_keyboard": [[{"text": "↗️ Doʻstlarga yuborish", "switch_inline_query": from_id}]]},
                     reply_to_message_id=reply_mid)

                # Referal bonus (kanal a'zo bo'lganda)
                t = random.randint(999999, 3456789)
                time.sleep(t / 1000000)

                ref_sum = float(referalsum or "0")
                if ref_sum > 0 and os.path.exists(f"{DATA_DIR}/{from_id}.referalid"):
                    ref_id = read(f"{DATA_DIR}/{from_id}.referalid")
                    if check_join(ref_id):
                        is_user_s = read(f"{DATA_DIR}/{from_id}.channel", "")
                        login_s = read(f"{DATA_DIR}/{from_id}.login", "")
                        if is_user_s == "false" and login_s == "false":
                            rr = int(get_referal(ref_id) or "0") + 1
                            write(f"{DATA_DIR}/{ref_id}.referal", str(rr))
                            write(f"{DATA_DIR}/{from_id}.channel", "true")
                            fn = first_name.replace("<","").replace(">","").replace("/","")
                            send(ref_id,
                                 f"<b>👏 Tabriklaymiz! Sizning referalingiz</b> <a href='tg://user?id={from_id}'>{fn}</a> <b>kanallarga a'zo bo'ldi.</b>\n<b>referalingiz roʻyxatdan oʻtsa, sizga {int(ref_sum)} {valbot} taqdim etiladi!</b>",
                                 reply_markup=menu_kb())
        else:
            answer_cb(cb_id, "Siz hali kanallarga aʼzo boʻlmadingiz!", False)
        return

    if data == "upgrade":
        referal = get_referal(from_id)
        all_users = get_users()
        member = len(all_users)
        ban_users = [l for l in read(BAN_FILE).split("\n") if l.strip()]
        banmember = len(ban_users)
        now = datetime.now()
        sana = now.strftime("%d-%b %Y")
        soat = now.strftime("%H:%M:%S")
        edit(chat_id, msg_id,
             f"<b>Botimiz a'zolari soni:</b> <code>{member}</code>\n<b>Qora roʻyxatdagi a'zolar soni:</b> <code>{banmember}</code>\n<b>Siz botga taklif qilgan aʼzolar soni:</b> <code>{referal}</code>\n\n{sana}-{soat}",
             reply_markup={"inline_keyboard": [[{"text": "♻️ Yangilash", "callback_data": "upgrade"}]]})
        answer_cb(cb_id, f"A'zolar: {member}\nBanlangan: {banmember}\nReferallar: {referal}\n{sana}-{soat}", True)
        return

    if data == "back":
        if check_join(from_id) and check_phone(from_id):
            delete(chat_id, msg_id)
            send(from_id, "<b>Kerakli boʻlimni tanlang</b> 👇", reply_markup=menu_kb())
        return

    if data == "production":
        if check_join(from_id) and check_phone(from_id) and not banned_cb:
            if tolovtt:
                if par != "OFF":
                    delete(chat_id, msg_id)
                    send(from_id,
                         f"💰 <b>Sizning hisobingizda: {sum_val}-{valbot} mavjud!</b>\n<b>Pulingizni yechib olish uchun hamyonni tanlang!</b>",
                         reply_markup={"inline_keyboard": [[{"text": "🅿 Payeer", "callback_data": "pay-Payeer"}]]})
                else:
                    answer_cb(cb_id, "To'lov tizimlari admin tarafidan o`chirilgan!", True)
            else:
                answer_cb(cb_id, "To'lov tizimlari topilmadi!", True)
        return

    if data.startswith("pay-"):
        wallet = data.split("-", 1)[1]
        if tolovtt:
            if sum_val >= float(minimalsumma or 2):
                delete(chat_id, msg_id)
                send(from_id,
                     f"❗ {wallet}-ga pulni yechib olish uchun {wallet} raqamni kiriting.\n\nTo'liq kiriting, Namuna: P123456789",
                     reply_markup={"resize_keyboard": True, "keyboard": [[{"text": "⬅️ Ortga"}]]})
                set_step(from_id, f"wallet-{wallet}")
            else:
                som = float(minimalsumma or 2) - sum_val
                answer_cb(cb_id, f"☝️ Hisobingizda mablag yetarli emas!\nYana {som} {valbot} kerak!\nHisobingizda: {sum_val} {valbot}", True)
        else:
            answer_cb(cb_id, "Toʻlov monitoringi kanali ulanmagan!", True)
        return

    if data.startswith("holat-"):
        xolat = data.split("-", 1)[1]
        write(f"{DATA_DIR}/holat.txt", xolat)
        api("editMessageText", {
            "chat_id": chat_id, "message_id": msg_id,
            "text": f"<b>🔎 Hozirgi holat:</b> {xolat}", "parse_mode": "html",
            "reply_markup": json.dumps({"inline_keyboard": [
                [{"text": "✅", "callback_data": "holat-✅"}, {"text": "❌", "callback_data": "holat-❌"}],
                [{"text": "Yopish", "callback_data": "qayt"}]
            ]})
        })
        return

    if data.startswith("val-"):
        valyuta_new = data.split("-", 1)[1]
        write(f"{DATA_DIR}/valbot.txt", valyuta_new)
        edit(chat_id, msg_id, f"<b>✅ Saqlandi:</b> {valyuta_new}")
        return

    if data == "kamissiya":
        api("editMessageText", {
            "chat_id": chat_id, "message_id": msg_id,
            "text": "To'lov uchun kammisiya 1.45% olinadi. Kimdan olinsin?", "parse_mode": "html",
            "reply_markup": json.dumps({"inline_keyboard": [
                [{"text": "♻ O'z hisobimdan", "callback_data": "kammisiya-sumOut"}],
                [{"text": "♻ Foydalanuvchi hisobidan", "callback_data": "kammisiya-sum"}]
            ]})
        })
        return

    if data.startswith("kammisiya-"):
        kamis = data.split("-", 1)[1]
        write(f"{DATA_DIR}/kamissiya.txt", kamis)
        edit(chat_id, msg_id, "<b>✅ Saqlandi</b>")
        return

    if data == "uptoken":
        api("editMessageText", {
            "chat_id": chat_id, "message_id": msg_id,
            "text": "<b>To'lov uchun token kiriting!\nTokenni @ScSMMBot dan oling.</b>", "parse_mode": "html"
        })
        set_step(from_id, "uptoken")
        return

    if data == "qoshish":
        delete(chat_id, msg_id)
        send(from_id, "<b>Kanalingiz userini kiriting:\n\nNamuna:</b> @ByKons",
             reply_markup={"resize_keyboard": True, "keyboard": [[{"text": "↩ ortga"}]]})
        set_step(from_id, "qo'shish")
        return

    if data == "ochirish":
        delete(chat_id, msg_id)
        remove(f"{DATA_DIR}/kanal.txt")
        send(from_id, "<b>Kanallar o'chirildi</b>")
        return

    if data == "royxat":
        kanal = read(f"{DATA_DIR}/kanal.txt", "").strip()
        soni = kanal.count("@")
        if not kanal:
            edit(chat_id, msg_id, "📂 <b>Kanallar ro'yxati bo'sh!</b>")
        else:
            edit(chat_id, msg_id, f"<b>📢 Kanallar ro'yxati:</b>\n\n{kanal}\n\n<b>Ulangan kanallar soni:</b> {soni} ta")
        return

    if data == "send":
        delete(chat_id, msg_id)
        send(from_id, "*Xabaringizni kiriting:*", parse_mode="markdown",
             reply_markup={"resize_keyboard": True, "keyboard": [[{"text": "↩ ortga"}]]})
        set_step(from_id, "users")
        return

    if data == "forsend":
        delete(chat_id, msg_id)
        send(from_id, "*Xabaringizni yuboring:*", parse_mode="markdown",
             reply_markup={"resize_keyboard": True, "keyboard": [[{"text": "↩ ortga"}]]})
        set_step(from_id, "forusers")
        return

    if data == "user":
        delete(chat_id, msg_id)
        send(from_id, "<b>Foydalanuvchi iD raqamini kiriting:</b>",
             reply_markup={"resize_keyboard": True, "keyboard": [[{"text": "↩ ortga"}]]})
        set_step(from_id, "user")
        return

    if data == "bekor":
        delete(chat_id, msg_id)
        clear_step(from_id)
        send(from_id, "Bekor qilindi", reply_markup=menu_kb())
        return

    if data == "qayt":
        delete(chat_id, msg_id)
        send(from_id, "Bekor qilindi", reply_markup=settings_kb())
        return


# ===================== POLLING =====================
def main():
    print("Bot ishga tushdi...")
    offset = 0
    while True:
        try:
            r = api("getUpdates", {"offset": offset, "timeout": 30})
            updates = r.get("result", [])
            for update in updates:
                offset = update["update_id"] + 1
                try:
                    if "message" in update:
                        handle_message(update)
                    elif "callback_query" in update:
                        handle_callback(update)
                except Exception as e:
                    logger.error(f"Update xato: {e}")
        except Exception as e:
            logger.error(f"Polling xato: {e}")
            time.sleep(3)


if __name__ == "__main__":
    main()
