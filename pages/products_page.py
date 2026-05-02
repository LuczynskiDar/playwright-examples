from base_page import BasePage
from pages import PageRole

class ProductsPage(BasePage):
    PRODUCT = "div.features_items .product-image-wrapper"
    PRODUCT_CARD = "div.features_items div.col-sm-4"
    
    VIEW_PRODUCT = PageRole(role="link",  name="View Product")
 
    def get_product_count(self) -> int:
        return self.page.locator(self.PRODUCT).count()
    
    def go_to_product_by_index(self, index):
        self.page.get_by_role(self.VIEW_PRODUCT.role, name=self.VIEW_PRODUCT.name).nth(index).click()