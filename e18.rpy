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

label e18:
play music "audio/推理2.mp3"
scene 工作间
with dissolve
narrator_adv "一楼走廊尽头有一扇不起眼的木门。推开门后，里面是一间狭小的工作间，墙边放着清洁工具和备用物品，桌面上堆着几本旧文件夹。"
show 许知微 at right
role3 "这里应该是林伯平时整理杂务的地方。"
hide 许知微
show 陈铭 at right
role1 "先看看桌上的文件。"
hide 陈铭
narrator_adv "陈铭翻开最上面的文件夹，里面记录着日常采购、房屋维修以及物品领用情况。"
show 许知微 at right
role3 "这些都是普通的工作记录。"
hide 许知微
show 陈铭 at right
role1 "再往后看看。"
hide 陈铭
narrator_adv "文件夹底部夹着一张折叠过的纸，上面写着几个日期和船只名称。"
scene 表
show 许知微 at right
with dissolve
role3 "这是……船只安排表吗？"
scene 工作间
hide 许知微
show 陈铭 at right
with dissolve
role1 "看起来像。上面还有接送时间。"
hide 陈铭
show 许知微 at right
role3 "等等，这个日期就是原本说好来接我们的那一天。"
hide 许知微
show 陈铭 at right
role1 "但旁边的备注似乎被修改过。"
hide 陈铭
show 许知微 at right
role3 "原本写的是什么？"
hide 许知微
show 陈铭 at right
role1 "字迹重叠在一起，暂时看不清楚。先不要破坏纸张，带回去仔细查看。"
hide 陈铭
narrator_adv "陈铭将纸张收好。原本以为只是普通的工作记录，没想到其中竟然记载着他们离岛的安排。"
menu:
    "回到大厅":
        jump e19
