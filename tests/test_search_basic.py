"""
Basic Search test.
"""

def test_basic_search(browser):
    browser.find_element_by_link_text("Search").click()
    browser.find_element_by_id("main-search-submit")