from pages.base_page import BasePage

class DropdownPage(BasePage):
    
    DROPDOWN_LOCATOR = 'select#dropdown'
    
    def _dropdown_locator(self):
        return self.page.locator(self.DROPDOWN_LOCATOR)
    
    def select_option(self, value: str):
        dropdown = self._dropdown_locator()
        dropdown.select_option(value)

    def get_selected_option(self) -> str:
        dropdown = self._dropdown_locator()
        return dropdown.input_value()