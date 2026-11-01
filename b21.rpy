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

label b21:
play music "audio/杀人之夜.mp3"
scene 走廊早
show 陈铭 at right
with dissolve
role1 "林伯，我想再核对一下昨晚的时间线。"
hide 陈铭
show 林伯 at right
role6 "好，您请说。"
hide 林伯
show 陈铭 at right
role1 "晚饭结束后，你说自己去找周砚安排了一些事情。之后就没有再见过他，对吗？"
hide 陈铭
show 林伯 at right
role6 "是的。"
hide 林伯
show 陈铭 at right
role1 "那之后，你有没有在走廊里遇见其他人？"
hide 陈铭
show 林伯 at right
role6 "我记得曾经在大厅附近见过一位客人，但当时光线不太好，我不能确定是谁。"
hide 林伯
show 陆闻川 at right
role2 "你昨天怎么没说这件事？"
hide 陆闻川
show 林伯 at right
role6 "当时大家都在慌乱之中，我没有意识到这件事有多重要。"
hide 林伯
show 陈铭 at right
role1 "你还记得大概是什么时候吗？"
hide 陈铭
show 林伯 at right
role6 "晚饭之后不久。具体时间，我无法确定。"
hide 林伯
show 陈铭 at right
role1 "那你有没有听到过房间附近的异常声音？"
hide 陈铭
show 林伯 at right
role6 "没有听到什么特别的声音。"
hide 林伯
show 陈铭 at right
role1 "最后一个问题。你今天早晨去送早餐之前，有没有人提前告诉你周砚的房间出了问题？"
hide 陈铭
show 林伯 at right
role6 "没有。是我自己发现房间里出了事。"
hide 林伯
show 陈铭 at right
role1 "好，我记下了。现在还不能确认这些细节是否与案件有关。"
hide 陈铭
show 陆闻川 at right
role2 "也就是说，我们还是不知道谁去过他的房间。"
hide 陆闻川
show 陈铭 at right
role1 "至少现在，我们知道林伯的证词里还有无法确定的时间段。之后需要与其他人的说法进行比较。"
hide 陈铭
narrator_adv "林伯始终保持着礼貌的态度，但对于昨晚在走廊里见到的人，他没有给出明确答案。"
menu:
    "追问林伯与周砚过去的关系":
        jump b22

    "进入第二次集中讨论":
        jump b23
