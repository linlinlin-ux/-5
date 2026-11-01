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

label g1:
play music "audio/推理2.mp3"
scene 盒子
with dissolve
narrator_adv "陈铭决定继续调查。他重新检查旧档案盒里的学生资料，寻找周砚与顾承骁能够相互区分的身份记录。"
scene 工作间
show 陈铭 at right
with dissolve
role1 "不能再只凭长相判断。"
hide 陈铭
narrator_adv "两人的旧学生照片被并排放在桌上。五官轮廓确实十分相似，但照片背后的登记信息分别属于两个人。"
show 陈铭 at right
role1 "他们以前就长得这么像……"
hide 陈铭
narrator_adv "陈铭找到一份旧校医登记记录，其中记载着两人的个人信息和当年的就诊情况。"
show 陈铭 at right
role1 "这份记录能确认他们各自的身份。"
hide 陈铭
narrator_adv "他又取出第一案留下的随身物品登记资料，开始与旧档案中的信息进行核对。"
show 陈铭 at right
role1 "如果能找到两边都能对应上的信息，就可以判断当时究竟是谁被认错了。"
hide 陈铭
narrator_adv "陈铭发现，第一案的身份判断缺少关键的独立核验。当时众人只是根据外貌和现场情况作出了推断。"
show 陈铭 at right
role1 "我们从来没有真正确认过。"
menu:
    "逐项核对记录":
        jump g2
