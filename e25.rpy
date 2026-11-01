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

label e25:
play music "audio/推力.mp3"
scene 走廊2
with dissolve
narrator_adv "几人离开工作间，重新回到一楼走廊。宅邸里依旧没有程烈的动静，先前发现的痕迹也还没有得到合理解释。"
show 许知微 at right
role3 "我总觉得程烈不像是自己离开的。"
hide 许知微
show 陈铭 at right
role1 "你有什么依据？"
hide 陈铭
show 许知微 at right
role3 "他失踪前没有带走多少东西，房间里还留下了钥匙和一些个人物品。"
hide 许知微
show 顾承骁 at right
role5 "但这也不能证明他遭遇了什么。"
hide 顾承骁
show 陈铭 at right
role1 "我们还需要找到能确定他最后出现地点的证据。"
hide 陈铭
narrator_adv "陈铭想起此前在程烈房间里发现的纸屑，以及地下储藏室中能够与之拼合的碎片。"
show 陈铭 at right
role1 "程烈失踪前，很可能去过地下储藏室。我们还没有弄清楚他在那里寻找什么。"
hide 陈铭
show 许知微 at right
role3 "可我们已经检查过那个夹层了。"
hide 许知微
show 陈铭 at right
role1 "检查过夹层，不代表检查过他离开储藏室之后的路线。"
hide 陈铭
show 顾承骁 at right
role5 "你想沿着地下室出口继续找？"
hide 顾承骁
show 陈铭 at right
role1 "对。看看有没有通往其他区域的通道，或者被忽略的出入口。"
menu:
    "继续探索":
        jump e26
