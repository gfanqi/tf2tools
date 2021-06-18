# encoding:utf-8
import re
import uuid
import requests
import os
import numpy
import imghdr
from PIL import Image


# 获取百度图片下载图片
def download_image(key_word, save_name, download_max):
    download_sum = 0
    str_gsm = '80'
    # 把每个类别的图片存放在单独一个文件夹中
    save_path = 'images' + '/' + save_name
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    while download_sum < download_max:
        # 下载次数超过指定值就停止下载
        if download_sum >= download_max:
            break
        str_pn = str(download_sum)
        # 定义百度图片的路径
        url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&' \
              'word=' + key_word + '&pn=' + str_pn + '&gsm=' + str_gsm + '&ct=&ic=0&lm=-1&width=0&height=0'
        # url = "https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E8%80%81%E4%BA%BA%E6%91%94%E5%80%92&step_word=&hs=2&pn=0&spn=0&di=28850&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=0&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=undefined&cs=2232623552%2C2580950713&os=4217491767%2C2860405015&simid=4207151205%2C507155202&adpicid=0&lpn=0&ln=1688&fr=&fmq=1617797042740_R&fm=&ic=undefined&s=undefined&hd=undefined&latest=undefined&copyright=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&ist=&jit=&cg=&bdtype=11&oriquery=&objurl=https%3A%2F%2Fgimg2.baidu.com%2Fimage_search%2Fsrc%3Dhttp%3A%2F%2Fnimg.ws.126.net%2F%3Furl%3Dhttp%253A%252F%252Fdingyue.ws.126.net%252F3GFKtE0Aenm1pNVuKnm5wPjOxyHPCKrb3Ud6SvfDWzL5U1617708187562.jpeg%26thumbnail%3D650x2147483647%26quality%3D80%26type%3Djpg%26refer%3Dhttp%3A%2F%2Fnimg.ws.126.net%26app%3D2002%26size%3Df9999%2C10000%26q%3Da80%26n%3D0%26g%3D0n%26fmt%3Djpeg%3Fsec%3D1620389076%26t%3D91e3ef42fe879ca93351f7c18365f54b&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3B8mn_z%26e3Bv54AzdH3F1yAzdH3Fw6ptvsjAzdH3FGmUcTJHAacnc9IXS_z%26e3Bip4s&gsm=1&rpstart=0&rpnum=0&islist=&querylist=&force=undefined"
        print(url)
        print('正在下载 %s 的第 %d 张图片.....' % (key_word, download_sum))
        try:
            # 获取当前页面的源码
            # result = requests.get(url, timeout=100).text
            result = '''
            
<!DOCTYPE html>           

<script>
    (function (context) {
        var data = {};
        var url = '//imgstat.baidu.com/17.gif';
        var start = +new Date;
        var createQuery = function (data) {
            var ret = [];
            for (var key in data) {
                ret.push(key + '=' + data[key]);
            }
            return ret.join('&');
        };

        var _mergeCommPara = function (data) {
            data.etype = 'speed';
            data.page = 'result';
            data.logid = "11806807618841733495";
            data.sid = 'f2c950b92c68b66d054fe462e44821aee1f83dbb';
            data.wh = window.screen.width + 'x' + window.screen.height ;
            data.sampid = '85';
            data.app = 'searchresult';
            data.spat = 0 + '-' + '';
            data.protocol = window.location.protocol.replace(':', '');
            if ('0' - 0) {
                data.ishttps = '0';
            }
            
            data.sync = "";
            return data;
        };
        var _profiles = {
            'slider': {
                _url: '//imgstat.baidu.com/17.gif',
                etype: 'slide'
            }
        };
        var speed = {
            set: function (key, value) {
                if (key) {
                    data[key] = value || 0;
                }
            },
            get: function (key) {
                return data[key] || ('start' === key && start);
            },
            mark: function (key, value, ts) {
                if (undefined === value) {
                    value = new Date - start;
                }
                if (true === ts) {
                    value = value - start;
                }
                data[key] = value;
            },
            send: function (ext) {
                if (ext) {
                    for (var key in ext) {
                        data[key] = ext[key];
                    }
                }
                _mergeCommPara(data);
                var queryString = createQuery(data);
                new Image().src = url + '?' + queryString;
            },
            loadmark: function () {
                value = new Date - start;

                if (speed.firstScCount) {
                    speed.firstScCount += 1;
                }else{
                    speed.firstScCount = 1;
                }

                data['firstSc'] = value;

            },
            log: function (profile, data) {
                var queryString = createQuery(data);
                var pf = _profiles[profile];
                var a = [];

                _mergeCommPara(data);
                for (var p in pf) {
                    if (p.indexOf('_') !== 0) {
                        data[p] = pf[p];
                    }

                }
                for (var p in data) {
                    a.push(p + '=' + data[p]);
                }


                (new Image).src = pf._url + '?' + a.join('&');
            }
        };
        context.speed = speed;
        speed.firstScCount = 0;
        (function () {
            window.logid = "11806807618841733495";
            loaded = 0;
            var addWindowEvent = window.addEventListener ?
                function(type, fn) { window.addEventListener(type, fn, false); } :
                function(type, fn) { window.attachEvent('on' + type, fn); };
            addWindowEvent('beforeunload', function () {
                if (!loaded) {
                    speed.mark('leave');
                    speed.send();
                }
            });

            addWindowEvent('load', function () {
                loaded = 1;
            });
        })();
    })(window);
</script>
<script>
    // ala进入打点
    try {
        if (!window._alaEnter) {
            window._alaEnter = true;
            function query2Json(query) {
                var json = {};
                var search = query.split("&");
                for (var i = search.length - 1; i >= 0; i--) {
                    var s = search[i].split('=');
                    json[s[0]] = s[1];
                }
                return json;
            }
            var query = query2Json((location.search || '').replace('?', ''));
            if (+query.hs && query.tn === 'baiduimage') {
                var payload = 'dsp=pc&tn=result&hs=' + query.hs;
                (new Image()).src = '//image.baidu.com/pv/pv.gif?' + payload + '&type=enter&t=' + (+new Date);
                window._alaEnter = function (type) {
                    (new Image()).src = '//image.baidu.com/pv/pv.gif?' + payload
                        + '&type=' + type + '&t=' + (+new Date);
                };
                var sid = "91dc552368e199e9c1cfcd1235a8776facb8af50";
                if (window.localStorage
                    && window.localStorage.sid
                    && window.localStorage.sid !== sid) {
                    window._alaEnter('change');
                }
                window.localStorage.sid = sid;
            }
        }
    } catch(e) {}
</script>

   <html>   <!--STATUS OK-->  <head>  
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<noscript>
<meta http-equiv="refresh" content="0;url=/search/index?ct=201326592&lm=-1&tn=baiduimagenojs&ipn=rnj&pv=&word=%E8%80%81%E4%BA%BA%E6%91%94%E5%80%92&z=0&pn=0&rn=20&cl=2&ie=utf-8">

<style>table,.p{display:none}</style>

</noscript>
 <title>
老人摔倒_百度图片搜索</title> <link rel="shortcut icon" href="//img1.bdstatic.com/static/common/img/icon_cf1b905.png" type="image/x-icon"> <link rel="icon" sizes="any" href="//img1.bdstatic.com/static/common/img/icon_cf1b905.png">  <script>
    void function(a,b,c,d,e,f,g){a.alogObjectName=e,a[e]=a[e]||function(){(a[e].q=a[e].q||[]).push(arguments)},a[e].l=a[e].l||+new Date,d="https:"===a.location.protocol?"https://fex.bdstatic.com"+d:"http://fex.bdstatic.com"+d;var h=!0;if(a.alogObjectConfig&&a.alogObjectConfig.sample){var i=Math.random();a.alogObjectConfig.rand=i,i>a.alogObjectConfig.sample&&(h=!1)}h&&(f=b.createElement(c),f.async=!0,f.src=d+"?v="+~(new Date/864e5)+~(new Date/864e5),g=b.getElementsByTagName(c)[0],g.parentNode.insertBefore(f,g))}(window,document,"script","/hunter/alog/alog.min.js","alog"),void function(){function a(){}window.PDC={mark:function(a,b){alog("speed.set",a,b||+new Date),alog.fire&&alog.fire("mark")},init:function(a){alog("speed.set","options",a)},view_start:a,tti:a,page_ready:a}}();
    void function(n){var o=!1;n.onerror=function(n,e,t,c){var i=!0;return!e&&/^script error/i.test(n)&&(o?i=!1:o=!0),i&&alog("exception.send","exception",{msg:n,js:e,ln:t,col:c}),!1},alog("exception.on","catch",function(n){alog("exception.send","exception",{msg:n.msg,js:n.path,ln:n.ln,method:n.method,flag:"catch"})})}(window);
</script>     
   <script>
        var Ihttps_agent_config = {"http:\/\/nssug.baidu.com":"https:\/\/sp1.baidu.com\/8qUZeT8a2gU2pMbgoY3K\/su","http:\/\/img.baidu.com":"https:\/\/gss2.bdstatic.com\/70cFsjip0QIZ8tyhnq","http:\/\/himg.bdimg.com":"https:\/\/ss1.bdstatic.com\/7Ls0a8Sm1A5BphGlnYG","http:\/\/apps.bdimg.com":"https:\/\/ss0.bdstatic.com\/9_QWf8Sm1A5BphGlnYG","http:\/\/f3.baidu.com":"https:\/\/sp3.baidu.com\/-uV1bjeh1BF3odCf","http:\/\/bzclk.baidu.com":"https:\/\/gsp0.baidu.com\/9q9JcDHa2gU2pMbgoY3K","http:\/\/img0.imgtn.bdimg.com":"https:\/\/ss0.bdstatic.com\/70cFvHSh_Q1YnxGkpoWK1HF6hhy","http:\/\/img1.imgtn.bdimg.com":"https:\/\/ss1.bdstatic.com\/70cFvXSh_Q1YnxGkpoWK1HF6hhy","http:\/\/img2.imgtn.bdimg.com":"https:\/\/ss2.bdstatic.com\/70cFvnSh_Q1YnxGkpoWK1HF6hhy","http:\/\/img3.imgtn.bdimg.com":"https:\/\/ss3.bdstatic.com\/70cFv8Sh_Q1YnxGkpoWK1HF6hhy","http:\/\/img4.imgtn.bdimg.com":"https:\/\/ss0.bdstatic.com\/70cFuHSh_Q1YnxGkpoWK1HF6hhy","http:\/\/img5.imgtn.bdimg.com":"https:\/\/ss1.bdstatic.com\/70cFuXSh_Q1YnxGkpoWK1HF6hhy","http:\/\/bdimg.share.baidu.com":"https:\/\/gss0.baidu.com\/9rA4cT8aBw9FktbgoI7O1ygwehsv","http:\/\/dispatcher.video.qiyi.com":"https:\/\/gss0.bdstatic.com\/-LsZfDe52w9JkxG9m9iS_HFjgAkrreHg-_","http:\/\/passport.bdimg.com":"https:\/\/ss0.bdstatic.com\/5LMZfyabBhJ3otebn9fN2DJv"};
    </script> <script type="text/javascript" src="//img0.bdstatic.com/static/common/mod_6f6741d.js"></script> 
<script>
    //记录页面开始时间
    window.pageStartTime = new Date();
    window.scrollTo(0, 0);
</script>
 <link rel="stylesheet" type="text/css" href="//img1.bdstatic.com/static/searchresult/pkg/result_e902311.css"/><link rel="stylesheet" type="text/css" href="//img0.bdstatic.com/static/searchresult/result/result_flip_ddbf9a0.css"/><link rel="stylesheet" type="text/css" href="//img1.bdstatic.com/static/common/pkg/co_e90514e.css"/><link rel="stylesheet" type="text/css" href="//img1.bdstatic.com/static/common/widget/ui/slider/slider_ecce195.css"/><link rel="stylesheet" type="text/css" href="//img0.bdstatic.com/static/common/widget/ui/userInfo/userInfo_0b12a55.css"/><link rel="stylesheet" type="text/css" href="//img0.bdstatic.com/static/searchresult/widget/ui/base/view/AvFilterView/AvFilterView_5709328.css"/><link rel="stylesheet" type="text/css" href="//img0.bdstatic.com/static/searchresult/widget/ui/base/view/AvMuiltSizeFilterView/AvMuiltSizeFilterView_5a57aa1.css"/><link rel="stylesheet" type="text/css" href="//img0.bdstatic.com/static/searchresult/widget/ui/base/view/AvTypeFilterView/AvTypeFilterView_cea6b92.css"/><link rel="stylesheet" type="text/css" href="//img1.bdstatic.com/static/searchresult/widget/ui/base/view/AvColorWallFilterView/AvColorWallFilterView_cf8a646.css"/><link rel="stylesheet" type="text/css" href="//img2.bdstatic.com/static/searchresult/widget/ui/base/view/AvColorFilterView/AvColorFilterView_5b1da63.css"/><link rel="stylesheet" type="text/css" href="//img1.bdstatic.com/static/searchresult/widget/pagelets/base/newImgfilter/newImgFilter_5fa9e0c.css"/><link rel="stylesheet" type="text/css" href="//img0.bdstatic.com/static/searchresult/widget/flip/paging_b3bc8d8.css"/></head>  <script> alog('speed.set', 'ht', +new Date); </script>  <body class="flip"> <script type="text/javascript">require.siteNS && require.siteNS(["searchresult", "common"]);require.resourceMap({"res":{"common:widget/ui/base/base.js":{"url":"//img0.bdstatic.com/static/common/widget/ui/base/base_a66ce51.js"},"common:widget/ui/browser-storage/browser-storage.js":{"url":"//img1.bdstatic.com/static/common/widget/ui/browser-storage/browser-storage_ad6bd42.js"},"common:widget/ui/arch/router.js":{"url":"//img2.bdstatic.com/static/common/widget/ui/arch/router_1670dcf.js","pkg":"common:p1","deps":["common:widget/ui/base/base.js"]},"common:widget/ui/arch/app.js":{"url":"//img2.bdstatic.com/static/common/widget/ui/arch/app_c1dac05.js","pkg":"common:p1","deps":["common:widget/ui/base/base.js","common:widget/ui/arch/router.js"]},"common:widget/ui/base/EventDispatcher.js":{"url":"//img0.bdstatic.com/static/common/widget/ui/base/EventDispatcher_e71d337.js","pkg":"common:p1"},"common:widget/ui/base/events.js":{"url":"//img0.bdstatic.com/static/common/widget/ui/base/events_f8b4e1f.js","pkg":"common:p1","deps":["common:widget/ui/base/base.js","common:widget/ui/base/EventDispatcher.js"]},"common:widget/ui/arch/behavior/pageresizer.js":{"url":"//img1.bdstatic.com/static/common/widget/ui/arch/behavior/pageresizer_9f05f70.js","pkg":"common:p1","deps":["common:widget/ui/base/base.js","common:widget/ui/base/events.js"]},"common:widget/ui/arch/localdb.js":{"url":"//img1.bdstatic.com/static/common/widget/ui/arch/localdb_1fa8a65.js","pkg":"common:p1","deps":["common:widget/ui/base/base.js"]},"common:widget/ui/arch/collection.js":{"url":"//img2.bdstatic.com/static/common/widget/ui/arch/collection_8624f21.js","pkg":"common:p1","deps":["common:widget/ui/base/base.js","common:widget/ui/base/events.js","common:widget/ui/arch/localdb.js"]},"common:widget/ui/arch/handlers.js":{"url":"//img2.bdstatic.com/static/common/widget/ui/arch/handlers_2d9d42f.js","pkg":"common:p1","deps":["common:widget/ui/base/base.js"]},"common:widget/ui/events/events.js":{"url":"//img2.bdstatic.com/static/common/widget/ui/events/events_87337df.js","pkg":"common:p1","deps":["common:widget/ui/base/base.js","common:widget/ui/base/EventDispatcher.js"]},"common:widget/ui/utils/scroller.js":{"url":"//img0.bdstatic.com/static/common/widget/ui/utils/scroller_efc1f29.js","pkg":"common:p1","deps":["common:widget/ui/base/base.js","common:widget/ui/events/events.js"]},"common:widget/ui/utils/pageresizer.js":{"url":"//img1.bdstatic.com/static/common/widget/ui/utils/pageresizer_9feba52.js","pkg":"common:p1","deps":["common:widget/ui/base/base.js","common:widget/ui/events/events.js"]},"common:widget/ui/utils/utils.js":{"url":"//img0.bdstatic.com/static/common/widget/ui/utils/utils_bd26384.js","pkg":"common:p1","deps":["common:widget/ui/base/base.js","common:widget/ui/utils/scroller.js","common:widget/ui/utils/pageresizer.js"]},"common:widget/ui/arch/history.js":{"url":"//img1.bdstatic.com/static/common/widget/ui/arch/history_dbb6541.js","pkg":"common:p1","deps":["common:widget/ui/base/base.js","common:widget/ui/utils/utils.js","common:widget/ui/base/events.js"]},"common:widget/ui/arch/model.js":{"url":"//img0.bdstatic.com/static/common/widget/ui/arch/model_32910e4.js","pkg":"common:p1","deps":["common:widget/ui/base/base.js"]},"common:widget/ui/arch/pagemodel.js":{"url":"//img1.bdstatic.com/static/common/widget/ui/arch/pagemodel_8be1499.js","pkg":"common:p1","deps":["common:widget/ui/base/base.js","common:widget/ui/utils/utils.js","common:widget/ui/base/events.js","common:widget/ui/arch/model.js"]},"common:widget/ui/base/subject.js":{"url":"//img0.bdstatic.com/static/common/widget/ui/base/subject_7c3c6c3.js","pkg":"common:p1","deps":["common:widget/ui/base/base.js"]},"common:widget/ui/EventEmitter/EventEmitter.js":{"url":"//img0.bdstatic.com/static/common/widget/ui/EventEmitter/EventEmitter_655344a.js","pkg":"common:p1","deps":["common:widget/ui/base/base.js"]},"common:widget/ui/monitorRequest/monitorRequest.js":{"url":"//img0.bdstatic.com/static/common/widget/ui/monitorRequest/monitorRequest_cabcf84.js","pkg":"common:p1"},"common:widget/ui/searchUtils/searchUtils.js":{"url":"//img1.bdstatic.com/static/common/widget/ui/searchUtils/searchUtils_17600ce.js","pkg":"common:p1","deps":["common:widget/ui/base/base.js"]},"common:widget/ui/slider/slider.js":{"url":"//img1.bdstatic.com/static/common/widget/ui/slider/slider_545c0c2.js","pkg":"common:p1","deps":["common:widget/ui/base/base.js","common:widget/ui/EventEmitter/EventEmitter.js"]},"common:widget/ui/statistic/statistic.js":{"url":"//img2.bdstatic.com/static/common/widget/ui/statistic/statistic_228a319.js","pkg":"common:p1","deps":["common:widget/ui/base/base.js","common:widget/ui/monitorRequest/monitorRequest.js","common:widget/ui/base/events.js","common:widget/ui/utils/utils.js"]},"common:widget/ui/suggest/data.js":{"url":"//img0.bdstatic.com/static/common/widget/ui/suggest/data_efd5670.js","pkg":"common:p1","deps":["common:widget/ui/base/base.js","common:widget/ui/utils/utils.js","common:widget/ui/base/events.js"]},"common:widget/ui/suggest/inputwatcher.js":{"url":"//img2.bdstatic.com/static/common/widget/ui/suggest/inputwatcher_2eb7c40.js","pkg":"common:p1","deps":["common:widget/ui/base/base.js","common:widget/ui/base/events.js"]},"common:widget/ui/suggest/suggestionlist.js":{"url":"//img0.bdstatic.com/static/common/widget/ui/suggest/suggestionlist_24c3638.js","pkg":"common:p1","deps":["common:widget/ui/base/base.js","common:widget/ui/base/events.js"]},"common:widget/ui/suggest/suggestion.js":{"url":"//img2.bdstatic.com/static/common/widget/ui/suggest/suggestion_22deee6.js","pkg":"common:p1","deps":["common:widget/ui/base/base.js","common:widget/ui/base/events.js","common:widget/ui/suggest/data.js","common:widget/ui/suggest/inputwatcher.js","common:widget/ui/suggest/suggestionlist.js"]},"common:widget/ui/sugHistory/sugHistory.js":{"url":"//img2.bdstatic.com/static/common/widget/ui/sugHistory/sugHistory_1117abb.js","pkg":"common:p1","deps":["common:widget/ui/base/base.js","common:widget/ui/statistic/statistic.js","common:widget/ui/utils/utils.js"]},"common:widget/ui/SugRec/SugRec.js":{"url":"//img2.bdstatic.com/static/common/widget/ui/SugRec/SugRec_3755387.js","pkg":"common:p1","deps":["common:widget/ui/base/base.js","common:widget/ui/statistic/statistic.js"]},"common:widget/ui/swf/swf.js":{"url":"//img1.bdstatic.com/static/common/widget/ui/swf/swf_b5294d0.js","pkg":"common:p1"},"common:widget/ui/userInfo/userInfo.js":{"url":"//img1.bdstatic.com/static/common/widget/ui/userInfo/userInfo_296f165.js","pkg":"common:p1","deps":["common:widget/ui/base/base.js","common:widget/ui/searchUtils/searchUtils.js","common:widget/ui/base/events.js","common:widget/ui/browser-storage/browser-storage.js","common:widget/ui/utils/utils.js","common:widget/ui/statistic/statistic.js"]},"common:widget/ui/feedback/feedback.js":{"url":"//img0.bdstatic.com/static/common/widget/ui/feedback/feedback_527d5a5.js","pkg":"common:p1"},"common:widget/ui/backtop/backTop.js":{"url":"//img1.bdstatic.com/static/common/widget/ui/backtop/backTop_72880bc.js","pkg":"common:p1","deps":["common:widget/ui/base/base.js"]},"common:widget/shitu/static/animate.js":{"url":"//img1.bdstatic.com/static/common/widget/shitu/static/animate_d5993fc.js","deps":["common:widget/ui/base/base.js"]},"common:widget/shitu/run.js":{"url":"//img0.bdstatic.com/static/common/widget/shitu/run_2c1ca54.js","deps":["common:widget/ui/base/base.js","common:widget/ui/utils/utils.js","common:widget/shitu/static/animate.js"]},"searchresult:widget/ui/app/noResultPage.js":{"url":"//img0.bdstatic.com/static/searchresult/widget/ui/app/noResultPage_aac2743.js","deps":["common:widget/ui/base/base.js","searchresult:widget/ui/controls/relsearchBox/relsearchBox.js","common:widget/ui/userInfo/userInfo.js","searchresult:widget/ui/controls/hotwordBox/hotwordBox.js","searchresult:widget/ui/controls/suggBox/suggBox.js","searchresult:widget/ui/models/filtermodel.js","searchresult:widget/ui/statistic/statistic.js","common:widget/ui/utils/utils.js"]},"searchresult:widget/pagelets/base/topRs/topRs.js":{"url":"//img1.bdstatic.com/static/searchresult/widget/pagelets/base/topRs/topRs_c41d15e.js","deps":["common:widget/ui/base/base.js","common:widget/ui/utils/utils.js"]},"common:widget/ui/historyRecord/historyRecord.js":{"url":"//img2.bdstatic.com/static/common/widget/ui/historyRecord/historyRecord_31e31e1.js","deps":["common:widget/ui/base/base.js","common:widget/ui/base/events.js"]},"searchresult:widget/flip/flip_model.js":{"url":"//img0.bdstatic.com/static/searchresult/widget/flip/flip_model_fd8d2a1.js"},"searchresult:widget/flip/app.js":{"url":"//img2.bdstatic.com/static/searchresult/widget/flip/app_dc66440.js","pkg":"searchresult:p10","deps":["common:widget/ui/base/base.js","searchresult:widget/ui/utils/utils.js","common:widget/ui/juicer/juicer.js","common:widget/ui/userInfo/userInfo.js","searchresult:widget/flip/flip_model.js","searchresult:widget/ui/controls/relsearchBox/relsearchBox.js","searchresult:widget/ui/controls/hotwordBox/hotwordBox.js","searchresult:widget/ui/statistic/statistic.js","searchresult:widget/pagelets/base/topInfoBar/topInfoBar.js"]},"common:widget/ui/fmCheck/fmCheck.js":{"url":"//img1.bdstatic.com/static/common/widget/ui/fmCheck/fmCheck_e6197fc.js","deps":["common:widget/ui/base/base.js"]},"common:widget/ui/durationStat/durationStat.js":{"url":"//img0.bdstatic.com/static/common/widget/ui/durationStat/durationStat_d292e9f.js","deps":["common:widget/ui/utils/utils.js","common:widget/ui/base/base.js"]}},"pkg":{"common:p1":{"url":"//img0.bdstatic.com/static/common/pkg/cores_936fb40.js"},"searchresult:p10":{"url":"//img0.bdstatic.com/static/searchresult/pkg/flip_f3905f0.js"}}});</script> 
<div id="search" class="">
<script>
        (function() {
            var search = document.getElementById('search');
            var width = window.innerWidth
                || (document.documentElement && document.documentElement.clientWidth)
                || (document.body && document.body.clientWidth);
            if (search && width < 1217) {
                search.className = 'narrow ' + search.className;
            }
        })();
    </script>
<div class="s_search">
<div id="imgSearchBox">
<div id="imgMainSearch">
<a href="/" class="s_logo">
<img src="//www.baidu.com/img/flexible/logo/pc/result@2.png" alt="到 百度图片首页 来" title="返回 百度图片首页">
</a>
<div class="s_nav">
<form action="/search/index" class="searchform" name="f1" onsubmit="return s_submit(this,true)">
<input type="hidden" name="tn" value="baiduimage">
<input type="hidden" name="ipn" value="r">
<input name="ct" type="hidden" value="201326592">
<input name="cl" type="hidden" value="2">
<input name="lm" type="hidden" value="-1">
<input name="st" type="hidden" value="-1">
<input name="fm" type="hidden" value="result">
<input name="fr" type="hidden" value="">
<input name="sf" type="hidden" value="1">
<input name="fmq" type="hidden" value="">
<input name="pv" type="hidden" value="">
<input name="ic" type="hidden" value="0">
<input name="nc" type="hidden" value="1">
<input name="z" type="hidden" value="0">
<input name="hd" type="hidden" value="0">
<input name="latest" type="hidden" value="0">
<input name="copyright" type="hidden" value="0">
<input name="se" type="hidden" value="">
<input name="showtab" type="hidden" value="0">
<input name="fb" type="hidden" value="0">
<input name="width" type="hidden" value="">
<input name="height" type="hidden" value="">
<input name="face" type="hidden" value="0">
<input name="istype" type="hidden" value="2">
<input name="ie" type="hidden" value="utf-8">
<input name="ctd" type="hidden" value="">
<input name="sid" type="hidden" value="">
<span class="s_ipt_wr"><input id="kw" name="word" class="s_ipt" value="老人摔倒" autocomplete="off" onfocus="this.parentNode.className='s_ipt_wr active'" onblur="this.parentNode.className='s_ipt_wr'"/></span><span class="s_btn_wr"><input type="submit" class="s_btn" onmousedown="this.className='s_btn s_btn_h'" onmouseout="this.className='s_btn'"  value="百度一下"   /></span>
</form><div id="stcontent" class="common-shitu"> <a class="sttb" hidefocus="true" id="sttb" href="javascript:void(0)" title="上传图片，搜索相关信息"> <img class="st_camera_off" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAAgY0hSTQAAeiYAAICEAAD6AAAAgOgAAHUwAADqYAAAOpgAABdwnLpRPAAAAqNJREFUaN7tWMtu1DAULeL1B2XBCgRL3j8APwBLxIblsCqbfkAH/qAJsROGne2CsuiyXY5gTVsJluUfAIlHRRkN9ySdiTMMtZ3JJIzqK1mKZnJ9z/E9vnbu0pI3b968Lbxxnl4MIvV4PRJd0wi5WsO78PkvwK/H6kHAxE8CN3Qb8kfIxP12wTN1h4AcuoMfkzh8kYjbrYBPkvdng0h+GIE5eu5aDSY+6n5pmp5rnEDA5DNtNb8xpi7b+uJd+BT+6nmz4OM3N0j3v8YAmFxxl59c0aUU8Ne3agfa7/fPQKOk9Y4ugSAS+2MJMPluOByecp0bPgT8bTGP+FSWGcWkPQYMlcAztnGdAuyZKkkcq6tVFyh6lV4h4N8NMfaAxRk8rfLBcRPT5vtK2r03a5ZDLu7mcx0XSxxYk0DKJlb+M1WNpHQQxeIR55vL9R2Em8uYE3NrlSrJYmuZsJJTXtsL8GEvveQKqNfbuBBG8mHA5SoGnvGbc3YodokEYbMh0CkcROJUnaiSULq3yXcwRQoD/Be9VDfdqlWWiVxKXDwxO+QpHAXt2oNXT6ki/TadvngH71oTcMVThQAA/QUykjvZ6tHA8yQ5WxJzJ5DJRgOHq8G0QymXl3b1yDJhPrzmTyDXfAF+a+v8P9+l/8r3J7HdKgFUltGGtV3RiYwNTNVprgRQHrXV37He8NgfR36YozUCqPFVSm65NMpVT+DESmjhN/HCl9FZDzKbe5G/SpyIy5zLddr1471RAnV/0LRGoNbunzOBGb7I5tO+LE5tYDM6ZH2gYsN9cem41W2IDQwjPFZ91DRNTwdM7Ook9K5EYwPlVwMPTMBm1w1I5DVTX6jJASzA5NbSAAktE62BJwzO4HU5TeuNNiMh1UFsa9l48+bNm7cq9gfmr6wmxprr4wAAAABJRU5ErkJggg==" width="24" height="24"> <img class="st_camera_on" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAAgY0hSTQAAeiYAAICEAAD6AAAAgOgAAHUwAADqYAAAOpgAABdwnLpRPAAAAphJREFUaN7tWMtuEzEULeL1B7BgBYIljzhpK1iVJRtYVYjNeNJWgU3Z8AEE/iK/wA90DfsUCZb0HyhSCxW2dblnKiZ3otCxJ5MZovpKlkaJr32OfXz8WFmJESNGjKWPhwnd6GmbqNQMS0vi3qIucv4L8L2+faa0/dVJDIUUldifHW2ftgpeaeoyEBMKXpAw3T6pVsB3B3RZafMlB8PfXhLKZGS+yrzNIV1pnEBHm3eT0bRHq1t0yzcXdZEjZuN9o+DXtug+6/53DiB1u8EDwDlSSr1t6tQOdGNIl6BRpd2gKAH7TUjgExFdCG0bOZz7cdKOPSj0gT55jQFDtQWa0D2WyecyJ1lP6U5lE9im2wz8+MzFzhiApQJ4e1IC/kc3MY/ntuHUbKCts0nYE28SmLLCyGv7nUdpNLURvXj0iq7VJVW0hTbR9kRCdoS+5Ux4yQm6k+DXduhmKKD1Hbqu+vZ5V7s3KPjGb8FmwX1LEsDmQcANxMIaBcmBnYRz9rhTN0MGDv+tpvQgbLPkmchl616WJ/D05Qn87b2xafeatWw9dl+Lut4EQvFUIQBA0yDZIsfZ2skKf0+R8yWxcAKZbAQ4HA1mbUqn8hJHD87x2bwWTiDTvAD/ZJeu/qsu/iuen+xeqwTgLH8XrO+IFmaMc8vcaaEEYI9i9Mf+zmLGeR630RoBeHwVy5XWiDYigXMroaVfxEtvo/NuZD7noniUOBeHuZDjdOjlvVECdV9oWiNQ6+tfMIE5bmSLeb4UNzLGVr4Y+6QEgcOQF7e6A30DQ+5cPu+omx/ookrMviRReJVoqpxa8OHEvcw+sPlZYkp3y96FGi2MBZjCXp85Qc5EWwUYgsFLOc18G21EQm6Avr1lEyNGjBgxqsQfpdcIhlb9ZYwAAAAASUVORK5CYII=" width="24" height="24"> <div class="st_tips" id="stTipsBox">按图片搜索</div> </a> <div id="stsug" class="stsug" style="display:none"> <div id="sthead"><span>识图</span><img id="sthelp" width="13" height="13" src="//img2.bdstatic.com/static/common/widget/shitu/images/mark_cac9c0b.png" /></div> <div class="stf"> <form id="form2" target="_self" enctype="multipart/form-data" name="form2"> <a id="uploadImg" href="javascript:void(0)" data-nsclick="p=1811102&tn=index&event_type=shitu.search.click&pos=upload">本地上传<input type="file" name="image" id="stfile" size="2"></a> <div class="st_dragtg" id="dragtg" style="display:none;">提示：您也可以把图片拖到这里</div> <input id="shitu2" name="pos" value="" type="hidden"> <input name="uptype" value="upload_pc" type="hidden"> <input name="fm" value="index" type="hidden"> </form> <form id="form1" target="_self" enctype="multipart/form-data" method="get" name="form1"> <div id="sturl"> <span class="stuwr"> <input type="text" id="stuurl" placeholder="在此处粘贴图片网址" value="" autocomplete="off"  class="stuurl" name="objurl"> </span> <span class="stsb"> <input type="submit" id="sbobj" class="stsb2" onmousedown="this.className='stsb2 stsb3'" onmouseout="this.className='stsb2'" onmouseover="this.className='stsb2 stsb4'" value="识图一下"> </span> </div> <input name="filename" id="filename" value="" type="hidden"> <input name="rt" value="0" type="hidden"> <input name="rn" value="10" type="hidden"> <input id="stftn" name="ftn" value="wantu" type="hidden"> <input name="ct" value="1" type="hidden"> <input name="stt" value="0" type="hidden"> <input name="tn" value="shituresultpc" type="hidden"> <input id="shitu1" name="uptype" value="paste" type="hidden"> <input name="fm" value="index" type="hidden"> </form> </div> <div class="drag-text-tip" id="dttip">拖拽图片到此处试试</div> <div id="stmore" style="display:none;"> <div class="stmore-header">百度识图</div> <ul> <li>识别人物、搜索服饰、寻找高清素材、浏览相似美图，尽在百度识图!</li> </ul> <div class="stmore_arrow_in"></div> <div class="stmore_arrow_out"></div> </div> <a id="closest" href="javascript:void(0);" title="关闭"></a> <div id="point" style="display:none;"> <img src="//img1.bdstatic.com/img/image/shitu/feimg/uploading.gif" /><span>正在识别中，请稍候...</span> <a id="cancelst" href="javascript:void(0);" title="取消"></a> </div> <div class="undrag-text-tip" id="undragtip"> <p>抱歉，Safari不支持拖拽识图。<br/> 请保存图片到本地，通过本地上传或在搜索框粘贴图片url进行识图。</p> </div> <div class="undrag-text-tip" id="untip"> <p>IE9及以下版本浏览器不支持识图功能，<br/> 请升级浏览器或使用Chrome、QQ、搜狗浏览器进行识图</p> </div> <div id="dragtip" style="display:none;"> <span>请拖拽图片到此处</span> <div class="drag_dot_area drag_dot_left_top"></div> <div class="drag_dot_area drag_dot_left_bottom"></div> <div class="drag_dot_area drag_dot_right_top"></div> <div class="drag_dot_area drag_dot_right_bottom"></div> <a id="cancelst" href="javascript:void(0);" title="取消"></a> </div> <div class="left-border"></div> <div class="right-border"></div> </div> <div id="mock-stsug"></div> <script>
        /***
        * 识图渠道号。
        */
        window['__abbaidu_2033_subidgetf'] = function () {
            var subid = 'shitu_pc';
            return subid;
        };
    </script> <script>
        window['__abbaidu_2033_cb'] = function (responseData) {
            window.sdkParams = responseData;
        };
    </script> <script async="" src="https://dlswbr.baidu.com/heicha/mw/abclite-2033-s.js"></script> </div>  </div>
<div id='userInfo'>
<a target='_blank' href='http://www.baidu.com/'>百度首页</a>
</div>
</div>
</div>
</div>
<div id="pageLayoutTipWindow">
<div class="page-layouttip-banner">
<div class="page-layouttip-describe">温馨提示：由于您的浏览器安装了某些插件，导致页面布局失败，重新加载可恢复布局</div>
<div class="page-layouttip-loadbtn">重新加载</div>
<div class="page-layouttip-viewbtn">继续查看</div>
</div>
</div><script>
var commonHeaderConf = {
	sugProdName: "image",
	searchInputId: "kw"
};
void function(w){
	window.setHeadUrl= function(o){
		var links = {
		i_news:['word','https://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&fr=image&ie=utf-8',1],
        i_webpage:['wd','https://www.baidu.com/s?ie=utf-8',1],
		i_tieba:['kw','http://tieba.baidu.com/f?ie=utf-8',1],
		i_zhidao:['word','http://zhidao.baidu.com/q?ct=17&pn=0&tn=ikaslist&rn=10&lm=0&ie=utf-8',1],
		i_b2b:['q','https://b2b.baidu.com/s?fr=img&ie=utf-8',1],
		i_video:['wd','https://www.baidu.com/sf/vsearch?pd=video&tn=vsearch&ie=utf-8&wrsv_spt=10',1],
		i_map:['wd','http://map.baidu.com/?newmap=1&ie=utf-8&s=s',2],
		i_baike:['word','http://baike.baidu.com/search/word?pic=1&sug=1&enc=utf8',1],
		i_wenku:['word','http://wenku.baidu.com/search?ie=utf-8',1]
		},
		name = o.name,
		items = links[name],
		kw = document.getElementById(w),
		reg = new RegExp('^\\s+|\\s+\x24'),
		key = kw.value.replace(reg,'');
		if(items){
			if(key.length > 0){
				var wd = items[0],
					url = items[1],
					proSign = items[2];
				url = pro(url,wd,key,proSign);
				o.href = url;

			}else{
				o.href = o.href.match(new RegExp('^http:\/\/.+\\.baidu\\.com'))[0];
			}
            if(!o.clickHandle){
                o.onclick = function(e){
                    if(typeof p === 'function'){
                        e = e || window.event;
                        p(e, 52, {isAsyn : true, to : this.name, href : this.href});
                    }

                };
                o.clickHandle = true;
            }
		}
		function pro(url,wd,key,proSign){
			/*日文片假部分乱码\u30f7--\u30fb,转换成实体*/
			function HtmlEncodeAndComponent(inTXT){
				/*地图，uri编码，不转换成实体*/
				if(proSign==2){
					return encodeURIComponent(key);
				}
				var hexArray =[],entityCode = '',finalKey = '', character='',tmpInt=0;
				for(i=0; i<inTXT.length; i++){
					character = inTXT.charCodeAt(i).toString(16).toUpperCase();
					tmpInt = parseInt(character,16);
					if(tmpInt>=0x30f7&&tmpInt<=0x30fb){
						decCode = tmpInt.toString(10);
						entityCode = '&#'+decCode+';';
						finalKey += encodeURIComponent(entityCode);

					}else{
						entityCode = inTXT.charAt(i);
						if(proSign>0){
							finalKey += encodeURIComponent(entityCode);
						}else{
							finalKey += entityCode;
						}
					}
				}
				return finalKey;
			}
			var prefix = (url.indexOf('?')>0?'&':'?') + wd +'=';
			if(proSign == 2){
				prefix = encodeURIComponent(prefix);
			}
			key = HtmlEncodeAndComponent(key);
			return url + prefix + key;
		}
	}
}(commonHeaderConf.searchInputId);
</script>
<div class="s_tab" id="bdpcImgTab">
<div id="bdpcImgTopTab">
<a class="s_tab_item s_tab_webpage" href="https://www.baidu.com/"  onmousedown="setHeadUrl(this)" name="i_webpage" >网页</a>
<a class="s_tab_item s_tab_news" href="http://news.baidu.com/" onmousedown="setHeadUrl(this)" name="i_news">资讯</a>
<a class="s_tab_item s_tab_video" href="http://www.baidu.com/" onmousedown="setHeadUrl(this)" name="i_video" >视频</a>
<b class="s_tab_item s_tab_img">图片</b>
<a class="s_tab_item s_tab_zhidao" href="http://zhidao.baidu.com/" onmousedown="setHeadUrl(this)" name="i_zhidao" >知道</a>
<a class="s_tab_item s_tab_wenku" href="http://wenku.baidu.com/" onmousedown="setHeadUrl(this)" name="i_wenku">文库</a>
<a class="s_tab_item s_tab_tieba" href="http://tieba.baidu.com/" onmousedown="setHeadUrl(this)" name="i_tieba">贴吧</a>
<a class="s_tab_item s_tab_b2b" href="https://b2b.baidu.com/" onmousedown="setHeadUrl(this)" name="i_b2b">采购</a>
<a class="s_tab_item s_tab_map" href="http://map.baidu.com/" onmousedown="setHeadUrl(this)" name="i_map" >地图</a>
<a class="s_tab_item s_tab_more" href="https://www.baidu.com/more/" onmousedown="setHeadUrl(this)" name="i_more">更多</a>
</div>
</div>
<script>
	var imgMainSearch = document.getElementById('imgMainSearch');
    var imgSearchBox = document.getElementById('imgSearchBox');
	var bdpcImgTab = document.getElementById('bdpcImgTab');
	var bdpcImgTopTab = document.getElementById('bdpcImgTopTab');
	
	var setSearchStyle = function (flag) {
		var winWidth = window.innerWidth
		|| (document.documentElement && document.documentElement.clientWidth)
		|| (document.body && document.body.clientWidth);
		if (imgMainSearch && imgSearchBox && bdpcImgTab && bdpcImgTopTab && winWidth > 1920) {
			bdpcImgTab.className = 's_tab s_img_tab';
		    bdpcImgTopTab.className = 's_imgtop_tab';
		    imgMainSearch.className = 's_img_search';
	        imgSearchBox.className = 's_img_search_out';
		} else if (flag) {
        	imgMainSearch.className = '';
            imgSearchBox.className = '';
            bdpcImgTab.className = 's_tab';
	    	bdpcImgTopTab.className = '';
        }
	};

	setSearchStyle();

	window.onresize = function () {
		setSearchStyle(1);
    };
</script>
<div id="topInfoBar">
<div id="resultInfo" style="font-size: 13px;">找到相关图片约112,000张</div>
<div id="newImgFilter">
<div class="new-filter-container filter">
<div id="typeFilter" class="typeFilter"></div>
<div id="sizeFilter" class="subFilter sizeFilter"></div>
<div id="colorFilter" class="subFilter"></div>
</div>
</div><div id="topRS">
<em class="pull-rs-title">相关搜索：</em><a class="pull-rs" title="查看 老人住院"  target="_self"  href="/search/index?ct=201326592&cl=2&st=-1&lm=-1&nc=1&ie=utf-8&tn=baiduimage&ipn=r&rps=1&pv=&fm=rs1&word=%E8%80%81%E4%BA%BA%E4%BD%8F%E9%99%A2&hs=0&oriquery=%25E8%2580%2581%25E4%25BA%25BA%25E6%2591%2594%25E5%2580%2592&ofr=%25E8%2580%2581%25E4%25BA%25BA%25E6%2591%2594%25E5%2580%2592&sensitive=0">老人住院</a><a class="pull-rs" title="查看 老人受伤"  target="_self"  href="/search/index?ct=201326592&cl=2&st=-1&lm=-1&nc=1&ie=utf-8&tn=baiduimage&ipn=r&rps=1&pv=&fm=rs1&word=%E8%80%81%E4%BA%BA%E5%8F%97%E4%BC%A4&hs=0&oriquery=%25E8%2580%2581%25E4%25BA%25BA%25E6%2591%2594%25E5%2580%2592&ofr=%25E8%2580%2581%25E4%25BA%25BA%25E6%2591%2594%25E5%2580%2592&sensitive=0">老人受伤</a><a class="pull-rs" title="查看 老人骑车摔倒"  target="_self"  href="/search/index?ct=201326592&cl=2&st=-1&lm=-1&nc=1&ie=utf-8&tn=baiduimage&ipn=r&rps=1&pv=&fm=rs1&word=%E8%80%81%E4%BA%BA%E9%AA%91%E8%BD%A6%E6%91%94%E5%80%92&hs=0&oriquery=%25E8%2580%2581%25E4%25BA%25BA%25E6%2591%2594%25E5%2580%2592&ofr=%25E8%2580%2581%25E4%25BA%25BA%25E6%2591%2594%25E5%2580%2592&sensitive=0">老人骑车摔倒</a><a class="pull-rs" title="查看 老奶奶摔倒了"  target="_self"  href="/search/index?ct=201326592&cl=2&st=-1&lm=-1&nc=1&ie=utf-8&tn=baiduimage&ipn=r&rps=1&pv=&fm=rs1&word=%E8%80%81%E5%A5%B6%E5%A5%B6%E6%91%94%E5%80%92%E4%BA%86&hs=0&oriquery=%25E8%2580%2581%25E4%25BA%25BA%25E6%2591%2594%25E5%2580%2592&ofr=%25E8%2580%2581%25E4%25BA%25BA%25E6%2591%2594%25E5%2580%2592&sensitive=0">老奶奶摔倒了</a><a class="pull-rs" title="查看 老人摔倒 真实"  target="_self"  href="/search/index?ct=201326592&cl=2&st=-1&lm=-1&nc=1&ie=utf-8&tn=baiduimage&ipn=r&rps=1&pv=&fm=rs1&word=%E8%80%81%E4%BA%BA%E6%91%94%E5%80%92+%E7%9C%9F%E5%AE%9E&hs=0&oriquery=%25E8%2580%2581%25E4%25BA%25BA%25E6%2591%2594%25E5%2580%2592&ofr=%25E8%2580%2581%25E4%25BA%25BA%25E6%2591%2594%25E5%2580%2592&sensitive=0">老人摔倒 真实</a><a class="pull-rs" title="查看 老人摔倒讹人"  target="_self"  href="/search/index?ct=201326592&cl=2&st=-1&lm=-1&nc=1&ie=utf-8&tn=baiduimage&ipn=r&rps=1&pv=&fm=rs1&word=%E8%80%81%E4%BA%BA%E6%91%94%E5%80%92%E8%AE%B9%E4%BA%BA&hs=0&oriquery=%25E8%2580%2581%25E4%25BA%25BA%25E6%2591%2594%25E5%2580%2592&ofr=%25E8%2580%2581%25E4%25BA%25BA%25E6%2591%2594%25E5%2580%2592&sensitive=0">老人摔倒讹人</a><a class="pull-rs" title="查看 医院老人"  target="_self"  href="/search/index?ct=201326592&cl=2&st=-1&lm=-1&nc=1&ie=utf-8&tn=baiduimage&ipn=r&rps=1&pv=&fm=rs1&word=%E5%8C%BB%E9%99%A2%E8%80%81%E4%BA%BA&hs=0&oriquery=%25E8%2580%2581%25E4%25BA%25BA%25E6%2591%2594%25E5%2580%2592&ofr=%25E8%2580%2581%25E4%25BA%25BA%25E6%2591%2594%25E5%2580%2592&sensitive=0">医院老人</a><a class="pull-rs" title="查看 扶老人卡通"  target="_self"  href="/search/index?ct=201326592&cl=2&st=-1&lm=-1&nc=1&ie=utf-8&tn=baiduimage&ipn=r&rps=1&pv=&fm=rs1&word=%E6%89%B6%E8%80%81%E4%BA%BA%E5%8D%A1%E9%80%9A&hs=0&oriquery=%25E8%2580%2581%25E4%25BA%25BA%25E6%2591%2594%25E5%2580%2592&ofr=%25E8%2580%2581%25E4%25BA%25BA%25E6%2591%2594%25E5%2580%2592&sensitive=0">扶老人卡通</a><a class="pull-rs" title="查看 老人摔倒卡通图片"  target="_self"  href="/search/index?ct=201326592&cl=2&st=-1&lm=-1&nc=1&ie=utf-8&tn=baiduimage&ipn=r&rps=1&pv=&fm=rs1&word=%E8%80%81%E4%BA%BA%E6%91%94%E5%80%92%E5%8D%A1%E9%80%9A%E5%9B%BE%E7%89%87&hs=0&oriquery=%25E8%2580%2581%25E4%25BA%25BA%25E6%2591%2594%25E5%2580%2592&ofr=%25E8%2580%2581%25E4%25BA%25BA%25E6%2591%2594%25E5%2580%2592&sensitive=0">老人摔倒卡通图片</a><a class="pull-rs" title="查看 老人中风"  target="_self"  href="/search/index?ct=201326592&cl=2&st=-1&lm=-1&nc=1&ie=utf-8&tn=baiduimage&ipn=r&rps=1&pv=&fm=rs1&word=%E8%80%81%E4%BA%BA%E4%B8%AD%E9%A3%8E&hs=0&oriquery=%25E8%2580%2581%25E4%25BA%25BA%25E6%2591%2594%25E5%2580%2592&ofr=%25E8%2580%2581%25E4%25BA%25BA%25E6%2591%2594%25E5%2580%2592&sensitive=0">老人中风</a><a class="pull-rs" title="查看 扶起老人"  target="_self"  href="/search/index?ct=201326592&cl=2&st=-1&lm=-1&nc=1&ie=utf-8&tn=baiduimage&ipn=r&rps=1&pv=&fm=rs1&word=%E6%89%B6%E8%B5%B7%E8%80%81%E4%BA%BA&hs=0&oriquery=%25E8%2580%2581%25E4%25BA%25BA%25E6%2591%2594%25E5%2580%2592&ofr=%25E8%2580%2581%25E4%25BA%25BA%25E6%2591%2594%25E5%2580%2592&sensitive=0">扶起老人</a><a class="pull-rs" title="查看 冬天摔倒"  target="_self"  href="/search/index?ct=201326592&cl=2&st=-1&lm=-1&nc=1&ie=utf-8&tn=baiduimage&ipn=r&rps=1&pv=&fm=rs1&word=%E5%86%AC%E5%A4%A9%E6%91%94%E5%80%92&hs=0&oriquery=%25E8%2580%2581%25E4%25BA%25BA%25E6%2591%2594%25E5%2580%2592&ofr=%25E8%2580%2581%25E4%25BA%25BA%25E6%2591%2594%25E5%2580%2592&sensitive=0">冬天摔倒</a><a class="pull-rs" title="查看 摔倒卡通"  target="_self"  href="/search/index?ct=201326592&cl=2&st=-1&lm=-1&nc=1&ie=utf-8&tn=baiduimage&ipn=r&rps=1&pv=&fm=rs1&word=%E6%91%94%E5%80%92%E5%8D%A1%E9%80%9A&hs=0&oriquery=%25E8%2580%2581%25E4%25BA%25BA%25E6%2591%2594%25E5%2580%2592&ofr=%25E8%2580%2581%25E4%25BA%25BA%25E6%2591%2594%25E5%2580%2592&sensitive=0">摔倒卡通</a><a class="pull-rs" title="查看 人摔倒"  target="_self"  href="/search/index?ct=201326592&cl=2&st=-1&lm=-1&nc=1&ie=utf-8&tn=baiduimage&ipn=r&rps=1&pv=&fm=rs1&word=%E4%BA%BA%E6%91%94%E5%80%92&hs=0&oriquery=%25E8%2580%2581%25E4%25BA%25BA%25E6%2591%2594%25E5%2580%2592&ofr=%25E8%2580%2581%25E4%25BA%25BA%25E6%2591%2594%25E5%2580%2592&sensitive=0">人摔倒</a><a class="pull-rs" title="查看 老人卡通"  target="_self"  href="/search/index?ct=201326592&cl=2&st=-1&lm=-1&nc=1&ie=utf-8&tn=baiduimage&ipn=r&rps=1&pv=&fm=rs1&word=%E8%80%81%E4%BA%BA%E5%8D%A1%E9%80%9A&hs=0&oriquery=%25E8%2580%2581%25E4%25BA%25BA%25E6%2591%2594%25E5%2580%2592&ofr=%25E8%2580%2581%25E4%25BA%25BA%25E6%2591%2594%25E5%2580%2592&sensitive=0">老人卡通</a></div>
<div id="timeliness" class="hotpot-container">
</div>
<script type="text/juicer" id="timeliness-tpl">
    <div id="timeliness-bless">
        <div class="blessing-img-wrapper">
            <img class="blessing-img" src="${icon.normal}" alt="" />
            <img class="blessing-img icon-zoomup" src="${icon.normal}" alt="" />
        </div>
        <span class="blessing-content">
            ${title}
        </span>
        <div class="blessing-count-wrapper">
            (<span class="blessing-count"></span>人)
        </div>
    </div>
    <div class="egg">
        <img class="blessing-img-egg" src="${egg}" alt="" />
    </div>
</script>
</div>
<div id="specialQuery"></div>
<div id="browser-hotword"></div>

</div>
 
<div id="wrapper">
<div id="imgContainer" >
<div id="pnlBeforeImgList">
</div>
<div id="specialRecommend"></div>
<div id="imgid"></div>
</div>
<div style="clear:both;"></div>
<div id="page">
<strong><span class="pc">1</span></strong>
<a href="/search/flip?tn=baiduimage&ie=utf-8&word=%E8%80%81%E4%BA%BA%E6%91%94%E5%80%92&pn=20&gsm=3c&ct=&ic=0&lm=-1&width=0&height=0"><span class="pc" data="right">2</span></a>
<a href="/search/flip?tn=baiduimage&ie=utf-8&word=%E8%80%81%E4%BA%BA%E6%91%94%E5%80%92&pn=40&gsm=0&ct=&ic=0&lm=-1&width=0&height=0"><span class="pc" data="right">3</span></a>
<a href="/search/flip?tn=baiduimage&ie=utf-8&word=%E8%80%81%E4%BA%BA%E6%91%94%E5%80%92&pn=60&gsm=0&ct=&ic=0&lm=-1&width=0&height=0"><span class="pc" data="right">4</span></a>
<a href="/search/flip?tn=baiduimage&ie=utf-8&word=%E8%80%81%E4%BA%BA%E6%91%94%E5%80%92&pn=80&gsm=0&ct=&ic=0&lm=-1&width=0&height=0"><span class="pc" data="right">5</span></a>
<a href="/search/flip?tn=baiduimage&ie=utf-8&word=%E8%80%81%E4%BA%BA%E6%91%94%E5%80%92&pn=100&gsm=0&ct=&ic=0&lm=-1&width=0&height=0"><span class="pc" data="right">6</span></a>
<a href="/search/flip?tn=baiduimage&ie=utf-8&word=%E8%80%81%E4%BA%BA%E6%91%94%E5%80%92&pn=120&gsm=0&ct=&ic=0&lm=-1&width=0&height=0"><span class="pc" data="right">7</span></a>
<a href="/search/flip?tn=baiduimage&ie=utf-8&word=%E8%80%81%E4%BA%BA%E6%91%94%E5%80%92&pn=140&gsm=0&ct=&ic=0&lm=-1&width=0&height=0"><span class="pc" data="right">8</span></a>
<a href="/search/flip?tn=baiduimage&ie=utf-8&word=%E8%80%81%E4%BA%BA%E6%91%94%E5%80%92&pn=160&gsm=0&ct=&ic=0&lm=-1&width=0&height=0"><span class="pc" data="right">9</span></a>
<a href="/search/flip?tn=baiduimage&ie=utf-8&word=%E8%80%81%E4%BA%BA%E6%91%94%E5%80%92&pn=180&gsm=0&ct=&ic=0&lm=-1&width=0&height=0"><span class="pc" data="right">10</span></a>
<a href="/search/flip?tn=baiduimage&ie=utf-8&word=%E8%80%81%E4%BA%BA%E6%91%94%E5%80%92&pn=20&gsm=3c&ct=&ic=0&lm=-1&width=0&height=0" class="n">下一页</a>
<div class="goto">
<span>到第</span>
<input type="text" class="pn">
<span>页</span>
<a href="javascript:;" class="n gotobtn">确定</a>
</div>
</div><div id="pnlAfterContent" style="display:none">
<div id="cmsimage">
<div id="hotWordDiv"></div>
</div>
</div>
</div>
<script>
    window.alogObjectConfig = {
        product: '11',
        page: '2', 
        speed_page: '2',  
 
        speed: {
            sample: '0.01'   
        },
 
       
        monkey: {
            sample: '0.01'   
        },
 
        exception: { 
            sample: '0.01' 
        },
 
        feature: {
            sample: '0.01'
        },
 
        
        cus: {
            sample: '0.01' 
        },
 
        csp: {
            sample: '0.01',
            'default-src': [
                {match: '*bae.baidu.com', target: 'Accept,Warn'},
                {match: '*.baidu.com,*.bdstatic.com,*.bdimg.com,localhost,*.hao123.com,*.hao123img.com', target: 'Accept'},
                {match: /^(127|172|192|10)(\.\d+){3}$/, target: 'Accept'},
                {match: '*', target: 'Accept,Warn'}
            ]
        }
    };
 
    // pc和mobile端会稍有不同，必须严格按照该文档来部署，该段代码必须放在上面的window.alogObjectConfig配置之后
    void function(a,b,c,d,e,f,g){a.alogObjectName=e,a[e]=a[e]||function(){(a[e].q=a[e].q||[]).push(arguments)},a[e].l=a[e].l||+new Date,d="https:"===a.location.protocol?"https://fex.bdstatic.com"+d:"http://fex.bdstatic.com"+d;var h=!0;if(a.alogObjectConfig&&a.alogObjectConfig.sample){var i=Math.random();a.alogObjectConfig.rand=i,i>a.alogObjectConfig.sample&&(h=!1)}h&&(f=b.createElement(c),f.async=!0,f.src=d+"?v="+~(new Date/864e5)+~(new Date/864e5),g=b.getElementsByTagName(c)[0],g.parentNode.insertBefore(f,g))}(window,document,"script","/hunter/alog/alog.min.js","alog"),void function(){function a(){}window.PDC={mark:function(a,b){alog("speed.set",a,b||+new Date),alog.fire&&alog.fire("mark")},init:function(a){alog("speed.set","options",a)},view_start:a,tti:a,page_ready:a}}();
    void function(n){var o=!1;n.onerror=function(n,e,t,c){var i=!0;return!e&&/^script error/i.test(n)&&(o?i=!1:o=!0),i&&alog("exception.send","exception",{msg:n,js:e,ln:t,col:c}),!1},alog("exception.on","catch",function(n){alog("exception.send","exception",{msg:n.msg,js:n.path,ln:n.ln,method:n.method,flag:"catch"})})}(window);
</script>  <script>
    void function(e,t){for(var n=t.getElementsByTagName("img"),a=+new Date,i=[],o=function(){this.removeEventListener&&this.removeEventListener("load",o,!1),i.push({img:this,time:+new Date})},s=0;s< n.length;s++)!function(){var e=n[s];e.addEventListener?!e.complete&&e.addEventListener("load",o,!1):e.attachEvent&&e.attachEvent("onreadystatechange",function(){"complete"==e.readyState&&o.call(e,o)})}();alog("speed.set",{fsItems:i,fs:a})}(window,document);
</script> 
 <a id="common-back-top" href="javascript:;" data-title="返回顶部"> <div class="btn-inner-text"></div> </a> <a href="javascript:;" id="common-feedback-link" data-title="反馈图片"> <div class="common-feedback-text">反馈</div> </a> <img style="display:none;" src="//imgstat.baidu.com/4.gif?pv=flip&time=1617797150">
 
<script>
        var Hunter = window.Hunter || {};
        Hunter.userConfig = Hunter.userConfig || [];
        Hunter.userConfig.push({
            hid: 36991
        });
    </script>
                    <script>
    void function(a,b,c,d,e,f){function g(b){a.attachEvent?a.attachEvent("onload",b,!1):a.addEventListener&&a.addEventListener("load",b)}function h(a,c,d){d=d||15;var e=new Date;e.setTime((new Date).getTime()+1e3*d),b.cookie=a+"="+escape(c)+";path=/;expires="+e.toGMTString()}function i(a){var c=b.cookie.match(new RegExp("(^| )"+a+"=([^;]*)(;|$)"));return null!=c?unescape(c[2]):null}function j(){var a=i("PMS_JT");if(a){h("PMS_JT","",-1);try{a=a.match(/{["']s["']:(\d+),["']r["']:["']([\s\S]+)["']}/),a=a&&a[1]&&a[2]?{s:parseInt(a[1]),r:a[2]}:{}}catch(c){a={}}a.r&&b.referrer.replace(/#.*/,"")!=a.r||alog("speed.set","wt",a.s)}}if(a.alogObjectConfig){var k=a.alogObjectConfig.sample,l=a.alogObjectConfig.rand;d="https:"===a.location.protocol?"https://fex.bdstatic.com"+d:"http://fex.bdstatic.com"+d,k&&l&&l>k||(g(function(){alog("speed.set","lt",+new Date),e=b.createElement(c),e.async=!0,e.src=d+"?v="+~(new Date/864e5)+~(new Date/864e5),f=b.getElementsByTagName(c)[0],f.parentNode.insertBefore(e,f)}),j())}}(window,document,"script","/hunter/alog/dp.min.js");
</script>   </body><script type="text/javascript"  src="//img0.bdstatic.com/static/common/widget/ui/base/base_a66ce51.js" ></script>
<script type="text/javascript"  src="//img0.bdstatic.com/static/common/pkg/cores_936fb40.js" ></script>
<script type="text/javascript"  src="//img1.bdstatic.com/static/common/widget/ui/browser-storage/browser-storage_ad6bd42.js" ></script>
<script type="text/javascript"  src="//img1.bdstatic.com/static/common/widget/verificationCode/useAIVerificationCode_fe7964c.js" ></script>
<script type="text/javascript"  src="//img1.bdstatic.com/static/common/widget/ui/juicer/juicer_59c3d50.js" ></script>
<script type="text/javascript"  src="//img1.bdstatic.com/static/searchresult/pkg/result_62fa15f.js" ></script>
<script type="text/javascript">!function(){    window.tn = 'result';
    window.vsid = '10ff4e48ad8ab5acc0d249b74e2c15b8860e603f';
    if ('index' === window.tn
        || 'result' === window.tn
        || 'detail' === window.tn) {
        var sttb = document.getElementById('sttb');
        sttb.removeAttribute && sttb.removeAttribute('title');
    }
    /**
     * 统计代码
    **/
    window.ss = function(){
        var URL = '//imgstat.baidu.com/9.gif?rainbow=1&';
        function request(url){
            var seed = Math.random();
            var img = window[seed] = new Image;
            img.onload = img.onerror = function(){
                window[seed] = null;
                img.onload = img.onerror = null;
                img = null;
            };
            img.src = url;
        }

        /* p = 0, 首页八张demo图片点击统计
         * p = 1, 结果页tab相关： name=stu相同tab显示；name=face 人脸搜索tab显示; type=show展现；type=click点击
         * p = pv, 结果页PV统计：data=1，有结果；data=0无结果；data=-1，down页面
         **/

        return function(arg, url, e){
            var s = URL + json2Query(arg) + '&' + Math.random();
            request(s);
            if(url){
                setTimeout(function(){
                    location.href = url;
                }, 300);
                e = e || window.event;
                if(e){
                    if(e.preventDefault){
                        e.preventDefault();
                    }else{
                        e.returnValue = false;
                    }
                }

            }
        };

    }();
    window.__originTitle = document.title;
    function json2Query(json){
        if(json == null || typeof json != 'object') return json;
        var query = [];
        for(var i in json){
            if(i != '')
                query[query.length] = i + '=' + json[i];
        }
        return query.join('&');
    }

    require.async(["common:widget/ui/base/base","common:widget/shitu/run"],function($, shitu){
        window.$ = $;
        $(document).ready(function() {
            var st = new shitu();
            st.init();
            window.stInstance = st;
        });
    });

}();
!function(){    require.async(["searchresult:widget/pagelets/base/topRs/topRs"],function(topRsClass){
        var topRs = new topRsClass();
        var changeFilter = false;
                    changeFilter = true;
                topRs.init({
            changeFilter: changeFilter
        });
    })
}();
!function(){    if (window.hotspotData) {
        require.async(['searchresult:widget/pagelets/base/timeliness/init'], function (Timeliness) {
            new Timeliness().init(window.hotspotData);
        });
    }
}();
!function(){/**
* isRefresh 用来判断禁止se或查询的参数是否生效,false表示无须清零，true表示需要清零
*/
require.async(["common:widget/ui/base/base","searchresult:widget/ui/utils/utils","common:widget/ui/historyRecord/historyRecord","common:widget/ui/utils/utils"],function( $, utils, HistoryRecord, commonUtils){

    window.s_submit = function(form,isRefresh){


//图片url检索跳转
var keyword = form.word.value;

if ($.trim(keyword).length > 0) {
    var historyRecord = new HistoryRecord({historyKey: 'indexPageSugList'});
    historyRecord.setRecord(keyword);
    $.cookie.set('cleanHistoryStatus', 0, {path: '/'});
}


var tiaoma = /^[\s]*http[s]*\:\/\/[\s\S]*\.[jpg|gif|png|bmp|jpeg]*[\s]*$/.test(keyword) ||/img5\.imgtn\.bdimg\.com/.test(keyword) || /mt1\.baidu\.com\/timg/.test(keyword);
var ajaxURL = 'https://graph.baidu.com/upload?image=' + encodeURIComponent(keyword) + '&range=imagePage&tn=pc&from=pc&image_source=PC_UPLOAD_IMAGE_ICONURL&extUiData%5bisLogoShow%5d=1';
var isIE6789 = $.browser.msie && ($.browser.version <= 9);

        if (tiaoma && !isIE6789) {
            // speed
            $.cookie('uploadTime', new Date().getTime(), {path: '/'});

            $.ajax({
                url: ajaxURL,
                type: 'post',
                success: function (response) {
                    if (response.status === 0) {
                        location.href = response.data.url;
                    } else if (response.status === 1002) {
                        alert('未找到该图片的详细信息，请上传其他图片');
                    } else {
                        alert('出错了！（规则未定）');
                    }
                },
                error: function () {
                    alert('网络问题，请稍候再试！');
                }
            });
           return false;
        }


        var searchConf = utils.query2Json(utils.escapeXSS(window.location.search.substring(1)));
        if(typeof searchConf.fm == "undefined"){searchConf.fm = '';}
        if(typeof searchConf.fmq == "undefined"){searchConf.fmq = '';}
        if(utils.trim(searchConf.queryWord) == form.word.value){
            form.fmq.value = utils.fmqValueSet();
        }else{
            var fmqDate = new Date();
            var T = fmqDate.getTime();
            if(searchConf.fmq.indexOf('m') > -1 && searchConf.fmq.indexOf('_m') == -1 && searchConf.fmq.indexOf('_R') == -1){
                var fmqvalue = searchConf.fmq;
                form.fmq.value = T + '_' +fmqvalue + '_R';
            }else{
                form.fmq.value =  T + '_R';
            }

        }
        var isflip = $('body').hasClass('flip');
        form.tn.value = "baiduimage";

        form.ct.value = "201326592";
        form.cl.value = "2";
        
        form.pv.value = "";
        form.action = "/search/index";

        // 新筛选，及未命中阿凡达筛选时，重新检索时需要记录筛选
                    form.z.value = commonUtils.getQueryValue('z');
            form.ic.value = commonUtils.getQueryValue('ic');
            form.lm.value = commonUtils.getQueryValue('lm');
            form.hd.value = commonUtils.getQueryValue('hd');
            form.latest.value = commonUtils.getQueryValue('latest');
            form.copyright.value = commonUtils.getQueryValue('copyright');
            form.width.value = commonUtils.getQueryValue('width');
            form.height.value = commonUtils.getQueryValue('height');
        
        if (window.canUseHttps) {
            form.action = 'https://' + window.location.host + '/search/index';
        }

        if(isflip) {
            form.action = "/search/flip";
        }
        if(isRefresh == true){
            // submit直接提交新query
            form.se.value = "1";
        }else{
            var showtab =  parseInt(searchConf.showtab);
            if(!isNaN(showtab)&&showtab>0){
                form.showtab.value = showtab;
            }
        }
        form.ctd.value = (+new Date()) + "^00_" + $(window).width() + "X" +  window.innerHeight;

        return true;
    }
})

}();
!function(){    require.async(['common:widget/ui/backtop/backTop']);

    require.async(['common:widget/ui/feedback/feedback'], function (feedback) {
        var callbacks = {};
        var containerId = 'common-feedback-link';
        feedback.init(callbacks, containerId);
    });
}();
!function(){    window._alaEnter && window._alaEnter !== true && window._alaEnter('sample');
    var sample = [];
    var keyValue = '';
    for(var name in sample) {
        keyValue +=  name + ':' + sample[name] + ',';
    }
    window.samplekey = keyValue.substr(0, keyValue.length - 1);
}();
!function(){    require.async(['searchresult:widget/flip/app'], function (flip) {
    flip.setData('pageInfo',{
    tpl: "flip",
    queryPageType : '0',
    gsm: '3c',
    logicPn: '0',
    listNum : "1688",
    dispNum : "112953",
    bdIsClustered : "1",
    frStr : "&fr=",
    sme : "0",
    ie : "utf-8",
    oe : "utf-8",
    fInsertNum : "0",
    queryWordEnc: "%E8%80%81%E4%BA%BA%E6%91%94%E5%80%92",
    queryWordGBKEnc: "%C0%CF%C8%CB%CB%A4%B5%B9",
    queryWord : "老人摔倒",
    queryUrlWord : "%E8%80%81%E4%BA%BA%E6%91%94%E5%80%92",
    bdFmtDispNum : "112953",
    bdSearchTime : "",
    gbkword:'%C0%CF%C8%CB%CB%A4%B5%B9',
    resTabs : [],
    queryRecommendTab : "",
    userid:"",
    useSign:"",
    userNumID:"",//这个才是真正的 userid
    encodeUserNumId:"",
    spaceUrl:"",
    hasUserName: ('' == '0'),
    queryClassFlag : '-1',
    bdstoken : '',
    thirdLogo :'0',//第三方网站登录的logo，为空则不显示
    se:'',
    needIE:'1',
    jit:'',
    showHot:'',
    hasResult: '1'||'',
    aspSID:'a3da34f9646fe977',
    oriquery: '',
    fm: '',
    personalized:'0',
    hs: '0'
    });
    flip.setData('jsConfs', {    "normal": {        "margin": 5,        "padding": 0,        "pageNumHeight": 33,"lineHeight": 200,        "maxBaseLineHeight": 220,        "minBaseLineHeight": 200,"pageLineNum": 3,        "pageImgLimit": 20,        "imgDigestHeight": 0,        "maxImgWidth": 400,        "pageMoreNum": 10,"leftMenu": 0    },    "comic": {        "margin": 5,        "padding": 0,        "pageNumHeight": 33,        "lineHeight": 190,        "maxBaseLineHeight": 210,        "minBaseLineHeight": 190,        "pageLineNum": 3,        "pageImgLimit": 20,        "imgDigestHeight": 0,        "maxImgWidth": 400,        "pageMoreNum": 10,        "leftMenu": 0    },    "ald": {        "margin": 5,        "padding": 0,        "pageNumHeight": 33,        "lineHeight": 190,        "maxBaseLineHeight": 210,        "minBaseLineHeight": 190,        "pageLineNum": 3,        "pageImgLimit": 20,        "imgDigestHeight": 0,        "maxImgWidth": 400,        "pageMoreNum": 10,        "leftMenu": 0    },    "star": {        "margin": 5,        "padding": 0,        "pageNumHeight": 33,        "lineHeight": 260,        "maxBaseLineHeight": 280,        "minBaseLineHeight": 250,        "pageLineNum": 3,        "pageImgLimit": 20,        "imgDigestHeight": 0,        "maxImgWidth": 400,        "pageMoreNum": 10,        "leftMenu":0    },    "avatar_brand": {        "margin": 5,        "padding": 0,        "pageNumHeight": 33,        "lineHeight": 300,        "maxBaseLineHeight": 320,        "minBaseLineHeight": 280,        "pageLineNum": 3,        "pageImgLimit": 20,        "imgDigestHeight": 0,        "maxImgWidth": 500,        "pageMoreNum": 10,"leftMenu": 0    },    "avatar_star": {        "margin": 5,        "padding": 0,        "pageNumHeight": 33,        "lineHeight": 260,        "maxBaseLineHeight": 280,        "minBaseLineHeight": 250,        "pageLineNum": 3,        "pageImgLimit": 20,        "imgDigestHeight": 0,        "maxImgWidth": 400,        "pageMoreNum": 10,"leftMenu": 0    },    "avatar_head": {        "margin": 5,        "padding": 0,        "pageNumHeight": 33,        "lineHeight": 200,        "maxBaseLineHeight": 210,        "minBaseLineHeight": 190,        "pageLineNum": 3,        "pageImgLimit": 20,        "imgDigestHeight": 0,        "maxImgWidth": 400,        "pageMoreNum": 10,        "leftMenu": 190    },    "avatar_wallpaper": {        "margin": 5,        "padding": 0,        "pageNumHeight": 33,        "lineHeight": 180,        "maxBaseLineHeight": 200,        "minBaseLineHeight": 160,        "pageLineNum": 3,        "pageImgLimit": 20,        "imgDigestHeight": 0,        "maxImgWidth": 400,        "pageMoreNum": 10,        "leftMenu": 190    },    "single": {        "margin": 5,        "padding": 0,        "pageNumHeight": 33,        "lineHeight": 200,        "maxBaseLineHeight": 220,        "minBaseLineHeight": 200,        "pageLineNum": 1,        "pageImgLimit": 20,        "imgDigestHeight": 0,        "maxImgWidth": 400,        "pageMoreNum": 10,        "leftMenu": 0    },    "personalized": {        "margin": 5,        "padding": 0,        "pageNumHeight": 33,        "lineHeight": 200,        "maxBaseLineHeight": 220,        "minBaseLineHeight": 200,        "pageLineNum": 2,        "pageImgLimit": 20,        "imgDigestHeight": 0,        "maxImgWidth": 400,        "pageMoreNum": 10,        "leftMenu": 0    }}
);
    flip.setData('imgData', {    "queryEnc":"%E8%80%81%E4%BA%BA%E6%91%94%E5%80%92",    "displayNum":112953,    "bdIsClustered" : "1",    "listNum":1688,    "bdFmtDispNum" : "112953",    "bdSearchTime" : "",    "isNeedAsyncRequest":0,"data":[{"thumbURL":"https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2232623552,2580950713&fm=11&gp=0.jpg","middleURL":"https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2232623552,2580950713&fm=11&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"",            "pageNum":0,     
           "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fnimg.ws.126.net%2F%3Furl%3Dhttp%253A%252F%252Fdingyue.ws.126.net%252F3GFKtE0Aenm1pNVuKnm5wPjOxyHPCKrb3Ud6SvfDWzL5U1617708187562.jpeg%26thumbnail%3D650x2147483647%26quality%3D80%26type%3Djpg&refer=http%3A%2F%2Fnimg.ws.126.net&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=759cf01745f7626e9ff21f8edbb5cc9c",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Fooo_z&e3B8mn_z&e3Bv54AzdH3F1yAzdH3Fw6ptvsjAzdH3FGmUcTJHAacnc9IXS_z&e3Bip4s",            "fromURLHost":"www.163.com",            "currentIndex":"",            "width":640,            "height":559,            "type":"jpeg",            "filesize":"",            "bdSrcType":"11",            "di":"28850",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2021-04-06 20:11",            "fromPageTitle":"河南<strong>老人摔倒<\/strong>路人发出灵魂一问扶还是不扶老人我不讹你",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "2232623552,2580950713",            "os" : "4217491767,2860405015",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=2771251045,3816777448&fm=26&gp=0.jpg","middleURL":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=2771251045,3816777448&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=2771251045,3816777448&fm=26&gp=0.jpg",            "pageNum":1,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fimages%2F20191129%2Fbf49cb42614e4251a79deb9f15de9963.jpeg&refer=http%3A%2F%2F5b0988e595225.cdn.sohucs.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=2cfc2e7fdd590fc2ec72f932ad7c7e94",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Fooo_z&e3Bf5i7_z&e3Bv54AzdH3FwAzdH3Fnc0n80cnm_8dadaam9m",            "fromURLHost":"www.sohu.com",            "currentIndex":"",            "width":6720,            "height":4480,            "type":"jpeg",            "filesize":"",            "bdSrcType":"0",            "di":"234520",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2019-11-29 00:00",            "fromPageTitle":"<strong>老人摔倒<\/strong>率居高不下(图片来源于网络)",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "2771251045,3816777448",            "os" : "1823589656,727440984",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2329878976,1306213109&fm=26&gp=0.jpg","middleURL":"https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2329878976,1306213109&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2329878976,1306213109&fm=26&gp=0.jpg",            "pageNum":2,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fwww.aihami.com%2Fuploads%2Fallimg%2F180711%2F173-1PG11J519A7.jpg&refer=http%3A%2F%2Fwww.aihami.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=e456a2eda582cb6edaf83cdb0f6bd32b",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Fooo_z&e3Bwtiw4t_z&e3Bv54AzdH3FwAzdH3F1wg23twgAzdH3Fz725g2AzdH3Fn9la98_d_z&e3Bip4s",            "fromURLHost":"www.aihami.com",            "currentIndex":"",            "width":400,            "height":297,            "type":"jpg",            "filesize":"",            "bdSrcType":"0",            "di":"135740",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2019-03-01 00:00",            "fromPageTitle":"<strong>老人<\/strong>街头摔倒要求去医院 女子竟直接跪下求放过网友评论炸开锅(2)",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "2329878976,1306213109",            "os" : "1878176087,1551782587",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=2212322980,2179800595&fm=26&gp=0.jpg","middleURL":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=2212322980,2179800595&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=2212322980,2179800595&fm=26&gp=0.jpg",            "pageNum":3,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fwww.liaotuo.com%2Fuploadfile%2F2019%2F0110%2F20190110095212168.jpg&refer=http%3A%2F%2Fwww.liaotuo.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=9648218d5730733b09c972cfdcc3e23d",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Fooo_z&e3Bstw5p75_z&e3Bv54AzdH3Fu36oAzdH3Fiv6oAzdH3FgiufAzdH3Fn9lanm_z&e3Bip4s",            "fromURLHost":"www.liaotuo.com",            "currentIndex":"",            "width":484,            "height":300,            "type":"jpg",            "filesize":"",            "bdSrcType":"0",            "di":"70180",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2019-01-10 00:00",            "fromPageTitle":"<strong>老人摔倒<\/strong>后扶不扶?",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "2212322980,2179800595",            "os" : "3703649798,2679838756",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=3473023557,4069978483&fm=26&gp=0.jpg","middleURL":"https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=3473023557,4069978483&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=3473023557,4069978483&fm=26&gp=0.jpg",            "pageNum":4,            "objURL":"https://pics2.baidu.com/feed/cc11728b4710b9129bc0b10faf866b05934522bb.jpeg?token=4f8c604b9fe46532ba866fa3ff5804a8",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Fkwt3twiw5_z&e3Bkwt17_z&e3Bv54AzdH3Ff?t1=8mmcnb0dadmmdcnna8b&ou6=frt1j6&u56=rv",            "fromURLHost":"baijiahao.baidu.com",            "currentIndex":"",            "width":438,            "height":220,            "type":"jpeg",            "filesize":"",            "bdSrcType":"0",            "di":"42130",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2020-04-30 00:00",            "fromPageTitle":"如何预防<strong>老人摔倒<\/strong>?救助工作又有哪些?",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "3473023557,4069978483",            "os" : "966628946,3179413130",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=813649153,696748656&fm=26&gp=0.jpg","middleURL":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=813649153,696748656&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=813649153,696748656&fm=26&gp=0.jpg",            "pageNum":5,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fimages%2F20170814%2F3b0a75a702a74e04801220ccdc6e9354.jpeg&refer=http%3A%2F%2F5b0988e595225.cdn.sohucs.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=4817e3639cf653f32180c81a9c2fa7a0",            "fromURL":"ippr_z2C$qAzdH3FAzdH3F4p_z&e3Bf5i7_z&e3Bv54AzdH3Fda80ab89AzdH3Fgcammcb8d9_z&e3Bfip4s",            "fromURLHost":"mt.sohu.com",            "currentIndex":"",            "width":600,            "height":410,            "type":"jpeg",            "filesize":"",            "bdSrcType":"0",            "di":"41580",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2017-08-16 19:20",            "fromPageTitle":"预防<strong>老人<\/strong>跌倒也要从颈部下手",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "813649153,696748656",            "os" : "1149713185,868291163",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=3744824933,965584512&fm=26&gp=0.jpg","middleURL":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=3744824933,965584512&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=3744824933,965584512&fm=26&gp=0.jpg",            "pageNum":6,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fwww.pntagsyy.com%2Fuploadfile%2Fupload%2Fimage%2F20200511%2F20200511091530_89947.jpg&refer=http%3A%2F%2Fwww.pntagsyy.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=b02ad976c0e55d37215a39e9bc706761",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Fooo_z&e3Bf5i7_z&e3Bv54AzdH3FwAzdH3Fnmb9db8bd_0cb8la",            "fromURLHost":"www.sohu.com",            "currentIndex":"",            "width":1080,            "height":788,            "type":"jpg",            "filesize":"",            "bdSrcType":"0",            "di":"228690",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2019-04-09 23:00",            "fromPageTitle":"贵港87岁<strong>老人<\/strong>不慎摔倒致胯骨骨折,手术还是保守治疗?",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "3744824933,965584512",            "os" : "294583113,199545418",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=138119458,2437542068&fm=26&gp=0.jpg","middleURL":"https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=138119458,2437542068&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=138119458,2437542068&fm=26&gp=0.jpg",            "pageNum":7,            "objURL":"https://ss0.baidu.com/94o3dSag_xI4khGko9WTAnF6hhy/zhidao/pic/item/f7246b600c3387442bf39aea5b0fd9f9d72aa076.jpg",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Fr_z&e3Bkwt17_z&e3Bv54AzdH3Fq7jfpt5gAzdH3Fb1mvm8mdmnmnm9nmmdnanmamaa",            "fromURLHost":"p.baidu.com",            "currentIndex":"",            "width":840,            "height":560,            "type":"jpg",            "filesize":"",            "bdSrcType":"0",            "di":"131340",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2019-01-24 00:00",            "fromPageTitle":"路上看见<strong>老人摔倒<\/strong>,扶还是不扶?",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "138119458,2437542068",            "os" : "3260596785,2979062424",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=1075822513,2971818292&fm=26&gp=0.jpg","middleURL":"https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=1075822513,2971818292&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=1075822513,2971818292&fm=26&gp=0.jpg",            "pageNum":8,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg.mp.itc.cn%2Fupload%2F20170109%2F5c97bf59897142e685403f9b6107ec35_th.jpeg&refer=http%3A%2F%2Fimg.mp.itc.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=aced7cd51b2677ae9eaa7c891d71c5fa",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Fooo_z&e3Bf5i7_z&e3Bv54AzdH3FwAzdH3F8dn0cbna8_90m9am",            "fromURLHost":"www.sohu.com",            "currentIndex":"",            "width":734,            "height":380,            "type":"jpeg",            "filesize":"",            "bdSrcType":"0",            "di":"232980",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2017-01-09 00:15",            "fromPageTitle":"所以说,看到<strong>老人<\/strong>在街边摔倒,在施救前要充分观察现场周围,比如机动",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "1075822513,2971818292",            "os" : "3798363123,635080069",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=176142907,4204307830&fm=26&gp=0.jpg","middleURL":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=176142907,4204307830&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=176142907,4204307830&fm=26&gp=0.jpg",            "pageNum":9,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fpic2.zhimg.com%2Fv2-c635d980ff5cef992644bb4d5db625d6_1200x500.jpg&refer=http%3A%2F%2Fpic2.zhimg.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=630b079a287b330121ef0d92c2d8c102",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Fzi7wgswg_z&e3Bziti7_z&e3Bv54AzdH3FrAzdH3F8a00cldlb?37fp_r7kstfij1=8",            "fromURLHost":"zhuanlan.zhihu.com",            "currentIndex":"",            "width":399,            "height":240,            "type":"jpg",            "filesize":"",            "bdSrcType":"0",            "di":"235180",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2020-02-19 00:00",            "fromPageTitle":"老年人居家安全——如何预防老年人<strong>跌倒<\/strong>",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "176142907,4204307830",            "os" : "1082602231,2977817246",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=383893497,831079528&fm=26&gp=0.jpg","middleURL":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=383893497,831079528&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=383893497,831079528&fm=26&gp=0.jpg",            "pageNum":10,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fs3.sinaimg.cn%2Fmw690%2F006qQ80izy769aN6xTsd2%26690&refer=http%3A%2F%2Fs3.sinaimg.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=3cd064cb66059bd541a60f55abe5941c",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Fks52_z&e3Bftgw_z&e3Bv54_z&e3BvgAzdH3FfAzdH3Fks52_8cu9mnk0da8ado6da_z&e3Bip4s",            "fromURLHost":"blog.sina.com.cn",            "currentIndex":"",            "width":481,            "height":296,            "type":"jpg",            "filesize":"",            "bdSrcType":"0",            "di":"61490",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2016-11-04 09:56",            "fromPageTitle":"智慧养老帮了跌倒<strong>老人<\/strong>大忙",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "383893497,831079528",            "os" : "1405395679,3990546474",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=2695395198,703165050&fm=26&gp=0.jpg","middleURL":"https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=2695395198,703165050&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=2695395198,703165050&fm=26&gp=0.jpg",            "pageNum":11,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fn.sinaimg.cn%2Fsinacn%2F120%2Fw1440h1080%2F20180419%2F1ed1-fzihnep7228537.jpg&refer=http%3A%2F%2Fn.sinaimg.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=f4c8af202aab8c4bb1ec24c6e68baebb",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Fh_z&e3Bftgw_z&e3Bv54_z&e3BvgAzdH3Fw6ptvsj_809anl0ml0_rm0kvcvb8aa8aamda8_z&e3Bip4s",            "fromURLHost":"k.sina.com.cn",            "currentIndex":"",            "width":1440,            "height":1080,            "type":"jpg",            "filesize":"",            "bdSrcType":"0",            "di":"233200",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2018-04-21 05:26",            "fromPageTitle":"<strong>老人摔倒<\/strong>街头,西安工商人勇敢施救传播正能量",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "2695395198,703165050",            "os" : "2063076739,644248584",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=2582473739,3949582740&fm=26&gp=0.jpg","middleURL":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=2582473739,3949582740&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=2582473739,3949582740&fm=26&gp=0.jpg",            "pageNum":12,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg.777n.com%2Fmmbiz_jpg%2FibHfgzjJxf44B5IOxibFSZ8Ca59TfctviaugQ5libxLDWEBWrBBhWhEGOt5heWeobreAcgiaS7hfwwicibplRT68tlTibA%2F640%3Fwx_fmt%3Djpeg&refer=http%3A%2F%2Fimg.777n.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=afbf4623ad2e9e42110ceee8ff4a0ef0",            "fromURL":"ippr_z2C$qAzdH3FAzdH3F000g_z&e3Bv54AzdH3Fpty7AzdH3Fbn8mc_z&e3Bip4s",            "fromURLHost":"777n.com",            "currentIndex":"",            "width":466,            "height":318,            "type":"jpg",            "filesize":"",            "bdSrcType":"0",            "di":"52470",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2018-08-20 00:00",            "fromPageTitle":"<strong>老人摔倒<\/strong>有个\"正确姿势\",关键时刻能救命!",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "2582473739,3949582740",            "os" : "975693025,3893680277",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=1649757577,4265941013&fm=26&gp=0.jpg","middleURL":"https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=1649757577,4265941013&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=1649757577,4265941013&fm=26&gp=0.jpg",            "pageNum":13,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimages.wenming.cn%2Fweb_sc%2Fyw%2F201510%2FW020151029321378360476.jpg&refer=http%3A%2F%2Fimages.wenming.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=73254fcc2befa7822533a580756acdde",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Ffv_z&e3Bojg4tg2_z&e3BvgAzdH3FyoAzdH3Fda8c8aAzdH3Fpda8c8adl_dln00ml_z&e3Bip4",            "fromURLHost":"sc.wenming.cn",            "currentIndex":"",            "width":637,            "height":409,            "type":"jpg",            "filesize":"",            "bdSrcType":"0",            "di":"58080",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2019-01-01 00:00",            "fromPageTitle":"97岁<strong>老人摔倒<\/strong>扶不扶?攀枝花众多市民既搀扶还给钱送医",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "1649757577,4265941013",            "os" : "567742024,1957477294",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=417933752,660107872&fm=26&gp=0.jpg","middleURL":"https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=417933752,660107872&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=417933752,660107872&fm=26&gp=0.jpg",            "pageNum":14,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fimages%2F20180902%2F51945626c0bd421eb70ab4c7ba7990c5.jpeg&refer=http%3A%2F%2F5b0988e595225.cdn.sohucs.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=2000c458eb33d09cf1dda9ed9f265496",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Fooo_z&e3Bf5i7_z&e3Bv54AzdH3FwAzdH3Fdc8cd8bmd_dcmdn9",            "fromURLHost":"www.sohu.com",            "currentIndex":"",            "width":491,            "height":304,            "type":"jpeg",            "filesize":"",            "bdSrcType":"0",            "di":"160930",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2018-09-02 00:00",            "fromPageTitle":"聊城九旬<strong>老人摔倒<\/strong>,满脸是血!扶不扶?他是这样做的.",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "417933752,660107872",            "os" : "460697071,1383426170",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=3775292637,158910830&fm=26&gp=0.jpg","middleURL":"https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=3775292637,158910830&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=3775292637,158910830&fm=26&gp=0.jpg",            "pageNum":15,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fn.sinaimg.cn%2Fsinacn17%2F717%2Fw932h585%2F20181017%2Ffdf7-hmhafis2640657.jpg&refer=http%3A%2F%2Fn.sinaimg.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=5620d47b56b786e98ae7e2111f86776f",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Fh_z&e3Bftgw_z&e3Bv54_z&e3BvgAzdH3Fw6ptvsj_ma0mdldaa9_8mwdv1kw9aa8aauuem_z&e3Bip4s",            "fromURLHost":"k.sina.com.cn",            "currentIndex":"",            "width":932,            "height":585,            "type":"jpg",            "filesize":"",            "bdSrcType":"0",            "di":"126830",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2018-10-17 00:00",            "fromPageTitle":"疾病<strong>摔倒<\/strong>吃过期食品……老人的风险令人心酸",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "3775292637,158910830",            "os" : "3309568460,366563781",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=1512264541,1361175966&fm=26&gp=0.jpg","middleURL":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=1512264541,1361175966&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=1512264541,1361175966&fm=26&gp=0.jpg",            "pageNum":16,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Finews.gtimg.com%2Fnewsapp_bt%2F0%2F10002454837%2F1000.jpg&refer=http%3A%2F%2Finews.gtimg.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=84d3cdcb265c81d20d2ea5a1adb21421",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Fgjo_z&e3Bqq_z&e3Bv54AzdH3F54gAzdH3Fda8lab8nAzdH3Fda8lab8nAaHIbSaa",            "fromURLHost":"new.qq.com",            "currentIndex":"",            "width":500,            "height":300,            "type":"jpg",            "filesize":"",            "bdSrcType":"0",            "di":"63030",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2020-03-11 00:00",            "fromPageTitle":"如何做好预防及应对老年人<strong>跌倒<\/strong>?",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "1512264541,1361175966",            "os" : "1140366441,1667334793",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=4283101697,1483901268&fm=26&gp=0.jpg","middleURL":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=4283101697,1483901268&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=4283101697,1483901268&fm=26&gp=0.jpg",            "pageNum":17,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Finews.gtimg.com%2Fnewsapp_match%2F0%2F5196593546%2F0.jpg&refer=http%3A%2F%2Finews.gtimg.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=fc42e7e4bb5e412a992390e0a4d9fe99",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Fh_z&e3Bftgw_z&e3Bv54_z&e3BvgAzdH3Fw6ptvsj_nbbln88mld_j01dduvvaa8aaunyh_z&e3Bip4s?v6j=ptwgyt&451=rvrw2j6_u5v7f&s5v=d9&6=l&15vp=a&6u7gv=nc&p3=g5gj&p6=l&o4=",            "fromURLHost":"k.sina.com.cn",            "currentIndex":"",            "width":640,            "height":427,            "type":"jpg",            "filesize":"",            "bdSrcType":"0",            "di":"156640",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2018-11-11 16:36",            "fromPageTitle":"所以许多<strong>老人摔倒<\/strong>后起不来,真不是为了碰瓷.",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "4283101697,1483901268",            "os" : "2915058313,3118695153",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2008599087,2873776636&fm=26&gp=0.jpg","middleURL":"https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2008599087,2873776636&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2008599087,2873776636&fm=26&gp=0.jpg",            "pageNum":18,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fwww.hao123m.com%2Fuploads%2Fallimg%2F190522%2F151A22Z7-0.jpg&refer=http%3A%2F%2Fwww.hao123m.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=1330b15bde5c20592b181e1daea9f1df",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Fooo_z&e3Biw58dn4_z&e3Bv54AzdH3F6jgq7gAzdH3Fsw56jgAzdH3F8ln9al_z&e3Bip4s",            "fromURLHost":"www.hao123m.com",            "currentIndex":"",            "width":365,            "height":230,            "type":"jpg",            "filesize":"",            "bdSrcType":"0",            "di":"133430",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2017-07-18 00:00",            "fromPageTitle":"<strong>老人摔倒<\/strong>后不要急着站起来",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "2008599087,2873776636",            "os" : "3191591244,209353555",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=2840256098,109569896&fm=26&gp=0.jpg","middleURL":"https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=2840256098,109569896&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=2840256098,109569896&fm=26&gp=0.jpg",            "pageNum":19,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2F1861.img.pp.sohu.com.cn%2Fimages%2Fblog%2F2011%2F9%2F20%2F9%2F8%2Fu82730558_133416cacacg213.jpg&refer=http%3A%2F%2F1861.img.pp.sohu.com.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=aaf778268438ff60d186a95b8530006f",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Fks52_z&e3Bftgw_z&e3BvgAzdH3F1r55sAzdH3Fks52AzdH3FfAzdH3Fks52_0kunlvb1a8aayrhr_z&e3Bip4s?ep=9",            "fromURLHost":"blog.sina.cn",            "currentIndex":"",            "width":640,            "height":476,            "type":"jpg",            "filesize":"",            "bdSrcType":"0",            "di":"148170",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2017-05-17 00:00",            "fromPageTitle":"[转载]从<strong>老人摔倒<\/strong>方式可辨疾病",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "2840256098,109569896",            "os" : "2054271308,4198649190",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=1372384040,2632873634&fm=26&gp=0.jpg","middleURL":"https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=1372384040,2632873634&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=1372384040,2632873634&fm=26&gp=0.jpg",            "pageNum":20,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fdingyue.ws.126.net%2F2020%2F0429%2Fc6c5ca39j00q9jbte000mc000hs00cwm.jpg&refer=http%3A%2F%2Fdingyue.ws.126.net&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=2d1d4ae7bbe48eca8ec57fcef108ccd5",            "fromURL":"ippr_z2C$qAzdH3FAzdH3F1y_z&e3B8mn_z&e3Bv54AzdH3FedAzdH3Fw6ptvsjAzdH3F1jpwtsAzdH3FFBCRN8mPacn9c98c_z&e3Bip4s",            "fromURLHost":"dy.163.com",            "currentIndex":"",            "width":640,            "height":464,            "type":"jpg",            "filesize":"",            "bdSrcType":"0",            "di":"221870",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2020-04-29 00:00",            "fromPageTitle":"<strong>老人<\/strong>不能跌跤,跌倒是导致老人死亡的主因之一,这九件小事防跌倒",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "1372384040,2632873634",            "os" : "3292033386,1655356092",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=3766404973,442568249&fm=26&gp=0.jpg","middleURL":"https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=3766404973,442568249&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=3766404973,442568249&fm=26&gp=0.jpg",            "pageNum":21,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fn.sinaimg.cn%2Fsinacn20190911s%2F600%2Fw600h800%2F20190911%2Fb7c4-iekuaqu0033658.jpg&refer=http%3A%2F%2Fn.sinaimg.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=1484133ec4622fd422484cbe90c4ebcb",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Fh_z&e3Bftgw_z&e3Bv54_z&e3BvgAzdH3Fw6ptvsj_8mcnmanlcc_emdbuuj0nadaaa5s41_z&e3Bip4s",            "fromURLHost":"k.sina.com.cn",            "currentIndex":"",            "width":600,            "height":800,            "type":"jpg",            "filesize":"",            "bdSrcType":"0",            "di":"46640",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2019-09-12 00:00",            "fromPageTitle":"视频:八旬<strong>老人摔倒<\/strong>流血,她蹲地托举20分钟,直到120人员赶到",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "3766404973,442568249",            "os" : "47487919,125705441",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=1842244230,1501344129&fm=26&gp=0.jpg","middleURL":"https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=1842244230,1501344129&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=1842244230,1501344129&fm=26&gp=0.jpg",            "pageNum":22,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fwww.51wendang.com%2Fpic%2Fda562bd85b984958af9187ef%2F3-810-jpg_6-1080-0-0-1080.jpg&refer=http%3A%2F%2Fwww.51wendang.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=80b56683829124b6dbd201e156dfe980",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Fooo_z&e3Bc8ojg1wg2_z&e3Bv54AzdH3F15vAzdH3F1wcmdk1bcklb9lcbwul8b0juAzdH3Fn",            "fromURLHost":"www.51wendang.com",            "currentIndex":"",            "width":1080,            "height":810,            "type":"jpg",            "filesize":"",            "bdSrcType":"0",            "di":"53460",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2010-04-01 00:00",            "fromPageTitle":"<strong>老人<\/strong>跌倒[1]ppt",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "1842244230,1501344129",            "os" : "1882553212,2657448201",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1050916965,3783484423&fm=26&gp=0.jpg","middleURL":"https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1050916965,3783484423&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1050916965,3783484423&fm=26&gp=0.jpg",            "pageNum":23,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fpccoo.cn%2Fbbs%2F20121219%2F2012121922303571.jpg&refer=http%3A%2F%2Fpccoo.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=da1ec8d835c38b14707c73c527ca44bc",            "fromURL":"ippr_z2C$qAzdH3FAzdH3F4_z&e3Bvijg24wt_z&e3BvgAzdH3FkkfAzdH3Fp5rtv_z&e3Bwfrx?t1=mnl9b88",            "fromURLHost":"m.chengmai.cn",            "currentIndex":"",            "width":3200,            "height":2400,            "type":"jpg",            "filesize":"",            "bdSrcType":"0",            "di":"244530",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2012-12-04 00:00",            "fromPageTitle":"下午四点左右在文明路一<strong>老人<\/strong>跌倒在地?",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "1050916965,3783484423",            "os" : "3142189838,1260956402",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=2093931415,1521583464&fm=26&gp=0.jpg","middleURL":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=2093931415,1521583464&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=2093931415,1521583464&fm=26&gp=0.jpg",            "pageNum":24,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fn.sinaimg.cn%2Ftransform%2F20151012%2FPxK1-fxirwnr6926370.jpg&refer=http%3A%2F%2Fn.sinaimg.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=2c29a5f7bee421eb355dde1b3cbcb616",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Fvq_z&e3Bftgw_z&e3Bv54_z&e3BvgAzdH3FgjofAzdH3FkAzdH3Fda8c-8a-8dAzdH3F1jpwts-tuxt6og6mldm9ml_z&e3Bfip4s",            "fromURLHost":"cq.sina.com.cn",            "currentIndex":"",            "width":400,            "height":300,            "type":"jpg",            "filesize":"",            "bdSrcType":"0",            "di":"131890",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2015-10-12 00:00",            "fromPageTitle":"<strong>老人摔倒<\/strong>众人不敢扶 大学生挺身而出助其脱困",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "2093931415,1521583464",            "os" : "2375923126,2672114776",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=1821634180,2216134578&fm=26&gp=0.jpg","middleURL":"https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=1821634180,2216134578&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=1821634180,2216134578&fm=26&gp=0.jpg",            "pageNum":25,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fphotocdn.sohu.com%2F20150921%2Fmp32637847_1442798880909_1_th.jpeg&refer=http%3A%2F%2Fphotocdn.sohu.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=8029f4758e08caabc23c1c0ede0dfcdd",            "fromURL":"ippr_z2C$qAzdH3FAzdH3F4p_z&e3Bf5i7_z&e3Bv54AzdH3Fda8cald8AzdH3Fg9d8mm00nm_z&e3Bfip4s",            "fromURLHost":"mt.sohu.com",            "currentIndex":"",            "width":393,            "height":295,            "type":"jpeg",            "filesize":"",            "bdSrcType":"0",            "di":"227260",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2015-09-20 17:30",            "fromPageTitle":"小编说话喜欢跑火车,所以开头总结一下搀扶跌倒<strong>老人<\/strong>(伤者)的步骤,再说",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "1821634180,2216134578",            "os" : "645233660,2124816021",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=591666896,79185021&fm=26&gp=0.jpg","middleURL":"https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=591666896,79185021&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=591666896,79185021&fm=26&gp=0.jpg",            "pageNum":26,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fupload.sq1996.com%2F2015%2F0115%2F1421282770829.jpg&refer=http%3A%2F%2Fupload.sq1996.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=035e45b982d9afec6f200ac0db4719d2",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Fooo_z&e3Bcvvv_z&e3BgjpAzdH3Frt7h3pAzdH3Fda8mab8bmmc9a_z&e3Bip4s",            "fromURLHost":"www.5ccc.net",            "currentIndex":"",            "width":500,            "height":273,            "type":"jpg",            "filesize":"",            "bdSrcType":"0",            "di":"159280",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2015-01-15 00:00",            "fromPageTitle":"照片由张艺冬提供,自称<strong>摔倒老人<\/strong>是他花一百元请来的.",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "591666896,79185021",            "os" : "4071960298,1812419137",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=1997473551,3736491292&fm=26&gp=0.jpg","middleURL":"https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=1997473551,3736491292&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=1997473551,3736491292&fm=26&gp=0.jpg",            "pageNum":27,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fn.sinaimg.cn%2Ffront%2F288%2Fw600h488%2F20181017%2F_rfB-hmhswin1387254.jpg&refer=http%3A%2F%2Fn.sinaimg.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=3fdb7979244a65f758e110e4bea27923",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Fh_z&e3Bftgw_z&e3Bv54_z&e3BvgAzdH3Fw6ptvsj_mmalclld99_8blum0kavaa8aavhtq_z&e3Bip4s?v6j=ptwgyt&451=rvrw2j6_u5v7f&s5v=8n&6=l&15vp=a&6u7gv=8aa&p3=g5gj&p6=l&o4=",            "fromURLHost":"k.sina.com.cn",            "currentIndex":"",            "width":600,            "height":488,            "type":"jpg",            "filesize":"",            "bdSrcType":"0",            "di":"244420",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2018-10-12 00:00",            "fromPageTitle":"<strong>老人摔倒<\/strong>后没人搀扶, 小学生扶起后, 老人: 喊你家长送我去医院",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "1997473551,3736491292",            "os" : "3467784234,951214083",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=4103676308,3394928279&fm=26&gp=0.jpg","middleURL":"https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=4103676308,3394928279&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=4103676308,3394928279&fm=26&gp=0.jpg",            "pageNum":28,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fm.images.ofweek.com%2FUpload%2Fplainimages%2Fweixiang%2FAug%2F0806%2F4%2F2.png&refer=http%3A%2F%2Fm.images.ofweek.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=ecb0c2b3639b9e021381bf171ff9e4c3",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Fooo_z&e3Bu6jjr_z&e3BvgAzdH3Fp57ptw5AzdH3Fdabl8cn_z&e3Bip4",            "fromURLHost":"www.freep.cn",            "currentIndex":"",            "width":740,            "height":424,            "type":"png",            "filesize":"",            "bdSrcType":"0",            "di":"132000",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2018-08-17 10:05",            "fromPageTitle":"防止<strong>老人摔倒<\/strong>的产品",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "4103676308,3394928279",            "os" : "2320850974,3660628807",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=4265447469,2263206117&fm=26&gp=0.jpg","middleURL":"https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=4265447469,2263206117&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=4265447469,2263206117&fm=26&gp=0.jpg",            "pageNum":29,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fgss0.baidu.com%2F-vo3dSag_xI4khGko9WTAnF6hhy%2Fzhidao%2Fpic%2Fitem%2Fd043ad4bd11373f05f16550fa60f4bfbfbed0470.jpg&refer=http%3A%2F%2Fgss0.baidu.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=7ae658cd257fd34bbb7db2ea377a82e3",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Fzit1w5_z&e3Bkwt17_z&e3Bv54AzdH3Fq7jfpt5gAzdH3F8dn0lnlbc98cccdam8l_z&e3Bip4s",            "fromURLHost":"zhidao.baidu.com",            "currentIndex":"",            "width":1500,            "height":1000,            "type":"jpg",            "filesize":"",            "bdSrcType":"0",            "di":"57970",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2014-07-15 00:00",            "fromPageTitle":"我是视觉传达的一名大四学生,毕业设计需要主题是<strong>老人摔倒<\/strong>的,求老人",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "4265447469,2263206117",            "os" : "2429544076,2256125815",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=887719445,2962509409&fm=26&gp=0.jpg","middleURL":"https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=887719445,2962509409&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=887719445,2962509409&fm=26&gp=0.jpg",            "pageNum":30,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fimages%2F20181119%2F56d65126f83b47cc82a630bf0bd7c2e3.jpeg&refer=http%3A%2F%2F5b0988e595225.cdn.sohucs.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=97538e27af6e1343d69331fe194093fd",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Fooo_z&e3Bf5i7_z&e3Bv54AzdH3FwAzdH3Fd0m900dnd_8daaaac8b",            "fromURLHost":"www.sohu.com",            "currentIndex":"",            "width":400,            "height":300,            "type":"jpeg",            "filesize":"",            "bdSrcType":"0",            "di":"146630",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2018-11-19 00:00",            "fromPageTitle":"<strong>老人<\/strong>跌倒不是病,但可能会要了命",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "887719445,2962509409",            "os" : "183681658,2198524890",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=1805094477,3464173948&fm=26&gp=0.jpg","middleURL":"https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=1805094477,3464173948&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=1805094477,3464173948&fm=26&gp=0.jpg",            "pageNum":31,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fcrawler-fs.intsig.net%2Fcamfs%2Fdownload%3Ffilename%3D10005_426dc532cb025d0bf819e6555a3320b2_avatar.jpeg&refer=http%3A%2F%2Fcrawler-fs.intsig.net&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=e40266ffc5cd377063826a73d8971e40",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Fkkf_z&e3Be5v_z&e3Bv54_z&e3BvgAzdH3Fp5rtv-nbcblcb-8-8_z&e3Bip4s",            "fromURLHost":"bbs.voc.com.cn",            "currentIndex":"",            "width":962,            "height":960,            "type":"jpeg",            "filesize":"",            "bdSrcType":"0",            "di":"48400",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2011-12-06 22:07",            "fromPageTitle":"【扩散】\"<strong>老人摔倒<\/strong>\"可以放心扶了! - 行业动态即时报",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "1805094477,3464173948",            "os" : "607045625,1358878940",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=4272530019,3999883704&fm=26&gp=0.jpg","middleURL":"https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=4272530019,3999883704&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=4272530019,3999883704&fm=26&gp=0.jpg",            "pageNum":32,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimgsa.baidu.com%2Fexp%2Fw%3D500%2Fsign%3De3274083d088d43ff0a991f24d1fd2aa%2Faa64034f78f0f736b0e7abf70c55b319ebc4132e.jpg&refer=http%3A%2F%2Fimgsa.baidu.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=8fb4150458f5bebf7c700ab64b3e97fc",            "fromURL":"ippr_z2C$qAzdH3FAzdH3F3tg2ywg_z&e3Bkwt17_z&e3Bv54AzdH3Fw6ptvsjAzdH3Funw101aua8dcmualvnn9ckj1_z&e3Bip4s?fp=n&5f=a&k1_rw2j_pyrj=8&gjp_pyrj=d&6fp=m",            "fromURLHost":"jingyan.baidu.com",            "currentIndex":"",            "width":320,            "height":240,            "type":"jpg",            "filesize":"",            "bdSrcType":"0",            "di":"230560",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2016-03-18 00:00",            "fromPageTitle":"生活/家居 > 生活常识  1 5,如果<strong>摔倒老人<\/strong>神志不清昏迷,呕吐,那么要将",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "4272530019,3999883704",            "os" : "2876787098,635856990",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=1819859474,1271377178&fm=26&gp=0.jpg","middleURL":"https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=1819859474,1271377178&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=1819859474,1271377178&fm=26&gp=0.jpg",            "pageNum":33,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fepaper.jwb.com.cn%2Fjwb%2Fresfile%2F2017-02-21%2F05%2Fggj72152_b.jpg&refer=http%3A%2F%2Fepaper.jwb.com.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=04417a4c5ce4abbb0942fa1280f49e23",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Fgjof_z&e3Bkt2c_z&e3Bjg56pi_z&e3Bv54_z&e3BvgAzdH3Ffyfpj4AzdH3Fda80AzdH3FadAzdH3Fd8AzdH3Fan8cbnmnm_z&e3Bfip4s",            "fromURLHost":"news.big5.enorth.com.cn",            "currentIndex":"",            "width":320,            "height":240,            "type":"jpg",            "filesize":"",            "bdSrcType":"0",            "di":"71500",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2017-02-21 00:00",            "fromPageTitle":"一位八旬<strong>老人摔倒<\/strong>,被一名热心小伙扶起,小伙还因此耽误了工作.",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "1819859474,1271377178",            "os" : "2235595202,4156406638",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2288229950,651263115&fm=26&gp=0.jpg","middleURL":"https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2288229950,651263115&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2288229950,651263115&fm=26&gp=0.jpg",            "pageNum":34,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg1.gtimg.com%2Fhenan%2Fpics%2Fhv1%2F240%2F216%2F2232%2F145191120.jpg&refer=http%3A%2F%2Fimg1.gtimg.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=ee1494ae66394eddcb58ab46278331b1",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Fijgwg_z&e3Bqq_z&e3Bv54AzdH3FwAzdH3Fda80ab80AzdH3Fac8a80_z&e3Bip4",            "fromURLHost":"henan.qq.com",            "currentIndex":"",            "width":630,            "height":472,            "type":"jpg",            "filesize":"",            "bdSrcType":"0",            "di":"42570",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2017-08-17 00:00",            "fromPageTitle":"鹤壁78岁<strong>老人<\/strong>路边摔倒动弹不得 路人做法让人感动",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "2288229950,651263115",            "os" : "831043212,3367136092",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2950442100,713321001&fm=26&gp=0.jpg","middleURL":"https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2950442100,713321001&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2950442100,713321001&fm=26&gp=0.jpg",            "pageNum":35,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fss2.meipian.me%2Fusers%2F8295802%2F74b98668f03b4a3e9b6ad1519e38d2f9.jpg%3Fmeipian-raw%2Fbucket%2Fivwen%2Fkey%2FdXNlcnMvODI5NTgwMi83NGI5ODY2OGYwM2I0YTNlOWI2YWQxNTE5ZTM4ZDJmOS5qcGc%3D%2Fsign%2F058db175ea13fe79e0b5ffc&refer=http%3A%2F%2Fss2.meipian.me&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=968caa40999c796903f524ef4c574c13",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Fooo_z&e3B4jtrtwg_z&e3BvgAzdH3F8ho4895c",            "fromURLHost":"www.meipian.cn",            "currentIndex":"",            "width":668,            "height":676,            "type":"jpg",            "filesize":"",            "bdSrcType":"0",            "di":"52580",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2018-08-24 00:00",            "fromPageTitle":"教<strong>老人<\/strong>如何\"正确\"摔倒,新余市红十字会老年介护普及培训开课啦!",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "2950442100,713321001",            "os" : "743023055,1202368952",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=3288813106,466759429&fm=26&gp=0.jpg","middleURL":"https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=3288813106,466759429&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=3288813106,466759429&fm=26&gp=0.jpg",            "pageNum":36,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fs9.rr.itc.cn%2Fr%2FwapChange%2F201612_30_9%2Fa7k1ij5837561174325.png&refer=http%3A%2F%2Fs9.rr.itc.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=edda7624c1da3bc08e91b0f4ebfba13c",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Fijwspi_z&e3Bf5i7_z&e3Bv54AzdH3Fda8m8dnaAzdH3Fg900n9lnan_z&e3Bfip4s?u654=w7p5_r5f_0",            "fromURLHost":"health.sohu.com",            "currentIndex":"",            "width":523,            "height":747,            "type":"png",            "filesize":"",            "bdSrcType":"0",            "di":"232870",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2016-12-30 00:00",            "fromPageTitle":"这几种情况下,<strong>老人<\/strong>跌倒了不能扶?",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "3288813106,466759429",            "os" : "167366285,4153602062",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1890085703,1529997319&fm=26&gp=0.jpg","middleURL":"https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1890085703,1529997319&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1890085703,1529997319&fm=26&gp=0.jpg",            "pageNum":37,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fn.sinaimg.cn%2Fsinacn%2Fw590h370%2F20180125%2F0646-fyqwiqk4978609.jpg&refer=http%3A%2F%2Fn.sinaimg.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=6d1a944b5e97e594cd657d8a83ac185c",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Fh_z&e3Bftgw_z&e3Bv54_z&e3BvgAzdH3Fw6ptvsj_mnl98lnbl9_8018uw0jmaa8aadgb8_z&e3Bip4s?v6j=ptwgyt&451=rvrw2j6_gjof&s5v=8d&6=l&15vp=a&6u7gv=8aa&p3=g5gj&p6=l",            "fromURLHost":"k.sina.com.cn",            "currentIndex":"",            "width":590,            "height":370,            "type":"jpg",            "filesize":"",            "bdSrcType":"0",            "di":"228360",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2017-02-28 00:00",            "fromPageTitle":"上海下雪了,因路滑<strong>老人摔倒<\/strong>扶不扶的问题,根本不存在的!",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "1890085703,1529997319",            "os" : "708289033,3868325955",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1089966240,1150128150&fm=26&gp=0.jpg","middleURL":"https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1089966240,1150128150&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1089966240,1150128150&fm=26&gp=0.jpg",            "pageNum":38,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fnewpic.jxnews.com.cn%2F003%2F012%2F587%2F00301258718_f5eeba37.jpg&refer=http%3A%2F%2Fnewpic.jxnews.com.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=da8fe06b9bf506a80faa7eb9895ed756",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Fgv_z&e3B3xgjof_z&e3Bv54_z&e3BvgAzdH3Ffyfpj4AzdH3Fda8bAzdH3FacAzdH3FdcAzdH3Fa8mldbmbm_z&e3Bfip4s",            "fromURLHost":"nc.jxnews.com.cn",            "currentIndex":"",            "width":1080,            "height":1920,            "type":"jpg",            "filesize":"",            "bdSrcType":"0",            "di":"227810",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2018-05-25 00:00",            "fromPageTitle":"南昌消防官兵救助7旬倒地<strong>老人<\/strong>获赞 老人摔倒原因正在调查中",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "1089966240,1150128150",            "os" : "397904524,259397397",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=2695495432,3370412844&fm=26&gp=0.jpg","middleURL":"https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=2695495432,3370412844&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=2695495432,3370412844&fm=26&gp=0.jpg",            "pageNum":39,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fimages%2F20171011%2Ff5a75eb813c944f0b845e33433a65fb2.jpeg&refer=http%3A%2F%2F5b0988e595225.cdn.sohucs.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=7285d34c240a9db1ae00a66b9014fd36",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Fooo_z&e3Bf5i7_z&e3Bv54AzdH3FwAzdH3F8l0990ccn_9m99bm",            "fromURLHost":"www.sohu.com",            "currentIndex":"",            "width":480,            "height":360,            "type":"jpeg",            "filesize":"",            "bdSrcType":"0",            "di":"161370",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2015-10-19 20:52",            "fromPageTitle":"【和谐医患】<strong>老人<\/strong>路边摔倒扶不扶?受伤救不救?",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "2695495432,3370412844",            "os" : "2058156021,1463343653",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=710424229,2270093425&fm=26&gp=0.jpg","middleURL":"https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=710424229,2270093425&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=710424229,2270093425&fm=26&gp=0.jpg",            "pageNum":40,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fss2.meipian.me%2Fusers%2F4677301%2F6fe5f64e6e1d4086a50aa3853f88b5a0.jpg%3Fmeipian-raw%2Fbucket%2Fivwen%2Fkey%2FdXNlcnMvNDY3NzMwMS82ZmU1ZjY0ZTZlMWQ0MDg2YTUwYWEzODUzZjg4YjVhMC5qcGc%3D%2Fsign%2F3082a496d8f8701510554d0&refer=http%3A%2F%2Fss2.meipian.me&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=78548e1f15bfae8ce6e8781ed37871db",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Fooo_z&e3B4jtrtwg_z&e3BvgAzdH3F881h6mgz",            "fromURLHost":"www.meipian.cn",            "currentIndex":"",            "width":1080,            "height":696,            "type":"jpg",            "filesize":"",            "bdSrcType":"0",            "di":"227920",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2016-04-21 00:00",            "fromPageTitle":"<strong>老人<\/strong>意外跌倒别不重视,这种骨折是\"老年人最后一次骨折\",可能要命!",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "710424229,2270093425",            "os" : "415084995,3633699392",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=2864204778,4011499019&fm=26&gp=0.jpg","middleURL":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=2864204778,4011499019&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=2864204778,4011499019&fm=26&gp=0.jpg",            "pageNum":41,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimage.xinmin.cn%2F2015%2F10%2F19%2F20151019111422652738.jpg&refer=http%3A%2F%2Fimage.xinmin.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=f374208b059f07923d170d26aa2e733c",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Ffiwg2iwt_z&e3Bxtg4tg_z&e3BvgAzdH3Fx4fqAzdH3Fda8cAzdH3F8aAzdH3F8lAzdH3Fdb009nnl_z&e3Bip4s",            "fromURLHost":"shanghai.xinmin.cn",            "currentIndex":"",            "width":627,            "height":390,            "type":"jpg",            "filesize":"",            "bdSrcType":"0",            "di":"159830",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2015-10-20 00:00",            "fromPageTitle":"龙华街道调查:80岁以上<strong>老人<\/strong>跌倒发生率高达46%",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "2864204778,4011499019",            "os" : "2707871091,1243579316",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=2606134312,4218763426&fm=26&gp=0.jpg","middleURL":"https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=2606134312,4218763426&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=2606134312,4218763426&fm=26&gp=0.jpg",            "pageNum":42,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fn.sinaimg.cn%2Fsinacn20190522s%2F530%2Fw774h556%2F20190522%2Ff989-hxhyiun1819561.png&refer=http%3A%2F%2Fn.sinaimg.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=76296942933016e609b7f9d0b28dc828",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Fh_z&e3Bftgw_z&e3Bv54_z&e3BvgAzdH3Fw6ptvsj_cdlnacandd_8nk01bl1daa8aai62a_z&e3Bip4s?v6j=ptwgyt&451=rvrw2j6_gjof&s5v=0&6=l&6u7gv=0m&p3=g5gj&p6=l",            "fromURLHost":"k.sina.com.cn",            "currentIndex":"",            "width":774,            "height":556,            "type":"png",            "filesize":"",            "bdSrcType":"0",            "di":"236280",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2018-10-30 00:13",            "fromPageTitle":"<strong>老人摔倒<\/strong>,路过却不扶,最终老人死亡,路人要承担责任吗",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "2606134312,4218763426",            "os" : "200806132,388495055",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2781769483,976075150&fm=26&gp=0.jpg","middleURL":"https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2781769483,976075150&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2781769483,976075150&fm=26&gp=0.jpg",            "pageNum":43,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fwww.wendangwang.com%2Fpic%2Fc7010367ca47a278500d40a8%2F1-810-jpg_6-1080-0-0-1080.jpg&refer=http%3A%2F%2Fwww.wendangwang.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=54661766e0af32ca09216a9aad78ea6e",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Fooo_z&e3Bojg1wg2owg2_z&e3Bv54AzdH3F15vAzdH3Fv0a8anm0vw90wd0bcaa19awb",            "fromURLHost":"www.wendangwang.com",            "currentIndex":"",            "width":1080,            "height":810,            "type":"jpg",            "filesize":"",            "bdSrcType":"0",            "di":"65670",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2019-09-18 00:00",            "fromPageTitle":"<strong>老人摔倒<\/strong>,扶不扶ppt",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "2781769483,976075150",            "os" : "2798075578,4086358936",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1050031720,1324125308&fm=26&gp=0.jpg","middleURL":"https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1050031720,1324125308&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1050031720,1324125308&fm=26&gp=0.jpg",            "pageNum":44,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fgbres.dfcfw.com%2FFiles%2Fpicture%2F20190730%2FECC8ACFDACB85235285595976F94EB69_w1080h718.jpg&refer=http%3A%2F%2Fgbres.dfcfw.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=16d3f6c2db8a1a7fb6e08b19c43243eb",            "fromURL":"ippr_z2C$qAzdH3FAzdH3F27kw_z&e3Bjwfp45gjy_z&e3Bv54AzdH3Fgjof,5uaa09a0,bcl8nldad_z&e3Bip4s",            "fromURLHost":"guba.eastmoney.com",            "currentIndex":"",            "width":1080,            "height":718,            "type":"jpg",            "filesize":"",            "bdSrcType":"0",            "di":"45540",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2019-09-08 11:30",            "fromPageTitle":"功能简介:在佩戴者<strong>摔倒<\/strong>瞬间给气囊充气,保护腰部,臀部,避免老人因跌倒",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "1050031720,1324125308",            "os" : "4156087858,2637525810",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=1809240081,1046921126&fm=26&gp=0.jpg","middleURL":"https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=1809240081,1046921126&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=1809240081,1046921126&fm=26&gp=0.jpg",            "pageNum":45,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fwww.tianya999.com%2Fuploads%2Fallimg%2F150910%2F2298-150910094031-50.jpg&refer=http%3A%2F%2Fwww.tianya999.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=ff04f7a55a0a29e3f8328d651e40c8cd",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Fooo_z&e3Bfj6jg2jfjkw_z&e3Bv54AzdH3FoAzdH3F%Eb%ba%b8%E9%BA%BA%Em%l8%l9%Ec%ba%ld%Em%l0%Aa%E9%BA%BA%Em%bl%Bm%E0%bE%Ba%Eb%B8%A8AzdH3F",            "fromURLHost":"www.serengeseba.com",            "currentIndex":"",            "width":376,            "height":257,            "type":"jpg",            "filesize":"",            "bdSrcType":"0",            "di":"240020",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2015-09-09 00:00",            "fromPageTitle":"<strong>老人摔倒<\/strong>无人敢扶图片以及现象讨论 扶摔倒老人被讹自杀",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "1809240081,1046921126",            "os" : "2700407375,657140089",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=2595563989,4131435889&fm=26&gp=0.jpg","middleURL":"https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=2595563989,4131435889&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=2595563989,4131435889&fm=26&gp=0.jpg",            "pageNum":46,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fs6.sinaimg.cn%2Fmiddle%2F7135c0e2gc75924cce615%26690&refer=http%3A%2F%2Fs6.sinaimg.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=67f4f745dbfabfdedf11d25f0c08c2bf",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Fks52_z&e3Bftgw_z&e3Bv54_z&e3BvgAzdH3FfAzdH3Fks52_08ncvajda8a80hve_z&e3Bip4s",            "fromURLHost":"blog.sina.com.cn",            "currentIndex":"",            "width":317,            "height":416,            "type":"jpg",            "filesize":"",            "bdSrcType":"0",            "di":"76780",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2012-08-16 10:51",            "fromPageTitle":"上海<strong>老人<\/strong>街头跌倒,目击者称有人欲扶被劝阻,外国人出手相救",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "2595563989,4131435889",            "os" : "1011261154,4242527645",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=292897429,60986185&fm=26&gp=0.jpg","middleURL":"https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=292897429,60986185&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=292897429,60986185&fm=26&gp=0.jpg",            "pageNum":47,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fi2.chinanews.com%2Fsimg%2Fhpic%2F2014%2F04-08%2Fm_81ab6caf77d4bb5de1ec26a66a7fde70-9804022.jpg&refer=http%3A%2F%2Fi2.chinanews.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=da7604d49bfd7b4ff35be0cf612b08a9",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Fooo_z&e3Bvitgwgjof_z&e3Bv54AzdH3FstujAzdH3Fda89AzdH3Fa9-abAzdH3Fman0adb_z&e3Bfip4s",            "fromURLHost":"www.chinanews.com",            "currentIndex":"",            "width":360,            "height":270,            "type":"jpg",            "filesize":"",            "bdSrcType":"0",            "di":"220550",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2018-03-28 00:00",            "fromPageTitle":"<strong>老人<\/strong>路上摔倒鲜血直流 市民二十分钟接力救助",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "292897429,60986185",            "os" : "1843900443,3114553041",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=4219636955,3716219128&fm=26&gp=0.jpg","middleURL":"https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=4219636955,3716219128&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=4219636955,3716219128&fm=26&gp=0.jpg",            "pageNum":48,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fgss0.baidu.com%2F7LsWdDW5_xN3otqbppnN2DJv%2Fzhidao%2Fpic%2Fitem%2F024f78f0f736afc396f7f4fab819ebc4b64512b2.jpg&refer=http%3A%2F%2Fgss0.baidu.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=1e0fbd63a74662fc614a17f6ef464e40",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Fhg5o_z&e3Bkwt17_z&e3Bv54AzdH3Fojg1wAzdH3Fq7jfpt5gAzdH3Ftgu5?qt1=danndc9jacv1numnndw8d18cwjk19b8m9mnla8v",            "fromURLHost":"know.baidu.com",            "currentIndex":"",            "width":550,            "height":320,            "type":"jpg",            "filesize":"",            "bdSrcType":"0",            "di":"75020",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2019-06-26 00:00",            "fromPageTitle":"其次要给<strong>老人<\/strong>手机上的最经常联系的人,或者写着儿女的那个电话联系.",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "4219636955,3716219128",            "os" : "2602081233,3349079483",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=232548589,2423971400&fm=26&gp=0.jpg","middleURL":"https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=232548589,2423971400&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=232548589,2423971400&fm=26&gp=0.jpg",            "pageNum":49,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fupload.taihainet.com%2F2019%2F1216%2F1576455185175.JPEG&refer=http%3A%2F%2Fupload.taihainet.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=64a9871922ec5e8f97ce945c819a30de",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Fooo_z&e3Bpwtiwtgjp_z&e3Bv54AzdH3FgjofAzdH3Fu73twgAzdH3Ffz33AzdH3Fda8l-8d-8mAzdH3Fdnn0m9m_d_z&e3Bip4s",            "fromURLHost":"www.taihainet.com",            "currentIndex":"",            "width":1080,            "height":810,            "type":"jpeg",            "filesize":"",            "bdSrcType":"0",            "di":"243100",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2019-12-13 00:00",            "fromPageTitle":"寒冬街头现暖心一幕!<strong>老人摔倒<\/strong>街头被福州小伙扶起(2)",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "232548589,2423971400",            "os" : "3218836937,2182468475",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=445231443,2405129546&fm=26&gp=0.jpg","middleURL":"https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=445231443,2405129546&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=445231443,2405129546&fm=26&gp=0.jpg",            "pageNum":50,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg1.gtimg.com%2Fkid%2Fpics%2Fhv1%2F66%2F114%2F1143%2F74352711.jpg&refer=http%3A%2F%2Fimg1.gtimg.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=e1ceb4392acb31b6b5542a54381ffef6",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Fht1_z&e3Bqq_z&e3Bv54AzdH3FwAzdH3Fda8dal89AzdH3Faaaa80_z&e3Bip4",            "fromURLHost":"kid.qq.com",            "currentIndex":"",            "width":550,            "height":437,            "type":"jpg",            "filesize":"",            "bdSrcType":"0",            "di":"238480",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2014-03-05 00:00",            "fromPageTitle":"遇到<strong>老人摔倒<\/strong>了 怎么办",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "445231443,2405129546",            "os" : "2008115028,453949755",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=4157372495,1627778518&fm=26&gp=0.jpg","middleURL":"https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=4157372495,1627778518&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=4157372495,1627778518&fm=26&gp=0.jpg",            "pageNum":51,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fimages%2F20180827%2F349be4a07dd844e8b63fd7faf8696f10.jpeg&refer=http%3A%2F%2F5b0988e595225.cdn.sohucs.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=637e6360712112e89ae878b3cab0b5ec",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Fooo_z&e3Bf5i7_z&e3Bv54AzdH3FwAzdH3Fdcaddlcna_0l09c8",            "fromURLHost":"www.sohu.com",            "currentIndex":"",            "width":450,            "height":291,            "type":"jpeg",            "filesize":"",            "bdSrcType":"0",            "di":"62480",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2018-08-27 00:00",            "fromPageTitle":"<strong>老人<\/strong>跌倒的危险因素有什么?",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "4157372495,1627778518",            "os" : "1787306953,1104982129",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=235536006,630702120&fm=26&gp=0.jpg","middleURL":"https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=235536006,630702120&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=235536006,630702120&fm=26&gp=0.jpg",            "pageNum":52,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fimages%2F20171109%2F3af05334a5a04ec8a023d69f5084e198.jpeg&refer=http%3A%2F%2F5b0988e595225.cdn.sohucs.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=98f87d18af4c2d30b2e0adc8b57765e1",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Fooo_z&e3Bf5i7_z&e3Bv54AzdH3FwAzdH3Fdann09l88_lll880d8",            "fromURLHost":"www.sohu.com",            "currentIndex":"",            "width":550,            "height":264,            "type":"jpeg",            "filesize":"",            "bdSrcType":"0",            "di":"126060",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2017-11-09 00:00",            "fromPageTitle":"1,遇见<strong>老人<\/strong>跌倒怎么办?",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "235536006,630702120",            "os" : "560366243,807403585",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2555938012,2869035633&fm=26&gp=0.jpg","middleURL":"https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2555938012,2869035633&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2555938012,2869035633&fm=26&gp=0.jpg",            "pageNum":53,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fp0.qhimgs4.com%2Ft018654cc6491f11fc6.jpg&refer=http%3A%2F%2Fp0.qhimgs4.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=56d3a0071b0be9148a180bb5654c857b",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Ffi_z&e3Bqti55_z&e3Bv54AzdH3FrvAzdH3Fdfd8rrozr4f?ft2g=nma_jnlnml18",            "fromURLHost":"sh.qihoo.com",            "currentIndex":"",            "width":960,            "height":577,            "type":"jpg",            "filesize":"",            "bdSrcType":"0",            "di":"49170",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2018-01-07 06:49",            "fromPageTitle":"暖心!<strong>老人<\/strong>结冰路面摔倒 情侣毫不犹豫搀扶 感动一座城",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "2555938012,2869035633",            "os" : "3512164973,1433285523",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=2516143853,3059807479&fm=26&gp=0.jpg","middleURL":"https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=2516143853,3059807479&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=2516143853,3059807479&fm=26&gp=0.jpg",            "pageNum":54,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg.xinmin.cn%2Fxmwb%2F2017%2F9%2FNEM1_20170912_C0321993792_A729826.jpg&refer=http%3A%2F%2Fimg.xinmin.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=8f7209789b3ebbe39e1f60ea78361a20",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Fgjofx4ok_z&e3Bxtg4tg_z&e3BvgAzdH3Ffiwg2iwtpwgAzdH3Fda80AzdH3FalAzdH3F8dAzdH3Fn8d0m08m_z&e3Bip4s",            "fromURLHost":"newsxmwb.xinmin.cn",            "currentIndex":"",            "width":450,            "height":580,            "type":"jpg",            "filesize":"",            "bdSrcType":"0",            "di":"64130",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2017-09-12 00:00",            "fromPageTitle":"<strong>老人摔倒<\/strong>血流不止 好心民警及时送医",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "2516143853,3059807479",            "os" : "440194035,308539763",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=3013456534,3593382909&fm=26&gp=0.jpg","middleURL":"https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=3013456534,3593382909&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=3013456534,3593382909&fm=26&gp=0.jpg",            "pageNum":55,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fs.wasu.tv%2Fmrms%2Fpic%2F20131212%2F201312121434217534193cf8e.jpg&refer=http%3A%2F%2Fs.wasu.tv&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=4f925befbf6b2142251560330e39dcf3",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Ff5f5da8aan89xn90dbal_z&e3Bp7xt_z&e3Bv54_z&e3BvgAzdH3Fetjok-da0m0n8b8m98nb8-da0m0n8b8m98nb88adb_z&e3Bip4s",            "fromURLHost":"soso20100314x3472809.tuxi.com.cn",            "currentIndex":"",            "width":320,            "height":240,            "type":"jpg",            "filesize":"",            "bdSrcType":"0",            "di":"125840",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2016-12-14 00:00",            "fromPageTitle":"<strong>老人摔倒<\/strong>了好几天不排便怎么办",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "3013456534,3593382909",            "os" : "1665582902,2185983962",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=1799505476,894396457&fm=26&gp=0.jpg","middleURL":"https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=1799505476,894396457&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=1799505476,894396457&fm=26&gp=0.jpg",            "pageNum":56,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fpccoo.cn%2Fbbs%2F20121219%2F201212192244290.jpg&refer=http%3A%2F%2Fpccoo.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=46311f029b6cd834a5b37231d6a9d7da",            "fromURL":"ippr_z2C$qAzdH3FAzdH3F4_z&e3Bvijg24wt_z&e3BvgAzdH3FkkfAzdH3Fp5rtv_z&e3Bwfrx?t1=mnl9b88",            "fromURLHost":"m.chengmai.cn",            "currentIndex":"",            "width":3200,            "height":2400,            "type":"jpg",            "filesize":"",            "bdSrcType":"0",            "di":"213290",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2013-11-28 00:00",            "fromPageTitle":"下午四点左右在文明路一<strong>老人<\/strong>跌倒在地?",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "1799505476,894396457",            "os" : "2622968902,1647073582",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=534424503,56606182&fm=26&gp=0.jpg","middleURL":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=534424503,56606182&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=534424503,56606182&fm=26&gp=0.jpg",            "pageNum":57,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fcms-bucket.nosdn.127.net%2Fbe1341c390e34addac6c88fe6c08c65820180401191232.jpeg%3FimageView%26thumbnail%3D550x0&refer=http%3A%2F%2Fcms-bucket.nosdn.127.net&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=b8a08fe348f1f2402656d482753cc271",            "fromURL":"ippr_z2C$qAzdH3FAzdH3F2x_z&e3Bgjof_z&e3B8mn_z&e3Bv54AzdH3F8bAzdH3Fa9a8AzdH3F8lAzdH3FDEBdVncSa99albAR_z&e3Bip4s",            "fromURLHost":"gx.news.163.com",            "currentIndex":"",            "width":364,            "height":365,            "type":"jpeg",            "filesize":"",            "bdSrcType":"0",            "di":"243980",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2018-04-01 19:13",            "fromPageTitle":"昨日平果和谐小区内一七旬<strong>老人<\/strong>在家中摔倒",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "534424503,56606182",            "os" : "381249331,3822051004",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=1381718164,1833961067&fm=26&gp=0.jpg","middleURL":"https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=1381718164,1833961067&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=1381718164,1833961067&fm=26&gp=0.jpg",            "pageNum":58,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fpic1.nmgnews.com.cn%2F0%2F11%2F43%2F28%2F11432845_281123.jpg&refer=http%3A%2F%2Fpic1.nmgnews.com.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=3f5fc2dbad517e8f77c571aba0fc0fcd",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Fooo_z&e3Bg42gjof_z&e3Bv54_z&e3BvgAzdH3Fy7q7wgq7AzdH3Ffyfpj4AzdH3Fda80AzdH3Fa8AzdH3F88AzdH3Fa8dd989d8_z&e3Bfip4s",            "fromURLHost":"www.nmgnews.com.cn",            "currentIndex":"",            "width":550,            "height":347,            "type":"jpg",            "filesize":"",            "bdSrcType":"0",            "di":"225830",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2019-05-30 00:00",            "fromPageTitle":"<strong>老人<\/strong>骑车摔倒 众人出手相助",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "1381718164,1833961067",            "os" : "3404854801,1446321998",            "source_type":"",            "adPicId":"0"        },{"thumbURL":"https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2760752991,4187216326&fm=26&gp=0.jpg","middleURL":"https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2760752991,4187216326&fm=26&gp=0.jpg",            "largeTnImageUrl":"",            "hasLarge" :0,            "hoverURL":"https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2760752991,4187216326&fm=26&gp=0.jpg",            "pageNum":59,            "objURL":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fphotoshow.108sq.cn%2Fuser%2F2017%2F1116%2F12171883836333506035141870.jpg&refer=http%3A%2F%2Fphotoshow.108sq.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1620389150&t=e5b97120a26b811d5c7af8fc2cfbab0f",            "fromURL":"ippr_z2C$qAzdH3FAzdH3Ffijg2zi57_z&e3B8abfq_z&e3BvgAzdH3Ffi75AzdH3F1jpwtsAzdH3Fdncdd9bc",            "fromURLHost":"shengzhou.108sq.cn",            "currentIndex":"",            "width":600,            "height":800,            "type":"jpg",            "filesize":"",            "bdSrcType":"0",            "di":"63250",            "pi":"0",            "is":"0,0",            "partnerId":0,            "bdSetImgNum":0,            "bdImgnewsDate":"2017-10-21 21:49",            "fromPageTitle":"<strong>老人摔倒<\/strong>",            "bdSourceName":"",            "bdFromPageTitlePrefix":"",            "isAspDianjing":0,            "token":"",            "imgType" : "",            "cs" : "2760752991,4187216326",            "os" : "1107100922,625775333",            "source_type":"",            "adPicId":"0"        },{}]});
    flip.setData('fcadData', {"fcData":[],"fcMidData":[],"fcBtData":[],"fcType":"","adType":0,"fcAdDatasLen":"0"}
);
    flip.setData('albumBannerData', [    {        "type": 'album',        "showLabel": "0",        "thumbURL": "https:\/\/emoji.cdn.bcebos.com\/yunque\/hejirukou.jpg",        "width": "240",        "height": "380",        "pageNum": 0,        "tab": "设计素材",        "albumId": "283",        "isQueryHit": "0"    }]);
    flip.setData('xgMidData', {"xgMidData":[],"xgMidDataLen":"0"});
    flip.setData('rpData', {"data": []});
    flip.setData('browserRsData', {    "Status" : "0",    "query" : "",    "desc" : "",    "id" : "",    "photos" :[]}
);
    flip.setData('rsQuery', [["老人住院", "%C0%CF%C8%CB%D7%A1%D4%BA", "0", "0"],["老人受伤", "%C0%CF%C8%CB%CA%DC%C9%CB", "0", "0"],["老人骑车摔倒", "%C0%CF%C8%CB%C6%EF%B3%B5%CB%A4%B5%B9", "0", "0"],["老奶奶摔倒了", "%C0%CF%C4%CC%C4%CC%CB%A4%B5%B9%C1%CB", "0", "0"],["老人摔倒 真实", "%C0%CF%C8%CB%CB%A4%B5%B9%20%D5%E6%CA%B5", "0", "0"],["老人摔倒讹人", "%C0%CF%C8%CB%CB%A4%B5%B9%B6%EF%C8%CB", "0", "0"],["医院老人", "%D2%BD%D4%BA%C0%CF%C8%CB", "0", "0"],["扶老人卡通", "%B7%F6%C0%CF%C8%CB%BF%A8%CD%A8", "0", "0"],["老人摔倒卡通图片", "%C0%CF%C8%CB%CB%A4%B5%B9%BF%A8%CD%A8%CD%BC%C6%AC", "0", "0"],["老人中风", "%C0%CF%C8%CB%D6%D0%B7%E7", "0", "0"],["扶起老人", "%B7%F6%C6%F0%C0%CF%C8%CB", "0", "0"],["冬天摔倒", "%B6%AC%CC%EC%CB%A4%B5%B9", "0", "0"],["摔倒卡通", "%CB%A4%B5%B9%BF%A8%CD%A8", "0", "0"],["人摔倒", "%C8%CB%CB%A4%B5%B9", "0", "0"],["老人卡通", "%C0%CF%C8%CB%BF%A8%CD%A8", "0", "0"],["老人摔倒卡通", "%C0%CF%C8%CB%CB%A4%B5%B9%BF%A8%CD%A8", "0", "0"],["老人散步", "%C0%CF%C8%CB%C9%A2%B2%BD", "0", "0"],["骑车摔倒", "%C6%EF%B3%B5%CB%A4%B5%B9", "0", "0"],["扶老人", "%B7%F6%C0%CF%C8%CB", "0", "0"],["老人摔倒无人扶", "%C0%CF%C8%CB%CB%A4%B5%B9%CE%DE%C8%CB%B7%F6", "0", "0"],["老人腰痛", "%C0%CF%C8%CB%D1%FC%CD%B4", "0", "0"],["老人摔倒骨折", "%C0%CF%C8%CB%CB%A4%B5%B9%B9%C7%D5%DB", "0", "0"],["老人在家", "%C0%CF%C8%CB%D4%DA%BC%D2", "0", "0"],["老人晚上睡觉", "%C0%CF%C8%CB%CD%ED%C9%CF%CB%AF%BE%F5", "0", "0"],["老人摔跤", "%C0%CF%C8%CB%CB%A4%F5%D3", "0", "0"],["老人摔倒图片", "%C0%CF%C8%CB%CB%A4%B5%B9%CD%BC%C6%AC", "0", "0"],["老人家中摔倒", "%C0%CF%C8%CB%BC%D2%D6%D0%CB%A4%B5%B9", "0", "0"],["老人在家摔倒", "%C0%CF%C8%CB%D4%DA%BC%D2%CB%A4%B5%B9", "0", "0"],["独居老人", "%B6%C0%BE%D3%C0%CF%C8%CB", "0", "0"],["老人摔倒扶不扶", "%C0%CF%C8%CB%CB%A4%B5%B9%B7%F6%B2%BB%B7%F6", "0", "0"]]);
    flip.setData('hotWords', [{            "query": "重庆4.8级地震",            "flag": "重庆4.8级地震",            "url": "http:\/\/image.baidu.com\/search\/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=sugrec&sf=1&fmq=1452955267929_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E9%87%8D%E5%BA%864.8%E7%BA%A7%E5%9C%B0%E9%9C%87",            "hot": "0",            "fromurl": "",            "photos": []        },{            "query": "内蒙古现罕见日柱",            "flag": "内蒙古现罕见日柱",            "url": "http:\/\/image.baidu.com\/search\/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=sugrec&sf=1&fmq=1452955267929_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%86%85%E8%92%99%E5%8F%A4%E7%8E%B0%E7%BD%95%E8%A7%81%E6%97%A5%E6%9F%B1",            "hot": "0",            "fromurl": "",            "photos": []        },{            "query": "女歌手本兮22岁逝世",            "flag": "女歌手本兮22岁逝世",            "url": "http:\/\/image.baidu.com\/search\/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=sugrec&sf=1&fmq=1452955267929_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%A5%B3%E6%AD%8C%E6%89%8B%E6%9C%AC%E5%85%AE22%E5%B2%81%E9%80%9D%E4%B8%96",            "hot": "0",            "fromurl": "",            "photos": []        },{            "query": "蒋劲夫托举佟丽娅",            "flag": "蒋劲夫托举佟丽娅",            "url": "http:\/\/image.baidu.com\/search\/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=sugrec&sf=1&fmq=1452955267929_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E8%92%8B%E5%8A%B2%E5%A4%AB%E6%89%98%E4%B8%BE%E4%BD%9F%E4%B8%BD%E5%A8%85",            "hot": "0",            "fromurl": "",            "photos": []        },{            "query": "打工钱被咬成碎片",            "flag": "打工钱被咬成碎片",            "url": "http:\/\/image.baidu.com\/search\/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=sugrec&sf=1&fmq=1452955267929_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E6%89%93%E5%B7%A5%E9%92%B1%E8%A2%AB%E5%92%AC%E6%88%90%E7%A2%8E%E7%89%87",            "hot": "0",            "fromurl": "",            "photos": []        },{            "query": "村民发现奇石似飞碟",            "flag": "村民发现奇石似飞碟",            "url": "http:\/\/image.baidu.com\/search\/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=sugrec&sf=1&fmq=1452955267929_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E6%9D%91%E6%B0%91%E5%8F%91%E7%8E%B0%E5%A5%87%E7%9F%B3%E4%BC%BC%E9%A3%9E%E7%A2%9F",            "hot": "0",            "fromurl": "",            "photos": []        },{            "query": "环卫夫妻身高不足一米四",            "flag": "环卫夫妻身高不足一米四",            "url": "http:\/\/image.baidu.com\/search\/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=sugrec&sf=1&fmq=1452955267929_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E7%8E%AF%E5%8D%AB%E5%A4%AB%E5%A6%BB%E8%BA%AB%E9%AB%98%E4%B8%8D%E8%B6%B3%E4%B8%80%E7%B1%B3%E5%9B%9B",            "hot": "0",            "fromurl": "",            "photos": []        },{            "query": "沙滩现巨大黑色怪物",            "flag": "沙滩现巨大黑色怪物",            "url": "http:\/\/image.baidu.com\/search\/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=sugrec&sf=1&fmq=1452955267929_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E6%B2%99%E6%BB%A9%E7%8E%B0%E5%B7%A8%E5%A4%A7%E9%BB%91%E8%89%B2%E6%80%AA%E7%89%A9",            "hot": "0",            "fromurl": "",            "photos": []        },{            "query": "黄子韬搂何炅",            "flag": "黄子韬搂何炅",            "url": "http:\/\/image.baidu.com\/search\/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=sugrec&sf=1&fmq=1452955267929_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E9%BB%84%E5%AD%90%E9%9F%AC%E6%90%82%E4%BD%95%E7%82%85",            "hot": "0",            "fromurl": "",            "photos": []        },{            "query": "2016nba圣诞大战",            "flag": "2016nba圣诞大战",            "url": "http:\/\/image.baidu.com\/search\/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=sugrec&sf=1&fmq=1452955267929_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=2016nba%E5%9C%A3%E8%AF%9E%E5%A4%A7%E6%88%98",            "hot": "0",            "fromurl": "",            "photos": []        }]);
        
    flip.init();

    });
    }();
!function(){            }();
!function(){    require.async(['common:widget/ui/monitorRequest/monitorRequest'],function(monitorRequest){
	var userid = "";
	var q = "%E8%80%81%E4%BA%BA%E6%91%94%E5%80%92";
	var tn = "result";
	var host = "//imgstat.baidu.com/4.gif";
	var hostSweb = "//image.baidu.com/pv/pv2.gif";
    var rsw = "";

    if(location.href !== document.referrer && document.referrer != ""){
        rsw = "&rs=";
    }
    else{
        rsw = '';
    }
    var samplekey = window.samplekey || '';
    var img = window["__log__" + (new Date()).getTime()*Math.random()] = document.createElement('img');
    monitorRequest( host + "?logid=11806807618841733495&ie=utf-8&q="+ q +"&userid=" + userid + "&samplekey=" + encodeURIComponent(samplekey) + "&event_type=pv&tn=" + tn + "&tpl=result_flip.page&fr=" + rsw);
    var imgSweb = window["__log__" + (new Date()).getTime()*Math.random()] = document.createElement('img');
    imgSweb.src = hostSweb + "?ie=utf-8&q="+ q +"&userid=" + userid + "&samplekey=" + encodeURIComponent(samplekey) + "&event_type=pv&tn=" + tn + "&tpl=&fr=" + rsw + '&' + new Date() * Math.random();
    });
}();
!function(){    require.async(["common:widget/ui/fmCheck/fmCheck"],function(fmCheck){
        fmCheck.init();
    });
}();
!function(){require.async(['common:widget/ui/base/base'], function($) {
    var userFrom = '';

    var elem = document.createElement('a');
    elem.href = document.referrer;
    var hostname = elem['hostname'];
    var urlfr = '';
    var chenjin = '';
    var urlword = '%E8%80%81%E4%BA%BA%E6%91%94%E5%80%92';

    if (hostname !== 'image.baidu.com') {
        if (urlfr) {
            userFrom += urlfr;
            if (chenjin === '1') {
                userFrom += 'chenjin1';
            } else if (chenjin === '0') {
                var wordList = ["%E7%BE%8E%E5%A5%B3%E5%9B%BE%E7%89%87",
                    "%E6%89%8B%E6%9C%BA%E5%A3%81%E7%BA%B8",
                    "%E6%89%8B%E6%9C%BA%E5%A3%81%E7%BA%B8%E5%9B%BE%E7%89%87",
                    "%E5%A4%B4%E5%83%8F",
                    "%E5%A4%B4%E5%83%8F%E5%9B%BE%E7%89%87"];
                if (wordList.indexOf(urlword) >= 0) {
                    userFrom += 'chenjin0';
                }
            }
        } else {
            userFrom = hostname;
        }
    } else {
        userFrom = $.cookie('userFrom') || '';
    }

    if (userFrom.length > 0) {
        var date = new Date();
        date.setTime(date.getTime() + (10 * 60 * 1000));
        $.cookie('userFrom', userFrom, {path: '/', expires: date, domain: '.baidu.com'});
    } else {
        $.cookie('userFrom', null, {path: '/', domain: '.baidu.com'});
    }
});
}();
!function(){            require.async(["common:widget/ui/durationStat/durationStat"],function(durationStat){
            durationStat.heartStart({
                pageId: 2 - 0,
                sid: '2afd4b91a3223abb91869cc0fdff06b0356201fa',
                cs: '',
                word: '老人摔倒'
            });
        });
    }();</script>   </html> 
            '''
            # 获取当前页面的图片URL
            print(requests)
            img_urls = re.findall('"objURL":"(.*?)",', result, re.S)
            print(img_urls[0])
            input()
            if len(img_urls) < 1:
                break
            # 把这些图片URL一个个下载
            for img_url in img_urls:
                # 获取图片内容
                img = requests.get(img_url, timeout=30)
                img_name = save_path + '/' + str(uuid.uuid1()) + '.jpg'
                # 保存图片
                with open(img_name, 'wb') as f:
                    f.write(img.content)
                download_sum += 1
                if download_sum >= download_max:
                    break
        except Exception as e:
            print('【错误】当前图片无法下载，%s' % e)
            download_sum += 1
            # continue
            raise
    print('下载完成')

    # 删除不是JPEG或者PNG格式的图片


