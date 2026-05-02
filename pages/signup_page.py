from collections import namedtuple

from base_page import BasePage
import uuid

from pages import PageRole

class SignupPage(BasePage):
       
    SIGNUP_LOCATOR = ".nav.navbar-nav a[href='/login']"
    # page.get_by_role("link", name="Signup / Login")
    
    LOGIN_EMAIL_LOCATOR = "input[type='email'][data-qa='login-email']"
    LOGIN_PASSWORD_LOCATOR = "input[type='password'][data-qa='login-password']"
    BUTTON_LOGIN = 'button[type="submit"][data-qa="login-button"]'
    
    SIGNUP_NAME_LOCATOR = "input[type='text'][data-qa='signup-name']"
    SIGNUP_EMAIL_LOCATOR = "input[type='email'][data-qa='signup-email']"
    BUTTON_SIGNUP = 'button[type="submit"][data-qa="signup-button"]'
       
    COOKIE_ACCEPT = 'button.fc-button.fc-cta-consent'
    
    LOGOUT_LOCATOR = 'a[href="/logout"]'
    LOGGED_USER_LOCATOR = 'a:has-text("Logged in as") b'

    DELETE_ACCOUNT ='a[href="/delete_account"]'
    
    CONTACT_US = 'a[href="/contact_us"]'
    PRODUCTS = 'a[href="/products"]'
    PRODUCTS_ROLE = PageRole(role='link', name="Products")
  
    def __init__(self, page):
        super().__init__(page)
        self.name = f"test_{uuid.uuid4().hex[:8]}"
        self.email = f"{self.name}@test.com"
           
    def get_name(self) -> str:
        return self.name
    
    def get_email(self) -> str:
        return self.email
    
    def navbar_login(self):
        self.page.click(self.SIGNUP_LOCATOR)
        return self.email
    
    def navbar_contact_us(self):
        self.page.click(self.CONTACT_US)
    
    def navbar_products(self):
        self.page.get_by_role(self.PRODUCTS_ROLE.role, name=self.PRODUCTS_ROLE.name).click()
    
    def signup(self, name: str, email: str):
        self.page.fill(self.SIGNUP_NAME_LOCATOR, name) 
        self.page.fill(self.SIGNUP_EMAIL_LOCATOR, email)
        self.page.click(self.BUTTON_SIGNUP)   
     
    def login(self, email: str, password: str):
        self.page.fill(self.LOGIN_EMAIL_LOCATOR, email)
        self.page.fill(self.LOGIN_PASSWORD_LOCATOR, password)
        self.page.click(self.BUTTON_LOGIN)
    
    def accept_cookies(self):
        consent = self.page.locator(self.COOKIE_ACCEPT)
        if consent.is_visible():
            consent.click()
    
    def is_logout_exists(self) -> bool:
        return self.page.locator(self.LOGOUT_LOCATOR).is_visible()
    
    def check_logged_as(self) -> str:
        return self.page.locator(self.LOGGED_USER_LOCATOR).inner_text().strip()
    
    def delete_account(self):
        self.page.click(self.DELETE_ACCOUNT)