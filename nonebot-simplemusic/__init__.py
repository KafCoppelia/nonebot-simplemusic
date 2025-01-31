from nonebot import on_command
from nonebot import logger
from nonebot.params import CommandArg
from nonebot.adapters.onebot.v11 import Bot, Message, GroupMessageEvent
from . import data_source
from nonebot.adapters.onebot.v11 import MessageSegment
qqmusic = on_command("点歌", priority=5)

@qqmusic.handle()
async def handle(bot: Bot, event: GroupMessageEvent, args: Message=CommandArg()):
    args = args.extract_plain_text().strip()
    # logger.info(args)
    msg = ''  
    if args !='':
        id =await data_source.qq_search(args)
        if id != '':
            msg=MessageSegment.music(type_='qq',id_=id)
    Msg = Message(msg)
    await qqmusic.finish(Msg)

music = on_command("网易点歌", priority=5)

@music.handle()
async def handle(bot: Bot, event: GroupMessageEvent, args: Message=CommandArg()):
    args = args.extract_plain_text().strip()
    # logger.info(args)
    msg = ''  
    if args !='':
        id =await data_source.neteasy_search(args)
        if id != '':
            msg=MessageSegment.music(type_='163',id_=id)
    Msg = Message(msg)
    await music.finish(Msg)

