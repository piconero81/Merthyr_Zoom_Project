from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
driver= webdriver.Chrome(executable_path=r'C:\software\chromedriver.exe')

def delete_cache():
    driver.execute_script("window.open('');")
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(2)
    driver.get('chrome://settings/clearBrowserData') # for old chromedriver versions use cleardriverData
    time.sleep(2)
    actions = ActionChains(driver)
    #actions.send_keys(ARROW_RIGHT + keys.DOWN * 11) # send right combination
    actions.send_keys(keys.TAB * 3 + keys.DOWN * 3) # send right combination
    actions.perform()
    time.sleep(5)
    actions = ActionChains(driver)
    #actions.send_keys(keys.DOWN + ARROW_RIGHT + keys.DOWN * 11)  # send right combination
    actions.send_keys(Keys.TAB * 4 + Keys.ENTER) # confirm
    actions.perform()
    time.sleep(5) # wait some time to finish
    driver.close() # close this tab
    driver.switch_to.window(driver.window_handles[0]) # switch back
delete_cache()

