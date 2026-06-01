from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "توكنك_هنا"
WEB_APP_URL = "https://walefalham-ctrl.github.io/Aziz-store/"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton(
        "🛒 فتح المتجر",
        web_app=WebAppInfo(url=WEB_APP_URL)
    )]]
    await update.message.reply_text(
        "أهلاً بك في AZIZ STORE! 🎮",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def receive_order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.effective_message.web_app_data.data
    await update.message.reply_text(f"✅ استلمنا طلبك:\n\n{data}")

if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, receive_order))
    app.run_polling()
