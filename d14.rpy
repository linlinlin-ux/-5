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

label d14:
play music "audio/宁静.mp3"
scene 大厅早
with dissolve
narrator_adv "陈铭回到大厅时，许知微和程烈正坐在沙发两侧。顾承骁站在窗边，望着外面的海面。"
show 许知微 at right
role3 "你刚才去哪了？"
hide 许知微
show 陈铭 at right
role1 "回第一案的房间重新检查了一遍。"
hide 陈铭
show 程烈 at right
role4 "有发现吗？"
hide 程烈
show 陈铭 at right
role1 "找到了一件之前遗漏的东西。"
hide 陈铭
show 许知微 at right
role3 "什么东西？"
hide 许知微
show 陈铭 at right
role1 "一根孔雀羽毛，藏在床头柜和墙壁之间。"
hide 陈铭
show 顾承骁 at right
role5 "孔雀羽毛？"
hide 顾承骁
show 陈铭 at right
role1 "嗯，目前还不知道它为什么会在那里。"
hide 陈铭
show 顾承骁 at right
role5 "一根羽毛而已，能说明什么？"
hide 顾承骁
show 陈铭 at right
role1 "现在确实说明不了什么，但它出现在第一案现场，就值得留下来。"
hide 陈铭
narrator_adv "陈铭没有继续解释，将证物袋收了起来。"
narrator_adv "陆闻川和林伯接连死亡，第一案现场又出现了此前遗漏的物品。陈铭意识到，自己可能还没有真正理解这座豪宅里发生的一切。"
menu:
    "继续整理现有线索":
        jump d15
