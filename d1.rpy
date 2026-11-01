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

label d1:
play music "audio/恐怖.mp3"
scene 卧室早
with dissolve
narrator_adv "清晨，阳光透过窗帘照进房间。陈铭醒来后，看了一眼床头柜上的旧照片。"
scene 大厅早
with dissolve
narrator_adv "他简单整理好衣物，打开房门走向大厅。"
narrator_adv "大厅里已经有几个人先到了，但气氛与往常不同。"
show 陈铭 at right
role1 "早。其他人呢？"
hide 陈铭
show 许知微 at right
role3 "陆闻川还没下来。"
hide 许知微
show 程烈 at right
role4 "我刚才去敲过他的门，没有人回应。"
hide 程烈
show 陈铭 at right
role1 "他昨晚没有回来吗？"
hide 陈铭
show 顾承骁 at right
role5 "昨晚我没注意。"
hide 顾承骁
show 许知微 at right
role3 "会不会还在房间里？"
hide 许知微
show 陈铭 at right
role1 "先别急着下结论。我们去看看。"
scene 门
hide 陈铭
with dissolve
narrator_adv "陈铭带着几人来到陆闻川的房间门前。"
show 程烈 at right
role4 "陆闻川！开门！"
hide 程烈
narrator_adv "房间里没有回应。程烈又敲了几下，依旧无人应答。"
show 许知微 at right
role3 "他不会出什么事了吧？"
hide 许知微
show 陈铭 at right
role1 "先确认房门是否上锁。"
hide 陈铭
narrator_adv "陈铭伸手试着转动门把手，发现房门并没有锁。"
menu:
    "进入陆闻川的房间":
        jump d2
