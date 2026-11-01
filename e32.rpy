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

label e32:
play music "audio/恐怖.mp3"
scene 窄门
with dissolve
narrator_adv "陈铭走到窄门前，伸手试着转动门把。门没有上锁，但似乎被什么东西从另一侧抵住了。"
show 许知微 at right
role3 "打不开吗？"
hide 许知微
show 陈铭 at right
role1 "门后面有东西挡着。"
hide 陈铭
show 顾承骁 at right
role5 "需要把门撞开吗？"
hide 顾承骁
show 陈铭 at right
role1 "先试着推几次。"
hide 陈铭
narrator_adv "几人合力推动门板，门后传来一阵沉闷的摩擦声。经过几次尝试，门终于被推开了一道缝隙。"
scene 通道
show 许知微 at right
with dissolve
role3 "里面好像还有一条走道。"
hide 许知微
narrator_adv "窄门后是一条狭长的通道，墙面没有装饰，尽头隐约能看见一扇旧铁门。"
show 陈铭 at right
role1 "这不像普通的储物空间。"
hide 陈铭
show 顾承骁 at right
role5 "会不会通向宅邸外面？"
hide 顾承骁
show 陈铭 at right
role1 "先过去看看。"
menu:
    "继续探索":
        jump e33
