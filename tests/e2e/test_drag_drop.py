

def test_drag_a_to_b(drag_drop_page):
    drag_drop_page.navigate("https://the-internet.herokuapp.com/drag_and_drop")
    drag_drop_page.drag_a_to_b()
    assert drag_drop_page.get_header("A") == "B"
    assert drag_drop_page.get_header("b") == "A"