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

label e38:
play music "audio/恐怖.mp3"
scene 尸体
with dissolve
narrator_adv "顾承骁检查倒下的木凳和周围地面。木凳的一条腿有明显裂痕，旁边散落着几块木屑。"
show 顾承骁 at right
role5 "这张凳子应该不是自己倒下的。"
hide 顾承骁
show 陈铭 at right
role1 "周围有挣扎或碰撞的痕迹。"
hide 陈铭
narrator_adv "顾承骁继续检查地面，发现灰尘中有几道方向不同的擦痕。其中一道一直延伸到遮挡尸体的旧家具旁。"
show 顾承骁 at right
role5 "这些痕迹可能是有人移动家具时留下的。"
hide 顾承骁
show 陈铭 at right
role1 "也可能与尸体被藏起来有关。"
hide 陈铭
narrator_adv "旧家具后方还留着一处不太明显的鞋印，鞋印边缘已经被灰尘覆盖，无法直接判断留下的时间。"
show 顾承骁 at right
role5 "这里不止一个人的活动痕迹。"
hide 顾承骁
show 陈铭 at right
role1 "先拍下位置，之后再和其他地方的痕迹对照。"
menu:
    "汇总线索":
        jump e39
