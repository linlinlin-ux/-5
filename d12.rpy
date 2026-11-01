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

label d12:
play music "audio/推理.mp3"
scene 起点
with dissolve
narrator_adv "下午，陈铭独自来到最初发现尸体的房间。这里已经恢复了整洁，只有少数物品还保留着当时的位置。"
narrator_adv "他站在房间中央，重新回忆第一次调查时的情景。"
show 陈铭 at right
role1 "当时检查得太匆忙了……也许还有什么地方被忽略了。"
hide 陈铭
narrator_adv "陈铭先检查了床边和床头柜，随后沿着墙壁慢慢查看。"
show 陈铭 at right
role1 "房间里的物品基本没有变化。"
hide 陈铭
narrator_adv "他走到床头柜旁，蹲下身检查柜子与墙壁之间的缝隙。"
narrator_adv "就在这时，一抹暗绿色映入他的眼中。"
show 陈铭 at right
role1 "……这是？"
hide 陈铭
narrator_adv "一根细长的羽毛卡在床头柜与墙壁之间，颜色已经有些暗淡。它的位置十分隐蔽，如果不特意检查，很难注意到。"
show 陈铭 at right
role1 "之前调查的时候，竟然没有发现它。"
hide 陈铭
narrator_adv "陈铭戴上手套，小心地将羽毛取了出来。"
show 陈铭 at right
role1 "孔雀羽毛？为什么会出现在这里？"
hide 陈铭
narrator_adv "羽毛没有明显破损，末端还残留着一点灰尘，看起来不像是刚刚放进去的。"
show 陈铭 at right
role1 "先收起来。它可能与这间房间的主人有关。"
hide 陈铭
narrator_adv "陈铭将羽毛单独收好，又检查了一遍附近，却没有发现其他明显异常。"
narrator_adv "他看着手中的羽毛，隐约觉得这件东西并非偶然遗落，但一时无法判断它究竟意味着什么。"
menu:
    "仔细观察孔雀羽毛":
        jump d13

    "结束调查，返回大厅":
        jump d14
