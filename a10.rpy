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

label a10:
play music "audio/宁静.mp3"
scene 大厅
show 陈铭 at right
role1 "林伯，我还有一个问题。"
hide 陈铭
show 林伯 at right
role6 "您请说。"
hide 林伯
show 陈铭 at right
role1 "周先生邀请我们来到这里，却在我们抵达后突然说身体抱恙。你知道他究竟想和我们谈什么吗？"
hide 陈铭
show 林伯 at right
role6 "主人的想法，我不敢妄自揣测。邀请函是主人亲自安排寄出的，具体内容，想必各位都已经看过。"
hide 林伯
show 陆闻川 at right
role2 "邀请函上只说，要谈十年前的事情。除此之外，什么都没写。"
hide 陆闻川
show 林伯 at right
role6 "那就只能等主人明天亲自向各位解释了。"
hide 林伯
show 许知微 at right
role3 "如果他明天还是不肯露面呢？"
hide 许知微
show 林伯 at right
role6 "主人既然发出了邀请，自然不会无缘无故让各位白跑一趟。"
hide 林伯
show 程烈 at right
role4 "说了半天，还是一句有用的都没有。"
hide 程烈
show 顾承骁 at right
role5 "既然林伯不知道，继续追问也没意义。明天见到周砚，自然就清楚了。"
hide 顾承骁
show 陈铭 at right
role1 "好吧。既然如此，我们明天再谈。"
hide 陈铭
narrator_adv "林伯微微欠身，没有再多说什么，转身离开了大厅。"
narrator_adv "陈铭看着林伯离去的背影，隐约觉得这座宅邸里的每个人似乎都在等待某件事发生。"
menu:
    "继续留在大厅":
        jump a13

    "回客房休息":
        jump a12

    "趁夜观察走廊":
        jump a14
