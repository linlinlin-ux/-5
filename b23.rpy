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

label b23:
play music "audio/杀人之夜.mp3"
scene 走廊早
show 陈铭 at right
with dissolve
role1 "我们目前有两件事需要分开看待：一是房间里的死亡事件，二是十年前周砚与我们之间发生的事情。"
hide 陈铭
show 陆闻川 at right
role2 "你觉得这两件事有关？"
hide 陆闻川
show 陈铭 at right
role1 "目前还不能确定。但周砚特意邀请我们来到这里，又在我们抵达后发生了命案，这至少值得注意。"
hide 陈铭
show 许知微 at right
role3 "你是说，这可能不是意外？"
hide 许知微
show 陈铭 at right
role1 "我是说，不能因为我们不知道原因，就直接把它当成意外。"
hide 陈铭
show 程烈 at right
role4 "那你说说，现在线索到底指向谁？"
hide 程烈
show 陈铭 at right
role1 "目前没有足够证据指向任何一个人。房间没有明显的强行进入痕迹，窗边的压痕也无法确认来源。"
hide 陈铭
show 陆闻川 at right
role2 "林伯也说不清昨晚在走廊里见到的人是谁。"
hide 陆闻川
show 陈铭 at right
role1 "是的。这是目前尚未得到解释的细节，但不能仅凭这一点认定林伯在撒谎。"
hide 陈铭
show 顾承骁 at right
role5 "你们是不是忘了最重要的一件事？周砚为什么要邀请我们？"
hide 顾承骁
show 许知微 at right
role3 "因为十年前的事情……"
hide 许知微
show 顾承骁 at right
role5 "那件事早就过去了。难道他把我们叫来，就是为了翻旧账？"
hide 顾承骁
show 陆闻川 at right
role2 "你这么紧张干什么？"
hide 陆闻川
show 顾承骁 at right
role5 "我没有紧张。我只是觉得你们一直揪着过去不放，根本解决不了眼前的问题。"
hide 顾承骁
show 陈铭 at right
role1 "也许。但如果邀请本身就是为了让我们面对过去，那么回避它同样无法解决问题。"
hide 陈铭
narrator_adv "顾承骁没有继续回答。大厅里短暂地安静下来。"
show 陈铭 at right
role1 "今天先到这里。我们已经检查过房间，也核对过部分证词。接下来，最重要的是等待新的情况，看看有没有人遗漏了什么。"
menu:
    "直接进入第三天早晨（第三章）":
        jump b20
