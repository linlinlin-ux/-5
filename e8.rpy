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

label e8:
play music "audio/恐怖.mp3"
scene 大厅早
show 陈铭 at right
with dissolve
role1 "你那边有什么发现？"
hide 陈铭
show 顾承骁 at right
role5 "找到一本旧登记册，里面有几页被撕掉了。封底还夹着一张写有十年前日期的纸片。"
hide 顾承骁
show 许知微 at right
role3 "十年前？又是这个时间。"
hide 许知微
show 陈铭 at right
role1 "我们在地下储藏室附近找到了一小片纸，也发现有人进出过的痕迹。"
hide 陈铭
show 顾承骁 at right
role5 "两边的发现暂时没有直接联系。"
hide 顾承骁
show 许知微 at right
role3 "但至少能确定，这座宅邸里还有人隐瞒着某些事情。"
hide 许知微
show 陈铭 at right
role1 "先把纸片和登记册的日期记下来。至于那片碎纸，等找到对应文件再判断。"
hide 陈铭
show 顾承骁 at right
role5 "程烈呢？有他的消息吗？"
hide 顾承骁
show 陈铭 at right
role1 "没有。他依旧下落不明。"
hide 陈铭
show 许知微 at right
role3 "如果他真的发现了什么，才突然消失……"
hide 许知微
show 陈铭 at right
role1 "现在还不能确定。我们需要找到更多证据。"
hide 陈铭
show 顾承骁 at right
role5 "那接下来就检查这些纸片和旧登记册，看看能不能找到它们之间的联系。"
menu:
    "继续调查":
        jump e9
