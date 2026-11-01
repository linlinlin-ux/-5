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

label e31:
play music "audio/恐怖.mp3"
scene 储物间4
with dissolve
narrator_adv "陈铭移开挡在角落的旧木架，后面露出一块狭窄的地面。地面上有明显的摩擦痕迹，旁边还掉着一小片深色布料。"
show 许知微 at right
role3 "这是衣服上的碎片吗？"
hide 许知微
show 陈铭 at right
role1 "看起来像，但还不能确定属于谁。"
hide 陈铭
show 顾承骁 at right
role5 "这里最近确实有人活动过。"
hide 顾承骁
narrator_adv "陈铭蹲下身，发现布料旁边还有一道浅浅的擦痕，像是某件物品被拖动后留下的。"
show 陈铭 at right
role1 "先不要碰它。"
hide 陈铭
show 许知微 at right
role3 "你觉得程烈来过这里吗？"
hide 许知微
show 陈铭 at right
role1 "他房间里的纸屑和地下储藏室的碎片能证明他接触过相关资料，但还不能证明他最后来过这里。"
hide 陈铭
show 顾承骁 at right
role5 "那我们接下来怎么办？"
hide 顾承骁
show 陈铭 at right
role1 "把这里记录下来，再检查这间储物室有没有其他出口。"
scene 窄门
hide 陈铭
with dissolve
narrator_adv "陈铭站起身，目光落在角落后方的一道窄门上。门板与墙壁几乎融为一体，之前被旧家具挡住了。"
scene 储物间4
show 许知微 at right
with dissolve
role3 "那后面是什么地方？"
hide 许知微
show 陈铭 at right
role1 "打开就知道了。"
menu:
    "开门":
        jump e32
