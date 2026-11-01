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

label b6:
play music "audio/杀人之夜.mp3"
scene 命案现场
show 陈铭 at right
with dissolve
role1 "我再检查一下窗户和附近的地面。"
scene 窗户
hide 陈铭
with dissolve
narrator_adv "陈铭走到窗边，先检查窗框，再观察窗台与地板的连接处。"
show 陈铭 at right
role1 "窗户没有明显破损，窗框上也没有清楚的撬动痕迹。"
hide 陈铭
show 陆闻川 at right
role2 "这能说明什么？"
hide 陆闻川
show 陈铭 at right
role1 "只能说明目前没有发现明显的强行破窗迹象，不能据此排除有人从窗户进出。"
hide 陈铭
narrator_adv "陈铭蹲下查看窗边地面。地毯边缘有几处不太清晰的压痕，但无法辨认出完整的鞋印。"
show 陈铭 at right
role1 "这里有些痕迹，不过太模糊了，不能确认是不是鞋印，更不能判断属于谁。"
hide 陈铭
show 许知微 at right
role3 "会不会是凶手留下的？"
hide 许知微
show 陈铭 at right
role1 "有可能，也可能是平时走动留下的。需要其他证据才能判断。"
hide 陈铭
narrator_adv "陈铭又检查了窗户的开合状态，没有找到能够证明有人通过窗户进出的直接证据。"
show 程烈 at right
role4 "所以窗户这边也没有结果？"
hide 程烈
show 陈铭 at right
role1 "至少目前没有足够的证据支持有人从这里进出。我们先记下这些情况。"
scene 命案现场
hide 陈铭
with dissolve
narrator_adv "陈铭将窗边的模糊压痕记入调查记录，没有贸然把它认定为凶手留下的鞋印。"
menu:
    "检查房间遗留物":
        jump b7

    "返回检查尸体":
        jump b2

    "询问林伯":
        jump b4
