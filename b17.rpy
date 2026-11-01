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

label b17:
play music "audio/杀人之夜.mp3"
scene 大厅
with dissolve
narrator_adv "一整天过去，众人仍然没有找到足以解释死亡原因的证据。"
show 陆闻川 at right
role2 "我受够了。我们到底还要在这里待多久？"
hide 陆闻川
show 林伯 at right
role6 "请各位再耐心等一等。船只预计明天才能抵达。"
hide 林伯
show 程烈 at right
role4 "你昨天也是这么说的。"
hide 程烈
show 林伯 at right
role6 "这是原定的安排，我没有理由欺骗各位。"
hide 林伯
show 许知微 at right
role3 "可是……如果这里真的还有凶手，我们继续待下去不是很危险吗？"
hide 许知微
show 顾承骁 at right
role5 "危险？我看你们是自己吓自己。"
hide 顾承骁
show 陈铭 at right
role1 "现在争论没有意义。我们没有信号，也无法自行离岛，只能尽量保证所有人都待在一起。"
hide 陈铭
show 陆闻川 at right
role2 "你说得倒轻松。万一今晚再死人呢？"
hide 陆闻川
show 陈铭 at right
role1 "那就更不应该单独行动。今晚尽量不要离开公共区域，有事先通知其他人。"
menu:
    "查看大厅":
        jump b18

    "查看走廊":
        jump b19

    "直接进入第三天早晨（第三章）":
        jump b20
