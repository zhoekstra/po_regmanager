import discord

role_emoji = {
    "Attendee": '🎟️',
    "🥈Alumni": '🥈',
    "💡Playtester": '💡',
    "🎲Designer": '🎲',
    "🎬Press": '🎬',
    "⏳Publisher": '⏳',
    "Moderator": '🌎',
    "✨Organizer": '✨',
    "🧡1st Protospiel Online": '🧡',
    "Team Player": '♥',
    "Team♥️Hearts": '♥',
    "Team♣️Clubs": '♣',
    "Team♠️Spades": '♠',
    "Team♦️Diamonds": '♦',
    "Moderator Buddy": '🌎',
    "Task 1": '♥',
    "Task 2": '♥',
    "Task 3": '♥',
    "Task 4": '♥',
    "Task 5": '♥',
    "Task 6": '♥',
    "Congratulations": '♥',
    "🌳Treehouse": '🌳'
}

async def get_roles(guild: discord.Guild):
    return {k: discord.utils.get(guild.roles, name=k) for k, v in role_emoji.items()}


async def reply(message: discord.Message, content: str):
    await message.channel.send(content)
