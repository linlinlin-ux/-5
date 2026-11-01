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

label b24:
play music "audio/杀人之夜.mp3"
scene 走廊早
show 陈铭 at right
with dissolve
role1 "顾承骁，我还有几个问题想问你。"
hide 陈铭
show 顾承骁 at right
role5 "你怎么总有问题？问吧。"
hide 顾承骁
show 陈铭 at right
role1 "十年前，周末补课因为举报而取消。你还记得这件事吗？"
hide 陈铭
show 顾承骁 at right
role5 "当然记得。那时候大家都觉得周砚多管闲事，事情闹得很难看。"
hide 顾承骁
show 陈铭 at right
role1 "你也这么认为？"
hide 陈铭
show 顾承骁 at right
role5 "补课停了，钱退了，大家本来可以各过各的。他偏偏成了所有人的眼中钉。"
hide 顾承骁
show 陈铭 at right
role1 "可是，举报本身并没有错。"
hide 陈铭
show 顾承骁 at right
role5 "你现在是在跟我讲道理？十年前可没人这么想。"
hide 顾承骁
show 陈铭 at right
role1 "后来，他在班里受到排挤。你在其中扮演了什么角色？"
hide 陈铭
show 顾承骁 at right
role5 "你想说什么？直接说。"
hide 顾承骁
show 陈铭 at right
role1 "你是否参与过针对他的事情？"
hide 陈铭
show 顾承骁 at right
role5 "我没必要把十年前每一件小事都记下来。"
hide 顾承骁
show 陈铭 at right
role1 "那晚晚自习结束后呢？你还记得吗？"
hide 陈铭
show 顾承骁 at right
role5 "哪一晚？"
hide 顾承骁
show 陈铭 at right
role1 "有人告诉周砚班主任找他，把他的书包扔进教室，又关掉走廊的灯，把门锁上。"
hide 陈铭
show 顾承骁 at right
role5 "……你连这种事情都记得？"
hide 顾承骁
show 陈铭 at right
role1 "我当时也在学校。"
hide 陈铭
show 顾承骁 at right
role5 "那又怎么样？你不是也没做什么吗？"
hide 顾承骁
show 陈铭 at right
role1 "我是在问你。你有没有参与？"
hide 陈铭
show 顾承骁 at right
role5 "我不记得具体是谁做的了。就算当时有人闹着玩，也不至于被你说得这么严重吧？"
hide 顾承骁
show 陈铭 at right
role1 "他那天晚上赶着坐末班车回家。"
hide 陈铭
show 顾承骁 at right
role5 "我怎么知道他家里的情况？"
hide 顾承骁
show 陈铭 at right
role1 "你真的一点都不知道？"
hide 陈铭
show 顾承骁 at right
role5 "陈铭，你到底是来调查命案的，还是打算把十年前的事情重新审一遍？"
hide 顾承骁
show 陈铭 at right
role1 "我只是在确认，你们之间是否存在足以影响这起案件的矛盾。"
hide 陈铭
show 顾承骁 at right
role5 "那我告诉你，周砚和我们确实有过矛盾。但十年过去了，谁还会一直惦记这些事？"
hide 顾承骁
show 陈铭 at right
role1 "……好，我的问题问完了。"
hide 陈铭
narrator_adv "顾承骁的语气始终带着不耐烦。他没有承认自己参与过锁门事件，也没有明确否认。"
show 陈铭 at right
role1 "（他刻意避开了具体行为，却对那件事的严重程度表现得毫不在意。）"
hide 陈铭
narrator_adv "陈铭没有继续追问。他将这段谈话记了下来，准备与其他人的证词一起核对。"
menu:
    "询问陆闻川的旧事":
        jump b8

    "询问许知微的旧事":
        jump b9

    "询问程烈的旧事":
        jump b11

    "返回第一次集中讨论":
        jump b12
