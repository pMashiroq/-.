import discord
import os


client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("메구밍 폭렬과 함께 등장!!")


@client.event
async def on_message(message):
    if message.content.startswith("?새로 왔어요"):
        await message.channel.send("나의 이름은 메구밍! 아크위자드를 칭하는자로 최강의 공격마법 폭렬마법을 다루는 자!")
    if message.content.startswith("?익스플로전"):
        await message.channel.send("어둠보다 검게 어둠으로부터 어둡고 칠흙이며 나의 진홍의 불꽃을 담아 각성의 때가 왔느니 몽매의 경계에 떨어진 섭리여 무형의 왜곡이 되어 현현하라! 춤추라 춤추라 춤추라 나의 힘의 본류의 목적은 붕괴이니 대등 할 놈 없이 붕괴하느니 누구하나 없이 없애리 심연으로부터 오거라 이것이 인류 최대 위력의 공격수단이것이야말로 궁극의 공격마법 『익스 플로젼!』")
    if message.content.startswith("?안대 잡아당기기"):
        await message.channel.send("죄송해요! 당기지 말아주세요! 그..그만해라!!")
    if message.content.startswith("?놓기"):
        await message.channel.send("아앍아아아아ㅏㅏㅏ 아파!!! 눈이!!!")
    if message.content.startswith("?스킬"):
        await message.channel.send("에?? 무슨소리 입니까? 제가왜 아크위자드의 길을 고르겠습니까 당연히!! 폭렬마법을 사용하기 위함이기 때문이죠!! 그외에 스킬에는 관심 없습니다!!")
    if message.content.startswith("?에? 그거뿐?"):
        await message.channel.send("당연하죠!! 자! 당신도 저와함께 폭렬도를 걷지 않겠나요!!!!")
    if message.content.startswith("?스틸"):
        await message.channel.send("머.. 먼가요.. 레벨이랑 스텟이 올랐다고 모험자에서 변태로 전직하신 건가요?!")
    if message.content.startswith("?이게뭐지"):
        await message.channel.send("(손을 내밀며)저기.. 아래가 허전해서 그런데 그것좀 돌려주세요..?")
    if message.content.startswith("?지팡이"):
        await message.channel.send("아아~ 마력이 넘쳐흐르는 마나타이트제 지팡이의 이 윤기 하아~ 하하아~")
    if message.content.startswith("?모험"):
        await message.channel.send("오!! 드디어 최강의 아크위자드인 이 몸이 나설때군요!!!")
    if message.content.startswith("?폭렬마법 이쁘네"):
        await message.channel.send("오오.. 당신도 드디어 폭렬도를 이해할 수 있게 되었군요! 당신도 이제 저와함께 폭렬도에 함께 하시겠습니까?")
    if message.content.startswith("?폭렬마법 날린후"):
        await message.channel.send("하앍.. 최고에요...")
    if message.content.startswith("?근성 없는 녀석"):
        await message.channel.send("뭣이라! 이 몸이 근성이 없다고?! 잘 말해주시네요 당신같이 이상한 스킬만 쓰는 당신보다 내가 더 쓸모 있다고요!!")
    if message.content.startswith("?어이 로리"):
        await message.channel.send("에.. 하.. 이 몸이 로리꼬마..")
    if message.content.startswith("?화장실"):
        await message.channel.send("(옷깃을 잡고)혼자가게 두진 않아요.. 뭘 혼자서 시원 해지려고 그래요..? 우리는 동료 잖아요? 화장실이든 어디든 갈 때엔 같이 가는 거에요..")
    if message.content.startswith("?화장실2"):
        await message.channel.send("홍마족은 화장실 따위 안 가요")
    if message.content.startswith("?아쿠시즈교 세제 비누"):
        await message.channel.send("(멘탈나감.)먹을수 있어..?")
    if message.content.startswith("?머리이상한 폭렬 계집"):
        await message.channel.send("저 말인가요?! 그건 저를 말하는 건가요?! 제가 없을때 그 별명이 정착되어 있었나요!?")
    if message.content.startswith("?대결중"):
        await message.channel.send("제 몸이 어떻다고여? 아 이건 개구리 뱃속의 분비물 이에요..")
    if message.content.startswith("?그걸로 뭘.."):
        await message.channel.send("뭐긴 뭐겠어요 가까이 온 순간에 마구 안겨서 그대로 이 분비물을 옮겨 뭍혀드리죠..")
    if message.content.startswith("?도망 칠 준비"):
        await message.channel.send("어딜 가실려는 거죠..? 우리들.. 친구죠..?^^친구는 힘들때 고난을 나누는 것이라고 생각해요^^")
    if message.content.startswith("?메구밍"):
        await message.channel.send("네 부르셨나요?")
    if message.content.startswith("?배고파"):
        await message.channel.send("저도 배고픕니다...")
    if message.content.startswith("?잘자"):
        await message.channel.send("네 푹쉬고 내일도 모험을 갈 준비를 합시다!")
    if message.content.startswith("?졸려"):
        await message.channel.send("졸리시다고여 마나가 너무 낮군요 가서 쉬세요")
    if message.content.startswith("?귀여워"):
        await message.channel.send("뭐머머머머 위대한 아크위자드한테 귀엽다니 당신 눈이 어떻게 된건가요?!?")
    if message.content.startswith("?배부르다"):
        await message.channel.send("(침을 닦으며..)뭐.. 뭐 먹었나요..?")
    if message.content.startswith("?안녕 하살법"):
        await message.channel.send("안녕 하 살 법 받아치기!!!!!")
    if message.content.startswith("?안녕 화살법"):
        await message.channel.send("안녕 하살법 받아 칠까 말까!!")
    if message.content.startswith("?익스플로젼2"):
        await message.channel.send("저한테 맡겨주세요! 하하하하하! 나의 폭렬 마법을 받아라!!! 「익스플로전!!」 (안나옴..) 마력이!!! 큰일났어요! 폭렬 마법을 발동하기 위해 필요한 마력이 부족해요!!!")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
