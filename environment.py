from selenium import webdriver

def before_all(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

def before_scenario(context, scenario):
    context.driver.get("https://magento.softwaretestingboard.com/")

def after_all(context):
    context.driver.quit()