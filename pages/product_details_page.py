from base_page import BasePage

class ProductDetailsPage(BasePage):
    PRODUCT_INFORMATION_LOCATOR = "div.product-information"
    
    # 'h2.Blue Top'
    # 'p Category: Women > Tops'
    # 'span.span 
    # 'p  In Stock'
    def get_product_name(self)->str:
        return self.page.locator(self.PRODUCT_INFORMATION_LOCATOR).get_by_role('heading').inner_text().strip()
    
    def get_category(self) -> str:
        return self.page.locator(self.PRODUCT_INFORMATION_LOCATOR).locator('p:has-text("Category")').inner_text().strip()
    
    def get_availability(self) -> str:
        return self.page.locator(self.PRODUCT_INFORMATION_LOCATOR).locator("p:has(b:has-text('Availability'))").inner_text().strip()

    def get_price(self)-> str:
        return self.page.locator(self.PRODUCT_INFORMATION_LOCATOR).locator("span span").inner_text().strip()
        