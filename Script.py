class script(object):
    START_TXT = """𝙷𝙴𝙻𝙾 {},
𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 <a href=https://t.me/{}>{}</a>, 𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙼𝙾𝚅𝙸𝙴𝚂, 𝙹𝚄𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙴𝙽𝙹𝙾𝚈 😍"""
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT = """✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: {}
✯ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href=https://t.me/mr_yoouu>ሃዐሁ</a>
✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
✯ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
✯ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: 𝙷𝙴𝚁𝙾𝙺𝚄
✯ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: v1.0.1 [ 𝙱𝙴𝚃𝙰 ]"""
    SOURCE_TXT = """<b>NOTE:</b>
𝙼𝚘𝚟𝚒𝚎𝚜: <a href=https://t.me/mw_all>𝙏𝙝𝙚 𝙈𝙪𝙨𝙩𝙒𝙖𝙩𝙘𝙝 - 𝙈𝙤𝙫𝙞𝙚𝙨</a>
𝚂𝚎𝚛𝚒𝚎𝚜: <a href=https://t.me/mw_tvseries>𝙏𝙝𝙚 𝙈𝙪𝙨𝙩𝙒𝙖𝙩𝙘𝙝 - 𝙎𝙚𝙧𝙞𝙚𝙨</a>
𝙾𝚏𝚏𝚒𝚌𝚒𝚊𝚕: <a href=https://t.me/themustwatch>𝖳𝗁𝖾 𝖬𝗎𝗌𝗍𝖶𝖺𝗍𝖼𝗁!</a>
𝙶𝚛𝚘𝚞𝚙: <a href=https://t.me/mw_chats>𝗧𝗵𝗲 𝗠𝘂𝘀𝘁𝗪𝗮𝘁𝗰𝗵 - ᴄʜᴀᴛꜱ</a>

𝖮𝖶𝖭𝖤𝖱:<a href=https://t.me/mr_yoouu>ሃዐሁ</a>"""
    MANUELFILTER_TXT = """𝖧𝖾𝗅𝗉: 𝖥𝗂𝗅𝗍𝖾𝗋

- 𝗙𝗶𝗹𝘁𝗲𝗿 𝗶𝘀 𝘁𝗵𝗲 𝗳𝗲𝗮𝘁𝘂𝗿𝗲 𝘄𝗲𝗿𝗲 𝘂𝘀𝗲𝗿𝘀 𝗰𝗮𝗻 𝘀𝗲𝘁 𝗮𝘂𝘁𝗼𝗺𝗮𝘁𝗲𝗱 𝗿𝗲𝗽𝗹𝗶𝗲𝘀 𝗳𝗼𝗿 𝗮 𝗽𝗮𝗿𝘁𝗶𝗰𝘂𝗹𝗮𝗿 𝗸𝗲𝘆𝘄𝗼𝗿𝗱 𝗮𝗻𝗱 𝗕𝗼𝘁 𝘄𝗶𝗹𝗹 𝗿𝗲𝘀𝗽𝗼𝗻𝗱 𝘄𝗵𝗲𝗻𝗲𝘃𝗲𝗿 𝗮 𝗸𝗲𝘆𝘄𝗼𝗿𝗱 𝗶𝘀 𝗳𝗼𝘂𝗻𝗱 𝘁𝗵𝗲 𝗺𝗲𝘀𝘀𝗮𝗴𝗲

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """𝖧𝖾𝗅𝗉: 𝖡𝗎𝗍𝗍𝗈𝗇

- 𝗕𝗼𝘁 𝘀𝘂𝗽𝗽𝗼𝗿𝘁𝘀 𝗯𝗼𝘁𝗵 𝘂𝗿𝗹 𝗮𝗻𝗱 𝗮𝗹𝗲𝗿𝘁 𝗶𝗻𝗹𝗶𝗻𝗲 𝗯𝘂𝘁𝘁𝗼𝗻𝘀.

