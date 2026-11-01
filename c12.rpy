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

label c12:
play music "audio/宁静.mp3"
scene 储物间
with dissolve
narrator_adv "陈铭重新检查储物间，注意到靠墙的几只纸箱上都积着一层薄灰。"
show 陈铭 at right
role1 "这些箱子应该很久没有被移动过了。"
hide 陈铭
narrator_adv "唯独刚才发现的纸箱，底部有一道不太明显的拖动痕迹。"
show 许知微 at right
role3 "真的有人动过它。"
hide 许知微
show 陆闻川 at right
role2 "可是我们不知道是谁，也不知道他拿走了什么。"
hide 陆闻川
show 陈铭 at right
role1 "没错。现在还不能确定箱子里的东西是否缺失。"
hide 陈铭
show 程烈 at right
role4 "这地方越来越不对劲了。"
hide 程烈
show 顾承骁 at right
role5 "也可能只是林伯以前整理东西时留下的痕迹。"
hide 顾承骁
show 陈铭 at right
role1 "有这种可能。先把发现记录下来。"
hide 陈铭
narrator_adv "陈铭关上储物间的门，带着照片和文件回到了大厅。"
menu:
    "返回大厅":
        jump c13
