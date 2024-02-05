# tourism

## models

### 用户(User)

自带用户



### 景点(Attractions)

- title 景点标题
- desc 景点介绍
- main_pic 主图
- map_pic 地图
- about 关于标题 
- content 关于内容 
- created_at 发布日期
- type 类型 （是否已经删除） 0 删除 1 正常 default=1



### 轮播图(swiper)

- title 图片标题
- desc 图片描述
- picture 轮播图图片
- created_at 发布日期
- related_attraction 轮播图图片  ForeignKey(swiper)



### 景区文章(Article)

- title 文章标题
- subTitle 文章副标题
- scenic 所属景区
- content 文章内容
- img 文章图片
- isTop 文章是否置顶
- created_at 发布日期

### 段落(paragraph)

- title 段落标题
- content 段落标题
- created_at 发布日期
- related_article 段落 Foreign Key



### 公告(notice)

- title 公告标题
- content 公告内容
- created_at 发布时间



### 主页(home)

- title 主页标题
- description 主页描述
- picture 图片
- created_at 发布时间



### 提问(Qusetion)

- question 问题
- answer 答案
- created_at 发布日期
- category 分类 ForeignKey



### 分类(Category)

- title 分类名称
- created_at 发布日期







 





