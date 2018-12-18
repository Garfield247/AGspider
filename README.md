# 农业数据采集

## 网址

中国作物种质信息网http://www.cgris.net/query/croplist.php

## 接口

|          | API                              | Method | FormData                                                     |
| -------- | -------------------------------- | ------ | ------------------------------------------------------------ |
| 作物列表 | http://www.cgris.net/query/o.php | POST   | {   action:   menu , _: }                                    |
| 分类列表 | http://www.cgris.net/query/o.php | POST   | {   p:   {}  ,croptype:   ["%E7%B2%AE%E9%A3%9F%E4%BD%9C%E7%89%A9", "%E9%AB%98%E7%B2%B1"] , _: } |
| 详情     | http://www.cgris.net/query/o.php | POST   | {   action:   item , p:   01-00007 , croptype:   ["%E7%B2%AE%E9%A3%9F%E4%BD%9C%E7%89%A9", "%E9%AB%98%E7%B2%B1"] , _: } |