<b>NOTE:</b>
𝟭. 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝘄𝗶𝗹𝗹 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝘀 𝘆𝗼𝘂 𝘁𝗼 𝘀𝗲𝗻𝗱 𝗯𝘂𝘁𝘁𝗼𝗻𝘀 𝘄𝗶𝘁𝗵𝗼𝘂𝘁 𝗮𝗻𝘆 𝗰𝗼𝗻𝘁𝗲𝗻𝘁, 𝘀𝗼 𝗰𝗼𝗻𝘁𝗲𝗻𝘁 𝗶𝘀 𝗺𝗮𝗻𝗱𝗮𝘁𝗼𝗿𝘆.
𝟮. 𝗕𝗼𝘁 𝘀𝘂𝗽𝗽𝗼𝗿𝘁𝘀 𝗯𝘂𝘁𝘁𝗼𝗻𝘀 𝘄𝗶𝘁𝗵 𝗮𝗻𝘆 𝘁𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗺𝗲𝗱𝗶𝗮 𝘁𝘆𝗽𝗲.
𝟯. 𝗕𝘂𝘁𝘁𝗼𝗻𝘀 𝘀𝗵𝗼𝘂𝗹𝗱 𝗯𝗲 𝗽𝗿𝗼𝗽𝗲𝗿𝗹𝘆 𝗽𝗮𝗿𝘀𝗲𝗱 𝗮𝘀 𝗺𝗮𝗿𝗸𝗱𝗼𝘄𝗻 𝗳𝗼𝗿𝗺𝗮𝘁

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/MW_Moviesbot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """𝖧𝖾𝗅𝗉: 𝖠𝗎𝗍𝗈 𝖥𝗂𝗅𝗍𝖾𝗋

<b>NOTE:</b>
𝟭. 𝗠𝗮𝗸𝗲 𝗺𝗲 𝘁𝗵𝗲 𝗮𝗱𝗺𝗶𝗻 𝗼𝗳 𝘆𝗼𝘂𝗿 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 𝗶𝗳 𝗶𝘁'𝘀 𝗽𝗿𝗶𝘃𝗮𝘁𝗲.
𝟮. 𝗺𝗮𝗸𝗲 𝘀𝘂𝗿𝗲 𝘁𝗵𝗮𝘁 𝘆𝗼𝘂𝗿 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 𝗱𝗼𝗲𝘀 𝗻𝗼𝘁 𝗰𝗼𝗻𝘁𝗮𝗶𝗻𝘀 𝗰𝗮𝗺𝗿𝗶𝗽𝘀, 𝗽𝗼𝗿𝗻 𝗮𝗻𝗱 𝗳𝗮𝗸𝗲 𝗳𝗶𝗹𝗲𝘀.
𝟯. 𝗙𝗼𝗿𝘄𝗮𝗿𝗱 𝘁𝗵𝗲 𝗹𝗮𝘀𝘁 𝗺𝗲𝘀𝘀𝗮𝗴𝗲 𝘁𝗼 𝗺𝗲 𝘄𝗶𝘁𝗵 𝗾𝘂𝗼𝘁𝗲𝘀.
 𝗜'𝗹𝗹 𝗮𝗱𝗱 𝗮𝗹𝗹 𝘁𝗵𝗲 𝗳𝗶𝗹𝗲𝘀 𝗶𝗻 𝘁𝗵𝗮𝘁 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 𝘁𝗼 𝗺𝘆 𝗱𝗯."""
    CONNECTION_TXT = """𝖧𝖾𝗅𝗉: 𝖢𝗈𝗇𝗇𝖾𝖼𝗍𝗂𝗈𝗇

- 𝗨𝘀𝗲𝗱 𝘁𝗼 𝗰𝗼𝗻𝗻𝗲𝗰𝘁 𝗯𝗼𝘁 𝘁𝗼 𝗣𝗠 𝗳𝗼𝗿 𝗺𝗮𝗻𝗮𝗴𝗶𝗻𝗴 𝗳𝗶𝗹𝘁𝗲𝗿𝘀 
- 𝗶𝘁 𝗵𝗲𝗹𝗽𝘀 𝘁𝗼 𝗮𝘃𝗼𝗶𝗱 𝘀𝗽𝗮𝗺𝗺𝗶𝗻𝗴 𝗶𝗻 𝗴𝗿𝗼𝘂𝗽𝘀.

<b>NOTE:</b>
𝟭. 𝗢𝗻𝗹𝘆 𝗮𝗱𝗺𝗶𝗻𝘀 𝗰𝗮𝗻 𝗮𝗱𝗱 𝗮 𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗶𝗼𝗻.
𝟮. 𝗦𝗲𝗻𝗱 <code>/connect</code> 𝗳𝗼𝗿 𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗶𝗻𝗴 𝗺𝗲 𝘁𝗼 𝘂𝗿 𝗣𝗠

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """𝖧𝖾𝗅𝗉: <b>𝖤𝗑𝗍𝗋𝖺 𝖬𝗈𝖽𝗎𝗅𝖾𝗌</b>

<b>NOTE:</b>
𝗧𝗵𝗲𝘀𝗲 𝗮𝗿𝗲 𝘁𝗵𝗲 𝗲𝘅𝘁𝗿𝗮 𝗳𝗲𝗮𝘁𝘂𝗿𝗲𝘀

<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
