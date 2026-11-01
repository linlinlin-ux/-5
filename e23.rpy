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

label e23:
play music "audio/推理2.mp3"
scene 大厅
with dissolve
narrator_adv "大厅的桌面上摆着三份资料：林伯的工作记录本、船只安排表，以及缺失了一页的船只往来登记册。陈铭将它们按照日期依次排开。"
show 陈铭 at right
role1 "先从林伯的工作记录开始。这里记载着他原本要乘船离岛的日期。"
hide 陈铭
show 许知微 at right
role3 "船只安排表上也有同一天的记录。"
hide 许知微
show 顾承骁 at right
role5 "而且写着由林伯负责确认船方安排。"
hide 顾承骁
show 陈铭 at right
role1 "但是工作记录里没有明确写出他是否已经完成通知。"
hide 陈铭
show 许知微 at right
role3 "所以我们不知道船方到底有没有收到消息。"
hide 许知微
show 陈铭 at right
role1 "没错。再看这本登记册，原本应该记录实际往来的船只和乘船人员。"
hide 陈铭
show 顾承骁 at right
role5 "偏偏关键日期附近的那一页被撕掉了。"
hide 顾承骁
show 许知微 at right
role3 "这也太巧了。"
hide 许知微
show 陈铭 at right
role1 "目前只能确定，林伯负责过接送安排，而实际往来记录恰好缺失。"
hide 陈铭
show 顾承骁 at right
role5 "如果那艘船真的来过，应该会留下记录。"
hide 顾承骁
show 陈铭 at right
role1 "如果没有记录，也不能直接证明船没有来。我们还需要其他证据。"
hide 陈铭
narrator_adv "陈铭将登记册翻回最后一页，发现封底内侧夹着一张薄薄的纸片。"
show 许知微 at right
role3 "这里还有东西！"
hide 许知微
show 陈铭 at right
role1 "是一张船方联络信息的存根，上面有一个联系电话和一串日期。"
hide 陈铭
show 顾承骁 at right
role5 "联系电话还能用吗？"
hide 顾承骁
show 陈铭 at right
role1 "现在还不知道。先把信息抄下来，之后再想办法核实。"
menu:
    "继续调查":
        jump e24
