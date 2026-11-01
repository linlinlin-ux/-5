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

label e1:
play music "audio/恐怖.mp3"
scene 卧室早
with dissolve
narrator_adv "清晨，陈铭被一阵急促的敲门声吵醒。"
show 陈铭 at right
role1 "谁？"
hide 陈铭
show 许知微 at right
role3 "陈铭！你醒了吗？"
hide 许知微
show 陈铭 at right
role1 "怎么了？"
hide 陈铭
show 许知微 at right
role3 "程烈不见了！"
hide 许知微
show 陈铭 at right
role1 "不见了？什么意思？"
hide 陈铭
show 许知微 at right
role3 "我刚才去找他，房间里没人，敲门也没有回应。"
hide 许知微
show 陈铭 at right
role1 "你什么时候发现的？"
hide 陈铭
show 许知微 at right
role3 "就在刚才。我以为他已经起来了，可是大厅里也没有人。"
hide 许知微
narrator_adv "陈铭迅速穿好衣服，跟着许知微来到程烈的房间。"
scene 门
with dissolve
narrator_adv "房门紧闭，里面没有传出任何声音。"
show 陈铭 at right
role1 "你进去检查过了吗？"
hide 陈铭
show 许知微 at right
role3 "没有，我不敢一个人进去。"
hide 许知微
show 陈铭 at right
role1 "先进去看看。"
scene 卧室早
hide 陈铭
with dissolve
narrator_adv "陈铭推开房门，发现房间里空无一人。床铺有些凌乱，桌上的物品也没有收拾。"
show 许知微 at right
role3 "他到底去哪了？"
hide 许知微
show 陈铭 at right
role1 "先不要急着下结论。看看有没有留下什么线索。"
hide 陈铭
narrator_adv "陈铭环顾四周，开始检查房间。"
menu:
    "检查程烈的房间":
        jump e2

    "检查走廊":
        jump e3
