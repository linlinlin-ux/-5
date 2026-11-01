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

label f7:
play music "audio/推理2.mp3"
scene 工作间
with dissolve
narrator_adv "陈铭将所有资料重新排列。十年前的围堵、医院的抢救通知、四个人的询问记录，以及那段没有提交的录像，终于连成了一条完整的线索。"
show 陈铭 at right
role1 "周砚失去母亲，不一定能完全归咎于那场围堵。可他没能及时赶到医院，却是那天真实发生的事情。"
hide 陈铭
show 陈铭 at right
role1 "对他来说，那段时间可能就是最后的希望。"
hide 陈铭
narrator_adv "陈铭看着四个人的名字，逐渐明白周砚为什么会对他们怀有如此深的恨意。"
show 陈铭 at right
role1 "他不仅要他们为霸凌付出代价，也无法原谅他们毁掉了自己最后一次赶去见母亲的机会。"
hide 陈铭
narrator_adv "陈铭又看向自己的名字。"
show 陈铭 at right
role1 "而我明明知道这一切，却选择了沉默。"
hide 陈铭
narrator_adv "档案盒里还有几份关于宅邸和船只安排的资料。它们提醒陈铭，眼前发生的死亡事件并没有结束。"
show 陈铭 at right
role1 "顾承骁、陆闻川、程烈……还有林伯。"
hide 陈铭
show 陈铭 at right
role1 "这些人究竟是怎么一步步走到死亡的？"
hide 陈铭
narrator_adv "陈铭取出第一案的调查记录。比起其他疑问，他突然意识到，自己从未真正确认过第一具尸体的身份。"
show 陈铭 at right
role1 "如果第一案的身份判断本身就是错的，那么我们这几天的调查，可能从一开始就建立在错误的前提上。"
menu:
    "整理线索":
        jump f8
