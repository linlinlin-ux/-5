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

label c13:
play music "audio/推理.mp3"
scene 大厅早
with dissolve
narrator_adv "陈铭带着旧照片回到大厅，将照片放在桌面上。"
show 陆闻川 at right
role2 "你在储物间里找到的就是这个？"
hide 陆闻川
show 陈铭 at right
role1 "嗯。照片夹在一堆旧文件里，纸箱看起来最近被人动过。"
hide 陈铭
show 许知微 at right
role3 "这是一张学生合影？"
hide 许知微
narrator_adv "照片已经泛黄，画面中有几名穿着校服的学生，背景似乎是一间教室。"
show 程烈 at right
role4 "看起来像是很多年前拍的。"
hide 程烈
show 陆闻川 at right
role2 "这衣服……好像是我们以前学校的校服。"
hide 陆闻川
show 许知微 at right
role3 "你确定吗？"
hide 许知微
show 陆闻川 at right
role2 "领口和校徽的样式很像。我记得以前穿过。"
hide 陆闻川
narrator_adv "陈铭翻过照片，发现背面写着一行已经有些褪色的字迹。"
show 陈铭 at right
role1 "背面写着一个日期，还有高三年级的字样。"
hide 陈铭
show 程烈 at right
role4 "高三？"
hide 程烈
show 许知微 at right
role3 "难道这是周砚以前的照片？"
hide 许知微
show 顾承骁 at right
role5 "一张旧照片而已，能说明什么？"
hide 顾承骁
show 陈铭 at right
role1 "目前还不能确定照片里的人是谁。"
hide 陈铭
show 陆闻川 at right
role2 "如果真是以前的照片，那为什么会被放在储物间里？"
hide 陆闻川
show 许知微 at right
role3 "也许周砚一直留着这些东西。"
hide 许知微
show 程烈 at right
role4 "他把我们叫来，难道就是为了让我们看这些？"
hide 程烈
show 顾承骁 at right
role5 "他已经死了。你们现在讨论这些，也问不出答案。"
hide 顾承骁
narrator_adv "顾承骁说完，视线在照片上停留了片刻，随后移开。"
show 陈铭 at right
role1 "先把照片收好。它或许能帮我们确认一些过去的事情。"
hide 陈铭
show 陆闻川 at right
role2 "我不想再翻十年前那些破事了。"
hide 陆闻川
show 许知微 at right
role3 "可是我们已经被卷进来了，想躲也躲不掉。"
hide 许知微
narrator_adv "大厅再次陷入沉默。陈铭将照片收起。"
menu:
    "结束讨论":
        jump c14
