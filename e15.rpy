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

label e15:
play music "audio/推理2.mp3"
scene 室内
show 许知微 at right
with dissolve
role3 "这里就是林伯的房间？"
hide 许知微
show 陈铭 at right
role1 "应该是。房间里的东西摆放得很整齐，看来他平时生活习惯很严谨。"
hide 陈铭
show 顾承骁 at right
role5 "书桌上有一本工作记录。"
hide 顾承骁
show 陈铭 at right
role1 "打开看看。"
scene 记录
hide 陈铭
show 许知微 at right
with dissolve
role3 "里面记录的都是日常事务，采购、维修，还有一些客人的来访安排。"
hide 许知微
show 陈铭 at right
role1 "往前翻。看看十年前有没有记录。"
hide 陈铭
show 顾承骁 at right
role5 "这里有一页。日期和登记册上的日期只差两天。"
hide 顾承骁
show 许知微 at right
role3 "写了什么？"
hide 许知微
show 陈铭 at right
role1 "「旧物已按要求转移，原存放位置清理完毕。」"
scene 室内
hide 陈铭
show 顾承骁 at right
with dissolve
role5 "没有写明转移的是什么东西。"
hide 顾承骁
show 陈铭 at right
role1 "但这条记录至少能证明，十年前确实有人要求转移过某件旧物。"
hide 陈铭
show 许知微 at right
role3 "会不会就是地下室夹层里原本存放的东西？"
hide 许知微
show 陈铭 at right
role1 "时间和编号都能对上，这个可能性很高。"
hide 陈铭
show 顾承骁 at right
role5 "可是记录里没有提到是谁要求转移的。"
hide 顾承骁
show 陈铭 at right
role1 "还有没有其他内容？"
hide 陈铭
show 许知微 at right
role3 "下一页被撕掉了。只剩下一点纸根。"
hide 许知微
show 陈铭 at right
role1 "看来这本记录也有人动过手脚。"
hide 陈铭
show 顾承骁 at right
role5 "或许有人不想让我们知道那件旧物的去向。"
hide 顾承骁
show 陈铭 at right
role1 "先把这页记录保存好。现在我们至少知道，十年前有人转移过地下室里的东西。"
menu:
    "继续整理线索":
        jump e16
