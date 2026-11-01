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

label e41:
play music "audio/宁静.mp3"
scene 大厅
with dissolve
narrator_adv "夜色笼罩宅邸。程烈的尸体已经被重新妥善遮盖，地下通道暂时封闭。大厅里只剩下几个人，谁也没有主动开口。"
show 许知微 at right
role3 "我们已经死了这么多人……真的还能活着离开这里吗？"
hide 许知微
show 陈铭 at right
role1 "会有办法的。"
hide 陈铭
show 顾承骁 at right
role5 "你还是和以前一样，总能说出这种话。"
hide 顾承骁
show 陈铭 at right
role1 "……什么意思？"
hide 陈铭
show 顾承骁 at right
role5 "没什么。我只是觉得，你似乎一直很擅长让别人冷静下来。"
hide 顾承骁
narrator_adv "顾承骁没有继续说下去。他的目光在陈铭身上停留片刻，随后转身离开。"
narrator_adv "陈铭独自留在大厅。他想起档案中那句「旁观者」，却始终无法将它与自己的记忆联系起来。"
show 陈铭 at right
role1 "……十年前，到底发生了什么？"
hide 陈铭
narrator_adv "远处传来一声轻微的关门声。第五天结束了。"
menu:
    "进入第六章":
        jump f1
