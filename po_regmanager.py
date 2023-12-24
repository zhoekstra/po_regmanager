# Python 3.7.3 (Windows)
# discord.py 1.5.1

import discord
import os
from po_util import role_emoji, po_roles
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
    #community_role = discord.utils.find(lambda m: m.id==po_roles.COMMUNITY_ROLE_ID, guild.roles)
    attendee_role = discord.utils.find(lambda m: m.id == po_roles.ATTENDEE_ROLE_ID, guild.roles)
    registration_reason = args[1].strip()
    alumni_role = discord.utils.find(lambda m: m.id == po_roles.ALUMNI_ROLE_ID, guild.roles)
    if registration_reason in ('Designer', 'Playtester', 'Moderator'):
        role_id = int(args[4])
        event_role = discord.utils.find(lambda m: m.id == role_id, guild.roles)
        event_roles = [event_role, attendee_role]
        emoji = role_emoji.get(event_role.id, '❔')
        main_role = event_role
    else:
        event_roles = []
        if alumni_role not in user.roles:
            #emoji = role_emoji.get(community_role.id, '❔')
            emoji - role_emoji.get(alumni_role.id, '❔')
        else:
            emoji = role_emoji.get(alumni_role.id, '❔')
        #main_role = community_role
    #all_roles = [community_role, *event_roles]
    all_roles = [*event_roles]
    organizer_role = discord.utils.find(lambda m: m.id == po_roles.ORGANIZER_ROLE_ID, guild.roles)
    moderator_role = discord.utils.find(lambda m: m.id == po_roles.MODERATOR_ROLE_ID, guild.roles)
    first_po_role = discord.utils.find(lambda m: m.id == po_roles.FIRST_PO_ROLE_ID, guild.roles)
    info_roles_txt = args[12:]
    info_role_ids = [int(r) for r in info_roles_txt if(r != '')]
    info_roles = [discord.utils.find(lambda m: m.id == r, guild.roles) for r in info_role_ids]
    if user is None:
        print("{}".format(registration_string))
        print("ERROR: user cannot be found".format())
        return None
    # if role is None:
    #     print("{}".format(registration_string))
    #     print("ERROR: role cannot be found".format())
    #     return None
    elif organizer_role in user.roles:
        print("{}".format(registration_string))
        print("INFO: User {} is an organizer - ignoring".format(user.nick))
        return user
    else:
        await user.add_roles(*all_roles, reason="RegistrationBot")
        
        user_nickname = "{0}{1} ({2}) #{3}".format(emoji, name, pronoun, badgenumber)
        await user.edit(nick=user_nickname)
        if alumni_role not in user.roles and moderator_role not in user.roles:
            await user.add_roles(first_po_role, reason="RegistrationBot")
        print("INFO: User {} successfully registered as a {}".format(user.nick, main_role.name))
        if len(info_roles) > 0:
            await user.add_roles(*info_roles, reason="RegistrationBot")
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
                if role.id in role_emoji:
                    await message.add_reaction(role_emoji[role.id])
            await message.add_reaction('✅')
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