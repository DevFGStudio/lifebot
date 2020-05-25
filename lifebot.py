import discord
import asyncio
import datetime
from discord.ext import commands
from discord.ext.commands import bot
from itertools import cycle




client = discord.Client()
bot = commands.Bot(command_prefix='?!')


statusmsg = ['test1', 'test2', 'test3']

async def change_status():
    await client.wait_until_ready()
    messages = cycle(statusmsg)

    while not client.is_closed:
        current_status = next(messages)
        await client.change_presence(game=discord.Game(name=current_status))
        await asyncio.sleep(4)

 
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    game = discord.Game("관리자 관리 봇 :D")
    await client.change_presence(status=discord.Status.online,activity=game)








@client.event
async def on_message(message):


    if message.content.startswith("/예쁘지공지"):
        embed = discord.Embed(title="안내사항", color=0xFFFF24, description=" ".join(message.content.split()[2:]))
        embed.add_field(name='문의사항', value='FGStudio#6284', inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/714101231617835008/714432137792847902/4bc6c0ec79b50a0c.png")
        channel = client.get_channel(int(message.content.split()[1]))
        embed.set_footer(text="담당 관리자 | 예쁘지", icon_url="https://cdn.discordapp.com/attachments/714101231617835008/714432137792847902/4bc6c0ec79b50a0c.png")
        embed.timestamp = datetime.datetime.utcnow()

        await channel.send(embed=embed)







   



    if message.content.startswith("/관리자공지"):
        embed = discord.Embed(title="공지사항", color=0xFFFF24, description=" ".join(message.content.split()[2:]))
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/714101231617835008/714432137792847902/4bc6c0ec79b50a0c.png")
        channel = client.get_channel(int(message.content.split()[1]))
        embed.set_footer(text="디코 관리자 일동", icon_url="https://cdn.discordapp.com/attachments/714101231617835008/714432137792847902/4bc6c0ec79b50a0c.png")
        embed.timestamp = datetime.datetime.utcnow()

        await channel.send(embed=embed)

    #if message.content.startswith("/공지"):
     #   embed = discord.Embed(title="공지사항", color=0xFFFF24, description="ex) 신고양식\n\n- 고소인 : A__TO\n- 피고소인 : FGStudio\n- 사건 : 너무 다재다능함\n- 증거자료 : 첨부자료참고 (사진) or (동영상)")
      #  embed.add_field(name='문의사항', value='Days#9186', inline=False)
       # embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/542651500116181002/685363931489107968/JPEG_20190911_170206.jpg")
        #embed.set_footer(text="담당 관리자 | 에이티오", icon_url="https://cravatar.eu/head/A__TO/64.png")
        #embed.timestamp = datetime.datetime.utcnow()

     #   await message.channel.send(embed=embed)



    #if message.content.startswith("/공지2"):
    #    embed = discord.Embed(title="처벌내역", color=0xFFFF24, description="지옥에 인공적인 몹농장 건설\n\nPatsha 경고1회\ne0sa 경고1회\nPatsha 경고2회 누적으로 인한, 타우니 1일 밴")
    #    embed.add_field(name='문의사항', value='FGStudio#6284', inline=False)
    #    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/542651500116181002/685363931489107968/JPEG_20190911_170206.jpg")
    #    embed.set_footer(text="처리자 | 예쁘지", icon_url="https://cravatar.eu/head/FGStudio/64.png")
    #    embed.timestamp = datetime.datetime.utcnow()

      #  await message.channel.send(embed=embed)
        

    if message.content.startswith("/공지2"):
       # embed = discord.Embed(title="마을 명령어", color=0xFFFF24, description="\n모든 명령어는, 타우니월드에서 사용 하실 수 있습니다.\n\n/마을 : 당신이 속해있는 마을의 상태를 확인합니다.\n/마을 [마을] : 해당 마을의 정보를 알려줍니다.\n/마을 설립 [이름] : 해당 위치 16x16로 새 마을을 만듭니다. 공백 대신 '_'를 사용합니다.\n/마을 현위치 : 당신이 서있는 마을의 상태를 확인합니다.\n/마을 목록 : 전체적인 마을의 목록을 보여줍니다.\n마을 온라인 : 온라인 상태인 마을원 목록을 보여줍니다.\n/마을 떠나기 : 해당 마을을 떠납니다.\n/마을 주민목록 : 마을의 주민들을 보여줍니다.\n/마을 등급목록 : 마을의 등급 목록을 보여줍니다\n/마을 무법자목록 : 마을의 무법자 목록을 보여줍니다.\n/마을 토지 : 마을의 토지 정보를 보여줍니다.\n/마을 무법자 추가/제거 [주민] : 마을의 무법자를 추가 또는 제거합니다.\n/마을 말하기\n/마을 스폰 : 당신이 속해있는 마을 스폰으로 이동합니다.\n/마을 입금 [금액] : 마을 금고에 크레딧을 보관합니다.\n/마을 등급 추가/제거 [주민] [등급]\n촌장: /마을 촌장 ? : 촌장 명령어들을 확인합니다. ")
        #embed = discord.Embed(title="촌장 명령어", color=0xFFFF24, description="\n해당 명령어는, 촌장만 사용 하실 수 있습니다.\n\n/마을 출금 [금액] : 마을 금고에 있는 돈을 빼갑니다.\n/마을 점유 : /마을점유 ? 에 대한 도움말을 확인합니다.\n/마을 점유해제 : 마을 땅 점유를 해제합니다.\n/마을 [추가/추방] [주민] : 온라인 상태인 주민중에서 마을에 추가합니다.\n/마을 설정 : 마을 설정에 대한 도움말을 확인합니다.\n/마을 구매 : 마을 구매에 대한 도움말을 확인합니다.\n/마을 토지\n/마을 토글\n/마을 등급 추가/제거 [주민] [등급] : /마을 등급 ? 에 대한 도움말을 확인합니다.\n/마을 삭제")
        embed = discord.Embed(title="업데이트", color=0xFFFF24, description="\nPatch Notes: Early Access (EXPERIMENTAL) - v0.3.4.6 - Build 120739\n\n오늘의 패치는 Rimaged Doggos 에 대한 문제를 해결하고 Smart & Programmable Splitter를 위한 오버플로 설정을 소개할 것이다! \n아래 노트에서 확인 할 수 있는 몇 가지 추가 수정 사항이 함께 제공되고 있다. \n마지막 패치에서는 전 세계 Z-0 이하에서 제대로 작동하도록 유체 시뮬레이션을 업데이트 했다.\n만약 당신이 지금 당신의 유체에 문제가 있다면 그것은 당신의 설정이 우리가 고친 버그에 의존해 왔다는 것을 의미한다.\n이 경우 설정을 다시 살펴보고 올바르게 작동하고 펌프의 정확한 수와 위치를 사용해야 할 수 있다. \n\n 밸런싱\n1) 일부 이후 게임 부품의 복잡성을 반영하여 수공예 제작 시간 조정\n2) PowerShield 생산 시간이 생성자 사운드에 더 잘 작동하도록 변경됨\n3) Color Cartridge 생산 주기 단축, 생산값 변경 없음\n새로운 기능\n1) Smart & Programmable Splitter의 오버플로 설정\n\nUI\n1) 카운트다운 중에 자동 저장 알림 최소화\n\n버그 수정\n\n1) 고객이 이제 화물차를 올바르게 제작 및 스냅할 수 있어야함\n2) 도마뱀 Doggos 는 지금 실제로 despawn 하지 않아야 합니다.\n3) 빌드 건으로 전환하거나 건을 분해 할 때 1 차 사격이 중단되면 무기가 더 이상 계속 발사되지 않습니다.\n4) 창 벽 수정\n5) 전원 회로와 관련된 부하에서 충돌이 수정되었습니다.\n6) 해체 중 빌드 건이 장착되지 않은 경우 해체 효과가 더이상 지속되지 않아야 함\n7) Fluid Buffers, Freight Platforms 및 Freight Car 는 이제 설명서에 건물의 정확한 용량을 명시한다.\n8) 제련소 및 주조 공장에서 잘못된 재료 적용 수정\n\n번역 문제가 있을시 말해주세요.")
        embed.add_field(name='문의사항', value='FGStudio#6284', inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/635055942345687040/687111592323973120/common.jpg")
        embed.set_footer(text="담당 관리자 | 예쁘지", icon_url="https://cdn.discordapp.com/attachments/635055942345687040/687111592323973120/common.jpg")
        embed.timestamp = datetime.datetime.utcnow()

        await message.channel.send(embed=embed)
        



client.loop.create_task(change_status())          
client.run('NzE0NDMxNDUwMTUzMzUzMjI2.XsukVg.oVpyVypMFiY6bQfNL-qI4I-fv7o') 
