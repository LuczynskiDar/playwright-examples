import pytest
from pages.login_page import LoginPage
from pages.secure_area_page import SecureAreaPage   
from unittest.mock import MagicMock

@pytest.fixture
def mock_page():
    return MagicMock()