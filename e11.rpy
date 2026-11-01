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

label e11:
play music "audio/推理2.mp3"
scene 角落2
show 陈铭 at right
with dissolve
role1 "这是刚才在程烈房间里发现的纸屑，和地下储藏室的那片放在一起看看。"
scene 走廊早
hide 陈铭
show 顾承骁 at right
with dissolve
role5 "边缘形状……确实有些相似。"
hide 顾承骁
show 许知微 at right
role3 "能拼起来吗？"
hide 许知微
show 陈铭 at right
role1 "先别急。把两片纸的撕裂边缘对齐。"
hide 陈铭
show 顾承骁 at right
role5 "这里有一处缺口，形状能够吻合。"
hide 顾承骁
show 许知微 at right
role3 "所以它们来自同一张纸？"
hide 许知微
show 陈铭 at right
role1 "至少这两片纸原本是连在一起的。"
hide 陈铭
show 顾承骁 at right
role5 "一片出现在地下储藏室，另一片出现在程烈的房间。看来程烈确实接触过这张纸。"
hide 顾承骁
show 陈铭 at right
role1 "但还不能证明是程烈把它带进储藏室的，也不能确定是谁撕碎了它。"
hide 陈铭
show 许知微 at right
role3 "纸上还能看出什么吗？"
hide 许知微
show 陈铭 at right
role1 "目前只有残缺的印刷痕迹，内容不足以辨认。"
hide 陈铭
show 顾承骁 at right
role5 "这至少说明，程烈失踪前可能正在调查某件与地下室有关的事。"
hide 顾承骁
show 陈铭 at right
role1 "或者有人希望我们这样认为。"
hide 陈铭
show 许知微 at right
role3 "你的意思是，这些纸屑也可能是故意留下的？"
hide 许知微
show 陈铭 at right
role1 "不能排除。我们现在最需要的是找到程烈本人。"
hide 陈铭
show 顾承骁 at right
role5 "如果他还在宅邸里，应该不会一直没有动静。"
hide 顾承骁
show 陈铭 at right
role1 "我们再检查一遍地下储藏室，确认有没有其他遗漏。"
menu:
    "继续调查":
        jump e12
