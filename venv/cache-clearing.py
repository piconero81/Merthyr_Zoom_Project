from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
driver= webdriver.Chrome('c:\software\chromedriver.exe')

def delete_cache():
    driver.execute_script("window.open('');")
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[-1])
    driver.get('chrome://settings/clearBrowserData') # for old chromedriver versions use cleardriverData
    time.sleep(5)
    actions = ActionChains(driver)
    #actions.send_keys(Keys.TAB * 3 + Keys.DOWN * 3) # send right combination
    actions.send_keys(Keys.ARROW_RIGHT + Keys.TAB * 11 + Keys.ENTER)  # send right combination
    actions.perform()
    time.sleep(10)
    actions = ActionChains(driver)
    #actions.send_keys(Keys.TAB * 4 + Keys.ENTER) # confirm
    actions.perform()
    time.sleep(5) # wait some time to finish
    driver.close() # close this tab
    driver.switch_to.window(driver.window_handles[0]) # switch back
delete_cache()