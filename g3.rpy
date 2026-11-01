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

label g3:
play music "audio/荒谬2.mp3"
scene 工作间
with dissolve
narrator_adv "陈铭将两份旧校医记录和第一案的尸体资料重新收好。他终于有了足以推翻最初判断的证据。"
show 陈铭 at right
role1 "顾承骁已经死了。"
hide 陈铭
narrator_adv "他想起这些天与众人相处的点点滴滴。那个一直以顾承骁身份出现的人，从未主动提起过自己与周砚的关系。"
show 陈铭 at right
role1 "他不是顾承骁。他是周砚。"
hide 陈铭
narrator_adv "陈铭没有立刻声张。他知道，一旦当面揭穿，对方很可能不会再给自己追问的机会。"
show 陈铭 at right
role1 "我必须先弄清楚，他为什么要把所有人带到这座岛上。"
hide 陈铭
narrator_adv "他将资料放回档案盒，离开地下储物间。"
menu:
    "回到大厅":
        jump g4
