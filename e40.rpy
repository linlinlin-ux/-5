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

label e40:
play music "audio/推理2.mp3"
scene 大厅
with dissolve
narrator_adv "回到大厅后，陈铭将从程烈房间、地下储藏室以及程烈尸体现场发现的纸屑放在一起。"
show 陈铭 at right
role1 "这些纸片的纸质和边缘都有相似之处。"
hide 陈铭
show 许知微 at right
role3 "能拼起来吗？"
hide 许知微
narrator_adv "陈铭将几片纸屑调整位置，逐渐拼出一段残缺的文字。"
show 陈铭 at right
role1 "……学生事件记录……证人名单……"
hide 陈铭
show 顾承骁 at right
role5 "这是档案盒里的资料？"
hide 顾承骁
show 陈铭 at right
role1 "很可能。程烈应该接触过这份文件，而且试图带走其中的一部分。"
hide 陈铭
show 许知微 at right
role3 "所以他才会被杀？"
hide 许知微
show 陈铭 at right
role1 "还不能确定。但有人拿走了他的随身物品，又遮住尸体，说明至少有人不希望我们发现这里。"
hide 陈铭
show 顾承骁 at right
role5 "那个人可能已经看过档案了。"
hide 顾承骁
show 陈铭 at right
role1 "或者，他一直知道档案里有什么。"
hide 陈铭
narrator_adv "陈铭将拼好的纸片放在桌上。残缺文字的末尾，还能辨认出一个词语——「旁观者」。"
show 许知微 at right
role3 "旁观者……"
hide 许知微
narrator_adv "陈铭的目光停在那几个字上，脑海中闪过一段模糊的记忆。他很快移开视线，没有解释。"
show 陈铭 at right
role1 "今天先到这里。把档案和现场线索保存好，明天再统一整理。"
menu:
    "第五天夜间":
        jump e41
