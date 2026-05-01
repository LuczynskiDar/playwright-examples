from base_page import BasePage

class ContactUsPage(BasePage):
    NAME_LOCATOR = 'input[data-qa="name"]'
    EMAIL_LOCATOR = 'input[data-qa="email"]'
    SUBJECT_LOCATOR = 'input[data-qa="subject"]'
    MESSAGE_LOCATOR = 'textarea[data-qa="message"]'
    FILE_UPLOAD_LOCATOR = 'input[type="file"]'
    SUBMIT_BUTTON = 'input[data-qa="submit-button"]'
    SUBMIT_SUCCESS_LOCATOR = 'div .status.alert.alert-success'
    HOME_BUTTON_LOCATOR = 'a.btn.btn-success'
    
    def fill_form(self, name: str, email: str, subject: str, message: str):
        self.page.fill(self.NAME_LOCATOR, name)
        self.page.fill(self.EMAIL_LOCATOR, email)
        self.page.fill(self.SUBJECT_LOCATOR, subject)
        self.page.fill(self.MESSAGE_LOCATOR, message)
  
    def upload_file(self, file_path: str):
        self.page.set_input_files(self.FILE_UPLOAD_LOCATOR, file_path)
    
    def submit_button(self):
        self.page.click(self.SUBMIT_BUTTON)      
    
    def is_submit_successful(self):
        return self.page.locator(self.SUBMIT_SUCCESS_LOCATOR).inner_text().strip() == 'Success! Your details have been submitted successfully.'
    
    def home_button(self):
        self.page.click(self.HOME_BUTTON_LOCATOR)
    
    def trigger_confirm(self, action: str):
        handler = lambda dialog: dialog.accept() if action == "accept" else dialog.dismiss()
        self.page.on("dialog", handler)