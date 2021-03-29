#alive.py 
# Made by @koi_nhi_apna...
# use with credits or else u will get strike....
import asyncio
import random
from telethon import events
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
# hehehehehe
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "BLACK BOT"

# creation by @real_tera_baap

edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/1ce15cac96b30da9eb78f.jpg"
file2 = "https://telegra.ph/file/1ce15cac96b30da9eb78f.jpg"
file3 = "https://telegra.ph/file/1ce15cac96b30da9eb78f.jpg"
file4 = "https://telegra.ph/file/1ce15cac96b30da9eb78f.jpg"
""" =======================CONSTANTS====================== """
pm_caption = "鈦伂鈦伄鈦伄 HEYA BLAC 扫謫 謪占薀扫占蓻..!! **馃敟馃敟\n\n"
pm_caption += "鈿旓笍鈿旓笍 *Yes Master, I Am Alive And Systems Are Working Perfectly.. Let's Rock Together...hehehehehe...*鈿旓笍鈿旓笍\n\n"
pm_caption += "嗉嗋紕鈽狅笌锔嶢bout My System \n\n"
pm_caption += "馃敟馃敟 *岽涐磭薀岽囜礇蕼岽徤�*馃敟馃敟 >>銆� 20.0.0\n"
pm_caption += "馃毃馃毃 *group*馃毃馃毃   >>銆� [蕽謪扫占]()\n"
pm_caption += f"馃敯馃敯*岽嶀磤s岽涐磭蕗*馃敯馃敯  >>銆� {DEFAULTUSER}\n"
pm_caption += "馃審馃審 *岽勈�岽囜磤岽涐磸蕗*馃審馃審  >>銆� [岽忈础纱岽囀�](https://t.me/black_user_bot_B)\n\n"
pm_caption += "馃敹馃敹 *channel*馃敹馃敹  >>銆� [蕽謪扫占](https://t.me/black_user_bot_B)\n\n"
pm_caption += "*clan/gang* >>銆� [         ,-.\n     ___,---.__          /'|`\          __,---,___/n,-'    \`    `-.____,-'  |  `-.____,-'    //    `-./n,'        |           ~'\     /`~           |        `./n /      ___//              `. ,'          ,  , \___      \/n|    ,-'   `-.__   _         |        ,    __,-'   `-.    |/n|   /          /\_  `   .    |    ,      _/\          \   |/n\  |           \ \`-.___ \   |   / ___,-'/ /           |  //n\  \           | `._   `\\  |  //'   _,' |           /  //n`-.\         /'  _ `---'' , . ``---' _  `\         /,-'/n``       /     \    ,='/ \`=.    /     \       ''/n |__   /|\_,--.,-.--,--._/|\   __|/n /  `./  \\`\ |  |  | /,//' \,'  \/n /   /     ||--+--|--+-/-|     \   \/n|   |     /'\_\_\ | /_/_/`\     |   |/n\   \__, \_     `~'     _/ .__/   //n `-._,-'   `-._______,-'   `-._,-'/n](https://t.me/black_user_bot_B)\n\n"
@borg.on(admin_cmd(pattern=r"alive"))

async def amireallyalive(yes):
    chat = await yes.get_chat()

    on = await borg.send_file(yes.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file1)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file4)

    await alive.delete()
    
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()
