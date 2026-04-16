
import pytest
from pages.login_page import LoginPage
from pages.secure_area_page import SecureAreaPage
from playwright.sync_api import expect

SUCCESS_FLASH = 'div.flash.success'

@pytest.mark.smoke
def test_logout(login_page: LoginPage, secure_area_page: SecureAreaPage):
    # Arrange
    # Act
    login_page.navigate("https://the-internet.herokuapp.com/login")
    login_page.login("tomsmith", "SuperSecretPassword!")    
    secure_area_page.logout()
    # Assert
    expect(secure_area_page.locator(SUCCESS_FLASH)).to_be_visible()
