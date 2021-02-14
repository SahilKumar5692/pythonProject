from Insta_lib import *


driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
#Login into app
driver.find_element_by_id("com.instagram.android:id/one_tap_log_in_button").click()
time.sleep(10)

Act_name = driver.current_activity

take_screenshot("welcome_screen", Act_name, driver)

# Search Instagram Profile of Joe Biden
element_1 = driver.find_element_by_accessibility_id("Search and Explore").click()
driver.find_element_by_id("com.instagram.android:id/action_bar_search_edit_text").click()
driver.find_element_by_id("com.instagram.android:id/action_bar_search_edit_text").send_keys("Joe Biden")
time.sleep(5)

# Follow Instagram Profile of Joe Biden
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView").click()
time.sleep(5)
action = TouchAction(driver)

take_screenshot("Profile JoeBiden", Act_name, driver)

element_2 = driver.find_element_by_accessibility_id("Follow Joe Biden").click()
time.sleep(3)

take_screenshot("Now following Joe", Act_name, driver)
time.sleep(3)
driver.find_element_by_id("com.instagram.android:id/tab_avatar").click()

Logout(driver, action)
time.sleep(3)





