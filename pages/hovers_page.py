from pages.base_page import BasePage

class HooversPage(BasePage):
    HOVER_LOCATOR = '.figure'
    NAME_LOCATOR = '.figcaption h5'
    
    def hover_over(self, index: int):
        self.page.locator(self.HOVER_LOCATOR).nth(index).hover()

    def get_caption(self, index: int) -> str:
        element = self.page.locator(self.HOVER_LOCATOR).nth(index)
        return element.locator(self.NAME_LOCATOR).inner_text().strip()
