
def test_clear_and_retype(iframe_page):
    iframe_page.navigate("https://the-internet.herokuapp.com/iframe")
    text = "My test text"
    iframe_page.clear_and_type(text)
    content = iframe_page.get_content()
    assert content == text

def test_type_in_iframe(iframe_page):
    iframe_page.navigate("https://the-internet.herokuapp.com/iframe")
    text = "Another test text"
    frame =iframe_page.get_frame()
    frame.locator(iframe_page.ELEMENT_LOCATOR).fill(text)
    content = iframe_page.get_content()
    assert content == text