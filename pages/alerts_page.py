from pages.base_page import BasePage

class AlertsPage(BasePage):
    
    ALERT_BUTTON_LOCATOR = 'button[onclick="jsAlert()"]'
    CONFIRM_BUTTON_LOCATOR = 'button[onclick="jsConfirm()"]'
    PROMPT_BUTTON_LOCATOR = 'button[onclick="jsPrompt()"]'
    RESULT_TEXT_LOCATOR = 'p#result'
    
    def trigger_alert(self):
        self.page.on("dialog", lambda dialog: dialog.accept())
        return self.page.locator(self.ALERT_BUTTON_LOCATOR).click()
    
    def trigger_confirm(self, action: str):
        handler = lambda dialog: dialog.accept() if action == "accept" else dialog.dismiss()
        self.page.on("dialog", handler)
        return self.page.locator(self.CONFIRM_BUTTON_LOCATOR).click()
    
    def trigger_prompt(self, text: str):
        handler = lambda dialog: dialog.accept(text)
        self.page.on("dialog", handler)
        self.page.locator(self.PROMPT_BUTTON_LOCATOR).click()
    
    def get_result_text(self) -> str:
        return self.page.locator(self.RESULT_TEXT_LOCATOR).inner_text().strip()
