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

label d15:
play music "audio/荒谬2.mp3"
scene 大厅
with dissolve
narrator_adv "傍晚，陈铭回到大厅。桌面上摆着陆闻川留下的戒指、纸条和资金文件，旁边则放着刚刚发现的孔雀羽毛。"
show 许知微 at right
role3 "现在已经死了两个人，还有林伯……我们到底还要在这里待多久？"
hide 许知微
show 程烈 at right
role4 "船不是说好要来吗？怎么到现在一点消息都没有？"
hide 程烈
show 陈铭 at right
role1 "我们没有通讯设备，无法确认船只的具体情况。"
hide 陈铭
show 陆闻川 at right
role2 "旁白"
hide 陆闻川
show 顾承骁 at right
role5 "现在最重要的是弄清楚谁在杀人，而不是一直抱怨船的事情。"
hide 顾承骁
show 许知微 at right
role3 "可是我们连凶手是谁都不知道！"
hide 许知微
show 程烈 at right
role4 "这两起命案肯定不是巧合。有人在针对我们。"
hide 程烈
show 陈铭 at right
role1 "你为什么这么认为？"
hide 陈铭
show 程烈 at right
role4 "想想看，周砚把我们叫到这里，林伯死了，接着陆闻川也死了。难道不是有人想让所有知情的人闭嘴？"
hide 程烈
show 许知微 at right
role3 "知情的人……你是说十年前的事情？"
hide 许知微
show 程烈 at right
role4 "不然还能是什么？"
hide 程烈
show 顾承骁 at right
role5 "你们未免太看得起那件旧事了。"
hide 顾承骁
show 许知微 at right
role3 "可如果有人不想让十年前的事情曝光呢？"
hide 许知微
show 陈铭 at right
role1 "你的意思是，有人为了保住自己的工作和现在的生活，特意来到这座岛上销毁证据，甚至杀人灭口？"
hide 陈铭
show 许知微 at right
role3 "我只是觉得有这种可能。"
hide 许知微
show 程烈 at right
role4 "如果真是这样，那我们每个人都有可能成为下一个目标。"
hide 程烈
show 顾承骁 at right
role5 "你是在暗示我们当中有人是凶手？"
hide 顾承骁
show 程烈 at right
role4 "我可没指名道姓。"
hide 程烈
narrator_adv "程烈的目光从顾承骁身上移开，又扫过许知微。大厅里的气氛逐渐变得紧张。"
show 许知微 at right
role3 "你看着我干什么？我什么都没做！"
hide 许知微
show 程烈 at right
role4 "我又没说是你，你这么激动干什么？"
hide 程烈
show 许知微 at right
role3 "你！"
hide 许知微
show 陈铭 at right
role1 "够了。互相指责解决不了问题。"
hide 陈铭
show 顾承骁 at right
role5 "陈铭说得对。现在最应该做的是把已经找到的证据整理清楚。"
hide 顾承骁
narrator_adv "顾承骁说完，转身离开了大厅。许知微仍然坐在沙发上，脸色十分难看。"
show 程烈 at right
role4 "你觉得他刚才的反应正常吗？"
hide 程烈
show 陈铭 at right
role1 "现在谁的反应都不能作为判断依据。"
hide 陈铭
narrator_adv "陈铭将桌上的证物重新收好。众人虽然暂时停止了争吵，但彼此之间的信任已经明显动摇。"
menu:
    "继续调查现有证据":
        jump d16

    "与许知微单独交谈":
        jump d17

    "与程烈单独交谈":
        jump d18
