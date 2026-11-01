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

label a12:
play music "audio/推理.mp3"
scene 卧室
show 陈铭 at right
role1 "算了，今天已经很晚了。既然周砚暂时不愿露面，只能等到明天再说。"
hide 陈铭
narrator_adv "众人各自回到客房。豪宅逐渐安静下来，只剩走廊里的灯光还亮着。"
show 陈铭 at right
role1 "十年前的事情……周砚究竟掌握了什么？"
hide 陈铭
narrator_adv "陈铭躺在床上，脑海里不断浮现邀请函上的那句话。"
narrator_adv "夜色渐深。豪宅深处始终没有传出任何动静，仿佛这里的主人真的只是身体不适，早早休息了。"
narrator_adv "没有人知道，这一夜过去之后，他们将再也无法像来时那样离开这座岛。"
narrator_adv "第二天清晨，一阵急促的敲门声打破了豪宅的寂静。"
menu:
    "进入下一章节":
        jump b1
