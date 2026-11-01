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

label e6:
play music "audio/恐怖.mp3"
scene 地下室2
show 许知微 at right
with dissolve
role3 "又回到这里了……林伯就是在这附近死的。"
hide 许知微
show 陈铭 at right
role1 "先别碰任何东西。看看楼梯和储藏室入口有没有新的痕迹。"
hide 陈铭
show 许知微 at right
role3 "楼梯扶手上有一道浅浅的擦痕，像是有什么东西撞过这里。"
hide 许知微
show 陈铭 at right
role1 "擦痕的位置不高，更像是物体碰撞留下的，不一定与林伯的死亡有关。"
hide 陈铭
show 许知微 at right
role3 "储藏室门边有些灰尘被蹭掉了。最近应该有人进出过。"
hide 许知微
show 陈铭 at right
role1 "林伯死后，这里并不是完全无人来过。我们还不能确定是谁留下的。"
hide 陈铭
show 许知微 at right
role3 "里面的东西似乎也被动过。"
hide 许知微
show 陈铭 at right
role1 "先记录位置，不要随意移动。"
scene 角落
hide 陈铭
show 许知微 at right
with dissolve
role3 "等等，角落里有一小片纸。"
scene 地下室2
hide 许知微
show 陈铭 at right
with dissolve
role1 "像是从某份文件上撕下来的，上面只剩下一部分印刷痕迹。"
hide 陈铭
show 许知微 at right
role3 "能看清是什么吗？"
hide 许知微
show 陈铭 at right
role1 "现在还不行。先收起来，之后和其他文件对照。"
hide 陈铭
show 许知微 at right
role3 "这里还有别的值得检查的地方吗？"
hide 许知微
show 陈铭 at right
role1 "暂时没有。我们先回去和顾承骁汇合。"
menu:
    "会合":
        jump e8
