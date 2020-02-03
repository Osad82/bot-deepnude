from utils import *



def start(update, context):
    update.message.reply_text(
        'Здесь вы можете раздеть девушку',
        reply_markup=get_start_menu())



def send_me_photo(update, context):
    photo_path = os.path.join(os.getcwd(), 'images', 'examples', 'Kt2VZJCsawE.jpg')
    update.message.reply_text(msg_send_me_photo)
    context.bot.send_photo(
        chat_id=update.message.chat_id,
        photo=open(photo_path, 'rb')
    )


def replenish_balans(update, context):
    balans = context.user_data['balans']
    update.message.reply_text(msg_replenish_balans(balans, 'https://vk.cc/ajQ7Qk'))






if __name__ == "__main__":
    pass