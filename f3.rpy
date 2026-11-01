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

label f3:
play music "audio/推理2.mp3"
scene 盒子
with dissolve
narrator_adv "陈铭在档案盒底部找到一张旧联络记录。纸张已经泛黄，部分字迹因为保存不当而变得模糊。"
scene 工作间
show 陈铭 at right
with dissolve
role1 "这是……医院的联络记录？"
hide 陈铭
narrator_adv "记录显示，十年前的那一天，周砚的母亲因病情突然恶化，被送往医院抢救。"
show 陈铭 at right
role1 "抢救……"
hide 陈铭
narrator_adv "记录旁边还附有一张通知单，上面写着医院曾尝试联系周砚，希望家属尽快赶到。"
show 陈铭 at right
role1 "所以他那天一直想离开学校，是因为他的母亲正在医院抢救。"
hide 陈铭
narrator_adv "陈铭重新看向刚才那份校园事件记录。周砚一次又一次请求离开，而其他人却把这件事当成了普通的争执。"
show 陈铭 at right
role1 "他当时一定很着急。"
hide 陈铭
narrator_adv "通知单上没有记载周砚具体抵达医院的时间，也没有说明如果他早些赶到，结果是否会有所不同。"
show 陈铭 at right
role1 "可他连最后一点希望都没能抓住。"
hide 陈铭
narrator_adv "陈铭沉默下来。他忽然意识到，十年前那场冲突的后果，远比自己记忆中的严重。"
menu:
    "继续整理线索":
        jump f4
