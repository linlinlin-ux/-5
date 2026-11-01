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

label e16:
play music "audio/推理2.mp3"
scene 室内
show 陈铭 at right
with dissolve
role1 "目前能确认的有三件事：地下室存在一个被使用过的夹层，标签编号对应十年前的登记记录，林伯也记录过一次旧物转移。"
hide 陈铭
show 许知微 at right
role3 "但我们还是不知道那件东西是什么。"
hide 许知微
show 顾承骁 at right
role5 "也不知道它被转移到了哪里。"
hide 顾承骁
show 陈铭 at right
role1 "还有一个问题。林伯为什么没有在工作记录里写下具体的物品名称？"
hide 陈铭
show 许知微 at right
role3 "也许他只是奉命办事，并不知道里面是什么。"
hide 许知微
show 陈铭 at right
role1 "也有可能。我们不能只凭一条记录判断他的真实想法。"
hide 陈铭
show 顾承骁 at right
role5 "不过，这件事应该和十年前的那张照片一起调查。"
hide 顾承骁
show 陈铭 at right
role1 "没错。我们现在需要找到被撕掉的记录，或者找到那件被转移的旧物。"
hide 陈铭
show 许知微 at right
role3 "那程烈呢？我们还没有找到他。"
hide 许知微
show 陈铭 at right
role1 "……先前发现的东西越来越多，但程烈依旧没有消息。"
hide 陈铭
show 顾承骁 at right
role5 "我们不能一直等下去。"
hide 顾承骁
show 陈铭 at right
role1 "再检查一次宅邸。如果还是找不到，我们就必须重新考虑他可能离开的方向。"
menu:
    "继续调查":
        jump e17
