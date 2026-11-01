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

label e34:
play music "audio/恐怖.mp3"
scene 尸体
with dissolve
narrator_adv "陈铭缓缓推开铁门。门后是一间面积不大的旧杂物室，里面堆放着废弃家具和一些工具。"
show 许知微 at right
role3 "这里怎么会有一间房间？"
hide 许知微
show 陈铭 at right
role1 "应该是宅邸早期留下的辅助空间。"
hide 陈铭
narrator_adv "陈铭刚走进去，就注意到墙边有一只倒下的木凳。地面上的灰尘被大片擦乱，像是有人在这里移动过。"
show 顾承骁 at right
role5 "那边好像有东西。"
hide 顾承骁
narrator_adv "顾承骁指向房间深处。几件旧布料堆在一起，下面露出一截衣袖。"
show 许知微 at right
role3 "……那是什么？"
hide 许知微
show 陈铭 at right
role1 "先别过去。"
hide 陈铭
narrator_adv "陈铭走近后，发现布料下面是一只人的手。手指僵硬，皮肤已经失去血色。"
show 许知微 at right
role3 "不会吧……"
hide 许知微
show 陈铭 at right
role1 "退后。"
hide 陈铭
narrator_adv "陈铭掀开遮挡的布料，终于看清了下面的人。那是程烈。"
show 许知微 at right
role3 "程烈？！"
hide 许知微
show 顾承骁 at right
role5 "他怎么会在这里……"
hide 顾承骁
narrator_adv "程烈已经死亡。他的尸体被藏在杂物堆后方，衣物凌乱，附近还有明显的挣扎痕迹。"
show 陈铭 at right
role1 "他失踪之前，应该来过这条通道。"
hide 陈铭
show 许知微 at right
role3 "到底是谁把他藏在这里的？"
hide 许知微
show 陈铭 at right
role1 "先不要碰现场。我们需要仔细检查。"
menu:
    "调查尸体":
        jump e35
