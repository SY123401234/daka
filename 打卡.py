import requests
import time
import datetime
import random
cookie = "JSESSIONID=" + input("输入jsessionid:")
jb = time.strftime("%Y")
lat = 29.607838
lng = 106.57144
dkwz = "重庆市江北区内环快速路"
url = "http://weixin.cqcet.edu.cn/wx/weixin/st/need/sxdk/add"
host = "weixin.cqcet.edu.cn"
origin = "http://" +host
referer = url + "?date=" + time.strftime("%Y-%m-%d") + "&jb=" + jb
UA = "mozilla/5.0 (linux; u; android 4.1.2; zh-cn; mi-one plus build/jzo54k) applewebkit/534.30 (khtml, like gecko) version/4.0 mobile safari/534.30 micromessenger/5.0.1.352"
header = {
        "HOST":host,
        "Connection":"keep-alive",
        "Accept":"application/json",
        "X-Requested-With":"XMLHttpRequest",
        "User-Agent":UA,
        "Content-Type":"application/x-www-form-urlencoded",
        "Origin":origin,
        "Referer":referer,
        "Accept-Encoding":"gzip,deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie":cookie
            }

print("当前日期:" + time.strftime("%Y-%m-%d"))
begin = input("输入开始日期:") or "2021-11-30"   #默认21-11-30
end = input("输入结束日期:") or time.strftime("%Y-%m-%d") #默认当前日期
rjnr = input("打卡内容:") or "实习"
b1 = begin.rsplit("-")
b = datetime.date(int(b1[0]),int(b1[1]),int(b1[2]))
e1 = end.rsplit("-")
e = datetime.date(int(e1[0]),int(e1[1]),int(e1[2]))
delta = datetime.timedelta(days=1)
while b <= e:
    date = b.strftime("%Y-%m-%d")
    lat += random.randint(0,4)
    lng += random.randint(0,4)
    data = {
        "jb":jb,
        "date":date,
        "lat":lat,
        "lng":lng,
        "fxdj":"低风险",
        "dkwz":dkwz,
        "rjnr":rjnr
            }
    r = requests.post(url , headers = header , data = data)
    print (b)
    print(str(r) + r.text)
    b += delta
    time.sleep(2)
