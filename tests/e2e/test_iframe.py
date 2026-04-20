
def test_clear_and_retype(iframe_page):
    iframe_page.navigate("https://the-internet.herokuapp.com/iframe")
    text = "My test text"
    iframe_page.clear_and_type(text)
    content = iframe_page.get_content()
    assert content == text