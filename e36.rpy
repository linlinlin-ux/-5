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

label e36:
play music "audio/恐怖.mp3"
scene 尸体
with dissolve
narrator_adv "陈铭蹲在尸体旁，仔细观察程烈的衣着和身体状况。程烈的衣服有多处褶皱，袖口也有明显的拉扯痕迹。"
show 陈铭 at right
role1 "衣服被拉扯过，身上也有一些擦伤。"
hide 陈铭
narrator_adv "陈铭注意到程烈的右手紧紧蜷着，指缝里似乎夹着一点深色的细小纤维。"
show 陈铭 at right
role1 "他的手里有东西。"
hide 陈铭
narrator_adv "陈铭小心查看，发现那是一小缕深色布料纤维，无法仅凭外观判断来源。"
show 许知微 at right
role3 "会不会是凶手衣服上留下的？"
hide 许知微
show 陈铭 at right
role1 "有这种可能，但也可能来自这里的旧布料。不能急着下结论。"
hide 陈铭
narrator_adv "陈铭继续检查，发现程烈身上没有明显的随身物品。口袋已经空了，只留下被翻动过的痕迹。"
show 陈铭 at right
role1 "他的随身物品可能被人拿走了。"
hide 陈铭
show 顾承骁 at right
role5 "是有人想拿走什么，还是不想让我们发现什么？"
hide 顾承骁
show 陈铭 at right
role1 "这两种可能都存在。先记录下来。"
menu:
    "检查遮挡尸体的布料":
        jump e37

    "检查程烈死亡现场周围":
        jump e38
