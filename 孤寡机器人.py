from asyncio import sleep

from nonebot import on_notice
from nonebot.adapters.cqhttp import Bot, Event

gugua = on_notice(priority=5)


@gugua.handle()
async def message_discernment_handle(bot: Bot, event: Event):
    print(f'检测到事件:{event.notice_type}')
    if event.notice_type == 'group_increase' and event.group_id == 967714381:
        new_id = event.user_id
        print(f'检测到受害者:{new_id}')
        await sleep(3)

        await gugua.send('您好我是您朋友给您点的孤寡青蛙')
        await sleep(0.5)
        await gugua.send('我要开始叫了')
        await sleep(0.5)
        await gugua.send('孤寡孤寡孤寡孤寡孤寡孤寡孤寡孤')
        await sleep(0.5)
        await gugua.send('寡孤寡孤寡孤寡孤寡孤寡孤寡孤寡')
        await sleep(0.5)
        await gugua.send('寡孤寡孤寡孤寡孤寡孤寡孤寡孤寡')
        await sleep(0.5)
        await gugua.send('寡孤寡孤寡孤寡孤寡孤寡孤寡孤寡')
        await sleep(0.5)
        await gugua.send('寡孤寡孤寡孤寡孤寡孤寡孤寡孤寡')
        await sleep(0.5)
        await gugua.send('服务完毕,欢迎您明年再来')

        await bot.set_group_kick(group_id=967714381, user_id=new_id)
