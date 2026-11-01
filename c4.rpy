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

label c4:
play music "audio/推理.mp3"
scene 地下室入口
with dissolve
narrator_adv "陈铭将众人召集到地下室入口，准备确认林伯昨天最后一次出现的时间。"
show 陈铭 at right
role1 "昨天晚上，你们最后一次见到林伯是什么时候？"
hide 陈铭
show 陆闻川 at right
role2 "晚饭结束后我就回房间了。那之后没再见过他。"
hide 陆闻川
show 许知微 at right
role3 "我也是。晚饭后一直待在房间里，没注意他去了哪里。"
hide 许知微
show 程烈 at right
role4 "我晚上出去过一次，在走廊上好像看见他往楼梯那边走。"
hide 程烈
show 陈铭 at right
role1 "你确定是地下室的方向？"
hide 陈铭
show 程烈 at right
role4 "不确定。当时隔得有点远，我只是看到一个人影。"
hide 程烈
show 顾承骁 at right
role5 "我没见过他。晚饭后我一直在房间里。"
hide 顾承骁
show 陈铭 at right
role1 "你们有人在昨晚晚饭后和林伯说过话吗？"
hide 陈铭
show 陆闻川 at right
role2 "没有。"
hide 陆闻川
show 许知微 at right
role3 "我没有。"
hide 许知微
show 程烈 at right
role4 "我也没有。"
hide 程烈
show 顾承骁 at right
role5 "没有。"
hide 顾承骁
narrator_adv "陈铭低头查看记录，随后又想起了林伯昨天晚上的行动。"
show 陈铭 at right
role1 "林伯昨天晚饭后还在大厅附近活动过。除此之外，我们没有可靠的目击信息。"
hide 陈铭
show 陆闻川 at right
role2 "所以他什么时候去的地下室，我们根本不知道？"
hide 陆闻川
show 陈铭 at right
role1 "是。目前只能确认，昨晚之后没人能说清他的具体行踪。"
hide 陈铭
show 许知微 at right
role3 "那会不会有人趁我们都回房间之后，单独找过他？"
hide 许知微
show 顾承骁 at right
role5 "现在猜测这些没有意义。还是先看现场有没有其他证据吧。"
hide 顾承骁
narrator_adv "陈铭将众人的说法记录下来，没有急着作出判断。"
show 陈铭 at right
role1 "三处调查已经有了初步结果。我们先把线索整理清楚。"
menu:
    "整理林伯死亡线索":
        jump c5
