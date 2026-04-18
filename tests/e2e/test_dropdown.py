
def test_select_option_1(dropdown_page):
    dropdown_page.navigate("https://the-internet.herokuapp.com/dropdown")
    dropdown_page.select_option('1')
    selected_option = dropdown_page.get_selected_option()
    assert selected_option == '1'

def test_select_option_2(dropdown_page):
    dropdown_page.navigate("https://the-internet.herokuapp.com/dropdown")
    dropdown_page.select_option('2')
    selected_option = dropdown_page.get_selected_option()
    assert selected_option == '2'