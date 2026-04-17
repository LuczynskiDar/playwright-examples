from unittest.mock import MagicMock
from pages.login_page import LoginPage
from pages.secure_area_page import SecureAreaPage
import pytest

@pytest.mark.smoke
@pytest.mark.parametrize("username,password", [
    ("tomsmith", "SuperSecretPassword!"),
    ("admin", "admin"),
    ("", ""),
])
def test_login_parametrized(mock_page, username, password):
    # Arrange
    login_page = LoginPage(mock_page)
    # Act
    login_page.login(username, password)
    # Assert
    mock_page.fill.assert_any_call(login_page.USERNAME_INPUT, username)
    mock_page.fill.assert_any_call(login_page.PASSWORD_INPUT, password)
    mock_page.click.assert_called_with(login_page.SUBMIT_BUTTON)
      
def test_login_calls_fill_and_click(mock_page):
    # Arrange
    login_page = LoginPage(mock_page)
    # Act
    login_page.login("tomsmith", "SuperSecretPassword!")
    # Assert
    mock_page.fill.assert_any_call(LoginPage.USERNAME_INPUT, 'tomsmith')
    mock_page.fill.assert_any_call(LoginPage.PASSWORD_INPUT, 'SuperSecretPassword!')
    mock_page.click.assert_called_with(LoginPage.SUBMIT_BUTTON)


def test_logout_calls_with_click(mock_page):
    # Arrange
    secure_area_page = SecureAreaPage(mock_page)
    # Act
    secure_area_page.logout()
    # Assert
    mock_page.click.assert_called_with(SecureAreaPage.LOGOUT_BUTTON)