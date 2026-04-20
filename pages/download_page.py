from pages.base_page import BasePage
from pathlib import Path

class DownloadPage(BasePage):
    FILE_LINKS_LOCATOR = 'div.example a'
    
    def download_file(self, filepath: str):
        filename= Path(filepath).name
        with self.page.expect_download() as download_info:
            self.page.locator(self.FILE_LINKS_LOCATOR).get_by_text(filename, exact=True).click()
        download = download_info.value
        download.save_as(filepath)
            
  
    def get_file_links(self) -> list[str]:
        return self.page.locator(self.FILE_LINKS_LOCATOR).all_inner_texts()
    
    