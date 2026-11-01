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

label c11:
play music "audio/宁静.mp3"
scene 储物间
with dissolve
narrator_adv "陈铭戴上手套，小心地翻看纸箱里的文件。"
show 陈铭 at right
role1 "大部分是一些旧账单和生活记录。"
hide 陈铭
narrator_adv "几张纸上记录着多年前的房屋租赁信息，其中一份文件的日期已经十分模糊。"
show 许知微 at right
role3 "这里怎么会有这么多旧账单？"
hide 许知微
show 陈铭 at right
role1 "可能是以前留下的资料。"
hide 陈铭
narrator_adv "陈铭继续翻找，发现其中夹着一张边缘破损的旧照片。"
show 陆闻川 at right
role2 "这是什么？"
hide 陆闻川
narrator_adv "照片上是几名学生的合影，背面没有写明具体日期。"
show 陈铭 at right
role1 "这张照片先单独收好。"
hide 陈铭
show 顾承骁 at right
role5 "几张旧照片而已，有必要这么认真吗？"
hide 顾承骁
show 陈铭 at right
role1 "既然是在异常打开的纸箱里发现的，就有必要确认它的来历。"
hide 陈铭
narrator_adv "陈铭将照片收好，决定之后再仔细查看。"
menu:
    "返回储物间":
        jump c12
