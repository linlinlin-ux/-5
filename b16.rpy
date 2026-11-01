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

label b16:
play music "audio/杀人之夜.mp3"
scene 走廊早
show 陈铭 at right
with dissolve
role1 "林伯，我还有几个问题需要确认。"
hide 陈铭
show 林伯 at right
role6 "您请问。"
hide 林伯
show 陈铭 at right
role1 "昨天晚上，您最后一次见到周砚是什么时候？"
hide 陈铭
show 林伯 at right
role6 "晚饭结束之后。我向主人询问了一些安排，随后便离开了。"
hide 林伯
show 陈铭 at right
role1 "你离开时，周砚是什么状态？"
hide 陈铭
show 林伯 at right
role6 "主人看起来有些疲惫，不太想说话。我没有继续打扰他。"
hide 林伯
show 陈铭 at right
role1 "之后你有没有再去过他的房间？"
hide 陈铭
show 林伯 at right
role6 "没有。主人既然已经休息，我自然不会无故打扰。"
hide 林伯
show 陈铭 at right
role1 "那今天早晨，你是怎么发现尸体的？"
hide 陈铭
show 林伯 at right
role6 "我照常准备早餐，随后去给主人送餐。敲门之后，里面一直没有回应。"
hide 林伯
show 陈铭 at right
role1 "你敲了几次？"
hide 陈铭
show 林伯 at right
role6 "两三次吧。我担心主人出了什么事，便打开房门进去查看。"
hide 林伯
show 陈铭 at right
role1 "房门当时锁着吗？"
hide 陈铭
show 林伯 at right
role6 "门是关着的，但没有上锁。我打开门后，就看见了里面的情形。"
hide 林伯
show 陈铭 at right
role1 "你进去之后，碰过房间里的东西吗？"
hide 陈铭
show 林伯 at right
role6 "我只顾着确认情况，没有刻意移动任何东西。不过，当时我确实很慌张，细节可能记得不够清楚。"
hide 林伯
show 陈铭 at right
role1 "你发现尸体后，第一时间通知了谁？"
hide 陈铭
show 林伯 at right
role6 "我立刻去找其他人。具体先遇见了谁，我现在不敢保证。"
hide 林伯
show 陆闻川 at right
role2 "你是说，你连自己先找了谁都不记得？"
hide 陆闻川
show 林伯 at right
role6 "当时的情形太突然了。我只记得自己很快就把各位叫了过来。"
hide 林伯
show 陈铭 at right
role1 "好，我暂时记录这些。之后如果想起其他细节，请及时告诉我。"
hide 陈铭
show 林伯 at right
role6 "一定。只要能帮上各位的忙，我都会配合。"
menu:
    "追问林伯昨晚是否见过其他人":
        jump b21

    "询问林伯关于十年前的旧事":
        jump b22

    "返回第一次集中讨论":
        jump b12
