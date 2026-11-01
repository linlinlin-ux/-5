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

label h3:
play music "audio/宁静.mp3"
scene 大厅早
with dissolve
narrator_adv "陈铭回到大厅。顾承骁仍然站在窗边。"
show 顾承骁 at right
role5 "你回来了。"
hide 顾承骁
show 陈铭 at right
role1 "我想知道，这一切到底是谁安排的。"
hide 陈铭
show 顾承骁 at right
role5 "你不是已经找到答案了吗？"
hide 顾承骁
show 陈铭 at right
role1 "十年前的围堵，母亲抢救，还有后来发生的这些死亡……它们之间一定存在联系。"
hide 陈铭
show 顾承骁 at right
role5 "你终于明白，那一天对某个人意味着什么了。"
hide 顾承骁
show 陈铭 at right
role1 "你为什么对这件事这么了解？"
hide 陈铭
show 顾承骁 at right
role5 "因为有些事情，不是旁观者能够轻易理解的。"
hide 顾承骁
narrator_adv "顾承骁低下头，手指轻轻摩挲着桌面。"
show 顾承骁 at right
role5 "那天，那个人一直求他们放自己走。他说母亲正在医院抢救，可没有人理会。"
hide 顾承骁
show 陈铭 at right
role1 "后来呢？"
hide 陈铭
show 顾承骁 at right
role5 "后来他没能及时赶到。"
hide 顾承骁
show 陈铭 at right
role1 "所以他恨他们。"
hide 陈铭
show 顾承骁 at right
role5 "如果换成你，你会原谅吗？"
hide 顾承骁
show 陈铭 at right
role1 "我不知道。"
hide 陈铭
show 顾承骁 at right
role5 "他也不知道。他只知道，那一天之后，有些东西再也回不来了。"
hide 顾承骁
narrator_adv "陈铭望着眼前的人，想从他的表情中寻找更多信息，却始终无法确定他究竟知道多少。"
show 陈铭 at right
role1 "那些死亡都是你安排的吗？"
hide 陈铭
show 顾承骁 at right
role5 "你觉得呢？"
hide 顾承骁
narrator_adv "对方没有给出明确回答。"
show 顾承骁 at right
role5 "陈铭，我只想问你一件事。"
hide 顾承骁
show 顾承骁 at right
role5 "十年前，你明明看见了。现在，你还打算继续装作什么都没发生吗？"
menu:
    "承认一切":
        jump h11

    "忘却一切":
        jump h12
