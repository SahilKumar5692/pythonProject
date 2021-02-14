import time
from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver


desired_cap ={
    "deviceName": "Android Emulator",
    "platformName": "Android",
    "noReset": "true",
    "app": "C:\\Users\\sahil.k\\Downloads\\Instagram-173.0.0.39.120.apk",
    "appPackage": "com.instagram.android",
    "appWaitActivity": "com.instagram.nux.activity.SignedOutFragmentActivity",
    "newCommadTimeout": "6000"
}
# Wrote another function to take screenshot which can also be used instead of taking screenshots in Allure
def take_screenshot(stepname, activityname, driver):
    ts = time.strftime("%Y_%m_%d_%H%M%S")
    activityname = driver.current_activity
    filename = activityname+ts
    driver.save_screenshot("C:/Users/sahil.k/PycharmProjects/pythonProject/Screenshots/" + stepname+ " " + filename + ".png")

#
def Logout(driver, touch):
    driver.find_element_by_accessibility_id("Options").click()
    time.sleep(3)
    driver.find_element_by_id("com.instagram.android:id/menu_settings_row").click()
    time.sleep(3)
    touch.press(x=666, y=1223).move_to(x=658, y=452).release().perform()
    time.sleep(3)
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.ListView/android.widget.Button[8]/android.widget.TextView").click()
    time.sleep(2)
    driver.find_element_by_id("com.instagram.android:id/primary_button").click()