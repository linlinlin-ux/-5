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

label f4:
play music "audio/推理2.mp3"
scene 工作间
with dissolve
narrator_adv "陈铭将当天的校园记录和医院通知放在一起，终于拼出了那天发生的事情。"
show 陈铭 at right
role1 "周砚得知母亲病危，想马上赶去医院。"
hide 陈铭
narrator_adv "可顾承骁、陆闻川、许知微和程烈当时围住了他。"
show 陈铭 at right
role1 "他们没有让他离开。"
hide 陈铭
narrator_adv "记录中的描述并不一致，有人说那只是几句争吵，有人说周砚曾经试图挣脱，还有人声称自己根本不知道他家里出了事。"
show 陈铭 at right
role1 "他们可能不知道他母亲正在抢救，但他们知道他一直在求他们放他走。"
hide 陈铭
narrator_adv "陈铭看着医院通知上的日期。那一天，周砚最终没能及时赶到医院。"
show 陈铭 at right
role1 "即使只剩下一丝希望，他也想赶回去见自己的母亲。"
hide 陈铭
narrator_adv "没有人能够证明，如果周砚早到一些，结果就一定会不同。但对周砚而言，那段被耽误的时间，已经成为无法挽回的遗憾。"
show 陈铭 at right
role1 "原来他一直记得的，不只是那些欺凌。"
hide 陈铭
narrator_adv "陈铭的视线落在四个人的名字上。"
show 陈铭 at right
role1 "他们毁掉的，是他最后一次见母亲的机会。"
menu:
    "继续调查":
        jump f5
