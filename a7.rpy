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

label a7:
play music "audio/宁静.mp3"
scene 大厅
show 陈铭 at right
role1 "你似乎不太在意这封邀请函。"
hide 陈铭
show 程烈 at right
role4 "在意又怎么样？人都已经来了。"
hide 程烈
show 陈铭 at right
role1 "你觉得今晚会发生什么？"
hide 陈铭
show 程烈 at right
role4 "最多就是有人拿十年前的事情出来说几句。"
hide 程烈
show 陈铭 at right
role1 "如果那些证据是真的呢？"
hide 陈铭
show 程烈 at right
role4 "那就让他拿出来。"
hide 程烈
show 陈铭 at right
role1 "你不担心？"
hide 陈铭
show 程烈 at right
role4 "我有什么好担心的？"
hide 程烈
narrator_adv "程烈说得很快，随后像是意识到自己的语气有些过重，闭上了嘴。"
show 陈铭 at right
role1 "你和顾承骁最近还有联系吗？"
hide 陈铭
show 程烈 at right
role4 "偶尔。"
hide 程烈
show 陈铭 at right
role1 "他有没有提过这次邀请？"
hide 陈铭
show 程烈 at right
role4 "没有。"
hide 程烈
narrator_adv "你没有继续追问。"
narrator_adv "你决定接下来做什么。"
menu:
    " 和陆闻川聊聊":
        jump a5

    "和许知微聊聊":
        jump a6

    " 回到大厅等待顾承骁":
        jump a8
