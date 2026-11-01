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

label e12:
play music "audio/推理2.mp3"
scene 储物间
show 陈铭 at right
with dissolve
role1 "上次我们只检查了储藏室入口和附近的地面。这次从里面开始仔细检查。"
hide 陈铭
show 许知微 at right
role3 "你觉得那张被撕碎的纸原本就放在这里吗？"
hide 许知微
show 陈铭 at right
role1 "不一定。但既然两片纸能够拼在一起，就说明程烈和这个地方存在某种联系。"
scene 储物间2
hide 陈铭
show 许知微 at right
with dissolve
role3 "这里的柜子好像被移动过。"
hide 许知微
show 陈铭 at right
role1 "柜子底部有一道新鲜的拖擦痕迹，和周围积灰的情况不太一致。"
hide 陈铭
show 许知微 at right
role3 "要把柜子挪开看看吗？"
hide 许知微
show 陈铭 at right
role1 "小心一点。"
hide 陈铭
show 许知微 at right
role3 "后面有个夹层！"
hide 许知微
show 陈铭 at right
role1 "里面是空的，不过边缘积灰很少，应该不久前才有人打开过。"
hide 陈铭
show 许知微 at right
role3 "会不会是程烈发现了这里？"
hide 许知微
show 陈铭 at right
role1 "有可能。但也可能是其他人。"
hide 陈铭
show 许知微 at right
role3 "夹层里好像还剩下一点东西。"
scene 角落
hide 许知微
show 陈铭 at right
with dissolve
role1 "是一小截纸质标签，上面的字已经磨损了，只能辨认出一个残缺的编号。"
scene 储物间2
hide 陈铭
show 许知微 at right
with dissolve
role3 "这个编号有什么用？"
hide 许知微
show 陈铭 at right
role1 "暂时不知道。不过它不像普通的物品标签，更像是档案或物品登记时使用的编号。"
hide 陈铭
show 许知微 at right
role3 "和二楼那本旧登记册有关吗？"
hide 许知微
show 陈铭 at right
role1 "值得对照。先把它收起来。"
hide 陈铭
show 许知微 at right
role3 "这里应该没有其他东西了。"
hide 许知微
show 陈铭 at right
role1 "走吧。我们需要把这个编号和旧登记册上的记录核对一下。"
menu:
    "核对":
        jump e13
