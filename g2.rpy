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

label g2:
play music "audio/荒谬2.mp3"
scene 工作间
with dissolve
narrator_adv "陈铭将旧校医登记记录与第一案的尸体调查资料放在一起，逐项核对。"
show 陈铭 at right
role1 "这份记录里提到，顾承骁以前右手受过伤，留下过一道旧伤痕。"
hide 陈铭
narrator_adv "陈铭翻出第一案关于尸体右手的记录。当时调查时，曾经注意到死者右手上的旧伤，却没有将它与身份联系起来。"
show 陈铭 at right
role1 "位置和形状都能对应上。"
hide 陈铭
narrator_adv "他又查看周砚的旧校医记录。周砚的就诊资料中，并没有这处旧伤的记载。"
show 陈铭 at right
role1 "如果这份记录没有出错，那么第一具尸体更符合顾承骁的身份。"
hide 陈铭
narrator_adv "陈铭重新回忆当时的情景。众人因为两张相似的面孔，将死者认成了周砚，却没有真正核实过身份。"
show 陈铭 at right
role1 "死在第一案现场的……其实是顾承骁。"
hide 陈铭
narrator_adv "陈铭的视线逐渐移向那个一直以顾承骁身份留在众人身边的人。"
show 陈铭 at right
role1 "那么，真正的周砚一直就在我们中间。"
hide 陈铭
narrator_adv "这意味着第一案并不是周砚遇害，而是周砚利用两人天生相似的面孔，让所有人误以为自己已经死了。"
show 陈铭 at right
role1 "他从一开始就没有离开过这座宅邸。"
menu:
    "……":
        jump g3
