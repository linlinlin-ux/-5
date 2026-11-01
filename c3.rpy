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

label c3:
play music "audio/推理.mp3"
scene 地下室
with dissolve
narrator_adv "陈铭在林伯身旁蹲下，仔细观察他的身体状况。"
show 陈铭 at right
role1 "先看看身上有没有明显的外伤。"
hide 陈铭
narrator_adv "林伯穿着平时常穿的深色外套，衣服大体完整，没有明显的撕裂痕迹。"
show 许知微 at right
role3 "看起来不像是和别人发生过激烈冲突。"
hide 许知微
show 陈铭 at right
role1 "不能只凭衣服判断。继续检查。"
hide 陈铭
narrator_adv "陈铭轻轻拨开林伯后脑附近的头发，发现那里有一处明显的肿胀。"
show 陈铭 at right
role1 "后脑有撞击伤，可能是在坠落过程中造成的。"
hide 陈铭
show 陆闻川 at right
role2 "所以他真的是从楼梯上摔下来的？"
hide 陆闻川
show 陈铭 at right
role1 "也可能是先受到撞击，再倒在楼梯底部。现在还不能确定。"
hide 陈铭
narrator_adv "陈铭注意到林伯右手掌心有几道浅浅的擦伤，指缝里沾着少量灰尘。"
show 程烈 at right
role4 "手上也有伤？"
hide 程烈
show 陈铭 at right
role1 "可能是摔倒时撑地造成的，也可能有其他原因。"
hide 陈铭
narrator_adv "陈铭又检查了林伯的口袋，里面只有一串钥匙和一块旧手帕，没有发现其他特别的物品。"
show 顾承骁 at right
role5 "看来没什么有用的东西。"
hide 顾承骁
show 陈铭 at right
role1 "至少目前没有发现能够直接说明死因的物品。"
hide 陈铭
narrator_adv "陈铭站起身，将尸体的情况简单记录下来。"
show 陈铭 at right
role1 "后脑存在撞击伤，手掌有擦伤，但这些伤势还不足以证明他是意外坠落。"
hide 陈铭
show 陆闻川 at right
role2 "那我们接下来查什么？"
hide 陆闻川
show 陈铭 at right
role1 "先确认林伯昨天最后一次出现的时间。"
menu:
    "确认林伯最后出现的时间":
        jump c4

    "返回检查楼梯现场":
        jump c2
