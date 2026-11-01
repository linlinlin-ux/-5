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

label b20:
play music "audio/荒谬.mp3"
scene 长桌早
with dissolve
narrator_adv "第三天早晨，众人陆续从房间里出来。"
show 陆闻川 at right
role2 "林伯呢？今天怎么连早餐都没有准备？"
hide 陆闻川
show 许知微 at right
role3 "昨天晚上好像也没见到他。"
hide 许知微
show 程烈 at right
role4 "这老头又跑哪儿去了？"
hide 程烈
show 顾承骁 at right
role5 "先找找看，别浪费时间。"
hide 顾承骁
narrator_adv "众人在一楼寻找林伯，却始终没有找到他的身影。"
scene 走廊早
show 陆闻川 at right
with dissolve
role2 "他的房间没人，里面也没有什么异常。"
hide 陆闻川
show 许知微 at right
role3 "地下室的门好像开着。"
hide 许知微
show 程烈 at right
role4 "他会不会在下面？"
hide 程烈
show 顾承骁 at right
role5 "下去看看。"
scene 地下室
hide 顾承骁
with dissolve
narrator_adv "地下室的楼梯狭窄而昏暗，空气中弥漫着一股潮湿的气味。"
show 陆闻川 at right
role2 "等等……下面是不是躺着一个人？"
hide 陆闻川
show 许知微 at right
role3 "那是……林伯？"
hide 许知微
show 程烈 at right
role4 "林伯！"
hide 程烈
narrator_adv "林伯倒在楼梯底部，身体侧向一边，一只手臂压在身下。"
show 陆闻川 at right
role2 "怎么会这样？他怎么会死在这里？"
hide 陆闻川
show 许知微 at right
role3 "他昨天还好好的……"
hide 许知微
show 顾承骁 at right
role5 "别碰他，先让陈铭看看。"
hide 顾承骁
narrator_adv "陈铭走近尸体，确认林伯已经没有呼吸。"
show 陈铭 at right
role1 "现场暂时没有发现明显的大面积血迹，但仅凭尸体的位置，还不能判断他究竟是意外坠落，还是遭人袭击。"
hide 陈铭
show 程烈 at right
role4 "又死人了！我们到底还要在这个鬼地方待多久？"
hide 程烈
show 陆闻川 at right
role2 "先把这里查清楚再说。"
hide 陆闻川
show 陈铭 at right
role1 "我们分头检查现场，但不要随意移动任何东西。"
menu:
    "检查地下室楼梯现场":
        jump c2

    "检查林伯尸体":
        jump c3

    "确认林伯最后出现的时间":
        jump c4
