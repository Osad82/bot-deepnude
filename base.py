import logging
import sqlite3



logging.basicConfig(format='%(asctime)s - %(levelname)s - %(funcName)s - %(message)s',
                    level = logging.INFO,
                    filename = 'log.log'
                    )



def create_base():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()


    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        user_id         INTEGER NOT NULL PRIMARY KEY,
                        first_name      TEXT,
                        balans          INTEGER)'''
                    )



    conn.commit()
    conn.close()


def get_initial_data(update):
    user_id = update.message.from_user.id
    first_name = update.message.from_user.first_name
    initial_user_data = (user_id, first_name, 0)
    return initial_user_data


def write_initial_data_to_base(data):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('INSERT OR IGNORE INTO users (user_id, first_name, balans) VALUES (?, ?, ?)', data)
    conn.commit()
    conn.close()







def write_entry_to_base(column, entry, user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(f'UPDATE users SET {column}=? WHERE user_id=?', (entry, user_id))
    conn.commit()
    conn.close()


def write_cat_to_base(entry):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('INSERT OR IGNORE INTO cat (cat_name) VALUES (?)', (entry,))
    conn.commit()
    conn.close()


def write_sub_cat_to_base(sub_cat_name, cat_id):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT OR IGNORE INTO sub_cat 
                    (sub_cat_name, cat_id) 
                    VALUES (?, ?)''', 
                    (sub_cat_name, cat_id))
    conn.commit()
    conn.close()


def write_goods_to_base(data):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT OR IGNORE INTO goods
                    (title, description, photo, url, sub_cat_id, cat_id)
                    VALUES (?, ?, ?, ?, ?, ?)''', 
                    data)
    conn.commit()
    conn.close()


def get_data_row(table, column, user_id):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute(f'SELECT {column} FROM {table} WHERE user_id=?', (user_id,))
    row = cursor.fetchall()
    conn.commit()
    conn.close()
    return row[0]


def get_subcat_list(cat_id):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute(f'SELECT sub_cat_name, id FROM sub_cat WHERE cat_id=?', (cat_id,))
    data_list = cursor.fetchall()
    conn.commit()
    conn.close()
    return data_list


def list_from_base_column(table, 
                          column, 
                          sort=False, 
                          sort_column=None,
                          filter_col=None,
                          filter_val=None): # Возвращает список значений столбца
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    if sort:
        cursor.execute(f'SELECT {column} FROM {table} ORDER by {sort_column}')
    else:
        cursor.execute(f'SELECT {column} FROM {table}')
    if filter_col:
        cursor.execute(f'SELECT {column} FROM {table} WHERE {filter_col}=?', (filter_val,))
    column_list = cursor.fetchall()
    conn.commit()
    conn.close()
    return column_list # [('-yGIB7rf?NKU0Dk',), (None,)]


def delete_row(table, id):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute(f'''DELETE
                       FROM {table}
                       WHERE id=?''', (id,))
    conn.commit()
    conn.close()


def get_goods_titles(good_title):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute(f'SELECT id, title FROM goods WHERE title LIKE "%{good_title}%"')
    data_list = cursor.fetchall()
    conn.commit()
    conn.close()
    return data_list
