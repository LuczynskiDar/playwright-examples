


def test_basic_auth_success(basicauth_page):
    basicauth_page.navigate("https://admin:admin@the-internet.herokuapp.com/basic_auth")
    message = basicauth_page.get_success_message()   
    assert message == 'Congratulations! You must have the proper credentials.'