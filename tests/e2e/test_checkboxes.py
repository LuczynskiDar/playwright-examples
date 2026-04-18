

CHECKBOXES_URL = "https://the-internet.herokuapp.com/checkboxes"

def test_initial_state(checkboxes_page):
    checkboxes_page.navigate(CHECKBOXES_URL)
    assert not checkboxes_page.is_checked(0)
    assert checkboxes_page.is_checked(1)
    
def test_toggle_checkbox(checkboxes_page):
    checkboxes_page.navigate(CHECKBOXES_URL)
    checkboxes_page.toggle(0)
    assert checkboxes_page.is_checked(0)
    

