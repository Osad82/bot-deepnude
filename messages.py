EMOJI = {
    'target': '🎯',
    'money_bag': '💰',
    'money_with_wings': '💸',
    'calendar': '📅',
    'fire': '🔥',
    'wrapped_gift': '🎁',
    'megaphone': '📣',
    'sunglasses': '😎',
    'hand_right': '👉',
    'bar_chart': '📊',
    'ok_hand': '👌',
    'hand_pointing_down': '👇',
    'thumbs_up': '👍',
    'thinking_face': '🤔',
    'purse': '👛',
    'waving_hand': '👋',
    'money_mouth_face': '🤑',
    'trophy': '🏆',
    'winking_face': '😉',
    'foot': '👣',
    'double_exclamation_mark': '‼️',
    'shrug': '🤷<200d>♂️',
    'key': '🔑'
    
    }


msg_send_me_photo = '''Пришлите мне фото девушки, которую желаете раздеть 👸

Фотография будет обработана с помощью ИИ 🤖

Пример:''' 


def msg_replenish_balans(balans, url):
    text = f'''Пополните баланс, чтобы продолжить!

💰 Баланс: {str(balans)} p
💶 Цена обработки: 50 р

Пополнить 👉 {url} (комиссия 3%)'''
    return text


msg_examples_photo = '''ВНИМАНИЕ 🔞

Примеры обработаны цензурой!
На выходе получаются фото без цензуры!''' 




if __name__ == "__main__":
    pass
