from pages.base_page import BasePage

class IframePage(BasePage):
    IFRAME_LOCATOR = 'iframe'
    ELEMENT_LOCATOR = '#tinymce'
    
    def get_frame(self):
        frame = self.page.frame_locator(self.IFRAME_LOCATOR)
        return frame
    
    def clear_and_type(self, text: str):
        frame = self.get_frame()
        element = frame.locator(self.ELEMENT_LOCATOR)
        element.fill("")
        element.fill(text)
    
    def get_content(self) -> str:
        frame = self.get_frame()
        element = frame.locator(self.ELEMENT_LOCATOR)
        return element.inner_text().strip()