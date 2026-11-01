define role1 = Character('陈铭', color="#c8c8ff", image="role1")
define role2 = Character('陆闻川', color="#c8c8ff", image="role2")
define role3 = Character('许知微', color="#c8c8ff", image="role3")
define role4 = Character('程烈', color="#c8c8ff", image="role4")
define role5 = Character('顾承骁', color="#c8c8ff", image="role5")
define role6 = Character('林伯', color="#c8c8ff", image="role6")
define role7 = Character('周砚', color="#c8c8ff", image="role7")
define narrator_nvl = Character(None, kind=nvl)
define narrator_adv = Character(None, kind=adv)
define config.voice_filename_format = "audio/{filename}"

label f8:
play music "audio/推理2.mp3"
scene 工作间
with dissolve
narrator_adv "陈铭重新取出第一案的调查记录。那具尸体被发现时，所有人都认为死者是周砚。"
show 陈铭 at right
role1 "当时我们只顾着确认死亡和寻找离开的办法，几乎没有人质疑过死者的身份。"
hide 陈铭
narrator_adv "他翻看尸体右手、衣物和现场记录。"
show 陈铭 at right
role1 "这些线索能帮助我们还原现场，却不一定能证明死者是谁。"
hide 陈铭
narrator_adv "陈铭又想起那个一直以顾承骁身份留在众人之中的人。两个人原本就长得相似，这让当时的身份判断更加容易被混淆。"
show 陈铭 at right
role1 "如果有人故意利用这种相似，让我们认错了尸体……"
hide 陈铭
narrator_adv "他停下翻阅资料的动作。这个猜测还没有得到证实，但已经足以让他重新审视第一案。"
show 陈铭 at right
role1 "我需要找到能够证明身份的原始记录。"
hide 陈铭
narrator_adv "陈铭将第一案资料与十年前的学生档案放在一起。是否继续追查，已经成为眼下最重要的选择。"
menu:
    "深入核查第一案的真实身份":
        jump g1

    "暂时停止核查":
        jump h1
