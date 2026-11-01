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

label e7:
play music "audio/恐怖.mp3"
scene 尽头
show 顾承骁 at right
with dissolve
role5 "这间房间平时似乎很少有人使用。"
hide 顾承骁
role5 "门没有上锁。里面的家具也没有明显被移动过的痕迹。"
scene 登记
with dissolve
role5 "书桌上有一本旧登记册。"
role5 "里面记录着一些宅邸物品的存放位置和领用情况。"
role5 "最近几页有被撕掉的痕迹，但剩下的内容看不出具体缺失了什么。"
role5 "……这是什么？"
role5 "登记册的封底夹着一张旧纸片，上面写着一个日期。"
scene 尽头
with dissolve
role5 "日期是十年前的。"
role5 "这件事或许和我们之前发现的旧照片有关。"
role5 "先把纸片收起来，回去再和陈铭他们商量。"
menu:
    "会合":
        jump e8
