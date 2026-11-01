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

label c2:
play music "audio/荒谬2.mp3"
scene 地下室
show 陈铭 at right
with dissolve
role1 "先检查楼梯。林伯倒在最下面，坠落的位置可能留下了一些痕迹。"
hide 陈铭
narrator_adv "楼梯一侧安装着木质扶手，表面有些磨损，但整体没有明显松动。"
show 陆闻川 at right
role2 "如果扶手没问题，他怎么会突然摔下去？"
hide 陆闻川
show 陈铭 at right
role1 "现在还不能排除意外。继续检查台阶。"
hide 陈铭
show 陈铭 at right
role1 "靠近楼梯中段的一处台阶边缘，有一道新鲜的擦痕。"
hide 陈铭
show 许知微 at right
role3 "像是有什么东西撞到了这里。"
hide 许知微
show 陈铭 at right
role1 "擦痕附近没有发现明显的血迹，也无法判断它是什么时候留下的。"
hide 陈铭
show 程烈 at right
role4 "这能说明什么？"
hide 程烈
show 陈铭 at right
role1 "至少说明这里可能发生过碰撞，但还不能确定和林伯的死亡有关。"
hide 陈铭
show 陈铭 at right
role1 "楼梯底部的地面有一小片潮湿的痕迹，边缘还能看到不完整的鞋底印记。"
hide 陈铭
show 顾承骁 at right
role5 "地下室本来就潮湿，留下脚印也不奇怪。"
hide 顾承骁
show 陈铭 at right
role1 "确实如此。不过，这片痕迹的具体来源还需要结合其他线索判断。"
hide 陈铭
show 陆闻川 at right
role2 "也就是说，我们还是不知道他究竟怎么摔下来的？"
hide 陆闻川
show 陈铭 at right
role1 "仅凭楼梯现场还无法确定。先检查尸体，看看有没有其他发现。"
menu:
    "检查林伯尸体":
        jump c3

    "确认林伯最后出现的时间":
        jump c4
