

def test_products(signup_page, products_page, product_details_page):
    signup_page.navigate('https://automationexercise.com')
    signup_page.accept_cookies()
    signup_page.navbar_products()
    assert products_page.get_product_count() > 0
    products_page.go_to_product_by_index(0)
    assert product_details_page.get_product_name() == 'Blue Top'
    assert product_details_page.get_category() == 'Category: Women > Tops'
    assert product_details_page.get_price() == 'Rs. 500'
    assert product_details_page.get_availability() == 'Availability: In Stock'    