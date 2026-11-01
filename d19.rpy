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

label d19:
play music "audio/宁静.mp3"
scene 大厅
with dissolve
narrator_adv "夜色渐深，豪宅大厅里的灯光显得格外昏暗。"
scene 卧室
with dissolve
narrator_adv "陈铭将今天收集到的证据整理好，暂时放回自己的房间。"
scene 大厅
show 许知微 at right
with dissolve
role3 "今天又发生了这么多事情，我真的不敢睡觉了。"
hide 许知微
show 陈铭 at right
role1 "一直不休息也不是办法。我们需要保持体力。"
hide 陈铭
show 程烈 at right
role4 "我倒觉得，与其在这里浪费时间，不如想办法离开这座岛。"
hide 程烈
show 顾承骁 at right
role5 "现在外面天已经黑了，你打算怎么离开？"
hide 顾承骁
show 程烈 at right
role4 "至少不能一直坐以待毙。"
hide 程烈
show 许知微 at right
role3 "可是我们根本不知道外面是什么情况。"
hide 许知微
show 陈铭 at right
role1 "今晚先各自回房间。明天再想办法确认船只的情况。"
hide 陈铭
show 程烈 at right
role4 "随便你们。我可不想一直待在这里。"
hide 程烈
narrator_adv "程烈率先离开大厅，其他人也陆续回到自己的房间。"
scene 卧室
with dissolve
narrator_adv "陈铭回到房间后，再次检查了一遍随身携带的证物。"
narrator_adv "戒指、纸条、资金文件，以及那根后来发现的孔雀羽毛，都被他分别收好。"
show 陈铭 at right
role1 "还有太多事情没有弄清楚了……"
hide 陈铭
narrator_adv "陈铭关掉灯，躺在床上。窗外的海浪声持续不断。"
scene 走廊
with dissolve
narrator_adv "这一夜，豪宅里再次陷入寂静。"
menu:
    "进入第五章":
        jump e1
