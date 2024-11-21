from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from login import login
from search import search_twitter
import sys
print(sys.path)  # 输出当前Python路径，检查是否包含文件所在的目录


def create_driver():
    """
    创建并返回一个配置好的WebDriver实例
    """
    options = Options()
    # 不使用headless模式
    options.add_argument('--disable-gpu')  # 禁用GPU加速
    options.add_argument('--no-sandbox')  # 禁用沙盒
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def main():
    # 创建WebDriver实例
    driver = create_driver()

    try:
        # 登录Twitter
        username = "your_username"  # 替换为你的用户名
        password = "your_password"  # 替换为你的密码
        login(driver, username, password)

        # 在Twitter上搜索
        search_query = "weex"  # 搜索关键词
        search_twitter(driver, search_query)

    finally:
        # 关闭浏览器
        driver.quit()

if __name__ == "__main__":
    main()
