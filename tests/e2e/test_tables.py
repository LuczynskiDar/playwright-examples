
def test_cell_value(tables_page):
    tables_page.navigate("https://the-internet.herokuapp.com/tables")
    cell = tables_page.get_cell(2, 2)
    assert cell == "jdoe@hotmail.com"

def test_column_values(tables_page):
    tables_page.navigate("https://the-internet.herokuapp.com/tables")
    column_values = tables_page.get_column_values(0)
    expected_values = ["Smith", "Bach", "Doe", "Conway"]
    assert column_values == expected_values