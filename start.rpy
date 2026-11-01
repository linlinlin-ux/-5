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

label start:
play music "audio/宁静.mp3"
scene 信
narrator_adv "我掌握着十年前那件事的完整证据。"
narrator_adv "如果你不想让它出现在所有人面前，就来岛上。"
narrator_adv "你有机会解释自己当年做过的事。"
scene 信
narrator_adv "信封里没有寄信人的姓名，只有一张船票和一串坐标。"
narrator_adv "你认得那座岛。它远离航线，岛上只有一栋常年无人居住的豪宅。"
narrator_adv "十年前，周砚离开学校之后，就再也没有人见过他。"
narrator_adv "……你到底想让我去见谁？"
scene 沙滩
narrator_adv "你把信纸折好，放进外套口袋。"
narrator_adv "第二天早上，你登上了前往孤岛的船。"
narrator_adv "海面阴沉，雾气逐渐吞没岸线。船靠岸时，天色已经暗了下来。"
scene 沙滩2
narrator_adv "岸边没有接应的人，只有一条通往山坡的石板路。"
scene 石路
narrator_adv "你沿着石板路走向豪宅。远远地，你看见二楼有灯光。"
scene 豪宅
show 陈铭 at right
role1 "你准备进入豪宅。"
menu:
    "直接进入豪宅":
        jump Sheet2

    "先检查门口的信箱":
        jump Sheet3

    "观察豪宅周围的环境":
        jump a4
