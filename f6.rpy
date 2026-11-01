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

label f6:
play music "audio/推理2.mp3"
scene 工作间
with dissolve
narrator_adv "陈铭继续翻阅当天的资料。在一份没有正式归档的材料中，他发现了一段关于现场影像的记录。"
show 陈铭 at right
role1 "现场影像？"
hide 陈铭
narrator_adv "记录中提到，当天有人在走廊附近拍摄了冲突，但影像最终没有提交给学校。"
show 陈铭 at right
role1 "……"
hide 陈铭
narrator_adv "陈铭想起了那部手机，想起自己站在走廊尽头时，镜头里不断晃动的人影。"
show 陈铭 at right
role1 "是我拍的。"
hide 陈铭
narrator_adv "他终于想起，当时自己确实记录了那场围堵。"
show 陈铭 at right
role1 "我看见周砚一直想走。我也听见他说家里出了急事。"
hide 陈铭
show 陈铭 at right
role1 "可我没有过去。我只是站在那里拍摄，然后在事情结束后把录像留了下来。"
hide 陈铭
narrator_adv "那段影像本来有机会证明周砚当时的处境，也能证明四个人并非只是发生了一次普通争执。"
show 陈铭 at right
role1 "如果我当时把录像交出去，至少不会让他们那么轻易地否认。"
hide 陈铭
narrator_adv "可陈铭最终没有提交录像。他害怕自己被牵连，也害怕成为下一个被针对的人。"
show 陈铭 at right
role1 "我一直告诉自己，我没有参与他们的霸凌。"
hide 陈铭
show 陈铭 at right
role1 "但我明明看见了，却什么都没做。"
hide 陈铭
narrator_adv "陈铭将影像记录放在四个人的资料旁边。"
show 陈铭 at right
role1 "他们的傲慢、贪婪、嫉妒和暴怒，伤害了周砚。而我的懦弱和逃避，也让他失去了一个可以证明真相的机会。"
menu:
    "整理线索":
        jump f7
