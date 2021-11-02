"""
Add call test via UI.  
"""

import time
from selenium.webdriver.support.select import Select

def test_add_call(browser, config):
    browser.get(config["url"] + "/matters/" + config["matter_id"] + "/calls")

    browser.find_element_by_xpath('//button[text()="Start Call"]').click()

    browser.find_element_by_id("call-call-type-outgoing").click()

    browser.find_element_by_id("call-outbound-phone-number").send_keys("512-000-0000")

    Select(browser.find_element_by_xpath("//select[@id='call-neu-call-status']")).select_by_visible_text("N/A")

    time.sleep(0.75)

    browser.find_element_by_id("form-submit").click()
    
    assert browser.find_element_by_xpath("//p[contains(., 'Call successfully saved at')]")