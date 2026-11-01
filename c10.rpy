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

label c10:
play music "audio/宁静.mp3"
scene 大厅早
with dissolve
narrator_adv "午后，豪宅内安静得有些反常。众人各自待在大厅附近，没有人愿意独自离开。"
narrator_adv "陈铭正准备回房间，忽然听见走廊尽头传来一声轻响。"
show 陈铭 at right
role1 "你们听见了吗？"
hide 陈铭
show 陆闻川 at right
role2 "什么声音？"
hide 陆闻川
show 许知微 at right
role3 "好像是从走廊那边传来的。"
hide 许知微
show 程烈 at right
role4 "我去看看。"
hide 程烈
show 顾承骁 at right
role5 "别一个人过去。"
scene 走廊2
hide 顾承骁
with dissolve
narrator_adv "几人来到走廊尽头，发现通往二楼储物间的门没有完全关上。"
show 陆闻川 at right
role2 "这扇门之前不是关着的吗？"
hide 陆闻川
show 陈铭 at right
role1 "你确定？"
hide 陈铭
show 陆闻川 at right
role2 "我早上经过这里的时候，门是关着的。"
hide 陆闻川
show 许知微 at right
role3 "难道有人进去过？"
hide 许知微
show 程烈 at right
role4 "里面有什么值得偷的东西？"
hide 程烈
show 顾承骁 at right
role5 "先进去看看。"
scene 储物间
hide 顾承骁
with dissolve
narrator_adv "陈铭推开房门。储物间里堆放着一些旧家具、纸箱和杂物，看起来并没有明显被翻动过的痕迹。"
show 陈铭 at right
role1 "大部分东西都摆放得很整齐。"
hide 陈铭
narrator_adv "陈铭注意到靠墙的一只纸箱没有完全合上，箱盖边缘留有一道新鲜的折痕。"
show 许知微 at right
role3 "那里面是什么？"
hide 许知微
show 陈铭 at right
role1 "先别动，我看看。"
hide 陈铭
narrator_adv "纸箱里装着一些旧文件和已经泛黄的纸张，但没有明显的标签。"
show 陆闻川 at right
role2 "这些东西看起来放了很多年了。"
hide 陆闻川
show 顾承骁 at right
role5 "这里是周砚的房子，有些旧东西也不奇怪。"
hide 顾承骁
show 陈铭 at right
role1 "先记录下来。我们还不能确定是谁动过这个箱子。"
menu:
    "检查纸箱里的旧文件":
        jump c11

    "检查储物间其他位置":
        jump c12
