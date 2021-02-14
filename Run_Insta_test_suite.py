import allure
from allure_commons.types import AttachmentType
from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
from Insta_lib import *


def test_invoke():
    driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
    driver.implicitly_wait(5)
    status = driver.find_element_by_id("com.instagram.android:id/login_landing_logo").is_displayed()

    if status == True:
        assert True
    else:
        assert False

    allure.attach(driver.get_screenshot_as_png(), name="InstaAppLaunched", attachment_type=AttachmentType.PNG)

def test_search_profile_and_follow():
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
    # Login into app
    driver.find_element_by_id("com.instagram.android:id/one_tap_log_in_button").click()
    time.sleep(10)


    allure.attach(driver.get_screenshot_as_png(), name= "Welcome_screen", attachment_type=AttachmentType.PNG)

    # Search Instagram Profile of Joe Biden
    driver.find_element_by_accessibility_id("Search and Explore").click()
    driver.find_element_by_id("com.instagram.android:id/action_bar_search_edit_text").click()
    driver.find_element_by_id("com.instagram.android:id/action_bar_search_edit_text").send_keys("Joe Biden")
    time.sleep(5)

    # Follow Instagram Profile of Joe Biden
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView").click()
    time.sleep(5)
    action = TouchAction(driver)

 #   take_screenshot("Profile JoeBiden", Act_name, driver)
    allure.attach(driver.get_screenshot_as_png(), name= "Profile_Joe_Biden", attachment_type=AttachmentType.PNG)

   # element_2 = driver.find_element_by_accessibility_id("Follow Joe Biden").click()
    driver.find_element_by_accessibility_id("Follow Joe Biden").click()
    time.sleep(5)

#Check status change from Follow to Following
    status_1 = driver.find_element_by_accessibility_id("Following Joe Biden").is_displayed()
    if status_1 == True:
        assert True
    else:
        assert False
    print("true")
 #   take_screenshot("Now following Joe", Act_name, driver)
    allure.attach(driver.get_screenshot_as_png(), name= "Now_following_Joe", attachment_type=AttachmentType.PNG)
    action = TouchAction(driver)
    time.sleep(2)
    print("ok")
    driver.find_element_by_id("com.instagram.android:id/tab_avatar").click()
    print("logout now")
    Logout(driver, action)

def test_upload_profile_picture():
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
    # Login
    driver.find_element_by_id("com.instagram.android:id/one_tap_log_in_button").click()
    time.sleep(10)

#    Act_name = driver.current_activity

    # Open Profile
    driver.find_element_by_id("com.instagram.android:id/tab_avatar").click()
    driver.implicitly_wait(5)
#   take_screenshot("Logged in", Act_name, driver)
    allure.attach(driver.get_screenshot_as_png(), name= "Logged_In", attachment_type=AttachmentType.PNG)

    # Updating Profile Picture
    driver.find_element_by_accessibility_id("Profile picture of testinsta578").click()
    time.sleep(2)
#    take_screenshot("Profile Page", Act_name, driver)
    allure.attach(driver.get_screenshot_as_png(), name= "Profile_Page", attachment_type=AttachmentType.PNG)

    driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.ListView/android.widget.Button[1]/android.widget.LinearLayout/android.widget.TextView").click()
    time.sleep(5)

    # Touch Action
    action = TouchAction(driver)
    action.tap(x=210, y=1560).perform()
    time.sleep(5)

    # Selecting Profile Pic
    driver.find_element_by_accessibility_id("Next").click()
    action.tap(x=1000, y=1520).perform()
    action.tap(x=1000, y=1520).perform()
#   take_screenshot("Selecting_Image", Act_name, driver)
    allure.attach(driver.get_screenshot_as_png(), name= "Selecting_Image", attachment_type=AttachmentType.PNG)

    # Updating Profile Pic
    driver.find_element_by_id("com.instagram.android:id/next_button_imageview").click()
    time.sleep(3)
#    take_screenshot("Profile Pic Uploaded", Act_name, driver)
    allure.attach(driver.get_screenshot_as_png(), name= "Profile_pic_uploaded", attachment_type=AttachmentType.PNG)


    # Logging Out
    Logout(driver, action)
    time.sleep(3)
    Logged_out = driver.find_element_by_id("com.instagram.android:id/login_landing_logo").is_displayed()

    if Logged_out == True:
        assert True
    else:
        assert False
    allure.attach(driver.get_screenshot_as_png(), name="Logged_Out", attachment_type=AttachmentType.PNG)
