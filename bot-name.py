import logging
import os
import sys

from telegram import InlineQuery
from telegram.ext import (CallbackQueryHandler, CommandHandler, ConversationHandler, 
                          Filters, MessageHandler, PicklePersistence, RegexHandler, 
                          Updater)
from telegram.ext import messagequeue as mq

from threading import Thread
from config import *
from handlers import *
from messages import *

import error_handler
import utils




logging.basicConfig(format='%(asctime)s - %(levelname)s - %(funcName)s - %(message)s',
                    level = logging.INFO,
                    filename = 'bot.log'
                    )


    
my_persistence = PicklePersistence(filename='persistence_file', store_user_data=True)
mybot = Updater(TOKEN, persistence=my_persistence, use_context=True)



def stop_and_restart():
    """Gracefully stop the Updater and replace the current process with a new one"""
    mybot.stop()
    os.execl(sys.executable, sys.executable, *sys.argv)

def restart(update, context):
    update.message.reply_text('Bot is restarting...')
    Thread(target=stop_and_restart).start()


def main():   
       
    # Инициализируем MessageQueue 
    mybot.bot._msg_queue = mq.MessageQueue()
    mybot.bot._is_messages_queued_default=True


    logging.info('Бот запускается.')    

    dp = mybot.dispatcher
    

    # approve_conv = ConversationHandler(
    #     entry_points=[CallbackQueryHandler(add_or_not_user_access)], 

    #     states={
    #         '1': [MessageHandler(Filters.text, get_real_name),
    #               CallbackQueryHandler(pass_get_real_name, pattern='passs')]
    #     }, 

    #     fallbacks=[]
    # )

    

    # dp.add_handler(CallbackQueryHandler(query_handler, pattern='^start_conv'))        
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.regex('^(Раздеть девушку 👅)$'), send_me_photo))
    dp.add_handler(MessageHandler(Filters.photo, replenish_balans))
    

    dp.add_error_handler(error_handler.error)
    dp.add_handler(CommandHandler('r', restart, filters=Filters.user(DEV_ID)))

    # dp.add_handler(MessageHandler(Filters.user(TG_ADMIN_ID), send_admin_message_to_user))
    # dp.add_handler(
    #     MessageHandler(Filters.text & (~ Filters.user(TG_ADMIN_ID)), send_all_user_messages_to_admin)
    #     )


    
    # webhook_domain = 'https://python-developer.ru'    
    # PORT = 5015

    # mybot.start_webhook(listen='127.0.0.1',
    #                 port=PORT,
    #                 url_path=TOKEN,
    #                 webhook_url=f'{webhook_domain}/{TOKEN}'     
    #                 )

    # mybot.bot.set_webhook(f'{webhook_domain}/{TOKEN}')
    
    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()