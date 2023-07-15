import discord

roles = [
    (690972325922865202, '@everyone'),  # 0
    (690972758309470238, '✨Organizer'),  # 1
    (690979800566726676, '🎲Designer'),  # 2
    (690979836591603783, '💡Playtester'),  # 3
    (690988134481264671, 'Moderator'),  # 4
    (693261471345541231, '⏳Publisher'),  # 5
    (693622605755973803, 'Front Desk'),  # 6
    (694329301507637288, 'AVC S23'),  # 7
    (703054914334621776, '🎬Press'),  # 8
    (703061760126746704, 'Attendee'),  # 9
    (720818967282843719, '🥈Alumni'),  # 10
    (730432369659609179, 'MemberList'),  # 11
    (730998570215407656, 'Training'),  # 12
    (732060185983451238, 'Registration'),  # 13
    (761315681077559346, '🧩Info Only'),  # 14
    (765042505456025682, 'ProtospielOnlineBot'),  # 15
    (782795102845927444, 'ModMail'),  # 16
    (803788591770894378, 'Integrately'),  # 17
    (821938255095922688, 'Administrator'),  # 18
    (896871594796908565, 'Team♥️Hearts'),  # 19
    (896874202802552893, 'Team♦️Diamonds'),  # 20
    (896874579413336094, 'Team♣️Clubs'),  # 21
    (896874645947580437, 'Team♠️Spades'),  # 22
    (932083165747642369, 'NmcLogger'),  # 23
    (937831926465708102, 'ProtoOnBotManager'),  # 24
    (937951541296500756, 'Team Player'),  # 25
    (938583561139798069, 'Restream'),  # 26
    (938862838049566720, '🧡1st Protospiel Online'),  # 27
    (940284046817239051, 'YAGPDB.xyz'),  # 28
    (956075264511717437, 'Twitch Crew'),  # 29
    (956077229387964456, 'Twitch Host'),  # 30
    (956077373986578472, 'Twitch Player'),  # 31
    (992271340335812659, 'Event Prep Mentor'),  # 32
    (994419545907413044, 'Task 1'),  # 33
    (994425213221609553, 'Task 2'),  # 34
    (994425331228356628, 'Task 3'),  # 35
    (994425374052192306, 'Task 4'),  # 36
    (994425409775083521, 'Task 5'),  # 37
    (994425446991138897, 'Task 6'),  # 38
    (994425498061000834, 'Congratulations'),  # 39
    (994425573084504064, '🌳Treehouse'),  # 40
    (994443862758137937, 'Admin Support'),  # 41
    (999065260969431140, 'Ambassador'),  # 42
    (1000156672389566595, 'Special Guest'),  # 43
    (1001329784678260786, 'Server Booster'),  # 44
    (1004473646074576916, 'Buddy Match'),  # 45
    (1015272420824846426, 'Event Challenge'),  # 46
    (1017841541164830810, 'Refunded'),  # 47
    (1102733286717001788, '🌎May23 Mod'),  # 48
    (1118942069776470206, 'Team PO'),  # 49
    (1123327585879871539, 'New PO Bot'),  # 50
    (1123734372349120562, 'Newsletter Writer'),  # 51
    (1123736301615730768, 'Aug23 Sponsor'),  # 52
    (1123750707951058954, '⛱️Casual Gamer'),  # 53
    (1123752027361648672, '⛵Heavy Gamer'),  # 54
    (1123752176230072350, '🌊Medium Gamer'),  # 55
    (1123752360833974372, '⏰Medium Upcoming Tester'),  # 56
    (1123758009751982172, '⏲️Casual Upcoming Tester'),  # 57
    (1123758172847476876, '🕰️Heavy Upcoming Tester'),  # 58
    (1123768221397418084, '🖥️Screentop User'),  # 59
    (1123768496631840788, '🎠TTP User'),  # 60
    (1123768688949080094, '🃏PCIO User'),  # 61
    (1123768864166137856, '🧊Tabletopia User')  # 62
]


class role_list:
    ATTENDEE_ROLE_ID = roles[9][0]
    ORGANIZER_ROLE_ID = roles[1][0]
    ALUMNI_ROLE_ID = roles[10][0]
    MODERATOR_ROLE_ID = roles[48][0]
    FIRST_PO_ROLE_ID = roles[27][0]
    PUBLISHER_ROLE_ID = roles[5][0]
    PRESS_ROLE_ID = roles[8][0]
    PLAYTESTER_ROLE_ID = roles[3][0]
    DESIGNER_ROLE_ID = roles[2][0]
    TEAM_PLAYER_ROLE_ID = roles[25][0]
    TEAM_HEARTS_ROLE_ID = roles[19][0]
    TEAM_CLUBS_ROLE_ID = roles[21][0]
    TEAM_SPADES_ROLE_ID = roles[22][0]
    TEAM_DIAMONDS_ROLE_ID = roles[20][0]
    MODERATOR_BUDDY_ROLE_ID = roles[45][0]
    TASK_1_ROLE_ID = roles[33][0]
    TASK_2_ROLE_ID = roles[34][0]
    TASK_3_ROLE_ID = roles[35][0]
    TASK_4_ROLE_ID = roles[36][0]
    TASK_5_ROLE_ID = roles[37][0]
    TASK_6_ROLE_ID = roles[38][0]
    CONGRATULATIONS_ROLE_ID = roles[39][0]
    TREEHOUSE_ROLE_ID = roles[40][0]


po_roles = role_list()

role_emoji = {
    po_roles.ATTENDEE_ROLE_ID: '🎟️',
    po_roles.ALUMNI_ROLE_ID: '🥈',
    po_roles.PLAYTESTER_ROLE_ID: '💡',
    po_roles.DESIGNER_ROLE_ID: '🎲',
    po_roles.PRESS_ROLE_ID: '🎬',
    po_roles.PUBLISHER_ROLE_ID: '⏳',
    po_roles.MODERATOR_ROLE_ID: '🌎',
    po_roles.ORGANIZER_ROLE_ID: '✨',
    po_roles.FIRST_PO_ROLE_ID: '🧡',
    po_roles.TEAM_PLAYER_ROLE_ID: '♥',
    po_roles.TEAM_HEARTS_ROLE_ID: '♥',
    po_roles.TEAM_CLUBS_ROLE_ID: '♣',
    po_roles.TEAM_SPADES_ROLE_ID: '♠',
    po_roles.TEAM_DIAMONDS_ROLE_ID: '♦',
    po_roles.MODERATOR_BUDDY_ROLE_ID: '🌎',
    po_roles.TASK_1_ROLE_ID: '♥',
    po_roles.TASK_2_ROLE_ID: '♥',
    po_roles.TASK_3_ROLE_ID: '♥',
    po_roles.TASK_4_ROLE_ID: '♥',
    po_roles.TASK_5_ROLE_ID: '♥',
    po_roles.TASK_6_ROLE_ID: '♥',
    po_roles.CONGRATULATIONS_ROLE_ID: '♥',
    po_roles.TREEHOUSE_ROLE_ID: '🌳'
}


async def get_roles(guild: discord.Guild):
    return {k: discord.utils.get(guild.roles, id=k) for k, v in roles}


async def reply(message: discord.Message, content: str):
    await message.channel.send(content)
