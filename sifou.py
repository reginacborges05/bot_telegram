import telebot
from telebot import types
import random

# ضع التوكن الخاص ببوتك هنا
TOKEN = "8164008085:AAHmC1Ji7pzU2-1GieUMOWrN5-qWFWcD8Dc"
bot = telebot.TeleBot(TOKEN)

# قوائم أسماء
FIRST_NAMES = [
    "James","John","Robert","Michael","William","David","Richard","Joseph","Thomas","Charles",
    "Christopher","Daniel","Matthew","Anthony","Mark","Donald","Steven","Paul","Andrew","Joshua",
    "Mary","Patricia","Jennifer","Linda","Elizabeth","Barbara","Susan","Jessica","Sarah","Karen",
    "Alex","Taylor","Jordan","Casey","Riley","Morgan","Cameron","Avery","Quinn","Rowan"
]
LAST_NAMES = [
    "Smith","Johnson","Williams","Brown","Jones","Garcia","Miller","Davis","Rodriguez","Martinez",
    "Hernandez","Lopez","Gonzalez","Wilson","Anderson","Thomas","Taylor","Moore","Jackson","Martin"
]

# دالة توليد الاسم
def generate_name():
    first = random.choice(FIRST_NAMES)
    last = random.choice(LAST_NAMES)
    return f"{first} {last}"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # 🔗 روابط الأزرار
    dev_url = "https://t.me/XX_VV_88"
    channel_url = "https://t.me/G_L_S_B"

    # ⌨️ إنشاء الكيبورد
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(
        types.InlineKeyboardButton("👨‍💻 Bot Developer", url=dev_url),
        types.InlineKeyboardButton("📢 Bot Channel", url=channel_url)
    )

    # 🖼️ نص الكابشن (ترحيب + الرسالة الإنجليزية)
    caption_text = (
    "🇵🇭✨ Welcome to the *Philippine Info Generator Bot*! ✨🇵🇭\n\n"
    "🤖 I can generate random Filipino-style identity details for you.\n\n"
    "➡️ Just send */em* to receive:\n"
    "   🧑 Name\n"
    "   ✉️ Email\n"
    "   🔐 Password\n"
    "   📱 Phone Number\n\n"
    "Enjoy using the bot! 🚀"
    )

    # 🖼️ إرسال صورة مع الكابشن والكيبورد
    bot.send_photo(
        chat_id=message.chat.id,
        photo="https://t.me/G_K_L_A_K/8",
        caption=caption_text,
        parse_mode="Markdown",
        reply_markup=keyboard
    )

# أمر /em
@bot.message_handler(commands=['em'])
def send_name(message):
    bot.reply_to(message, f"🎲 اسم عشوائي:\n{generate_name()}")

# تشغيل البوت
print("✅ البوت شغال...")
bot.infinity_polling()
