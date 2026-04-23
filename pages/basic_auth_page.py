
from pages.base_page import BasePage

class BasicAuthPage(BasePage):
    
    def get_success_message(self) -> str:
        return self.page.locator("div.example p").inner_text()
