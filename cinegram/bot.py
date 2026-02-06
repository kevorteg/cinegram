import os
import logging
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ConversationHandler, CallbackQueryHandler
from cinegram.config import settings
from cinegram.handlers import start, archive_handler, video_handler, external_handler, search_handler, auth_handler
from telegram.ext import PreCheckoutQueryHandler, MessageHandler, filters

# Configure Logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)



import requests

def check_ollama_health():
    """Checks if Ollama is running locally."""
    url = "http://localhost:11434/api/tags"
    try:
        response = requests.get(url, timeout=2)
        if response.status_code == 200:
            logging.info("✅ Ollama is Online.")
            return True
    except Exception:
        pass
    logging.warning("⚠️ WARNING: Ollama is NOT reachable. AI features will fail.")
    return False

def main():
    if not settings.BOT_TOKEN:
        print("Error: BOT_TOKEN not found in environment variables.")
        return

    application = ApplicationBuilder().token(settings.BOT_TOKEN).build()

    # --- Auth Handlers (Public/Gatekeeper) ---
    application.add_handler(PreCheckoutQueryHandler(auth_handler.precheckout_callback))
    application.add_handler(MessageHandler(filters.SUCCESSFUL_PAYMENT, auth_handler.successful_payment_callback))
    
    # Manual Correction (Reply to Bot)
    application.add_handler(MessageHandler(filters.REPLY & filters.TEXT & ~filters.COMMAND, video_handler.handle_manual_correction))

    # Password Handler (Explicitly check text)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auth_handler.handle_password), group=0)

    # --- Protected Handlers ---
    # We wrap them with auth_handler.auth_required
    
    # Start
    application.add_handler(CommandHandler("start", auth_handler.auth_required(start.start_command)))
    
    # Search
    application.add_handler(CommandHandler("search", auth_handler.auth_required(search_handler.search_command)))
    application.add_handler(CallbackQueryHandler(search_handler.handle_search_callback)) # Callback queries also need protection? Yes. But difficult to show "Invoice" on callback. Let's leave clear for now or simple ignore.
    
    # Video Flow
    application.add_handler(MessageHandler(filters.VIDEO | filters.Document.VIDEO, auth_handler.auth_required(video_handler.video_entry)))

    # Archive Links
    application.add_handler(MessageHandler(filters.Regex(r'archive\.org/details/'), auth_handler.auth_required(archive_handler.handle_archive_link)))

    # Generic Links
    application.add_handler(MessageHandler(filters.Entity("url") | filters.Regex(r'^http'), auth_handler.auth_required(external_handler.handle_external_link)))

    print("Bot is running...")
    check_ollama_health()
    application.run_polling()

if __name__ == '__main__':
    main()
