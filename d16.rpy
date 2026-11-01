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

label d16:
play music "audio/推理.mp3"
scene 大厅
with dissolve
narrator_adv "陈铭重新拿出陆闻川留下的物品，将戒指、纸条和资金文件摆在一起。"
show 陈铭 at right
role1 "戒指的来历还没有查清，资金文件也缺少关键部分。"
hide 陈铭
narrator_adv "他将纸条上的金额与文件中的记录再次对照，确认两者确实对应同一笔交易。"
show 陈铭 at right
role1 "陆闻川生前似乎一直在处理这笔资金。"
hide 陈铭
narrator_adv "陈铭又想起公文包里那个被撕开的空文件袋。"
show 陈铭 at right
role1 "有人可能拿走了原本存放在里面的资料。"
hide 陈铭
narrator_adv "他把孔雀羽毛也放到桌面上。羽毛上的特殊纹路与其他物品毫无关联，暂时无法得出结论。"
show 陈铭 at right
role1 "这些线索还不够。必须找到缺失的资料，或者确认戒指的来源。"
hide 陈铭
narrator_adv "陈铭将物品重新收好，决定暂时不公开尚未确认的推测。"
menu:
    "暂停调查":
        jump d19

    "与许知微单独交谈":
        jump d17

    "与程烈单独交谈":
        jump d18
