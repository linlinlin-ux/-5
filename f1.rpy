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

label f1:
play music "audio/推理2.mp3"
scene 工作间
with dissolve
narrator_adv "第六天上午。地下储物间里，旧档案盒仍然摊开放在桌面上。经过前几天的调查，陈铭已经找到了不少与十年前校园事件有关的资料。"
scene 文件
with dissolve
narrator_adv "他将散落的学生名单、事件记录和询问材料重新整理，试图还原当年究竟发生过什么。"
scene 工作间
show 陈铭 at right
with dissolve
role1 "周砚、顾承骁、陆闻川、许知微、程烈……这些名字都出现过不止一次。"
hide 陈铭
narrator_adv "几份记录的日期十分接近，记录内容却各不相同。有些是同学之间的冲突，有些则是针对周砚的投诉。"
show 陈铭 at right
role1 "这不是一次偶然的争执。他们针对周砚已经有很长一段时间了。"
hide 陈铭
narrator_adv "陈铭翻到一张被折叠的事件记录。纸张边缘有明显的撕扯痕迹，记录日期恰好是十年前的某一天。"
show 陈铭 at right
role1 "这一天……为什么会单独留下记录？"
hide 陈铭
narrator_adv "他展开纸张，发现上面除了校园冲突的内容，还出现了几次关于周砚试图离开学校的描述。"
show 陈铭 at right
role1 "他那天似乎一直急着离开。"
hide 陈铭
narrator_adv "陈铭继续查看，却发现记录并不完整。"
show 陈铭 at right
role1 "得找到当天更完整的材料。"
menu:
    "继续调查":
        jump f2
