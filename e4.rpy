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

label e4:
play music "audio/恐怖.mp3"
scene 大厅早
show 陈铭 at right
with dissolve
role1 "程烈不在房间里，走廊也没有明显的离开痕迹。至少现在，我们还不知道他去了哪里。"
hide 陈铭
show 许知微 at right
role3 "他不会无缘无故离开。昨天晚上还好好的，今天早上却突然不见了。"
hide 许知微
show 顾承骁 at right
role5 "先别急着下结论。房间里的钥匙和纸条都检查过了吗？"
hide 顾承骁
show 陈铭 at right
role1 "检查过了。钥匙没有提供有用的信息，纸条上只有几道划痕，暂时看不出完整内容。"
hide 陈铭
show 许知微 at right
role3 "你觉得他是自己离开的，还是有人把他带走了？"
hide 许知微
show 陈铭 at right
role1 "目前两种可能都不能排除。我们不能因为他失踪，就认定他已经遇害。"
hide 陈铭
show 顾承骁 at right
role5 "那就先把已知的事情理清楚。陆闻川死了，林伯也死了，现在程烈失踪。我们掌握的线索却始终无法拼成完整的解释。"
hide 顾承骁
show 许知微 at right
role3 "还有十年前的事情。每当我们以为快要弄清楚时，就会出现新的问题。"
hide 许知微
show 陈铭 at right
role1 "陆闻川留下的纸条、资金往来文件、那枚戒指，还有第一案现场发现的孔雀羽毛，都还没有得到合理解释。"
hide 陈铭
show 顾承骁 at right
role5 "这些线索未必都指向同一个人。把它们强行拼在一起，只会让判断失去准确性。"
hide 顾承骁
show 陈铭 at right
role1 "你说得对。现在最重要的不是急着找出一个嫌疑人，而是确认每条线索究竟能证明什么。"
hide 陈铭
show 许知微 at right
role3 "那我们接下来怎么办？继续找程烈吗？"
hide 许知微
show 陈铭 at right
role1 "先确认宅邸里还有哪些地方没有仔细检查。程烈可能去了某个我们忽略的地方。"
hide 陈铭
show 顾承骁 at right
role5 "我建议分头行动，但不要单独进入偏僻的区域。发现任何异常，都立刻通知其他人。"
hide 顾承骁
show 陈铭 at right
role1 "好。我们先检查宅邸里尚未仔细调查的区域，再决定下一步。"
menu:
    "调查区域":
        jump e5
