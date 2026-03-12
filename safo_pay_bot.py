import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, LabeledPrice, PreCheckoutQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage

# ============ SOZLAMALAR ============
BOT_TOKEN = "YOUR_BOT_TOKEN"          # @BotFather dan oling
PROVIDER_TOKEN = "YOUR_PAYMENT_TOKEN" # @BotFather > Payments dan oling (Payme, Click, Uzum)
ADMIN_ID = 123456789                  # Sizning Telegram ID

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# ============ STATES ============
class PaymentState(StatesGroup):
    waiting_amount = State()
    waiting_description = State()

# ============ MAHSULOTLAR ============
PRODUCTS = {
    "product_1": {"name": "📦 Mahsulot 1", "price": 50000, "description": "Birinchi mahsulot"},
    "product_2": {"name": "🎁 Mahsulot 2", "price": 100000, "description": "Ikkinchi mahsulot"},
    "product_3": {"name": "⭐ Premium", "price": 200000, "description": "Premium paket"},
}

# ============ /start ============
@dp.message(CommandStart())
async def start(message: types.Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🛒 Mahsulotlar", callback_data="products")],
        [InlineKeyboardButton(text="💰 Balans", callback_data="balance")],
        [InlineKeyboardButton(text="📞 Yordam", callback_data="help")],
    ])
    await message.answer(
        f"👋 Assalomu alaykum, {message.from_user.first_name}!\n\n"
        "💳 To'lov botiga xush kelibsiz!\n"
        "Quyidagi tugmalardan birini tanlang:",
        reply_markup=kb
    )

# ============ MAHSULOTLAR RO'YXATI ============
@dp.callback_query(F.data == "products")
async def show_products(callback: types.CallbackQuery):
    buttons = []
    for key, product in PRODUCTS.items():
        price_formatted = f"{product['price']:,}".replace(",", " ")
        buttons.append([
            InlineKeyboardButton(
                text=f"{product['name']} — {price_formatted} so'm",
                callback_data=f"buy_{key}"
            )
        ])
    buttons.append([InlineKeyboardButton(text="🔙 Orqaga", callback_data="back")])
    
    kb = InlineKeyboardMarkup(inline_keyboard=buttons)
    await callback.message.edit_text("🛒 Mahsulotlarni tanlang:", reply_markup=kb)

# ============ XARID QILISH ============
@dp.callback_query(F.data.startswith("buy_"))
async def buy_product(callback: types.CallbackQuery):
    product_key = callback.data.replace("buy_", "")
    product = PRODUCTS.get(product_key)
    
    if not product:
        await callback.answer("❌ Mahsulot topilmadi!")
        return

    # Invoice yuborish
    await bot.send_invoice(
        chat_id=callback.from_user.id,
        title=product["name"],
        description=product["description"],
        payload=f"payment_{product_key}_{callback.from_user.id}",
        provider_token=PROVIDER_TOKEN,
        currency="UZS",
        prices=[LabeledPrice(label=product["name"], amount=product["price"] * 100)],  # tiyin
        start_parameter="pay",
        photo_url=None,  # mahsulot rasmi URL (ixtiyoriy)
        need_phone_number=True,
        need_name=True,
    )
    await callback.answer()

# ============ PRE-CHECKOUT (TASDIQLASH) ============
@dp.pre_checkout_query()
async def pre_checkout(pre_checkout_query: PreCheckoutQuery):
    # To'lovni tasdiqlash
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

# ============ MUVAFFAQIYATLI TO'LOV ============
@dp.message(F.successful_payment)
async def successful_payment(message: types.Message):
    payment = message.successful_payment
    payload = payment.invoice_payload
    amount = payment.total_amount // 100  # so'mga aylantirish
    amount_formatted = f"{amount:,}".replace(",", " ")
    
    # Foydalanuvchiga xabar
    await message.answer(
        f"✅ To'lov muvaffaqiyatli amalga oshirildi!\n\n"
        f"💰 Miqdor: {amount_formatted} so'm\n"
        f"🧾 ID: {payment.telegram_payment_charge_id}\n\n"
        f"Rahmat! Tez orada buyurtmangiz bajariladi. 🎉"
    )
    
    # Adminga xabar
    await bot.send_message(
        ADMIN_ID,
        f"💳 Yangi to'lov!\n\n"
        f"👤 Foydalanuvchi: {message.from_user.full_name} (@{message.from_user.username})\n"
        f"🆔 ID: {message.from_user.id}\n"
        f"💰 Miqdor: {amount_formatted} so'm\n"
        f"📦 Payload: {payload}\n"
        f"🧾 Charge ID: {payment.telegram_payment_charge_id}"
    )

# ============ BALANS ============
@dp.callback_query(F.data == "balance")
async def balance(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "💰 Sizning balansingiz: 0 so'm\n\n"
        "_(Bu funksiya database bilan ishlaydi)_",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🔙 Orqaga", callback_data="back")]
        ]),
        parse_mode="Markdown"
    )

# ============ YORDAM ============
@dp.callback_query(F.data == "help")
async def help_handler(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "📞 Yordam:\n\n"
        "• Muammo bo'lsa: @admin_username ga yozing\n"
        "• Ish vaqti: 09:00 - 18:00\n",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🔙 Orqaga", callback_data="back")]
        ])
    )

# ============ ORQAGA ============
@dp.callback_query(F.data == "back")
async def back(callback: types.CallbackQuery):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🛒 Mahsulotlar", callback_data="products")],
        [InlineKeyboardButton(text="💰 Balans", callback_data="balance")],
        [InlineKeyboardButton(text="📞 Yordam", callback_data="help")],
    ])
    await callback.message.edit_text(
        "🏠 Bosh menyu — tugmani tanlang:",
        reply_markup=kb
    )

# ============ ISHGA TUSHIRISH ============
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
