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

label Sheet2:
play music "audio/宁静.mp3"
scene 大厅
show 陈铭 at right
role1 "你推开沉重的大门。门轴发出一声短促的摩擦声。"
hide 陈铭
narrator_adv "大厅里亮着灯，壁炉却没有火。空气里有一股陈旧木头的气味。"
narrator_adv "陆闻川坐在沙发边，正低头看手机。"
show 陆闻川 at right
role2 "你总算到了。"
hide 陆闻川
show 陈铭 at right
role1 "你来多久了？"
hide 陈铭
show 陆闻川 at right
role2 "没多久。船把我送到岸边，我就直接过来了。"
hide 陆闻川
narrator_adv "他收起手机，没有继续解释。"
narrator_adv "许知微站在窗边，手里拿着一只没有点燃的打火机。"
show 许知微 at right
role3 "我还以为你不会来。"
hide 许知微
show 陈铭 at right
role1 "你希望我不来？"
hide 陈铭
show 许知微 at right
role3 "我只是觉得，有些事情拖得越久，就越没有谈的必要。"
hide 许知微
narrator_adv "楼梯旁传来沉重的脚步声。程烈从走廊走了出来。"
show 程烈 at right
role4 "人都到齐了？"
hide 程烈
show 陆闻川 at right
role2 "还差一个。"
hide 陆闻川
show 程烈 at right
role4 "顾承骁？他总是喜欢压轴。"
hide 程烈
narrator_adv "你扫过大厅。四个人都收到了邀请，但没有人主动提起邀请者。"
show 陈铭 at right
role1 "邀请你们的人，有没有说明今晚要谈什么？"
hide 陈铭
show 许知微 at right
role3 "只说要谈十年前的事情。"
hide 许知微
show 陆闻川 at right
role2 "还说手里有证据。"
hide 陆闻川
show 程烈 at right
role4 "哼。十年了，现在拿证据出来有什么用？"
hide 程烈
narrator_adv "你决定做点什么"
menu:
    "和陆闻川聊聊":
        jump a5

    "和许知微聊聊":
        jump a6

    "询问程烈是否知道更多情况":
        jump a7
