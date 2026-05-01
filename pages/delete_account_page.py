from base_page import BasePage

class DeleteAccountPage(BasePage):
        
    ACCOUNT_DELETED_CONFIRMATION = 'h2[data-qa="account-deleted"] b'
    # Account Deleted!
    
    CONTINUE_BUTTON = 'a[data-qa="continue-button"]'
    
    def delete_account_confirmation(self) -> str:
        return self.page.locator(self.ACCOUNT_DELETED_CONFIRMATION).inner_text().strip()
    
    def continue_button(self):
        self.page.click(self.CONTINUE_BUTTON)
    