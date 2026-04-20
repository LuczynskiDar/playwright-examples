import pytest
from pages.alerts_page import AlertsPage
from pages.checkboxes_page import CheckboxesPage
from pages.drag_drop_page import DragDropPage
from pages.dropdown_page import DropdownPage
from pages.iframe_page import IframePage
from pages.login_page import LoginPage
from pages.secure_area_page import SecureAreaPage   
from unittest.mock import MagicMock

from pages.tables_page import TablesPage

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


@pytest.fixture
def checkboxes_page(page):
    return CheckboxesPage(page)

@pytest.fixture
def dropdown_page(page):
    return DropdownPage(page)

@pytest.fixture
def tables_page(page):
    return TablesPage(page)

@pytest.fixture
def alerts_page(page):
    return AlertsPage(page)


@pytest.fixture
def drag_drop_page(page):
    return DragDropPage(page)

@pytest.fixture
def iframe_page(page):
    return IframePage(page)
