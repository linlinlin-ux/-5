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

label d4:
play music "audio/恐怖.mp3"
scene 命案现场2
with dissolve
narrator_adv "陈铭站起身，开始检查房间内的其他物品。房间整体并不算凌乱，但床边的椅子倒在地上，桌上的文件散落了一部分。"
show 陈铭 at right
role1 "看起来这里发生过一些动静。"
hide 陈铭
show 许知微 at right
role3 "他是不是和什么人发生了争执？"
hide 许知微
show 陈铭 at right
role1 "现在还不能确定。先看看周围有没有其他线索。"
hide 陈铭
narrator_adv "陈铭走到书桌前，发现桌面上放着一只打开的皮质公文包。"
show 程烈 at right
role4 "这是陆闻川的东西？"
hide 程烈
show 陈铭 at right
role1 "应该是。他平时似乎很在意自己的随身物品。"
hide 陈铭
narrator_adv "公文包里放着几份文件，其中几页涉及金额较大的资金往来，部分内容被人用笔划掉。"
show 许知微 at right
role3 "这些是什么？"
hide 许知微
show 陈铭 at right
role1 "看起来像是交易记录，但还需要进一步确认。"
hide 陈铭
show 陆闻川 at right
role2 "旁白"
hide 陆闻川
narrator_adv "陈铭没有回答。他注意到公文包内侧有一道新鲜的撕裂痕迹，像是曾经有东西被匆忙取走。"
show 陈铭 at right
role1 "这里可能少了什么东西。"
hide 陈铭
show 顾承骁 at right
role5 "也许只是他自己整理时弄坏的。"
hide 顾承骁
show 陈铭 at right
role1 "有可能，但最好先记录下来。"
hide 陈铭
narrator_adv "陈铭转向书桌另一侧，发现桌角压着一张被揉皱的纸。"
show 陈铭 at right
role1 "这张纸和尸体口袋里的纸条，或许能对照一下。"
hide 陈铭
narrator_adv "他将纸张展开，上面只留下几行不完整的文字和一个被反复圈出的金额。"
show 许知微 at right
role3 "他最近是不是遇到了什么麻烦？"
hide 许知微
show 陈铭 at right
role1 "这些文件可能与他的私人事务有关，但目前还不能确定是否和死亡有关。"
hide 陈铭
narrator_adv "陈铭将现场物品逐一记录，没有再发现明显的异常。"
menu:
    "查看桌上的资金文件":
        jump d5

    "检查公文包和缺失物品":
        jump d6
