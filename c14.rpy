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

label c14:
play music "audio/恐怖.mp3"
scene 大厅
with dissolve
narrator_adv "傍晚，窗外的天色逐渐暗了下来。经过一整天的调查和争吵，众人都显得疲惫不堪。"
show 陆闻川 at right
role2 "今天先到这里吧，我实在没力气继续查了。"
hide 陆闻川
show 许知微 at right
role3 "可是现在还有人在暗处，我们真的能安心休息吗？"
hide 许知微
show 程烈 at right
role4 "那你想怎么样？总不能一直守在大厅里。"
hide 程烈
show 顾承骁 at right
role5 "至少今晚不要单独行动。"
hide 顾承骁
show 陈铭 at right
role1 "我同意。发生任何异常，都先通知其他人，不要擅自处理。"
hide 陈铭
show 陆闻川 at right
role2 "说得容易。现在连林伯都死了，谁知道下一个会是谁？"
hide 陆闻川
show 许知微 at right
role3 "你别说了……"
hide 许知微
narrator_adv "陆闻川没有继续说下去。众人各自回到房间，约定暂时不要离开自己的楼层。"
scene 卧室
with dissolve
narrator_adv "陈铭回到房间，将白天找到的旧照片放在桌上。"
narrator_adv "他重新看了一遍照片背面的日期，随后将照片收好。"
show 陈铭 at right
role1 "十年前的照片……到底是谁留下的？"
hide 陈铭
narrator_adv "陈铭关掉台灯，房间逐渐陷入黑暗。"
narrator_adv "不知过了多久，走廊深处忽然传来一声轻微的响动。"
show 陈铭 at right
role1 "……什么声音？"
hide 陈铭
narrator_adv "陈铭坐起身，仔细听了一会儿。走廊里很快又恢复了安静。"
narrator_adv "他犹豫片刻，最终还是打开房门，走了出去。"
menu:
    "前往走廊查看":
        jump c15
