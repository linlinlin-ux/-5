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

label b10:
play music "audio/杀人之夜.mp3"
scene 命案现场
show 陈铭 at right
with dissolve
role1 "等一下，他的右手似乎有一道旧伤。"
hide 陈铭
role1 "伤口已经愈合很久了，不像是最近造成的。"
role1 "单凭这道伤痕，无法判断他生前经历过什么，更不能据此推断死因。"
role1 "不过……这道伤痕的位置，似乎有些眼熟。"
role1 "……我以前在哪里见过类似的伤？"
role1 "算了，现在不是想这些的时候。先把能确认的情况记录下来。"
menu:
    "返回检查衣着":
        jump b5

    "前往检查房间遗留物":
        jump b7
