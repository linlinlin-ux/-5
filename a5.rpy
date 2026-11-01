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

label a5:
play music "audio/宁静.mp3"
scene 大厅
show 陈铭 at right
role1 "你最近怎么样？"
hide 陈铭
show 陆闻川 at right
role2 "还行。工作忙，没什么特别的。"
hide 陆闻川
show 陈铭 at right
role1 "你收到邀请函的时候，是什么反应？"
hide 陈铭
show 陆闻川 at right
role2 "第一反应是恶作剧。后来看到信里提到十年前的事，就觉得没那么简单了。"
hide 陆闻川
show 陈铭 at right
role1 "你觉得寄信的人是谁？"
hide 陈铭
show 陆闻川 at right
role2 "不知道。可能是周砚，也可能是其他人。"
hide 陆闻川
show 陈铭 at right
role1 "你觉得周砚还会回来？"
hide 陈铭
show 陆闻川 at right
role2 "我不知道他现在在哪里。只是这封信让我想起了他。"
hide 陆闻川
narrator_adv "陆闻川说话时一直看着你，没有明显的慌乱。"
show 陆闻川 at right
role2 "你呢？收到信以后怎么想？"
hide 陆闻川
show 陈铭 at right
role1 "我只是想知道，寄信的人到底要做什么。"
hide 陈铭
show 陆闻川 at right
role2 "那就等人到齐吧。"
hide 陆闻川
narrator_adv "你结束了这次谈话。"
narrator_adv "你决定接下来做什么。"
menu:
    "和许知微聊聊":
        jump a6

    "询问程烈是否知道更多情况":
        jump a7

    " 回到大厅等待顾承骁":
        jump a8