def delete_error_image(father_path):
    # 获取父级目录的所有文件以及文件夹
    try:
        image_dirs = os.listdir(father_path)
        for image_dir in image_dirs:
            image_dir = os.path.join(father_path, image_dir)
            # 如果是文件夹就继续获取文件夹中的图片
            if os.path.isdir(image_dir):
                images = os.listdir(image_dir)
                for image in images:
                    image = os.path.join(image_dir, image)
                    try:
                        # 获取图片的类型
                        image_type = imghdr.what(image)
                        # 如果图片格式不是JPEG同时也不是PNG就删除图片
                        if image_type is not 'jpeg' and image_type is not 'png':
                            os.remove(image)
                            print('已删除：%s' % image)
                            continue
                        # 删除灰度图
                        img = numpy.array(Image.open(image))
                        if len(img.shape) is 2:
                            os.remove(image)
                            print('已删除：%s' % image)
                    except:
                        os.remove(image)
                        print('已删除：%s' % image)
    except:
        pass


if __name__ == '__main__':
    # 定义要下载的图片中文名称和英文名称，ps：英文名称主要是为了设置文件夹名
    key_words = {'老人摔倒': 'fall','跌倒':'fall','摔伤':'fall','老人跌倒':'fall','老人摔伤':'fall'}
    # 每个类别下载一千个
    max_sum = 500
    for key_word in key_words:
        save_name = key_words[key_word]
        download_image(key_word, save_name, max_sum)

    # 删除错误图片
    delete_error_image('images/')