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

label b7:
play music "audio/杀人之夜.mp3"
scene 命案现场
with dissolve
narrator_adv "陈铭重新检查房间里的桌面、床头柜和附近的摆设，寻找可能与案发有关的遗留物。"
show 陈铭 at right
role1 "这里的东西摆放得很整齐，不像是有人匆忙翻找过。"
scene 柜子
hide 陈铭
with dissolve
narrator_adv "床头柜上放着一杯喝剩的水，旁边有一张折叠过的纸。"
show 陈铭 at right
role1 "这张纸是什么？"
hide 陈铭
narrator_adv "陈铭戴好手套，小心地展开纸张。上面没有完整的文字，只有几道不太清晰的折痕，以及一小片被撕去的边角。"
show 陆闻川 at right
role2 "会不会是周砚留下的遗书？"
hide 陆闻川
show 陈铭 at right
role1 "现在还不能这么说。上面没有足够的信息证明它与死亡有关。"
hide 陈铭
narrator_adv "陈铭继续检查床头柜，没有发现明显的药瓶、凶器或其他能够直接确定死因的物品。"
show 许知微 at right
role3 "既然什么都没有，为什么还要检查这些？"
hide 许知微
show 陈铭 at right
role1 "因为看起来普通的东西，也可能在之后的调查中变得重要。不过，我们不能因为它可疑，就直接认定它是关键证据。"
hide 陈铭
narrator_adv "陈铭将纸张的外观和摆放位置记录下来，没有随意移动其他物品。"
show 陈铭 at right
role1 "目前只能确认这张纸值得留意，至于它的用途，还需要更多线索。"
hide 陈铭
show 顾承骁 at right
role5 "如果之后发现了与这张纸有关的信息，再回来核对也不迟。"
hide 顾承骁
show 陈铭 at right
role1 "没错。先继续调查其他线索。"
menu:
    "检查尸体衣着":
        jump b5

    "检查房间":
        jump b3

    "询问许知微的旧事":
        jump b9
