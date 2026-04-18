from pages.base_page import BasePage


class CheckboxesPage(BasePage):
    
    CHECKBOX_LOCATOR = 'form#checkboxes input[type="checkbox"]'
    
    def _checked_locator(self, index: int):
        return self.page.locator(self.CHECKBOX_LOCATOR).nth(index)
    
    def is_checked(self, index: int) -> bool:
        checkbox = self._checked_locator(index)
        return checkbox.is_checked()
    def toggle(self, index: int):
        checkbox = self._checked_locator(index)
        checkbox.click()