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

label e2:
play music "audio/恐怖.mp3"
scene 卧室早
with dissolve
narrator_adv "陈铭走进房间，先检查床铺和床头柜。"
show 陈铭 at right
role1 "床铺有被使用过的痕迹，不像是整晚没有回来。"
hide 陈铭
show 许知微 at right
role3 "你是说他昨晚确实回来睡过？"
hide 许知微
show 陈铭 at right
role1 "至少床铺的状态说明他可能在这里休息过。"
scene 钥匙
hide 陈铭
with dissolve
narrator_adv "陈铭走到书桌前，发现桌面上放着一串钥匙。"
show 陈铭 at right
role1 "这是他的钥匙吗？"
hide 陈铭
show 许知微 at right
role3 "应该是，我之前见他拿过。"
hide 许知微
narrator_adv "钥匙旁边还压着一张纸，纸面上没有写字，只留下几道凌乱的划痕。"
show 陈铭 at right
role1 "这张纸先收起来。"
hide 陈铭
narrator_adv "陈铭继续检查衣柜和房间角落，没有发现程烈的身影。"
show 许知微 at right
role3 "他会不会已经离开豪宅了？"
hide 许知微
show 陈铭 at right
role1 "如果是这样，至少应该留下离开的痕迹。"
hide 陈铭
narrator_adv "陈铭暂时没有找到能够确认程烈去向的证据。"
menu:
    "返回走廊":
        jump e3
