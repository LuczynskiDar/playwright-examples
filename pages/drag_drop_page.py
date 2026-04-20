from pages.base_page import BasePage

class DragDropPage(BasePage):
    DD_LOCATOR = '#column-'
    
    
    def drag_a_to_b(self):
        source = self.page.locator(f"{self.DD_LOCATOR}a")
        target = self.page.locator(f"{self.DD_LOCATOR}b")
        source.drag_to(target)
    
    def get_header(self, element_id: str) -> str:
        id = str.lower(element_id)
        header_locator = f"{self.DD_LOCATOR}{id}"
        self.page.wait_for_selector(header_locator)
        return self.page.locator(header_locator).inner_text().strip()