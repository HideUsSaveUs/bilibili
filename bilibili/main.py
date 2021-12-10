
import requests 
import re
import json
import time
import random
UserAgents = [
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
            "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
            "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
            "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
            "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
            "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
            "Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12",
            "Opera/9.27 (Windows NT 5.2; U; zh-cn)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Version/3.1 Safari/525.13",
            "Mozilla/5.0 (iPhone; U; CPU like Mac OS X) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/4A93 ",
            "Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 ",
            "Mozilla/5.0 (Linux; U; Android 3.2; ja-jp; F-01D Build/F0001) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13 ",
            "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_1 like Mac OS X; ja-jp) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8B117 Safari/6531.22.7",
            "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; da-dk) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5 ",
            "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-US) AppleWebKit/530.9 (KHTML, like Gecko) Chrome/ Safari/530.9 ",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/11.10 Chromium/27.0.1453.93 Chrome/27.0.1453.93 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36"
        ]

def decode(id):
    try:
        agent=random.choice(UserAgents)
        headers = {'user-agent': agent}
        req="http://api.bilibili.com/x/web-interface/view?"
        reqq=requests.get(req+id)
        #aid=170001
        #bvid=BV1Ny4y1G7Yk
        reqj=json.loads(reqq.text)
    except Exception as e :
        print(e)
    return reqj
def decodelive(id):
    try:
        agent=random.choice(UserAgents)
        headers = {'user-agent': agent}
        req="http://api.live.bilibili.com/room/v1/Room/room_init?"
        reqq=requests.get(req+id)
        #aid=170001
        #bvid=BV1Ny4y1G7Yk
        reqj=json.loads(reqq.text)
    except Exception as e :
        print(e)
    return reqj
def decoderoom(id):
    try:
        agent=random.choice(UserAgents)
        headers = {'user-agent': agent}
        req="http://api.bilibili.com/x/space/acc/info?"
        reqq=requests.get(req+id)
        #aid=170001
        #bvid=BV1Ny4y1G7Yk
        reqj=json.loads(reqq.text)
    except Exception as e :
        print(e)
    return reqj
class Event(object):
    def init(plugin_event, Proc):
        pass

    def private_message(plugin_event, Proc):
        private_reply(plugin_event, Proc)

    def group_message(plugin_event, Proc):
        unity_reply(plugin_event, Proc)

    def poke(plugin_event, Proc):
        poke_reply(plugin_event, Proc)

    def save(plugin_event, Proc):
        pass
