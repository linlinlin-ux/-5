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

label a11:
play music "audio/宁静.mp3"
scene 大厅
show 陆闻川 at right
role2 "周砚到底想干什么？把我们叫过来，自己却不见人。"
hide 陆闻川
show 许知微 at right
role3 "邀请函只说有十年前的证据，连具体是什么都没讲。"
hide 许知微
show 程烈 at right
role4 "明天见到他，直接问清楚就行。"
hide 程烈
show 顾承骁 at right
role5 "我也很好奇。他既然特意邀请我们，就不可能什么都不说。"
hide 顾承骁
show 陆闻川 at right
role2 "顾承骁，你和周砚以前有过联系吗？"
hide 陆闻川
show 顾承骁 at right
role5 "没有。我们很久没见过了。"
hide 顾承骁
show 陈铭 at right
role1 "既然大家都不清楚他的目的，就先别互相猜测。等见到周砚再说。"
hide 陈铭
show 许知微 at right
role3 "希望明天别再出什么意外。"
hide 许知微
narrator_adv "话题逐渐结束。众人各自回房，走廊里的脚步声慢慢消失。"
menu:
    "前往客房休息":
        jump a12

    "在大厅观察一会儿":
        jump a13

    "留意走廊的动静":
        jump a14
