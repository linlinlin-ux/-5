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

label e17:
play music "audio/推理2.mp3"
scene 大厅早
with dissolve
narrator_adv "午后的阳光透过走廊窗户，落在空荡荡的地板上。宅邸里异常安静，几个人已经分头检查了几个房间，却依然没有找到程烈。"
show 陈铭 at right
role1 "我们已经检查过林伯的房间、地下储藏室，还有二楼尽头的房间。"
hide 陈铭
show 许知微 at right
role3 "可程烈还是不见踪影。"
hide 许知微
show 顾承骁 at right
role5 "还有一楼的几个区域没有仔细检查。林伯平时负责宅邸的日常事务，或许还留下了其他工作资料。"
hide 顾承骁
show 陈铭 at right
role1 "尤其是和船只接送有关的东西。"
hide 陈铭
show 许知微 at right
role3 "你是说，原本应该来接我们的船？"
hide 许知微
show 陈铭 at right
role1 "没错。林伯死后，原定的接送安排一直没有下文。我们不能只等着船出现。"
hide 陈铭
show 顾承骁 at right
role5 "一楼有一间平时存放杂物和工作用品的小房间，也许有用。"
hide 顾承骁
show 陈铭 at right
role1 "那就去检查那里。"
menu:
    "前往一楼":
        jump e18
