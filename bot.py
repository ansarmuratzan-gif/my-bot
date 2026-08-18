import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CallbackQueryHandler, CommandHandler, ContextTypes

# Токенді Render-дегі Environment Variables-тен алады немесе осында жазасыз
TOKEN = os.getenv("8985821118", "AAHq6reIMwQmqr8UmeLtdb_VXfpFKGkYyj8")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Батырма жасау
    keyboard = [[InlineKeyboardButton("🔥 FREE FIRE 2022 ЖҮКТЕУ", callback_data="send_apk")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "Сәлем! Төмендегі батырманы басып, файлды жүктеп алыңыз:", 
        reply_markup=reply_markup
    )

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer() # Батырманың айналғанын бірден тоқтатады

    if query.data == "send_apk":
        await query.message.reply_text("Файл жіберілуде... ⏳")
        
        try:
            # Бұл жерге файлдың Telegram-дағы ID кодын жазасыз (төменде қалай алу керектігі жазылған)
            FILE_ID = "TELEGRAM_FILE_ID_КОДЫНЫЗДЫ_ОСЫ_ЖЕРГЕ_ЖАЗЫҢЫЗ"
            
            await context.bot.send_document(
                chat_id=query.message.chat_id,
                document=FILE_ID,
                caption="Міне, сіз сұраған Free Fire 2022 файлы! 📥"
            )
        except Exception as e:
            await query.message.reply_text(f"Қате шықты: {e}")

def main():
    app = ApplicationBuilder().token(TOKEN).read_timeout(30.0).write_timeout(30.0).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_click))

    print("Бот іске қосылды...")
    app.run_polling()

if __name__ == "__main__":
    main()

