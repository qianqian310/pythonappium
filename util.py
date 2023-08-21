from selenium import webdriver


# 创建并返回一个 Chromdriver 的实例
def GetT2ChromeDriver():
    options = webdriver.ChromeOptions()
    options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    driver = webdriver.Chrome(options=options)
    return driver