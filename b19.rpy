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

label b19:
play music "audio/推理.mp3"
scene 走廊
with dissolve
narrator_adv "走廊里比大厅昏暗得多，壁灯将众人的影子拉得很长。"
narrator_adv "几扇房门紧闭着，通往楼梯的方向没有其他人。"
show 陈铭 at right
role1 "大家似乎都已经回房间了。"
hide 陈铭
narrator_adv "陈铭经过一扇房门时，停下脚步听了片刻。里面没有明显的动静。"
show 陈铭 at right
role1 "……还是不要随便打扰别人。"
hide 陈铭
narrator_adv "他继续向前走，发现走廊尽头的窗户没有关严，夜风从缝隙里吹了进来。"
show 陈铭 at right
role1 "窗户没关好？"
hide 陈铭
narrator_adv "他伸手将窗户轻轻合上，没有发现明显的破损。"
show 陈铭 at right
role1 "明天再提醒林伯检查一下吧。"
hide 陈铭
narrator_adv "陈铭没有在走廊里停留太久，很快便回到了自己的房间。"
menu:
    "查看大厅":
        jump b18

    "前往第三天早晨（第三章）":
        jump b20
