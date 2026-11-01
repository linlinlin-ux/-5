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

label e9:
play music "audio/推理.mp3"
scene 大厅早
show 陈铭 at right
with dissolve
role1 "把找到的东西都放在一起吧。旧登记册、那张写着日期的纸片，还有之前发现的旧照片。"
scene 旧图
hide 陈铭
show 许知微 at right
with dissolve
role3 "纸片上的日期，和照片背面的日期是同一年。"
scene 大厅早
hide 许知微
show 陈铭 at right
with dissolve
role1 "确定吗？"
hide 陈铭
show 许知微 at right
role3 "我又核对了一遍，确实如此。"
hide 许知微
show 顾承骁 at right
role5 "也就是说，这些东西都和十年前有关。"
hide 顾承骁
show 陈铭 at right
role1 "至少可以确定，它们指向同一个时间段。但这还不能证明它们来自同一件事。"
hide 陈铭
show 许知微 at right
role3 "照片上的人……你们真的一点印象都没有吗？"
scene 旧图
hide 许知微
show 陈铭 at right
with dissolve
role1 "照片已经很模糊了，而且没有留下清楚的姓名。现在仅凭照片认人，很容易出错。"
scene 登记
hide 陈铭
show 顾承骁 at right
with dissolve
role5 "登记册被撕掉的部分，也许记录着当时某些物品的去向。"
scene 大厅早
hide 顾承骁
show 陈铭 at right
with dissolve
role1 "可惜缺失的内容还没有找到。地下室那片碎纸也太小，暂时无法确认是不是从登记册上撕下来的。"
hide 陈铭
show 许知微 at right
role3 "为什么有人要把这些东西藏起来？"
hide 许知微
show 陈铭 at right
role1 "也可能不是藏起来，而是有人不希望我们重新看到它们。"
hide 陈铭
show 顾承骁 at right
role5 "你认为程烈的失踪和十年前的事情有关？"
hide 顾承骁
show 陈铭 at right
role1 "目前还不能确定。但他失踪的时间太巧了，我们不能忽略这种可能。"
hide 陈铭
show 许知微 at right
role3 "那我们是不是应该再找找程烈？"
hide 许知微
show 陈铭 at right
role1 "是。先确认他有没有留下其他东西。尤其是他失踪前，是否接触过这些旧资料。"
hide 陈铭
show 顾承骁 at right
role5 "我们可以再检查一次他的房间。"
hide 顾承骁
show 陈铭 at right
role1 "好。这次重点检查之前遗漏的地方，不要重复已经确认过的线索。"
menu:
    "继续检查":
        jump e10
