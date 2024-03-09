import aiosqlite


# Добавление пользователей в бд (ПО ЗАЯВКЕ)
async def add_application_to_table(date, product, address, client_phone, full_name, chat_id):
    async with aiosqlite.connect('app/database/cryolife_database.db') as connect:
        await connect.execute('INSERT INTO users_delivery (date, product, address, сlient_phone, full_name, chat_id) VALUES (?, ?, ?, ?, ?, ?)',
                              (date, product, address, client_phone, full_name, chat_id))
        await connect.commit()


# Подсчет сколько всего было заявок
async def count_total_orders():
    async with aiosqlite.connect('app/database/cryolife_database.db') as connect:
        cursor = await connect.execute('SELECT COUNT(*) FROM users_delivery')
        count = await cursor.fetchone()
        total_orders = count[0]
        return total_orders


# Проверка есть ли юзер в бд!
async def check_user_to_db(name, chat_id):
    async with aiosqlite.connect('app/database/cryolife_database.db') as connect:
        cursor = await connect.execute('SELECT * FROM users WHERE chat_id = ?', (chat_id,))
        existing_user = await cursor.fetchone()
        if not existing_user:
            await connect.execute('INSERT INTO users (username, chat_id) VALUES (?, ?)', (name, chat_id))
            await connect.commit()


# Подсчет сколько всего пользователей в бд
async def count_users_in_db():
    async with aiosqlite.connect('app/database/cryolife_database.db') as connect:
        cursor = await connect.execute('SELECT COUNT(*) FROM users')
        count = await cursor.fetchone()
        return count[0]  # Возвращаем количество пользователей из первой колонки


# Получение всех chat_id Для рассылки
async def get_all_chat_ids():
    async with aiosqlite.connect('app/database/cryolife_database.db') as connect:
        cursor = await connect.execute('SELECT chat_id FROM users')
        all_chat_ids = await cursor.fetchall()
        return [id[0] for id in all_chat_ids]


# Получение текста из бд
async def get_text(id_text):
    async with aiosqlite.connect('app/database/cryolife_database.db') as connect:
        cursor = await connect.execute('SELECT text FROM price_list WHERE id = ?', (id_text,))
        result = await cursor.fetchone()
        await connect.commit()
        return result[0] if result else None


# Обновление текста в бд
async def add_text(new_text, id_text):
    async with aiosqlite.connect('app/database/cryolife_database.db') as connect:
        await connect.execute('UPDATE price_list SET text = ? WHERE id = ?', (new_text, id_text,))
        await connect.commit()






