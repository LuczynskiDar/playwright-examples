

import pytest


@pytest.mark.parametrize('details',[(
    {
        'title':"1",         
        'name':'',
        'password':'',
        'newsletter':True,
        'optin':False,
        'days':"10",
        'months':"5",
        'years':"1990",
        'first_name':"Jan",
        'last_name':"Kowalski",
        'company':"TestCo",
        'address1':"ul. Testowa 1",
        'address2':"",
        'country':"United States",
        'state':"California",
        'city':"Los Angeles",
        'zipcode':"90001",
        'mobile_number':"123456789",
    }
)])
def test_signup_page(signup_page, account_details_page, account_created_page, details):
    
    signup_page.navigate('https://automationexercise.com')
    signup_page.accept_cookies()
    signup_page.navbar_login()
    signup_page.signup(email=signup_page.get_email(), name=signup_page.get_name())
    
    details['name'] = signup_page.get_name()
    details['password'] = "Test1234!"
    
    account_details_page.fill_form(**details)
    
    assert account_created_page.get_success() == 'ACCOUNT CREATED!'
