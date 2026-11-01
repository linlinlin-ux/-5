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

label c15:
play music "audio/恐怖.mp3"
scene 走廊3
with dissolve
narrator_adv "夜晚的走廊空无一人，墙壁上的壁灯散发着微弱的暖黄色光芒。"
show 陈铭 at right
role1 "刚才的声音应该就是从这附近传来的。"
hide 陈铭
narrator_adv "陈铭沿着走廊向前走，发现远处的一扇房门没有完全关上。"
show 陈铭 at right
role1 "这是谁的房间？"
hide 陈铭
narrator_adv "他走近房门，发现门内没有亮灯，房间里也没有任何回应。"
narrator_adv "就在陈铭准备敲门时，身后忽然传来了脚步声。"
show 顾承骁 at right
role5 "陈铭？你在这里做什么？"
hide 顾承骁
show 陈铭 at right
role1 "我刚才听见走廊里有声音，出来看看。"
hide 陈铭
show 顾承骁 at right
role5 "这么晚了，你最好还是回房间。"
hide 顾承骁
show 陈铭 at right
role1 "你呢？怎么也在外面？"
hide 陈铭
show 顾承骁 at right
role5 "我也听见了声音。出来看看而已。"
hide 顾承骁
narrator_adv "两人短暂地对视了一眼。"
show 陈铭 at right
role1 "你刚才从哪个方向过来的？"
hide 陈铭
show 顾承骁 at right
role5 "楼梯那边。怎么了？"
hide 顾承骁
show 陈铭 at right
role1 "没什么，只是确认一下。"
hide 陈铭
narrator_adv "陈铭没有继续追问。他看了一眼那扇半开的房门，决定暂时不擅自进入。"
show 顾承骁 at right
role5 "回去吧。明天还有事情要处理。"
hide 顾承骁
narrator_adv "两人各自回到房间，走廊重新恢复了安静。"
menu:
    "返回房间":
        jump c16
