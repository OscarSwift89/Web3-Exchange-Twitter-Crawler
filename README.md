# Web3 Exchange Twitter Crawler 爬虫程序

使用 Python 编写的爬虫，自动搜索web3交易所在Twitter 上的相关内容并搜集数据。

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
``` 

## 环境依赖

运行此项目需要以下环境与依赖：

- **操作系统**：Windows 10 或更高版本
- **Python**：Python 3.8 或更高版本
- **浏览器**：Google Chrome (版本 131 或更高)
- **ChromeDriver**：与 Chrome 浏览器版本匹配的 [ChromeDriver](https://chromedriver.chromium.org/downloads)

### 安装依赖库

使用以下命令安装所需依赖：

```bash
pip install -r requirements.txt

requirements.txt 包含以下主要依赖库：

selenium
webdriver-manager



