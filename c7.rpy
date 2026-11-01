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

label c7:
play music "audio/荒谬2.mp3"
scene 地下室入口
show 陈铭 at right
with dissolve
role1 "现在互相猜疑，只会让凶手有机会继续行动。"
hide 陈铭
show 陈铭 at right
role1 "我们先把已经发生的事情弄清楚。周砚和林伯接连死亡，说明这座房子里还有我们不知道的秘密。"
hide 陈铭
show 许知微 at right
role3 "可是我们连手机都没有信号，船也不知道什么时候来。"
hide 许知微
show 陆闻川 at right
role2 "我不想再待在这里了。"
hide 陆闻川
show 顾承骁 at right
role5 "至少现在不能擅自行动。谁也不知道外面是什么情况。"
hide 顾承骁
show 程烈 at right
role4 "那就继续查！总不能一直等着下一个人死掉！"
hide 程烈
narrator_adv "众人虽然暂时停止了争吵，但彼此之间的戒备并没有消失。"
show 陈铭 at right
role1 "先回到大厅。我们需要重新考虑接下来该怎么办。"
menu:
    "结束讨论":
        jump c9
