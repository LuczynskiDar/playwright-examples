


import pytest

@pytest.mark.parametrize('details',[(
    {
        'name':'test_42b7b3cb',
        'email':'test_42b7b3cb@test.com',
        'password':'Test1234!',
    }
    
)])
def test_login_ae(signup_page, details):
    
    signup_page.navigate('https://automationexercise.com')
    signup_page.accept_cookies()
    signup_page.navbar_login()
    signup_page.login(email=details['email'],password=details['password'])
    assert signup_page.is_logout_exists()
    assert signup_page.check_logged_as() == details['name']