# qwerty：技术人网站完整解决方案

## 核心功能

+ [ ] 主页
+ [x] 博客（Blog）
+ [ ] 话题（Topic）：一个轻量级的 Github issue 管理，用于类似笔记和 Wiki 形式的记录
+ [ ] 微博（MicroBlog）：世界纷乱，不如一个人狂欢
+ [ ] 书籍（Books）：读书记录 + 简评
+ [ ] 简历（Resume）：无需华丽，但有条理

## Web Client

qwerty 只是一个服务端，目前有的客户端有：

+ [qwerty-client](https://github.com/zhangjie2012/qwerty-client)：基于 ant design pro 网页客户端，【官方版本】

## 使用教程

### 本地调试与上线部署

具体请查看[部署文档](./docs/deploy.md)。

### 数据迁移

因为数据迁移属于高危操作，所以所有的 API 调用时需要填写 get 参数`token`，token 可以在 config 文件的 `server` 下设置。

#### 备份与恢复

1. 调用 API `/datamgr/backup_all` 备份数据，备份数据的路径在 config 文件的 `backup` 下配置（注意：备份时会清空文件夹）
2. 恢复 API _TODO_

#### 如何从 Jekyll 博客迁移到 qwerty？

1. 将 Jekyll 的 `_posts` 置于 qwerty server 可被访问的目录下
2. `POST` 调用 API `/datamgr/import_jekyll_content` 执行导入操作，request body 为 `{"dst_dir": "_posts path"}`

注意：qwerty 不支持静态资源，如果原博客使用了图片资源，请将图片提交到云存储上，然后手动修改文章内容使之生效。

## 版本更新记录

### v0.0.1

只支持完整博客模块的版本。
