# Python 3.7.3 (Windows)
# discord.py 1.5.1

import discord
import os
from po_util import role_emoji
from datetime import datetime

client = discord.Client(
    intents=discord.Intents.all(),
    chunk_guilds_at_startup=True
)


@client.event
async def on_ready():
    print("Registration Manager Connected")


async def register_user(guild: discord.Guild, registration_string: str):
    args = [s.strip() for s in registration_string.split(',')]
    name = ''.join(args[0].strip())
    discord_name = [s.strip() for s in args[2].split('#')]
    if len(discord_name) == 2:
        discord_username = discord_name[0]
        discord_discriminator = discord_name[1]
    elif len(discord_name) == 1:
        discord_username = discord_name[0]
        discord_discriminator = '0'
    else:
        print("discord name {} is invalid".format(discord_name))
        return None
    pronoun = args[3]
    badgenumber = args[8].strip()
    user: discord.Member = discord.utils.get(guild.members, name=discord_username, discriminator=discord_discriminator)
    role_id = int(args[4])
    role = discord.utils.find(lambda m: m.id == role_id, guild.roles)
    attendee_role = discord.utils.find(lambda m: "Attendee" in m.name, guild.roles)
    organizer_role = discord.utils.find(lambda m: "Organizer" in m.name, guild.roles)
    alumni_role = discord.utils.find(lambda m: "Alumni" in m.name, guild.roles)
    moderator_role = discord.utils.find(lambda m: "Moderator" in m.name, guild.roles)
    first_po_role = discord.utils.find(lambda m: "1st Protospiel Online" in m.name, guild.roles)
    if user is None:
        print("{}".format(registration_string))
        print("ERROR: user cannot be found".format())
        return None
    if role is None:
        print("{}".format(registration_string))
        print("ERROR: role cannot be found".format())
        return None
    elif organizer_role in user.roles:
        print("{}".format(registration_string))
        print("INFO: User {} is an organizer - ignoring".format(user.nick))
        return user
    else:
        if role.name in ["⏳Publisher", "🎬Press"]:
            featured_guest_role = discord.utils.get(guild.roles, name="Featured Guest")
            await user.add_roles(attendee_role, featured_guest_role, role, reason="RegistrationBot")
        else:
            await user.add_roles(attendee_role, role, reason="RegistrationBot")
        emoji = role_emoji.get(role.name, '❔')
        user_nickname = "{0}{1} ({2}) #{3}".format(emoji, name, pronoun, badgenumber)
        await user.edit(nick=user_nickname)
        if alumni_role not in user.roles and moderator_role not in user.roles:
            await user.add_roles(first_po_role, reason="RegistrationBot")
        print("INFO: User {} successfully registered as a {}".format(user.nick, role.name))
        # Also post some info to member-ids
        memberidpoststr = "{},{},{}".format(discord_username, discord_discriminator, user.id)
        memberidschannel: discord.TextChannel = discord.utils.get(guild.text_channels, name="member-ids")
        await memberidschannel.send(memberidpoststr)
        return user


async def handle_registration(message: discord.Message):
    if discord.utils.find(lambda r: r.emoji == '✔️' or r.emoji == '❓', message.reactions):
        return None
    string_to_handle = None
    if message.content.startswith("!regbot register"):
        string_to_handle = message.content[len("!regbot register"):]
    elif message.content.startswith("@RegistrationManager"):
        string_to_handle = message.content[len("@RegistrationManager"):]
    elif message.channel.name == 'member-ids': # Ignore messages in member-ids
        string_to_handle = None
    if string_to_handle:
        print("Received message {}".format(message.content))
        registered_user = await register_user(message.guild, string_to_handle)
        if registered_user:
            for role in registered_user.roles:
                if role.name in role_emoji:
                    await message.add_reaction(role_emoji[role.name])
            await message.add_reaction('✔️')
        else:
            await message.add_reaction('❓')


@client.event
async def on_message(message: discord.Message):
    try:
        if message.author == client.user:
            return
        elif message.content.startswith("!regbot batch"):
            batchfromdate = datetime.min
            batchfromstr = message.content.strip("!regbot batch")
            if len(batchfromstr) > 0:
                batchfromdate = datetime.strptime(batchfromstr, "%m/%d/%Y")
            channel_history = await message.channel.history(limit=1000, oldest_first=True, after=batchfromdate).flatten()
            for history_message in channel_history:
                print("handling message {}".format(history_message.content))
                await handle_registration(history_message)
        else:
            await handle_registration(message)
    except Exception as e:
        await message.add_reaction('❌')
        raise e

client.run(os.environ.get('PROTOSPIEL_ONLINE_BOT_DISCORD_TOKEN'))