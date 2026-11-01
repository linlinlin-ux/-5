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

label e37:
scene 尸体
with dissolve
narrator_adv "许知微戴上手套，检查盖在程烈身上的旧布料。布料表面沾着灰尘，边缘有几处新鲜的折痕。"
show 许知微 at right
role3 "这些布料原本应该堆在旁边，不像是专门用来盖住尸体的。"
hide 许知微
show 陈铭 at right
role1 "也就是说，有人可能临时拿它们遮住了尸体。"
hide 陈铭
narrator_adv "许知微翻看布料内侧，发现其中一块布料上沾有少量暗色污渍。"
show 许知微 at right
role3 "这里有污渍。"
hide 许知微
show 陈铭 at right
role1 "先不要判断是什么，记录位置和形状。"
hide 陈铭
narrator_adv "布料底部还压着一小片纸屑，纸面已经受潮，无法辨认完整内容。"
show 许知微 at right
role3 "这会不会是档案盒里的纸？"
hide 许知微
show 陈铭 at right
role1 "需要拿回去和那些资料比对，暂时不能确定。"
menu:
    "汇总线索":
        jump e39
