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

label d7:
play music "audio/恐怖.mp3"
scene 走廊早
with dissolve
narrator_adv "陈铭结束了房间调查，将发现的物品和记录重新整理了一遍。"
show 陈铭 at right
role1 "目前发现了几项值得注意的东西。"
hide 陈铭
show 陈铭 at right
role1 "第一，陆闻川手里握着一枚陌生戒指，口袋里还有一张折叠纸条。"
hide 陈铭
show 陈铭 at right
role1 "第二，书桌上的文件涉及多笔资金往来，其中几笔金额被反复标记。"
hide 陈铭
show 陈铭 at right
role1 "第三，公文包内侧有一个空文件袋，里面似乎原本放着其他资料。"
hide 陈铭
show 许知微 at right
role3 "这些东西是不是说明他最近遇到了什么麻烦？"
hide 许知微
show 陈铭 at right
role1 "有这个可能。尤其是那些资金记录，值得进一步调查。"
hide 陈铭
show 程烈 at right
role4 "他平时就很在意钱，这有什么奇怪的？"
hide 程烈
show 顾承骁 at right
role5 "现在人已经死了，查他的账目能查出凶手吗？"
hide 顾承骁
show 陈铭 at right
role1 "至少能帮我们弄清楚，他死前是否有人在寻找某样东西。"
hide 陈铭
narrator_adv "陈铭拿出那张纸条，重新看了一遍上面的内容。"
show 陈铭 at right
role1 "这张纸条上的金额，和文件里被圈出的其中一笔金额相同。"
hide 陈铭
show 许知微 at right
role3 "所以这张纸条可能和那些交易有关？"
hide 许知微
show 陈铭 at right
role1 "目前只能说存在联系，还不能确定具体用途。"
hide 陈铭
show 程烈 at right
role4 "那枚戒指呢？总不能也是交易记录吧。"
hide 程烈
show 陈铭 at right
role1 "戒指的来历还不清楚，需要问问其他人是否见过。"
hide 陈铭
narrator_adv "陈铭将戒指、纸条和文件分别收好。"
show 陈铭 at right
role1 "我们还需要确认，昨晚到今天早晨，有谁见过陆闻川，或者进入过他的房间。"
hide 陈铭
show 许知微 at right
role3 "你怀疑有人来这里拿走了文件？"
hide 许知微
show 陈铭 at right
role1 "公文包里确实有东西不见了，但还不能确定是谁拿走的，也不能确定它是否与死亡有关。"
hide 陈铭
narrator_adv "众人暂时没有提出新的线索。陈铭决定先核对陆闻川死亡前后的行动。"
menu:
    "核对众人昨晚的行动":
        jump d8
