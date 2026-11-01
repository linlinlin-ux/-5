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

label a6:
play music "audio/宁静.mp3"
scene 大厅
show 陈铭 at right
role1 "你看起来不太高兴。"
hide 陈铭
show 许知微 at right
role3 "这里让我觉得不舒服。"
hide 许知微
show 陈铭 at right
role1 "因为十年前的事情？"
hide 陈铭
show 许知微 at right
role3 "也许吧。"
hide 许知微
show 陈铭 at right
role1 "你觉得寄信的人真有那些证据吗？"
hide 陈铭
show 许知微 at right
role3 "如果没有，为什么要把我们全都叫来？"
hide 许知微
show 陈铭 at right
role1 "也可能只是想吓唬我们。"
hide 陈铭
show 许知微 at right
role3 "那最好不过了。"
hide 许知微
narrator_adv "她低头摆弄着打火机，火石发出几声细小的摩擦声。"
show 陈铭 at right
role1 "你还记得周砚吗？"
hide 陈铭
show 许知微 at right
role3 "记得。"
hide 许知微
show 陈铭 at right
role1 "你觉得他会寄这封信吗？"
hide 陈铭
show 许知微 at right
role3 "我不知道。十年了，谁知道他变成什么样了。"
hide 许知微
narrator_adv "她没有再说下去。"
narrator_adv "你决定接下来做什么。"
menu:
    "和陆闻川聊聊":
        jump a5

    "询问程烈是否知道更多情况":
        jump a7

    "回到大厅等待顾承骁":
        jump a8
