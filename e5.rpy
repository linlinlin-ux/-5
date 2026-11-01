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

label e5:
play music "audio/恐怖.mp3"
scene 大厅早
show 陈铭 at right
with dissolve
role1 "宅邸里还有几个地方，我们之前只是匆匆经过，并没有仔细检查。"
hide 陈铭
show 许知微 at right
role3 "你是指地下室、储藏室，还有二楼尽头的那间房间？"
hide 许知微
show 陈铭 at right
role1 "没错。林伯死在地下储藏室附近，那里或许还有我们没注意到的东西。"
hide 陈铭
show 顾承骁 at right
role5 "二楼尽头的房间也值得检查。那里平时很少有人过去。"
hide 顾承骁
show 许知微 at right
role3 "可是我们现在还不知道程烈去了哪里。"
hide 许知微
show 陈铭 at right
role1 "所以不能只盯着他的房间。我们需要找到他可能留下的痕迹。"
hide 陈铭
show 顾承骁 at right
role5 "分开检查效率更高，但最好两个人一组。"
hide 顾承骁
show 陈铭 at right
role1 "我去地下储藏室附近。许知微，你和我一起。顾承骁，你检查二楼尽头的房间。"
hide 陈铭
show 顾承骁 at right
role5 "可以。如果发现什么，我会回来告诉你们。"
hide 顾承骁
show 许知微 at right
role3 "那就先这样。"
hide 许知微
show 陈铭 at right
role1 "出发吧。"
menu:
    "调查地下储藏室":
        jump e6

    "调查2楼尽头房间":
        jump e7
