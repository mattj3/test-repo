"""
Add note test via UI. 
"""

import time

def test_add_note(browser, config):
    browser.get(config["url"] + "/matters/" + config["matter_id"] + "/notes")

    browser.find_element_by_xpath('//button[text()="Add A Note"]').click()

    browser.find_element_by_id("message").send_keys("Test Note " + str(time.time()))

    browser.find_element_by_id("form-submit").click()
    
    assert browser.find_element_by_xpath("//div[contains(., 'Note created at')]")