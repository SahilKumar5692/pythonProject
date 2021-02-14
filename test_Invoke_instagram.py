#Test 1 - Invoke Instagram App
import time
import allure
from allure_commons.types import AttachmentType
from appium import webdriver
from Insta_lib import take_screenshot


def test_invoke():
    desired_cap ={
    "deviceName": "Android Emulator",
    "platformName": "Android",
    "noReset": "true",
    "app": "C:\\Users\\sahil.k\\Downloads\\Instagram-173.0.0.39.120.apk",
    "appPackage": "com.instagram.android",
    "appWaitActivity": "com.instagram.nux.activity.SignedOutFragmentActivity",
    "newCommandTimeout": "6000"
}
    driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
    Act_name = driver.current_activity
    driver.implicitly_wait(5)
    status = driver.find_element_by_id("com.instagram.android:id/login_landing_logo").is_displayed()

    if status == True:
        assert True
    else:
        assert False

    take_screenshot("Insta App Invoked", Act_name, driver)
    allure.attach(driver.get_screenshot_as_png(), name="InstaAppLaunched", attachment_type=AttachmentType.PNG)
