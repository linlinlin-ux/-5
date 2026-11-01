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

label e20:
play music "audio/推理2.mp3"
scene 大厅
with dissolve
narrator_adv "陈铭再次摊开船只安排表，将纸张放在灯光下仔细查看。几处被涂改的笔迹交叠在一起，原本的字迹已经不太清楚。"
show 陈铭 at right
role1 "这里有两种不同的笔迹。最上面的一层应该是后来补写的。"
hide 陈铭
show 许知微 at right
role3 "能看出原本写了什么吗？"
hide 许知微
show 陈铭 at right
role1 "日期还能辨认出来，但具体的接送时间被涂得很乱。"
hide 陈铭
show 顾承骁 at right
role5 "旁边还有一个备注。"
hide 顾承骁
show 陈铭 at right
role1 "……「由林伯确认后通知船方」。"
hide 陈铭
show 许知微 at right
role3 "也就是说，原本应该由林伯负责联系船只？"
hide 许知微
show 陈铭 at right
role1 "至少这份记录表明，他是负责确认接送安排的人。"
hide 陈铭
show 顾承骁 at right
role5 "可林伯已经死了。没人知道他有没有把最后的安排通知出去。"
hide 顾承骁
show 许知微 at right
role3 "那艘船会不会根本不知道要来接我们？"
hide 许知微
show 陈铭 at right
role1 "有这个可能。但如果只是没有收到通知，为什么记录表上还会出现后来的修改？"
hide 陈铭
show 顾承骁 at right
role5 "也许有人在林伯死后动过这张表。"
hide 顾承骁
show 陈铭 at right
role1 "现在还不能确定修改时间。我们需要找到更早的船只记录，确认原本的安排。"
hide 陈铭
narrator_adv "陈铭将船只安排表与林伯的工作记录放在一起。两份资料上的日期存在重合，但仍然缺少能够确认接送安排是否真正执行的凭据。"
menu:
    "继续调查":
        jump e21
