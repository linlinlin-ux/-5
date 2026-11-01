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

label e30:
play music "audio/恐怖.mp3"
scene 文件
with dissolve
narrator_adv "陈铭将档案盒里的文件全部取出，发现底层还压着一只薄薄的牛皮纸袋。纸袋没有封口，里面却已经空了。"
show 许知微 at right
role3 "这里面原本装过东西？"
scene 储物间4
hide 许知微
show 陈铭 at right
with dissolve
role1 "里面有纸张压出的痕迹，应该不止一份。"
hide 陈铭
show 顾承骁 at right
role5 "会不会就是被抽走的那些资料？"
hide 顾承骁
show 陈铭 at right
role1 "有可能。但纸袋本身没有留下明确的标记。"
hide 陈铭
narrator_adv "陈铭翻过纸袋，在背面发现了一处浅浅的墨迹。墨迹只剩下半个字，以及一串被划掉的编号。"
show 许知微 at right
role3 "这个编号和之前在储藏室发现的一样吗？"
hide 许知微
show 陈铭 at right
role1 "格式相似，但还不能确定是同一组编号。"
hide 陈铭
show 顾承骁 at right
role5 "先把这些东西收起来吧。"
hide 顾承骁
narrator_adv "陈铭将档案盒重新整理好。就在这时，他注意到木箱旁边的地面上有一道细小的划痕。"
show 陈铭 at right
role1 "等一下。这里还有东西。"
hide 陈铭
narrator_adv "划痕从木箱旁延伸到储物间另一侧，尽头停在一堆旧家具后面。"
show 许知微 at right
role3 "难道有人把什么东西藏在那里了？"
hide 许知微
show 陈铭 at right
role1 "过去看看。"
menu:
    "继续探索":
        jump e31
