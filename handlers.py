import logging
import os


from messages import *
from utils import *


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(funcName)s - %(message)s',
                    level = logging.INFO,
                    filename = 'log.log'
                    )



def start(update, context):
    data = get_initial_data(update)
    write_initial_data_to_base(data)
    update.message.reply_text(
        'Здесь вы можете раздеть девушку',
        reply_markup=get_start_menu())


'''РАЗДЕТЬ ДЕВУШКУ '''

def send_me_photo(update, context):
    photo_path = os.path.join(os.getcwd(), 'images', 'examples', 'Kt2VZJCsawE.jpg')
    update.message.reply_text(msg_send_me_photo)
    context.bot.send_photo(
        chat_id=update.message.chat_id,
        photo=open(photo_path, 'rb')
    )


def replenish_balans(update, context):
    user_id = update.message.from_user.id
    _, balans = load_user_data(user_id, context)    
    update.message.reply_text(msg_replenish_balans(balans, 'https://vk.cc/ajQ7Qk'))




'''ПРИМЕРЫ '''

def examples_photo(update, context):
    logging.info('Нажал "Примеры"...')
    update.message.reply_text(msg_examples_photo)
    context.bot.send_media_group(
        chat_id=update.message.chat_id, 
        media=get_photo_list()
    )
    



'''БАЛАНС '''

def get_balans(update, context):
    pass






def get_file_id(update, context):
    file_id = update.message.photo[-1].file_id
    logging.info(f'file_id = {file_id}')






if __name__ == "__main__":
    pass