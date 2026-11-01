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

label b9:
play music "audio/杀人之夜.mp3"
scene 走廊早
show 陈铭 at right
with dissolve
role1 "许知微，我想了解一下你对十年前那件事的记忆。"
hide 陈铭
show 许知微 at right
role3 "你想知道什么？"
hide 许知微
show 陈铭 at right
role1 "举报周末补课之后，周砚在学校里遭遇了什么？"
hide 陈铭
show 许知微 at right
role3 "一开始只是有人在背后议论他，后来事情变得越来越难看。"
hide 许知微
show 陈铭 at right
role1 "具体是什么情况？"
hide 陈铭
show 许知微 at right
role3 "班级群里有人故意提起举报的事，还会点名问他今天又举报了谁。"
hide 许知微
show 陈铭 at right
role1 "老师知道这些事吗？"
hide 陈铭
show 许知微 at right
role3 "知道。有一次班主任甚至当着其他人的面说他是叛徒。"
hide 许知微
show 陈铭 at right
role1 "你当时有没有站出来制止？"
hide 陈铭
show 许知微 at right
role3 "……没有。"
hide 许知微
show 陈铭 at right
role1 "为什么？"
hide 陈铭
show 许知微 at right
role3 "我不想成为下一个被针对的人。而且当时很多人都觉得，周砚只要道个歉，事情就能过去。"
hide 许知微
show 陈铭 at right
role1 "可是事情并没有过去，对吗？"
hide 陈铭
show 许知微 at right
role3 "没有。他的座位被搬到了最后一排靠门的位置，值日表上也总是安排他扫厕所。还有人撕过他的试卷。"
hide 许知微
show 陈铭 at right
role1 "你亲眼见过这些事？"
hide 陈铭
show 许知微 at right
role3 "有些是亲眼看见的，有些是后来听说的。我不能把没亲眼见过的事说成事实。"
hide 许知微
narrator_adv "许知微低下头，没有再看陈铭。她承认自己当年选择了沉默，却没有解释自己是否参与过其他事情。"
show 陈铭 at right
role1 "谢谢你告诉我这些。我还需要向其他人核实。"
menu:
    "询问程烈的旧事":
        jump b11

    "询问陆闻川的旧事":
        jump b8

    "询问顾承骁的旧事":
        jump b24

    "返回调查尸体":
        jump b2
