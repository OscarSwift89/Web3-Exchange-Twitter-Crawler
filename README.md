# Weex-Twitter

使用 Python 编写的爬虫，自动搜索 Weex 在 Twitter 上的相关内容并搜集数据。

## 功能简介

- 自动登录 Twitter 账户
- 搜索指定关键词（默认 `Weex`）
- 抓取并保存相关推文数据，包括推文内容、作者、发布时间等

## 目录结构

```plaintext
Weex-Twitter/
│
├── main.py                 # 主程序入口
├── login.py                # 登录功能模块
├── search.py               # 搜索功能模块
├── requirements.txt        # 依赖库列表
├── README.md               # 项目说明文档
└── chromedriver.exe        # ChromeDriver 执行文件

