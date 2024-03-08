import aiosqlite


async def check_user_to_db(name, chat_id):
    async with aiosqlite.connect('app/database/cryolife_database.db') as connect:
        cursor = await connect.execute('SELECT * FROM users WHERE chat_id = ?', (chat_id,))
        existing_user = await cursor.fetchone()
        if not existing_user:
            await connect.execute('INSERT INTO users (username, chat_id) VALUES (?, ?)', (name, chat_id))
            await connect.commit()


async def get_all_chat_ids():
    async with aiosqlite.connect('app/database/cryolife_database.db') as connect:
        cursor = await connect.execute('SELECT chat_id FROM users')
        all_chat_ids = await cursor.fetchall()
        return [id[0] for id in all_chat_ids]


async def get_text(id_text):
    async with aiosqlite.connect('app/database/cryolife_database.db') as connect:
        cursor = await connect.execute('SELECT text FROM price_list WHERE id = ?', (id_text,))
        result = await cursor.fetchone()
        await connect.commit()
        return result[0] if result else None


async def add_text(new_text, id_text):
    async with aiosqlite.connect('app/database/cryolife_database.db') as connect:
        await connect.execute('UPDATE price_list SET text = ? WHERE id = ?', (new_text, id_text,))
        await connect.commit()






