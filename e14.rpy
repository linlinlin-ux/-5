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

label e14:
play music "audio/推理2.mp3"
scene 登记
show 陈铭 at right
with dissolve
role1 "登记册上这条记录的日期是十年前的六月。编号和地下室找到的标签一致。"
scene 大厅早
hide 陈铭
show 许知微 at right
with dissolve
role3 "可是物品名称已经被撕掉了，我们怎么知道当时存放的是什么？"
hide 许知微
show 顾承骁 at right
role5 "登记册不一定是唯一的记录。宅邸里应该还有其他相关资料。"
hide 顾承骁
show 陈铭 at right
role1 "林伯负责管理这座宅邸的日常事务，他或许接触过这些旧档案。"
hide 陈铭
show 许知微 at right
role3 "可是林伯已经死了。"
hide 许知微
show 陈铭 at right
role1 "我知道。但我们可以从他的房间和遗留物品里找找线索。"
hide 陈铭
show 顾承骁 at right
role5 "林伯的房间之前检查过吗？"
hide 顾承骁
show 陈铭 at right
role1 "只检查过他死亡的地方，还没有仔细整理他的私人房间。"
hide 陈铭
show 许知微 at right
role3 "那就去看看吧。说不定他留下了什么记录。"
hide 许知微
show 顾承骁 at right
role5 "我和你们一起去。"
hide 顾承骁
show 陈铭 at right
role1 "好。先找与十年前登记记录有关的东西，不要把无关物品也当成线索。"
menu:
    "调查林伯房间":
        jump e15
