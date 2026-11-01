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

label c6:
play music "audio/荒谬2.mp3"
scene 地下室入口
with dissolve
narrator_adv "陈铭的话并没有让众人平静下来。地下室入口处的气氛愈发紧张，所有人都在提防着彼此。"
show 陆闻川 at right
role2 "说得轻巧。现在我们连谁能相信都不知道。"
hide 陆闻川
show 许知微 at right
role3 "我们不能一直这样待下去。林伯死了，下一个会是谁？"
hide 许知微
show 程烈 at right
role4 "谁想动手就冲我来！别在这里装神弄鬼！"
hide 程烈
show 顾承骁 at right
role5 "你喊得再大声，也解决不了问题。"
hide 顾承骁
show 程烈 at right
role4 "你什么意思？"
hide 程烈
show 陈铭 at right
role1 "够了。继续争吵没有任何意义。我们现在至少要弄清楚一件事。"
hide 陈铭
show 陈铭 at right
role1 "周砚为什么邀请我们来到这里？除了他说过的霸凌证据，你们还有没有隐瞒其他事情？"
hide 陈铭
narrator_adv "众人沉默下来。陈铭意识到，必须先控制局面，才能继续调查。"
menu:
    "先让众人冷静下来，继续讨论现有线索":
        jump c7

    "追问每个人来岛的真实目的":
        jump c8
