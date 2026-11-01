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

label d5:
play music "audio/杀人之夜.mp3"
scene 命案现场2
with dissolve
narrator_adv "陈铭重新翻看桌上的文件，试图找出这些资金往来的具体用途。"
show 陈铭 at right
role1 "这些记录的时间跨度不短，似乎不是临时发生的交易。"
hide 陈铭
show 许知微 at right
role3 "他一直在做这种事情吗？"
hide 许知微
show 陈铭 at right
role1 "还不能确定。文件没有完整的说明。"
hide 陈铭
narrator_adv "陈铭发现几笔金额相近的款项被单独标记出来，旁边写着不同的日期。"
show 程烈 at right
role4 "他到底在忙什么？"
hide 程烈
show 陈铭 at right
role1 "可能涉及某项长期交易，也可能只是私人投资。"
hide 陈铭
narrator_adv "文件中没有出现其他人的完整姓名，只有几个被缩写的代号。"
show 陈铭 at right
role1 "这些内容暂时无法确认身份，先保存起来。"
menu:
    "检查公文包和缺失物品":
        jump d6
