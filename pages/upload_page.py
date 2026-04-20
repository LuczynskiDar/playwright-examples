from pages.base_page import BasePage

class UploadPage(BasePage):
    
    FILE_UPLOAD_LOCATOR = "#file-upload"
    FILE_SUBMIT_LOCATOR = "#file-submit"    
    UPLOADED_FILES_LOCATOR = "#uploaded-files"
    
    def upload_file(self, file_path: str):
        self.page.set_input_files(self.FILE_UPLOAD_LOCATOR, file_path)
        self.page.click(self.FILE_SUBMIT_LOCATOR)
        
    def get_uploaded_filename(self) -> str:
        return self.page.locator(self.UPLOADED_FILES_LOCATOR).inner_text().strip()
