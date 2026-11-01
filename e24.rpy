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

label e24:
play music "audio/推理2.mp3"
scene 大厅
with dissolve
narrator_adv "陈铭将存根上的号码记录下来，又仔细核对了上面的日期。"
show 许知微 at right
role3 "这个日期比林伯原本计划离岛的时间晚一天。"
hide 许知微
show 陈铭 at right
role1 "也就是说，林伯可能原本打算先离开，再安排船只回来接其他人。"
hide 陈铭
show 顾承骁 at right
role5 "但他没能离开，后面的接送自然也可能受到影响。"
hide 顾承骁
show 许知微 at right
role3 "那我们是不是只要联系船方，就能知道到底发生了什么？"
hide 许知微
show 陈铭 at right
role1 "可以尝试。不过我们现在没有信号，而且不知道这个号码是否还有效。"
hide 陈铭
show 顾承骁 at right
role5 "先把存根保管好。等有机会联系外界，再核实这件事。"
hide 顾承骁
narrator_adv "陈铭将存根夹回记录册中。船只没有出现的原因仍然不明，但他们终于找到了一条能够向外界核实的线索。"
show 许知微 at right
role3 "可是如果船一直不来，我们还要在这里等多久？"
hide 许知微
show 陈铭 at right
role1 "不能一直等。我们还得继续找程烈，也要弄清楚宅邸里究竟发生了什么。"
hide 陈铭
show 顾承骁 at right
role5 "先回到之前的调查吧。程烈失踪的事情还没有解决。"
hide 顾承骁
show 陈铭 at right
role1 "好。我们再检查一下刚才发现的线索，看看有没有遗漏。"
menu:
    "检查线索":
        jump e25
