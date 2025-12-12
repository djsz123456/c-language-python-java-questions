# C语言、Python、Java题库

一个简单的编程考试题库系统，支持C++、Python和Java三种语言的题目管理和查询。

## 功能特点

### 前台功能
- 按科目筛选题目（C++、Python、Java）
- 按题型筛选题目（选择题、填空题、编程题）
- 关键词搜索题目
- 查看题目答案和解析
- 响应式设计，支持移动端访问

### 后台功能
- 管理员登录验证
- 添加新题目
- 编辑现有题目
- 删除题目
- 通过GitHub API管理题库数据

## 项目结构

```
├── index.html          # 前台题库展示页面
├── css/
│   └── style.css       # 全局样式文件
├── data/
│   └── questions.json  # 题库数据文件
├── admin/
│   └── index.html      # 管理员后台页面
└── README.md          # 项目说明文档
```

## 部署说明

### GitHub Pages部署
1. 将项目上传到GitHub仓库
2. 进入仓库设置，开启GitHub Pages
3. 选择分支：main，路径：/(root)
4. 保存设置后即可访问

### 本地运行
1. 下载项目到本地
2. 使用本地HTTP服务器运行（避免CORS问题）
3. 示例命令：`python -m http.server 8080 --bind 127.0.0.1`

## 使用说明

### 前台访问
- 访问首页：`http://your-username.github.io/repo-name/`
- 使用筛选和搜索功能查找题目
- 点击"查看答案"按钮显示答案和解析

### 后台管理
- 访问后台：`http://your-username.github.io/repo-name/admin/`
- 默认密码：admin123456（可在admin/index.html中修改）
- 添加/编辑/删除题目来管理题库

## 技术栈

- HTML5
- CSS3
- JavaScript (ES6+)
- GitHub API

## 许可证

MIT