import pytest

@pytest.mark.parametrize('details', [(
    {
        'name':'test_42b7b3cb',
        'email':'test_42b7b3cb@test.com',
        'subject': 'Temporary subject',
        'message': 'Expecting positive feed back from location componets tests.'
    }

)])
def test_contact_us(signup_page, contact_us_page, tmp_path, details):
    
    signup_page.navigate('https://automationexercise.com')
    signup_page.accept_cookies()
    signup_page.navbar_contact_us()
    file_path = tmp_path / 'tmp_file.txt'
    file_path.write_text('some temp text.')
    contact_us_page.fill_form(name=details['name'], email=details['email'], subject=details['subject'], message=details['message'])
    contact_us_page.upload_file(file_path=str(file_path))
    contact_us_page.trigger_confirm('accept')
    contact_us_page.submit_button()
    assert contact_us_page.is_submit_successful()
    contact_us_page.home_button()