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

label a9:
show 陈铭 at right
role1 "林伯，周砚是什么时候开始身体不舒服的？"
hide 陈铭
show 林伯 at right
role6 "今天傍晚。主人说身体不适，让我先招待各位。"
hide 林伯
show 陈铭 at right
role1 "他有没有交代明天什么时候见我们？"
hide 陈铭
show 林伯 at right
role6 "没有具体时间。等主人身体好些，我会再通知各位。"
hide 林伯
show 陈铭 at right
role1 "他现在在自己的房间里休息？"
hide 陈铭
show 林伯 at right
role6 "是的。主人需要休息，我不方便让人打扰。"
hide 林伯
show 陈铭 at right
role1 "好，那就不打扰他了。"
hide 陈铭
show 林伯 at right
role6 "多谢理解。客房就在走廊两侧，有什么需要可以来找我。"
hide 林伯
narrator_adv "林伯转身离开。陈铭没有发现明显异常，只是觉得这场邀请从一开始就透着几分古怪。"
menu:
    "继续询问邀请函的目的":
        jump a10

    "与其他人商量留宿安排":
        jump a11

    "前往客房休息":
        jump a12
