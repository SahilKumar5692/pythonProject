import time
import allure
from allure_commons.types import AttachmentType
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from Insta_lib import *


driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
#Login
driver.find_element_by_id("com.instagram.android:id/one_tap_log_in_button").click()
time.sleep(10)

Act_name = driver.current_activity

#Open Profile
driver.find_element_by_id("com.instagram.android:id/tab_avatar").click()
driver.implicitly_wait(5)
take_screenshot("Logged in", Act_name, driver)

# Updating Profile Picture
driver.find_element_by_accessibility_id("Profile picture of testinsta578").click()
time.sleep(2)
take_screenshot("Profile Page", Act_name, driver)

driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.ListView/android.widget.Button[1]/android.widget.LinearLayout/android.widget.TextView").click()
time.sleep(5)

#Touch Action
action = TouchAction(driver)
action.tap(x=210, y=1560).perform()
time.sleep(5)

#Selecting Profile Pic
driver.find_element_by_accessibility_id("Next").click()
action.tap(x=1000, y=1520).perform()
action.tap(x=1000, y=1520).perform()
take_screenshot("Selecting_Image", Act_name, driver)

#Updating Profile Pic
driver.find_element_by_id("com.instagram.android:id/next_button_imageview").click()
driver.implicitly_wait(10)
take_screenshot("Profile Pic Uploaded", Act_name, driver)

#Logging Out
time.sleep(6)
driver.find_element_by_id("com.instagram.android:id/tab_avatar").click()

Logout(driver, action)
time.sleep(3)

#status
take_screenshot("Logged_out", Act_name, driver)


