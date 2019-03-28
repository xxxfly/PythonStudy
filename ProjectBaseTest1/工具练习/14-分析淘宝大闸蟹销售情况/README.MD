# 分析淘宝中秋月饼销售情况

### 工具&模块
#### 工具:Python3.7
#### 模块: requests、jieba、matplotlib、wordcloud、imread、pandas、numpy 等。

### Response对象的属性
 - **r.status_code HTTP请求的返回状态，200表示连接成功，404表示失败 ；**
 - **r.text HTTP响应内容的字符串形式，即url对应的页面内容；**
 - **r.encoding 从HTTP header中猜测的响应内容编码方式；**
 - **r.apparent_encoding 从内容中分析出的响应内容编码方式（备选编码方式）**


### 数据清洗
