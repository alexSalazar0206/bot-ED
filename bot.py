from http import client
import discord
import sqlite3
connectionDB = sqlite3.connect("tutorial.db")
cur = connectionDB.cursor()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!crearUsuario'):
        first_name = message.content.split(' ')[1]
        last_name = message.content.split(' ')[2]
        full_name = f'{first_name} {last_name}'
        email = message.content.split(' ')[3]
        cur.execute('INSERT INTO users (discord_id, name) VALUES (?,?)', [message.author.id, full_name])
        connectionDB.commit()
        await message.channel.send('Usuario Creado')
        print('message.author.id')

    if message.content.startswith('!borrarUsuario'):
        cur.execute('DELETE FROM users WHERE discord_id = ? ', [message.author.id])
        connectionDB.commit()
        await message.channel.send('Usuario Eliminado')

client.run('MTAzMTY1NDkyMjkxMzA2Mjk4NA.G3JG_E.M6FAH4TB8eRnhhpYRvY4MY36hK8Ewbmc0j1yek')