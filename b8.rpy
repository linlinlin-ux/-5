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

label b8:
play music "audio/杀人之夜.mp3"
scene 走廊早
show 陈铭 at right
with dissolve
role1 "陆闻川，我想问问十年前学校里的事情。"
hide 陈铭
show 陆闻川 at right
role2 "都过去十年了，还有什么好问的？"
hide 陆闻川
show 陈铭 at right
role1 "周砚在邀请函里特意提到十年前的事。你们当年究竟发生过什么？"
hide 陈铭
show 陆闻川 at right
role2 "高中同学之间有过矛盾很正常。毕业这么多年，谁还记得那么清楚？"
hide 陆闻川
show 陈铭 at right
role1 "你刚才说得很轻松。你确定那只是普通的同学矛盾？"
hide 陈铭
show 陆闻川 at right
role2 "你想表达什么？"
hide 陆闻川
show 陈铭 at right
role1 "我只是在确认事实。听说当年学校里发生过一次举报事件，周砚也卷入其中。"
hide 陈铭
show 陆闻川 at right
role2 "是有这么回事。有人举报周末补课收费，后来补课停了，家长的钱也退了。"
hide 陆闻川
show 陈铭 at right
role1 "举报的人是周砚？"
hide 陈铭
show 陆闻川 at right
role2 "后来大家都这么说。但事情具体怎么查出来的，我不清楚。"
hide 陆闻川
show 陈铭 at right
role1 "事情发生之后，周砚在学校里的处境怎么样？"
hide 陈铭
show 陆闻川 at right
role2 "不太好吧。很多人觉得他害大家白忙一场，老师也不愿意多管。"
hide 陆闻川
show 陈铭 at right
role1 "你当时做过什么？"
hide 陈铭
show 陆闻川 at right
role2 "我没必要把十年前的每件事都向你交代。你有证据，就拿出来。"
hide 陆闻川
narrator_adv "陆闻川明显不愿继续谈论此事，但他承认，举报事件之后，周砚在学校里受到过排斥。"
show 陈铭 at right
role1 "好，我暂时问到这里。之后如果想起其他细节，希望你能如实说明。"
menu:
    "询问许知微的旧事":
        jump b9

    "询问程烈的旧事":
        jump b11

    "询问顾承骁的旧事":
        jump b24

    "返回调查房间":
        jump b3
