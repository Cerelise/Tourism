# tourism_api

主机地址

http:127.0.0.1:9000/api/

## 用户

### 登录

- token/create
- POST



## 景点

### 获取景点列表

- attractions/list
- GET



### 添加景点

- attractions/list
- POST



### 获取某个景点信息

- attractions/detail/<attraction_id>
- attraction_id 景点id
- GET



### 删除某个景点信息

- attractions/detail/<attraction_id>
- attraction_id 景点id
- DELETE



## 景点文章

### 获取景点文章列表

- attractions/article/list
- GET



### 添加景点文章

- attractions/article/list
- POST



### 获取某一篇景点文章

- attractions/article/detail/<article_id>
- article_id 文章id
- GET



### 删除某一篇景点文章

- attractions/article/detail/<article_id>
- article_id 文章id
- DELETE



### 获取景区类别

- attractions/scentic
- GET



## 问答

### 添加分类

- category/list
- POST



### 获取分类列表

- category/list
- GET



### 获取某个分类的问答

- category/detail/<category_id>
- category_id 分类id
- GET



### 删除某个分类

- category/detail/<category_id>
- category_id 分类id
- DELETE

### 获取问答列表

- question/list/
- GET



### 添加问答

- question/add/<category_id>
- category_id 分类id
- POST



### 删除某个问答

- question/delete/<question_id>
- question_id 问答的id



## 主页

### 获取所有主页

- home/list
- GET

### 添加主页

- home/list
- POST

### 获取某个主页

- home/detail/<home_id>
- home_id 主页id
- GET

### 删除某个主页

- home/detail/<home_id>

- home_id 主页id

- DELETE

  

## 公告

### 获取所有公告

- /notice/list
- GET

### 添加公告

- /notice/list
- POST

### 获取某个公告

- /notice/detail/<notice_id>
- notice_id 公告id
- GET

### 删除某个公告

- /notice/detail/<notice_id>
- notice_id 公告id
- DELETE



```
{
  "pictures":"[
  	{"title":"pic4","desc":"pic4"},
  	{"title":"pic6","desc":"pic6"}
  ]"
}



```

