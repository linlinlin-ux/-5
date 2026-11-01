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

label f5:
play music "audio/推理2.mp3"
scene 工作间
with dissolve
narrator_adv "陈铭重新翻看四个人的询问记录。他想知道，当年究竟是谁组织了围堵，又是谁在周砚反复请求离开时仍然没有放过他。"
show 陈铭 at right
role1 "顾承骁似乎是那次冲突的主导者。"
hide 陈铭
narrator_adv "顾承骁的记录中，多次出现他主动挑起争端、要求其他人配合自己的描述。他似乎从未认为自己的行为有什么问题。"
show 陈铭 at right
role1 "他总觉得自己可以决定别人该怎么做。傲慢……"
hide 陈铭
narrator_adv "陆闻川的记录则涉及索取财物、占有他人物品，以及利用周砚的处境满足自己的要求。"
show 陈铭 at right
role1 "贪婪。他想要的从来不只是某一件东西。"
hide 陈铭
narrator_adv "许知微曾多次针对周砚受到的关注和认可发表恶意言论。她还参与传播过贬低周砚的消息。"
show 陈铭 at right
role1 "她似乎无法接受周砚拥有自己没有的东西。嫉妒……"
hide 陈铭
narrator_adv "程烈的记录里，争吵和肢体冲突出现得最频繁。他经常因为一点不顺心就对周砚动手。"
show 陈铭 at right
role1 "暴怒。他把自己的愤怒发泄在别人身上。"
hide 陈铭
narrator_adv "四个人的行为并不相同，却在那一天共同挡住了周砚离开的路。"
show 陈铭 at right
role1 "他们也许早就忘了那一天，可周砚不会。"
menu:
    "继续翻阅资料":
        jump f6
