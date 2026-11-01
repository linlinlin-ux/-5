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

label c9:
play music "audio/荒谬2.mp3"
scene 地下室入口
with dissolve
narrator_adv "一番争论过后，众人终于暂时停止了争吵。地下室入口重新恢复了安静，但每个人脸上都带着明显的不安。"
show 陆闻川 at right
role2 "我们不能一直待在地下室。先回大厅吧。"
hide 陆闻川
show 许知微 at right
role3 "我现在只想知道，船到底什么时候才能来。"
hide 许知微
show 程烈 at right
role4 "等船来了，我绝对不会再踏进这个鬼地方一步。"
hide 程烈
show 顾承骁 at right
role5 "先离开这里再说。"
hide 顾承骁
narrator_adv "陈铭最后看了一眼楼梯底部的林伯，随后跟着众人离开地下室。"
scene 大厅早
with dissolve
narrator_adv "回到大厅后，众人各自找了位置坐下。没有人主动开口，彼此之间的距离似乎比之前更远了。"
show 陆闻川 at right
role2 "陈铭，你觉得林伯的死和周砚的死有关系吗？"
hide 陆闻川
show 陈铭 at right
role1 "目前还不能确定。但两起死亡接连发生，绝不能简单地当作巧合。"
hide 陈铭
show 许知微 at right
role3 "如果真的是同一个人做的，那他现在还在这里……"
hide 许知微
show 程烈 at right
role4 "别说了！越说越让人心烦。"
hide 程烈
show 顾承骁 at right
role5 "我们现在最应该做的是保护好自己，别单独行动。"
hide 顾承骁
show 陈铭 at right
role1 "这倒是个办法。至少在离开这里之前，尽量不要独自行动。"
hide 陈铭
narrator_adv "众人暂时达成了一致，但没有人真正放下戒备。"
narrator_adv "陈铭看向窗外。海面平静，远处没有船只的踪影。"
show 陆闻川 at right
role2 "看来今天也等不到船了。"
hide 陆闻川
show 陈铭 at right
role1 "先休息一会儿吧。等有新的情况再通知大家。"
hide 陈铭
narrator_adv "众人陆续散开。第三天的调查暂时告一段落。"
menu:
    "进入下一段剧情":
        jump c10
