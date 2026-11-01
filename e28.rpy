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

label e28:
scene 盒子
with dissolve
narrator_adv "陈铭将档案盒放在木箱上，小心地打开盒盖。里面的文件排列得并不整齐，有些纸张边缘已经发黄，还有几处明显的空缺。"
show 许知微 at right
role3 "怎么感觉里面的东西少了很多？"
hide 许知微
show 陈铭 at right
role1 "这些文件原本应该是按顺序整理的，但现在有几处明显缺失。"
hide 陈铭
show 顾承骁 at right
role5 "先看看留下来的资料吧。"
hide 顾承骁
narrator_adv "最上面是一份旧学校的资料登记表，纸张上印着十年前的日期。下面还夹着几张学生资料复印件。"
show 陈铭 at right
role1 "这是学校当年的资料。"
hide 陈铭
show 许知微 at right
role3 "这些名字……好像有些熟悉。"
scene 储物间4
hide 许知微
with dissolve
narrator_adv "陈铭翻过几页，发现其中一份资料提到了当年的校园事件，但关键内容被撕去了一部分。"
scene 旧图
show 陈铭 at right
with dissolve
role1 "这里记录的事情，应该和我们之前找到的旧照片有关。"
scene 储物间4
hide 陈铭
show 顾承骁 at right
with dissolve
role5 "也就是说，之前那些东西并不是随便放在宅邸里的。"
hide 顾承骁
show 陈铭 at right
role1 "先把留下来的资料整理出来。缺失的部分，或许才是最重要的。"
menu:
    "整理线索":
        jump e29
