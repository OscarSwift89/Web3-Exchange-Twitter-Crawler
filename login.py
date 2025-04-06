from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver, username, password):
    """
    登录Twitter账户
    :param driver: WebDriver实例
    :param username: Twitter用户名
    :param password: Twitter密码
    """
    # 打开Twitter登录页面
    driver.get("https://twitter.com/login")

    # 等待用户名输入框出现并输入用户名
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "text")))
    username_input = driver.find_element(By.NAME, "text")
    username_input.send_keys(username)

    # 点击下一个按钮
    driver.find_element(By.XPATH, '//span[text()="Next"]').click()

    # 等待密码输入框出现并输入密码
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys(password)

    # 点击登录按钮
    driver.find_element(By.XPATH, '//span[text()="Log in"]').click()

    # 等待页面加载
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@data-testid="SearchBox_Search_Input"]')))
    print("Logged in successfully.")

#测试