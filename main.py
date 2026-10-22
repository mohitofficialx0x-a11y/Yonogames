import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Token yahan daalein
TOKEN = "8677181982:AAFmGHtPKjOZqOHxI23LiKixVV1aNZB9r1c"

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

APPS_LIST = [
    {"name": "🎰 Spin Crush", "bonus": "₹100 Bonus", "link": "https://3xndhpkhk03.com/?code=ADEJXPMF9ME&t=1791682294"},
    {"name": "🎮 Yono Arcade", "bonus": "₹100 Bonus", "link": "https://yonoreferral8.com/?code=N347JULF3PK&t=1791683010"},
    {"name": "🔥 Spin 777", "bonus": "₹100 Bonus", "link": "http://spin777ee.com/?code=RHX29F3M1LL&t=1791683198"},
    {"name": "🃏 Yono Rummy", "bonus": "₹100 Bonus", "link": "https://yonorummy063.com/?code=MPXALT2UBS2&t=1791683265"},
    {"name": "💥 Yono 777", "bonus": "₹100 Bonus", "link": "https://yono777hub.online/?code=F9MGVJ2JANK&t=1791683360"},
    {"name": "👑 Rumble Rummy", "bonus": "₹100 Bonus", "link": "https://rumblerummyag.com/?code=L9TZZYKQMMY&t=1791683587"}
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("🔥 All Yono Apps", callback_data="all_apps")],
        [InlineKeyboardButton("🎁 Top Bonus Apps", callback_data="bonus_apps")],
        [InlineKeyboardButton("📢 Telegram Channel", url="https://t.me/THEAURA01"),
         InlineKeyboardButton("📸 Instagram", url="https://www.instagram.com/mohit__fzx")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    welcome_msg = (
        "<b>Yono Apps Ka Market 💥</b>\n\n"
        "Welcome Mohit bhai ke Official Bot par! 🚀\n"
        "Niche diye gaye buttons par click karke top Yono apps download karein:"
    )
    if update.message:
        await update.message.reply_text(welcome_msg, parse_mode="HTML", reply_markup=reply_markup)
    else:
        await update.callback_query.edit_message_text(welcome_msg, parse_mode="HTML", reply_markup=reply_markup)

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data in ["all_apps", "bonus_apps"]:
        keyboard = []
        for app in APPS_LIST:
            keyboard.append([InlineKeyboardButton(f"{app['name']} ({app['bonus']})", url=app['link'])])
        keyboard.append([InlineKeyboardButton("🔙 Back To Menu", callback_data="back_home")])
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("<b>🚀 Top Working Yono Apps List:</b>", parse_mode="HTML", reply_markup=reply_markup)
    
    elif query.data == "back_home":
        await start(update, context)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_click))
    print("Bot is live! 🚀")
    app.run_polling()

if __name__ == "__main__":
    main()
