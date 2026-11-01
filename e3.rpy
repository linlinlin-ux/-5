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

label e3:
play music "audio/恐怖.mp3"
scene 走廊早
with dissolve
narrator_adv "陈铭走出房间，沿着走廊检查附近的情况。"
show 陈铭 at right
role1 "昨晚有人听见过什么动静吗？"
hide 陈铭
show 许知微 at right
role3 "我没有。我睡得很晚，但没有听见敲门声。"
hide 许知微
narrator_adv "陈铭检查了走廊两侧的房门和楼梯附近，没有发现明显的异常。"
show 陈铭 at right
role1 "如果他昨晚离开过房间，应该还有其他线索。"
hide 陈铭
show 许知微 at right
role3 "那我们现在怎么办？"
hide 许知微
show 陈铭 at right
role1 "先把其他人叫到大厅。程烈失踪的事情不能隐瞒。"
menu:
    "前往大厅":
        jump e4
