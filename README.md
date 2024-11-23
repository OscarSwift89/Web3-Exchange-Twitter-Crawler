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


markdown
复制代码
# Weex-Twitter

使用 Python 编写的爬虫，自动搜索 Weex 在 Twitter 上的相关内容并搜集数据。

## 目录结构

Weex-Twitter/ │ ├── main.py # 主程序入口 ├── login.py # 登录功能模块 ├── search.py # 搜索功能模块 ├── requirements.txt # 依赖库列表 ├── README.md # 项目说明文档 └── chromedriver.exe # ChromeDriver 执行文件

markdown
复制代码

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
使用说明
1. 配置环境
确保 chromedriver.exe 位于项目根目录。
将 chromedriver.exe 的路径配置到系统环境变量，或直接在代码中指定完整路径。
2. 运行项目
运行 main.py 开始抓取数据：
python main.py
3. 修改功能
登录功能：在 login.py 中修改登录流程或账户信息。
搜索功能：在 search.py 中更改搜索逻辑或关键词。
4. 数据保存
目前的数据采集逻辑支持直接打印到控制台或保存到本地文件中（CSV/JSON 格式）。可以在 search.py 文件中修改保存逻辑。

贡献指南
欢迎贡献代码！请遵循以下步骤：

Fork 本仓库
创建新的分支：git checkout -b feature/你的功能名
提交修改：git commit -m '新增功能说明'
推送到分支：git push origin feature/你的功能名
提交 Pull Request
许可协议
本项目基于 MIT License 开源，欢迎自由使用和修改。