def private_reply(plugin_event, Proc):
    decode2j=decode(decodemessage(plugin_event.data.message))
    if decode2j["code"] == 0:
        a=decode2j["data"]["pubdate"]
        b=time.localtime(a) #通过time.localtime将时间戳转换成时间组
        c=time.strftime("%Y-%m-%d %H:%M:%S")#再将时间组转换成指定格式
        c=str(c)
        if decode2j["data"]["copyright"]==1:
            plugin_event.reply("Bvid为："+decode2j["data"]["bvid"]+"\n"+"Aid为："+str(decode2j["data"]["aid"])+"\n"+"稿件分P总数："+str(decode2j["data"]["videos"])+"\n"+"分区："+"\n"+decode2j["data"]["tname"]+"原创"+"\n"+"稿件标题："+decode2j["data"]["title"]+"\n"+"投稿时间："+c+"\n"+"简介："+decode2j["data"]["desc"]+"\n"+"UP主："+decode2j["data"]["owner"]["name"])
        elif decode2j["data"]["copyright"]==2:
            plugin_event.reply("Bvid为："+decode2j["data"]["bvid"]+"\n"+"Aid为："+str(decode2j["data"]["aid"])+"\n"+"稿件分P总数："+str(decode2j["data"]["videos"])+"\n"+"分区："+"\n"+decode2j["data"]["tname"]+"转载"+"\n"+"稿件标题："+decode2j["data"]["title"]+"\n"+"投稿时间："+c+"\n"+"简介："+decode2j["data"]["desc"]+"\n"+"UP主："+decode2j["data"]["owner"]["name"])
        plugin_event.reply("[CQ:image,file="+str(decode2j["data"]["pic"])+",c=10]")
    roomcheak=str(plugin_event.data.message[0:4])
    roomcheak=roomcheak.lower()
    try:
        if roomcheak =="room":
            roomid=str(plugin_event.data.message[4:])
            IAroomid="id="+roomid
            livecheak=decodelive(IAroomid)
            #plugin_event.reply(str(livecheak))
            roomfide=livecheak["data"]["uid"]
            MIroomfide="mid="+str(roomfide)
            roomfidecheak=decoderoom(MIroomfide)
            live_room=roomfidecheak["data"]["live_room"]
            if live_room["liveStatus"]==1:
                plugin_event.reply("[直播中]\n直播间网页url："+live_room["url"]+"\n直播间标题："+live_room["title"]+"\n直播间封面："+"[CQ:image,file="+str(live_room["cover"])+",c=10]"+"\n直播间人气："+str(live_room["online"]))
            elif live_room["liveStatus"]==0:
                plugin_event.reply("[未直播]\n直播间网页url："+live_room["url"]+"\n直播间标题："+live_room["title"]+"\n直播间封面："+"[CQ:image,file="+str(live_room["cover"])+",c=10]")
    except Exception as e:
        pass
    try:
        btvcheak=re.findall(r"https://b23.tv/(.*)",plugin_event.data.message,re.S)[0]
        if btvcheak !="":
            url = plugin_event.data.message
            r = requests.get(url,headers={"Content-Type":"application/json"})
            reditList = r.history#可以看出获取的是一个地址序列
            btvreal=reditList[0].headers["location"]
            btvrex=btvreal[31:43]
            avbv3=str(btvrex[0:2])
            # plugin_event.reply(btvrex)
            avbv3=avbv3.lower()
            if avbv3=="av":
                id = "aid="+str(btvrex[2:])
                decode2j=decode(id)
                if decode2j["code"] == 0:
                    a=decode2j["data"]["pubdate"]
                    b=time.localtime(a) #通过time.localtime将时间戳转换成时间组
                    c=time.strftime("%Y-%m-%d %H:%M:%S")#再将时间组转换成指定格式
                    c=str(c)
                    if decode2j["data"]["copyright"]==1:
                        plugin_event.reply("Bvid为："+decode2j["data"]["bvid"]+"\n"+"Aid为："+str(decode2j["data"]["aid"])+"\n"+"稿件分P总数："+str(decode2j["data"]["videos"])+"\n"+"分区："+"\n"+decode2j["data"]["tname"]+"原创"+"\n"+"稿件标题："+decode2j["data"]["title"]+"\n"+"投稿时间："+c+"\n"+"简介："+decode2j["data"]["desc"]+"\n"+"UP主："+decode2j["data"]["owner"]["name"])
                    elif decode2j["data"]["copyright"]==2:
                        plugin_event.reply("Bvid为："+decode2j["data"]["bvid"]+"\n"+"Aid为："+str(decode2j["data"]["aid"])+"\n"+"稿件分P总数："+str(decode2j["data"]["videos"])+"\n"+"分区："+"\n"+decode2j["data"]["tname"]+"转载"+"\n"+"稿件标题："+decode2j["data"]["title"]+"\n"+"投稿时间："+c+"\n"+"简介："+decode2j["data"]["desc"]+"\n"+"UP主："+decode2j["data"]["owner"]["name"])
                    plugin_event.reply("[CQ:image,file="+str(decode2j["data"]["pic"])+",c=10]")
            if avbv3=="bv":
                id = "bvid="+str(btvrex)
                decode2j=decode(id)
                if decode2j["code"] == 0:
                    a=decode2j["data"]["pubdate"]
                    b=time.localtime(a) #通过time.localtime将时间戳转换成时间组
                    c=time.strftime("%Y-%m-%d %H:%M:%S")#再将时间组转换成指定格式
                    c=str(c)
                    if decode2j["data"]["copyright"]==1:
                        plugin_event.reply("Bvid为："+decode2j["data"]["bvid"]+"\n"+"Aid为："+str(decode2j["data"]["aid"])+"\n"+"稿件分P总数："+str(decode2j["data"]["videos"])+"\n"+"分区："+"\n"+decode2j["data"]["tname"]+"原创"+"\n"+"稿件标题："+decode2j["data"]["title"]+"\n"+"投稿时间："+c+"\n"+"简介："+decode2j["data"]["desc"]+"\n"+"UP主："+decode2j["data"]["owner"]["name"])
                    elif decode2j["data"]["copyright"]==2:
                        plugin_event.reply("Bvid为："+decode2j["data"]["bvid"]+"\n"+"Aid为："+str(decode2j["data"]["aid"])+"\n"+"稿件分P总数："+str(decode2j["data"]["videos"])+"\n"+"分区："+"\n"+decode2j["data"]["tname"]+"转载"+"\n"+"稿件标题："+decode2j["data"]["title"]+"\n"+"投稿时间："+c+"\n"+"简介："+decode2j["data"]["desc"]+"\n"+"UP主："+decode2j["data"]["owner"]["name"])
                    plugin_event.reply("[CQ:image,file="+str(decode2j["data"]["pic"])+",c=10]")
    except Exception as e:
        pass
