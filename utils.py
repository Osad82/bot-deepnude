from glob import glob
import logging
import os

from telegram import InputMediaPhoto, ReplyKeyboardMarkup
from base import *
from config import *


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(funcName)s - %(message)s',
                    level = logging.INFO,
                    filename = 'log.log'
                    )



def get_start_menu():
    keyboard = [['Раздеть девушку 👅', 'Примеры 📷'],
                ['Баланс 💰', 'Пополнить']]
    kb = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    return kb


def load_user_data(user_id, context):
    first_name, balans = get_data_row('users', 'first_name, balans', user_id)
    context.user_data['first_name'] = first_name
    context.user_data['balans'] = balans
    return first_name, balans


def get_photo_list():
    photo_list = glob(os.path.join(IMAGES_FOLDER, 'examples', '*'))
    photo_list.remove(os.path.join(IMAGES_FOLDER, 'examples', 'Kt2VZJCsawE.jpg'))
    media_photo_list = []
    for photo in photo_list:
        photo = open(photo, 'rb')
        media_photo_list.append(InputMediaPhoto(photo))
    return media_photo_list


        







if __name__ == "__main__":
    pass