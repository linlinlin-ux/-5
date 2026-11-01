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

label e33:
play music "audio/恐怖.mp3"
scene 通道
with dissolve
narrator_adv "通道里十分昏暗，地面铺着一层薄灰。陈铭打开手电筒，发现灰尘上有几道不太完整的脚印。"
show 许知微 at right
role3 "有人来过这里！"
hide 许知微
show 陈铭 at right
role1 "而且不是很久以前。"
hide 陈铭
narrator_adv "陈铭沿着脚印往前走。脚印在通道中段变得凌乱，旁边的墙壁上还有一道明显的擦痕。"
show 顾承骁 at right
role5 "看起来像是有人在这里摔倒过。"
hide 顾承骁
show 陈铭 at right
role1 "也可能发生过拉扯。"
hide 陈铭
show 许知微 at right
role3 "会是程烈吗？"
hide 许知微
show 陈铭 at right
role1 "现在还不能确定。继续往前。"
hide 陈铭
narrator_adv "几人走到通道尽头，发现旧铁门没有完全关上。门缝里透出一丝微弱的光线。"
show 顾承骁 at right
role5 "后面还有房间？"
hide 顾承骁
show 陈铭 at right
role1 "看起来是。"
menu:
    "探查":
        jump e34
