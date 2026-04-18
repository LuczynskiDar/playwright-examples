from unittest.mock import MagicMock
from pages.base_page import BasePage
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
    
def test_navigate_calls_goto(mocker):
    # Arrange
    # mock_goto = mocker.patch("pages.base_page.Page")
    mock_goto = mocker.MagicMock()
    base_page = BasePage(mock_goto)
    # Act
    base_page.navigate("https://the-internet.herokuapp.com/login")
    # Assert
    mock_goto.goto.assert_called_with("https://the-internet.herokuapp.com/login")
    
def test_get_title_returns_page_title(mocker):
    # Arrange
    mock_title = mocker.MagicMock()
    mock_title.title.return_value = "Test Page Title"
    base_page = BasePage(mock_title)
    # Act
    title = base_page.get_title()
    # Assert
    assert title == "Test Page Title"

def test_navigate_raises_on_invalid_url(mocker):
    # Arrange
    mock_goto = mocker.MagicMock()
    mock_goto.goto.side_effect = Exception("Invalid URL")
    base_page = BasePage(mock_goto)
    with pytest.raises(Exception, match='Invalid URL'):
        # Act
        base_page.navigate("invalid-url")

