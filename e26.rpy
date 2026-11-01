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

label e26:
play music "audio/恐怖.mp3"
scene 储物间3
with dissolve
narrator_adv "陈铭一行人再次来到地下储藏室。昏暗的灯光下，柜子旁的地面仍留着之前发现的拖痕。"
show 陈铭 at right
role1 "之前我们只检查了柜子和夹层，还没有仔细看过这附近的墙壁。"
hide 陈铭
show 许知微 at right
role3 "你觉得这里还有别的空间？"
hide 许知微
show 陈铭 at right
role1 "不确定。不过，柜子被移动过，总该有原因。"
hide 陈铭
narrator_adv "陈铭沿着墙壁检查，发现柜子后方的墙面与周围略有不同。靠近地面的位置有一道不太明显的缝隙。"
show 顾承骁 at right
role5 "这里好像不是完整的墙。"
hide 顾承骁
show 陈铭 at right
role1 "帮我把柜子往旁边挪一点。"
scene 窄门
hide 陈铭
with dissolve
narrator_adv "几人合力移动柜子，墙面后方露出一扇窄小的储物门。门没有上锁，但边缘积着一层灰尘。"
show 许知微 at right
role3 "这里居然还有一扇门……"
hide 许知微
show 陈铭 at right
role1 "先别进去，看看门口有没有留下什么痕迹。"
hide 陈铭
narrator_adv "门槛附近有几处新鲜的擦痕，灰尘被蹭开了一小片，像是近期有人进出过。"
show 顾承骁 at right
role5 "程烈会不会来过这里？"
hide 顾承骁
show 陈铭 at right
role1 "现在还不能确定。进去看看。"
menu:
    "继续探索":
        jump e27
