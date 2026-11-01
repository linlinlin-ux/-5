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

label e13:
play music "audio/推理2.mp3"
scene 登记
show 陈铭 at right
with dissolve
role1 "找到了。旧登记册里有一部分编号格式和这截标签相同。"
scene 大厅早
hide 陈铭
show 许知微 at right
with dissolve
role3 "能找到对应的记录吗？"
scene 登记
hide 许知微
show 陈铭 at right
with dissolve
role1 "这里有一条记录，但后面的物品名称被撕掉了。"
scene 大厅早
hide 陈铭
show 顾承骁 at right
with dissolve
role5 "日期呢？"
hide 顾承骁
show 陈铭 at right
role1 "十年前。"
hide 陈铭
show 许知微 at right
role3 "又是十年前……"
hide 许知微
show 顾承骁 at right
role5 "这说明地下室的夹层很可能曾经存放过一件与旧登记记录有关的东西。"
hide 顾承骁
show 陈铭 at right
role1 "但我们不知道那件东西是什么，也不知道它现在在哪里。"
hide 陈铭
show 许知微 at right
role3 "程烈会不会就是为了找它才去了地下室？"
hide 许知微
show 陈铭 at right
role1 "这是一个可能性。可惜目前还缺少能证明这一点的证据。"
hide 陈铭
show 顾承骁 at right
role5 "如果那件东西已经被人拿走了，我们继续留在这里也不会有结果。"
hide 顾承骁
show 陈铭 at right
role1 "先把编号、日期和登记册的缺失部分记录下来。接下来要查清楚十年前究竟有什么东西被存放在这里。"
menu:
    "继续调查":
        jump e14
