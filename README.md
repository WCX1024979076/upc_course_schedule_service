upc_course_schedule_service
中国石油大学课表提醒qq机器人服务端代码（基于nonebot+cqhttp+mysql）
配置说明
pip install -r requirements.txt

详细注解：
https://wcx1024979076.github.io/2021/02/12/%E5%AE%89%E5%8D%93%E8%AF%BE%E8%A1%A8%E5%AE%A2%E6%88%B7%E7%AB%AF+%E6%9C%8D%E5%8A%A1%E7%AB%AF%E6%B3%A8%E8%A7%A3/

插件说明
menu
说明：插件汇总，菜单

命令：{ menu | 菜单 }

base
说明：基础命令，由于目前食用的nonebot2版本builtin插件有问题，因此做了简单的重写

命令：{ say | echo } { text }

character
说明：测试用插件，(1,100) 随机数

命令：今日人品

ai
说明：百度UNIX2，图灵机器人接口

命令：""，正常对话即可

食用指北：修改目录下config内的API_KEY等

ai_100000000
说明：价值一个亿的AI核心代码，dddd

命令：ai {}

bullshit
说明：狗屁不通生成器

命令：{ bullshit | 狗屁不通 | 狗屁不通生成器 } { theme }

zhihu
说明：知乎日报

命令：{ zhihu | 知乎 | 知乎日报 }

auto_agree
说明：自动同意好友申请和加群邀请

daily_hello
说明：每日问好，用到的插件https://github.com/nonebot/plugin-apscheduler

命令：无

食用指北： 修改awesome_bot/config/config.py文件中

MRWH_GROUP = [''] # 需要通知的群列表
MRWH_SPECIAL_USER = [''] # 需要特殊提醒的群成员
TIANQI_KEY = '' #Tianqi API Key
hhsh
说明：能不能好好说话？

命令：hhsh { text text }

remaind
说明：课表提醒+手动设置提醒，课表提醒需配合课表app食用，并打开plugins/remaind/service/port.py进行端口监听;手动设置提醒在qq聊天界面发送‘提醒’，按照指示添加即可。

命令：remaind

参考于：
https://github.com/beiyuouo/plugins-for-nonebot2
