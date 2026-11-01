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

label e27:
play music "audio/恐怖.mp3"
scene 储物间4
with dissolve
narrator_adv "储物间不大，里面堆放着一些旧家具和纸箱。空气中弥漫着潮湿的霉味，角落里有一只落满灰尘的木箱。"
show 许知微 at right
role3 "这里好像很久没人整理过了。"
hide 许知微
show 陈铭 at right
role1 "但门口的痕迹不像是很久以前留下的。"
hide 陈铭
narrator_adv "陈铭走近木箱，发现箱盖上有一道新鲜的擦痕，周围的灰尘也被清理过。"
show 顾承骁 at right
role5 "有人最近动过这个箱子。"
hide 顾承骁
show 陈铭 at right
role1 "打开看看。"
hide 陈铭
narrator_adv "木箱没有上锁。里面放着几叠旧文件，其中一个档案盒被压在最下面。盒子侧面贴着一张已经泛黄的标签。"
show 许知微 at right
role3 "这上面写着……十年前？"
hide 许知微
show 陈铭 at right
role1 "标签上的字已经模糊了，不过日期还能辨认。"
hide 陈铭
show 顾承骁 at right
role5 "这就是之前那些编号对应的东西？"
hide 顾承骁
show 陈铭 at right
role1 "很可能。先看看里面有什么。"
menu:
    "查看里面":
        jump e28
