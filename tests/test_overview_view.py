"""
Matter Overview check.  
"""

def test_overview_view(browser, config):
    browser.get(config["url"] + "/matters/" + config["matter_id"])

    assert browser.find_element_by_xpath("//h2[contains(., 'Account Overview')]")