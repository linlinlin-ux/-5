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

label b5:
play music "audio/杀人之夜.mp3"
scene 命案现场
with dissolve
narrator_adv "陈铭重新来到尸体旁，仔细观察死者的衣着。"
show 陈铭 at right
role1 "衣服整体比较整齐，没有明显被大力撕扯的痕迹。"
hide 陈铭
show 陆闻川 at right
role2 "这是不是说明他死前没有反抗？"
hide 陆闻川
show 陈铭 at right
role1 "不能这样判断。衣服没有明显破损，不代表死者没有反抗，也可能是其他原因。"
hide 陈铭
narrator_adv "陈铭检查了衣领、袖口和衣服前襟，注意到袖口有些轻微的褶皱。"
show 陈铭 at right
role1 "袖口有褶皱，但这也可能是日常穿着造成的，不能直接当作搏斗痕迹。"
hide 陈铭
show 许知微 at right
role3 "那衣服上有没有血迹？"
hide 许知微
show 陈铭 at right
role1 "目前没有看到明显的大面积血迹。至于是否存在其他痕迹，还需要进一步检查。"
hide 陈铭
narrator_adv "陈铭继续查看衣服口袋，没有擅自翻动或取走其中的物品。"
show 陈铭 at right
role1 "单从衣着来看，还无法确定死因，也不能判断凶手是否与死者发生过肢体冲突。"
hide 陈铭
show 顾承骁 at right
role5 "那就把这些情况记下来，等其他线索出现后再一起判断。"
hide 顾承骁
show 陈铭 at right
role1 "好。调查必须建立在证据上，不能因为着急就把普通细节当成结论。"
menu:
    "检查尸体右手旧伤":
        jump b10

    "返回检查尸体":
        jump b2

    "询问陆闻川的旧事":
        jump b8
