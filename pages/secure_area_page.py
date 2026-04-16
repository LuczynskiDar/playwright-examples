

from pages.base_page import BasePage


class SecureAreaPage(BasePage):
       
    LOGOUT_BUTTON = 'a.button.secondary.radius'

    def logout(self):
        self.page.click(self.LOGOUT_BUTTON)