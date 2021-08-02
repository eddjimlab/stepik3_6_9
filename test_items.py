import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_has_add_button(browser):
    print(browser)
    browser.get(link)
    time.sleep(3) # IMHO 30 is too much, but you free to change it
    assert len(browser.find_elements_by_class_name('btn-add-to-basket')) > 0, "No button element found!!!"
    # assert len(browser.find_elements_by_class_name('btn-add-to-basket1')) > 0, "No button element found!!!"
