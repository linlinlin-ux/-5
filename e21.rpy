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

label e21:
play music "audio/推理2.mp3"
scene 工作间
with dissolve
narrator_adv "几人重新回到一楼工作间。陈铭沿着桌边和文件柜逐一翻找，终于在抽屉深处找到一本较薄的登记册。"
show 许知微 at right
role3 "这是什么？"
hide 许知微
show 陈铭 at right
role1 "看起来是船只往来登记册。"
hide 陈铭
show 顾承骁 at right
role5 "打开看看，里面应该有实际的出入记录。"
hide 顾承骁
narrator_adv "登记册记录着不同日期的船只往返情况，包括出发时间、到达时间、船员姓名以及乘船人员。"
show 许知微 at right
role3 "这里有林伯的名字。"
hide 许知微
show 陈铭 at right
role1 "日期是他原本计划离岛的那一天。"
hide 陈铭
show 顾承骁 at right
role5 "记录上写着他已经安排好了离岛的船。"
hide 顾承骁
show 许知微 at right
role3 "可是他最后根本没有离开。"
hide 许知微
show 陈铭 at right
role1 "这条记录只能证明当时有过安排，不能证明船真的接到了人。"
hide 陈铭
show 顾承骁 at right
role5 "往后翻。看看有没有原定接我们的那艘船。"
hide 顾承骁
narrator_adv "陈铭继续翻阅，发现原定接送日期附近有一处记录被整页撕去，只留下靠近装订处的一小截纸根。"
show 许知微 at right
role3 "怎么会少了一页？"
hide 许知微
show 陈铭 at right
role1 "而且被撕掉的部分，正好是我们最需要确认的那段时间。"
hide 陈铭
show 顾承骁 at right
role5 "看来这本登记册也有人动过。"
hide 顾承骁
show 陈铭 at right
role1 "先保存好。现在还不能确定是谁撕掉了这一页。"
menu:
    "继续调查":
        jump e22
