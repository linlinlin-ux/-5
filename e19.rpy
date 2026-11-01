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

label e19:
play music "audio/推理2.mp3"
scene 大厅
with dissolve
narrator_adv "回到大厅后，陈铭将那张纸放在桌面上。几个人围了过来，仔细查看上面的内容。"
show 许知微 at right
role3 "这里确实写着接送安排。可是为什么日期旁边还有修改痕迹？"
hide 许知微
show 陈铭 at right
role1 "先看清楚原本的记录。"
hide 陈铭
show 顾承骁 at right
role5 "这里写着林伯原本要乘船离岛的时间。"
hide 顾承骁
show 许知微 at right
role3 "可林伯根本没能离开。"
hide 许知微
show 陈铭 at right
role1 "不仅如此，后面还有一项接送安排。应该就是原本负责送我们离岛的那艘船。"
hide 陈铭
show 顾承骁 at right
role5 "也就是说，林伯死亡后，原定的接送安排可能没有人继续处理。"
hide 顾承骁
show 许知微 at right
role3 "可是船为什么连出现都没有出现？"
hide 许知微
show 陈铭 at right
role1 "这正是我们需要查清楚的地方。记录上的修改痕迹，也许能告诉我们一些事情。"
hide 陈铭
show 顾承骁 at right
role5 "这张表是谁填写的？"
hide 顾承骁
show 陈铭 at right
role1 "目前还不能确定。我们得先弄清楚修改发生在什么时候。"
hide 陈铭
narrator_adv "陈铭重新收起记录表。原本以为只要等到船来就能离开，如今看来，事情远没有那么简单。"
menu:
    "继续调查":
        jump e20
