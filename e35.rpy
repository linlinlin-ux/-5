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

label e35:
play music "audio/恐怖.mp3"
scene 尸体
with dissolve
narrator_adv "陈铭示意许知微和顾承骁不要靠近尸体。他打开手电筒，先观察房间里的整体情况。"
show 许知微 at right
role3 "他怎么会死在这种地方……"
hide 许知微
show 陈铭 at right
role1 "先冷静。不要破坏现场。"
hide 陈铭
narrator_adv "程烈的尸体被几块旧布料遮挡，旁边堆着废弃家具。地面有明显的凌乱痕迹，倒下的木凳距离尸体不远。"
show 顾承骁 at right
role5 "看起来不像是意外。"
hide 顾承骁
show 陈铭 at right
role1 "至少这里发生过一些事情。我们分开检查，但不要随意移动物品。"
hide 陈铭
narrator_adv "陈铭将现场分成三个部分：程烈的尸体、遮挡尸体的布料，以及周围的杂物和地面痕迹。"
show 陈铭 at right
role1 "先检查尸体本身。"
hide 陈铭
show 许知微 at right
role3 "我检查这些布料，看看有没有留下什么。"
hide 许知微
show 顾承骁 at right
role5 "我看看周围的家具和地面。"
menu:
    "检查程烈尸体":
        jump e36

    "检查遮挡尸体的布料":
        jump e37

    "检查程烈死亡现场周围":
        jump e38
