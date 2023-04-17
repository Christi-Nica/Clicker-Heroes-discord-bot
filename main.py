import discord
import requests

intents = discord.Intents.all()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    guild_name = message.content[6:]
    data = {
        'uid': '0',
        'passwordHash': '0',
        'highestZoneReached': '0',
        'guildName': guild_name,
    }
    response = requests.get(f'https://guilds.clickerheroes.com/clans/findGuild.php', params=data)
    guild_info = response.json()
    ids_and_nicknames = {}
    c = 1
    if message.content.startswith('/clan'):
        if guild_info['success']:
            guild_data = guild_info['result']['guild']
            guild_name = guild_data['name']
            bot_message = f'>                                      **{guild_name}**\n> `MEMBERS                   HZE                      `'
            guild_members = guild_info['result']['guildMembers']
            for i in range(len(guild_members)):
                member = guild_members[str(i)]
                ids_and_nicknames[c] = member['uid']
                c += 1
                ids_and_nicknames[c] = member['nickname']
                c += 1
                bot_message += f'\n> `{member["nickname"]:<25} {member["highestZone"]:<25}`'
            await message.channel.send(bot_message)
        else:
            await message.channel.send(f'Guild not found.')


client.run('MTA3MDc0MzkwMTYyOTA3MTQwMg.GPCQAq.jLtu0GmJLi3Nk0hGVmZI2nCIXNk45NwG5yvwgM')