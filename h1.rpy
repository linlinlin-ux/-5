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

label h1:
play music "audio/推理2.mp3"
scene 工作间
with dissolve
narrator_adv "陈铭最终合上了第一案的调查记录。"
show 陈铭 at right
role1 "现在再追查，也未必能找到可靠答案。"
hide 陈铭
show 陈铭 at right
role1 "我们已经浪费了太多时间。眼下更重要的是弄清楚剩下的人是否安全。"
hide 陈铭
narrator_adv "他将第一案的资料放回档案盒，没有继续核对两人的身份记录。"
show 陈铭 at right
role1 "暂时就按照当初的判断处理吧。"
menu:
    "回到大厅":
        jump h2
