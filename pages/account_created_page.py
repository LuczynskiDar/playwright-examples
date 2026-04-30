
from base_page import BasePage

class AccountCreatedPage(BasePage):
    ACCOUNT_CREATED_LOCATOR ='h2[data-qa="account-created"]'
    CONTINUE_BUTTON = 'a[data-qa="continue-button"]'
    def get_success(self):
        return self.page.locator(self.ACCOUNT_CREATED_LOCATOR).inner_text() 
    
    def continue_button(self):
        self.page.locator(self.CONTINUE_BUTTON).click()