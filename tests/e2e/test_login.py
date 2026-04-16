
import pytest
from pages.login_page import LoginPage
from playwright.sync_api import expect

SUCCESS_FLASH = 'div.flash.success'
ERROR_FLASH   = 'div.flash.error'

@pytest.mark.smoke
def test_login_valid_credentials(login_page: LoginPage):
    # Arrange
    # Act
    login_page.navigate("https://the-internet.herokuapp.com/login")
    login_page.login("tomsmith", "SuperSecretPassword!")
    # Assert
    expect(login_page.locator(SUCCESS_FLASH)).to_be_visible()


@pytest.mark.regression
@pytest.mark.parametrize("username,password", [
    ("invalid_user", "invalid_password"),
    ("", ""),
    ("tomsmith", "wrong_password"),
  ])
def test_login_invalid_credentials(login_page: LoginPage, username: str, password: str):
    # Arrange
    # Act
    login_page.navigate("https://the-internet.herokuapp.com/login")
    login_page.login(username, password)
    # Assert
    expect(login_page.locator(ERROR_FLASH)).to_be_visible()
    