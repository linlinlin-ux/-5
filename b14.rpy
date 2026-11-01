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

label b14:
play music "audio/杀人之夜.mp3"
scene 走廊早
show 陈铭 at right
with dissolve
role1 "我们先把目前掌握的信息重新整理一遍。"
hide 陈铭
show 陈铭 at right
role1 "第一，尸体是在今天早晨被发现的，发现地点是房间内。"
hide 陈铭
role1 "第二，房门没有明显的破坏痕迹，窗户也没有发现明显的破损。"
role1 "第三，死者的衣着相对整齐，没有发现明显的撕扯痕迹。"
role1 "第四，窗边有一些模糊的压痕，但目前无法确认是不是鞋印，更无法确定属于谁。"
show 陆闻川 at right
role2 "所以这些东西根本没什么用？"
hide 陆闻川
show 陈铭 at right
role1 "不能这么说。没有立即得出结论，不代表线索毫无价值。"
hide 陈铭
show 许知微 at right
role3 "那张折起来的纸呢？床头柜上的那张。"
hide 许知微
show 陈铭 at right
role1 "纸上没有完整的文字，而且缺了一角。它可能与案件有关，也可能只是普通的遗留物。"
hide 陈铭
show 程烈 at right
role4 "还有尸体右手上的旧伤。你刚才不是也看到了吗？"
hide 程烈
show 陈铭 at right
role1 "看到了。但那是已经愈合的旧伤，不能直接用来判断死亡原因。"
hide 陈铭
show 顾承骁 at right
role5 "听起来，你什么都不敢确定。"
hide 顾承骁
show 陈铭 at right
role1 "因为我们现在确实没有足够的证据。比起急着指认某个人，我更不愿意把错误的推测当成事实。"
hide 陈铭
show 陆闻川 at right
role2 "那你觉得接下来应该查什么？"
hide 陆闻川
show 陈铭 at right
role1 "我建议从三个方向继续。第一，弄清楚林伯昨晚到今天早晨的行动；第二，追问我们与死者之间的旧事；第三，继续检查现场遗留物。"
menu:
    "追问林伯昨晚的行动":
        jump b16

    "继续追问十年前的旧事":
        jump b15

    "重新检查房间遗留物":
        jump b7
