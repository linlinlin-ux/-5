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

label e39:
play music "audio/恐怖.mp3"
scene 通道
with dissolve
narrator_adv "三人重新聚到一起。陈铭将刚才发现的情况逐一记录下来。"
show 陈铭 at right
role1 "目前可以确认，程烈不是单纯失踪。他死在这间杂物室里，现场存在明显的碰撞和移动痕迹。"
hide 陈铭
show 许知微 at right
role3 "而且尸体被人用旧布料遮住了。"
hide 许知微
show 顾承骁 at right
role5 "他的随身物品似乎也被翻动过。"
hide 顾承骁
show 陈铭 at right
role1 "还有他手里的纤维，以及布料下面的纸屑。这些都需要进一步比对。"
hide 陈铭
show 许知微 at right
role3 "你觉得他是自己来到这里的吗？"
hide 许知微
show 陈铭 at right
role1 "目前无法确定。但通道里的脚印和房间里的痕迹，说明这里确实有人活动过。"
hide 陈铭
show 顾承骁 at right
role5 "那档案盒呢？程烈会不会就是为了那些资料才来的？"
hide 顾承骁
show 陈铭 at right
role1 "有可能。我们已经找到档案盒，也发现程烈可能接触过里面的资料。接下来要弄清楚，他究竟看到了什么。"
hide 陈铭
narrator_adv "陈铭看向通道入口。程烈的死亡让原本分散的线索重新联系起来，但真正的经过仍然隐藏在缺失的资料和被遮掩的痕迹之中。"
menu:
    "对比程烈留下的纸屑":
        jump e40
