from telegram import ReplyKeyboardMarkup

def get_start_menu():
    keyboard = [['Раздеть девушку 👅', 'Примеры'],
                ['Баланс', 'Пополнить']]
    kb = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    return kb








if __name__ == "__main__":
    pass