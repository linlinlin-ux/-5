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

label e22:
play music "audio/推理2.mp3"
scene 工作间
with dissolve
narrator_adv "陈铭将登记册放在桌上，仔细观察缺页留下的纸根。纸张边缘已经泛黄，但撕裂处相对新鲜。"
show 许知微 at right
role3 "这页应该不是很久以前撕掉的。"
hide 许知微
show 陈铭 at right
role1 "是的。至少从边缘来看，它比其他纸页更新。"
hide 陈铭
show 顾承骁 at right
role5 "你是说，有人最近才撕掉它？"
hide 顾承骁
show 陈铭 at right
role1 "不能完全确定，但值得注意。"
hide 陈铭
show 许知微 at right
role3 "如果这页记录了接船情况，那撕掉它的人是不是不想让我们知道船为什么没来？"
hide 许知微
show 陈铭 at right
role1 "有这种可能。也可能只是想隐瞒其他往来记录。我们不能只凭缺页就确定动机。"
hide 陈铭
show 顾承骁 at right
role5 "现在我们有船只安排表、林伯的工作记录，还有这本缺页的登记册。"
hide 顾承骁
show 陈铭 at right
role1 "先把三份资料的日期整理出来。它们之间应该存在可以核对的地方。"
hide 陈铭
narrator_adv "陈铭将资料收好。原定接送安排究竟有没有被取消，船只为何没有出现，以及缺失的登记页上记录了什么，仍然没有答案。"
menu:
    "继续调查":
        jump e23
