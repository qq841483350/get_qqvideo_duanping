#coding:utf8
#获取腾讯视频最新短评评论数据：
import requests,json,re
def get_qqvedio_comment(url,num):
    html=requests.get(url).content
    vid=re.findall('vid:"(.*?)"',html)[0]
    print vid
    url="http://sns.video.qq.com/fcgi-bin/video_comment_id?otype=json&op=3&vid=%s"%vid
    html=requests.get(url).content
    comment_id=re.findall('"comment_id":"(.*?)"',html)[0]
    url="http://coral.qq.com/article/%s/comment?commentid=0&reqnum=%s"%(comment_id,num)
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0"}
    jscontent=requests.get(url,headers=headers).content
    jsdict=json.loads(jscontent)
    jsdata=jsdict['data']
    comments=jsdata['commentid']
    for comment in comments:
        print comment['content']
if __name__=="__main__":
    # url="http://v.qq.com/cover/t/t8ki4q8lvwfnuhx/u00161kvc1d.html"
    url=raw_input("请输视频URL地址然后回按回车继续：")
    num=raw_input("请输入获取评论的数量，如20条就输入20：")
    get_qqvedio_comment(url,num)