def unity_reply(plugin_event, Proc):
    try:
        decode2j=decode(decodemessage(plugin_event.data.message))
        if decode2j["code"] == 0:
            a=decode2j["data"]["pubdate"]
            b=time.localtime(a) #通过time.localtime将时间戳转换成时间组
            c=time.strftime("%Y-%m-%d %H:%M:%S")#再将时间组转换成指定格式
            c=str(c)
            if decode2j["data"]["copyright"]==1:
                plugin_event.reply("Bvid为："+decode2j["data"]["bvid"]+"\n"+"Aid为："+str(decode2j["data"]["aid"])+"\n"+"稿件分P总数："+str(decode2j["data"]["videos"])+"\n"+"分区："+"\n"+decode2j["data"]["tname"]+"原创"+"\n"+"稿件标题："+decode2j["data"]["title"]+"\n"+"投稿时间："+c+"\n"+"简介："+decode2j["data"]["desc"]+"\n"+"UP主："+decode2j["data"]["owner"]["name"])
            elif decode2j["data"]["copyright"]==2:
                plugin_event.reply("Bvid为："+decode2j["data"]["bvid"]+"\n"+"Aid为："+str(decode2j["data"]["aid"])+"\n"+"稿件分P总数："+str(decode2j["data"]["videos"])+"\n"+"分区："+"\n"+decode2j["data"]["tname"]+"转载"+"\n"+"稿件标题："+decode2j["data"]["title"]+"\n"+"投稿时间："+c+"\n"+"简介："+decode2j["data"]["desc"]+"\n"+"UP主："+decode2j["data"]["owner"]["name"])
            plugin_event.reply("[CQ:image,file="+str(decode2j["data"]["pic"])+",c=10]")
    except Exception as e:
        pass
    roomcheak=str(plugin_event.data.message[0:4])
    roomcheak=roomcheak.lower()
    try:
        if roomcheak =="room":
            roomid=str(plugin_event.data.message[4:])
            IAroomid="id="+roomid
            livecheak=decodelive(IAroomid)
            #plugin_event.reply(str(livecheak))
            roomfide=livecheak["data"]["uid"]
            MIroomfide="mid="+str(roomfide)
            roomfidecheak=decoderoom(MIroomfide)
            live_room=roomfidecheak["data"]["live_room"]
            if live_room["liveStatus"]==1:
                plugin_event.reply("[直播中]\n直播间网页url："+live_room["url"]+"\n直播间标题："+live_room["title"]+"\n直播间封面："+"[CQ:image,file="+str(live_room["cover"])+",c=10]"+"\n直播间人气："+str(live_room["online"]))
            elif live_room["liveStatus"]==0:
                plugin_event.reply("[未直播]\n直播间网页url："+live_room["url"]+"\n直播间标题："+live_room["title"]+"\n直播间封面："+"[CQ:image,file="+str(live_room["cover"])+",c=10]")
    except Exception as e:
        pass
    try:
        btvcheak=re.findall(r"https://b23.tv/(.*)",plugin_event.data.message,re.S)[0]
        if btvcheak !="":
            url = plugin_event.data.message
            r = requests.get(url,headers={"Content-Type":"application/json"})
            reditList = r.history#可以看出获取的是一个地址序列
            btvreal=reditList[0].headers["location"]
            btvrex=btvreal[31:43]
            avbv3=str(btvrex[0:2])
            # plugin_event.reply(btvrex)
            avbv3=avbv3.lower()
            if avbv3=="av":
                id = "aid="+str(btvrex[2:])
                decode2j=decode(id)
                if decode2j["code"] == 0:
                    a=decode2j["data"]["pubdate"]
                    b=time.localtime(a) #通过time.localtime将时间戳转换成时间组
                    c=time.strftime("%Y-%m-%d %H:%M:%S")#再将时间组转换成指定格式
                    c=str(c)
                    if decode2j["data"]["copyright"]==1:
                        plugin_event.reply("Bvid为："+decode2j["data"]["bvid"]+"\n"+"Aid为："+str(decode2j["data"]["aid"])+"\n"+"稿件分P总数："+str(decode2j["data"]["videos"])+"\n"+"分区："+"\n"+decode2j["data"]["tname"]+"原创"+"\n"+"稿件标题："+decode2j["data"]["title"]+"\n"+"投稿时间："+c+"\n"+"简介："+decode2j["data"]["desc"]+"\n"+"UP主："+decode2j["data"]["owner"]["name"])
                    elif decode2j["data"]["copyright"]==2:
                        plugin_event.reply("Bvid为："+decode2j["data"]["bvid"]+"\n"+"Aid为："+str(decode2j["data"]["aid"])+"\n"+"稿件分P总数："+str(decode2j["data"]["videos"])+"\n"+"分区："+"\n"+decode2j["data"]["tname"]+"转载"+"\n"+"稿件标题："+decode2j["data"]["title"]+"\n"+"投稿时间："+c+"\n"+"简介："+decode2j["data"]["desc"]+"\n"+"UP主："+decode2j["data"]["owner"]["name"])
                    plugin_event.reply("[CQ:image,file="+str(decode2j["data"]["pic"])+",c=10]")
            if avbv3=="bv":
                id = "bvid="+str(btvrex)
                decode2j=decode(id)
                if decode2j["code"] == 0:
                    a=decode2j["data"]["pubdate"]
                    b=time.localtime(a) #通过time.localtime将时间戳转换成时间组
                    c=time.strftime("%Y-%m-%d %H:%M:%S")#再将时间组转换成指定格式
                    c=str(c)
                    if decode2j["data"]["copyright"]==1:
                        plugin_event.reply("Bvid为："+decode2j["data"]["bvid"]+"\n"+"Aid为："+str(decode2j["data"]["aid"])+"\n"+"稿件分P总数："+str(decode2j["data"]["videos"])+"\n"+"分区："+"\n"+decode2j["data"]["tname"]+"原创"+"\n"+"稿件标题："+decode2j["data"]["title"]+"\n"+"投稿时间："+c+"\n"+"简介："+decode2j["data"]["desc"]+"\n"+"UP主："+decode2j["data"]["owner"]["name"])
                    elif decode2j["data"]["copyright"]==2:
                        plugin_event.reply("Bvid为："+decode2j["data"]["bvid"]+"\n"+"Aid为："+str(decode2j["data"]["aid"])+"\n"+"稿件分P总数："+str(decode2j["data"]["videos"])+"\n"+"分区："+"\n"+decode2j["data"]["tname"]+"转载"+"\n"+"稿件标题："+decode2j["data"]["title"]+"\n"+"投稿时间："+c+"\n"+"简介："+decode2j["data"]["desc"]+"\n"+"UP主："+decode2j["data"]["owner"]["name"])
                    plugin_event.reply("[CQ:image,file="+str(decode2j["data"]["pic"])+",c=10]")
    except Exception as e:
        pass
def poke_reply(plugin_event, Proc):
    pass

def decodemessage(message):
    abvcheak=message[0:2]
    abvcheak=abvcheak.lower()
    if abvcheak=="av" or abvcheak=="bv":
        if abvcheak=="av":
            return "aid="+message[2:]
        if abvcheak=="bv":
            return "bvid="+message
    httpscheak=message[0:8]
    httpscheak=httpscheak.lower()
    if httpscheak=="https://":
        btvcheak=message[8:15]
        btvcheak=btvcheak.lower()
        if btvcheak=="b23.tv/":
            return"btv"
        bilicheak=message[8:31]
        bilicheak=bilicheak.lower()
        if bilicheak=="www.bilibili.com/video/":
            spritcheak=message.rstrip('/')
            #print(spritcheak[31:])
            abvbilicheak=spritcheak[31:33]
            abvbilicheak=abvbilicheak.lower()
            if abvbilicheak=="av" or abvbilicheak=="bv":
                if abvbilicheak=="av":
                    return "aid="+spritcheak[33:]
                if abvbilicheak=="bv":
                    return "bvid="+spritcheak[31:]