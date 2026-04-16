import pytest
from pages.login_page import LoginPage
from pages.secure_area_page import SecureAreaPage   


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720},
    }

@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def secure_area_page(page):
    return SecureAreaPage(page)