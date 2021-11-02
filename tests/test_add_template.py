"""
Add template test via UI.  
"""

import time
from selenium.webdriver.support.select import Select

def test_add_template(browser, config):
    browser.get(config["url"] + "/document-templates/new")

    Select(browser.find_element_by_xpath("//select[@id='organization-id']")).select_by_index(1)

    browser.find_element_by_id("name").send_keys("Test Template " + str(time.time()))

    Select(browser.find_element_by_xpath("//select[@id='type']")).select_by_visible_text("Editable Template")

    Select(browser.find_element_by_xpath("//select[@id='page-size']")).select_by_visible_text("Legal")

    browser.switch_to.frame("html_ifr")

    browser.find_element_by_id("tinymce").send_keys("Selenium webdriver")

    browser.switch_to.default_content()

    browser.find_element_by_id("form-submit").click()
    
    assert browser.find_element_by_xpath("//p[contains(., 'Document Template created at')]")