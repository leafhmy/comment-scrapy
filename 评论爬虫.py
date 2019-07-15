import urllib.request
import re
import urllib.error
headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36")
opener=urllib.request.build_opener()
opener.addheaders=[headers]
urllib.request.install_opener(opener)
comid="6396297703216100553"
url="https://video.coral.qq.com/varticle/1409059210/comment/v2?callback=_varticle1409059210commentv2&orinum=10&oriorder=o&pageflag=1&cursor="+comid+"&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=132"
for i in range(0,6):
    try:
        data=urllib.request.urlopen(url).read().decode()
        patnext='last":"(.*?)",'
        nextid=re.compile(patnext).findall(data)
        patcom='"content":"(.*?)",'
        comdata=re.compile(patcom).findall(data)
        for j in range (0,len(data)):
            print("第"+str(j)+"条评论是："+comdata[j])
        url="https://video.coral.qq.com/varticle/1409059210/comment/v2?callback=_varticle1409059210commentv2&orinum=10&oriorder=o&pageflag=1&cursor="+nextid+"&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=132&"
    except urllib.error.URLError as e:
            if hasattr(e,"code"):
                print(e.code)
            if hasattr(e,"reason"):
                print(e.reason)
    except Exception as e:
        print(e)

