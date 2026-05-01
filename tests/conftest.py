import pytest
from pages.account_created_page import AccountCreatedPage
from pages.account_details_page import AccountDetailsPage
from pages.alerts_page import AlertsPage
from pages.basic_auth_page import BasicAuthPage
from pages.checkboxes_page import CheckboxesPage
from pages.contact_us_page import ContactUsPage
from pages.delete_account_page import DeleteAccountPage
from pages.download_page import DownloadPage
from pages.drag_drop_page import DragDropPage
from pages.dropdown_page import DropdownPage
from pages.hovers_page import HooversPage
from pages.iframe_page import IframePage
from pages.login_page import LoginPage
from pages.secure_area_page import SecureAreaPage   
from unittest.mock import MagicMock

from pages.signup_page import SignupPage
from pages.tables_page import TablesPage
from pages.upload_page import UploadPage

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


@pytest.fixture
def hovers_page(page):
    return HooversPage(page)


@pytest.fixture
def upload_page(page):
    return UploadPage(page)

@pytest.fixture
def download_page(page):
    return DownloadPage(page)

@pytest.fixture
def basicauth_page(page):
    return BasicAuthPage(page)

@pytest.fixture
def signup_page(page):
    return SignupPage(page)

@pytest.fixture
def account_details_page(page):
    return AccountDetailsPage(page)

@pytest.fixture
def account_created_page(page):
    return AccountCreatedPage(page)

@pytest.fixture
def delete_account_page(page):
    return DeleteAccountPage(page)

@pytest.fixture
def contact_us_page(page):
    return ContactUsPage(page)