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

label Sheet3:
play music "audio/宁静.mp3"
scene 大厅
narrator_adv "你没有立刻进门，而是走到门边的信箱前。"
narrator_adv "信箱没有上锁，里面只有一张被折叠过的纸。"
show 陈铭 at right
role1 "纸上写着几个人的名字，其中顾承骁的名字被单独圈了出来。"
hide 陈铭
role1 "为什么偏偏是他？"
narrator_adv "纸张背面没有署名，也没有其他说明。"
narrator_adv "你将纸收起来，推开了豪宅的大门。"
narrator_adv "大厅里，陆闻川、许知微和程烈已经到了。"
show 陆闻川 at right
role2 "你在门口做什么？"
hide 陆闻川
show 陈铭 at right
role1 "看了一下信箱。"
hide 陈铭
show 陆闻川 at right
role2 "有东西？"
hide 陆闻川
show 陈铭 at right
role1 "没有。"
hide 陈铭
narrator_adv "陆闻川点了点头，没有继续追问。"
narrator_adv "你决定先做什么。"
menu:
    "和陆闻川聊聊":
        jump a5

    "和许知微聊聊":
        jump a6

    "询问程烈是否知道更多情况":
        jump a7
