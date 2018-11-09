# qwerty：技术人网站完整解决方案

## 核心功能

+ [ ] 主页
+ [ ] 博客
+ [ ] 乱记：按话题（Topic）不断追加记录，随学随记
+ [ ] 书籍：读书记录 + 简评
+ [ ] 简历：无需华丽，但有条理
+ [ ] 资源：第三方网站链接集合

## 技巧

### 从 Jekyll 导入博客到 qwerty 中

1. 将 `jekyll/_posts` 置于 qwerty server 可被访问的目录下
2. `POST` 调用 API `/blog/__import_jekyll_content` 执行导入操作，request body 为 `{"dst_dir": "_posts path"}`
