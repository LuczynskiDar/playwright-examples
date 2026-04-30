from base_page import BasePage

class AccountDetailsPage(BasePage):
    
    TITLE_RADIO_GENDER = "div.radio-inline #uniform-id_gender"
    NAME = 'input[id="name"]'
    EMAIL = 'input[id="email"]'
    PASSWORD = 'input[data-qa="password"]'
    DAYS = 'select[id="days"]'
    MONTHS = 'select[id="months"]'
    YEARS = 'select[id="years"]'
    NEWSLETTER = 'input[type="checkbox"][name="newsletter"]'
    OPTIN = 'input[type="checkbox"][name="optin"]'
    FIRST_NAME = 'input[data-qa="first_name"]'
    LAST_NAME = 'input[data-qa="last_name"]'
    COMPANY = 'input[id="company"]'
    ADDRESS1 = 'input[id="address1"]'
    ADDRESS2 = 'input[id="address2"]'
    COUNTRY = 'select[id="country"]'
    STATE = 'input[id="state"]'
    CITY = 'input[id="city"]'
    ZIPCODE = 'input[id="zipcode"]'
    MOBILE_NUMBER = 'input[id="mobile_number"]'
    CREATE_ACCOUNT = 'button[type="submit"]'
    
    def fill_form(self, **kwargs):
        self.page.click(f"{self.TITLE_RADIO_GENDER}{kwargs['title']}")
        self.page.fill(self.NAME, kwargs['name'])
        # self.page.fill(self.EMAIL, kwargs['email'])
        self.page.fill(self.PASSWORD, kwargs['password'])
        self.page.click(self.NEWSLETTER) if kwargs['newsletter'] else None
        self.page.click(self.OPTIN) if kwargs['optin'] else None
        self.page.select_option(self.DAYS, kwargs['days'])
        self.page.select_option(self.MONTHS, kwargs['months'])
        self.page.select_option(self.YEARS, kwargs['years'])
        self.page.fill(self.FIRST_NAME, kwargs['first_name'])
        self.page.fill(self.LAST_NAME, kwargs['last_name'])
        self.page.fill(self.COMPANY, kwargs['company'])
        self.page.fill(self.ADDRESS1, kwargs['address1'])
        self.page.fill(self.ADDRESS2, kwargs['address2'])
        self.page.select_option(self.COUNTRY, kwargs['country'])
        self.page.fill(self.STATE, kwargs['state'])
        self.page.fill(self.CITY, kwargs['city'])
        self.page.fill(self.ZIPCODE, kwargs['zipcode'])
        self.page.fill(self.MOBILE_NUMBER, kwargs['mobile_number'])
        self.page.click(self.CREATE_ACCOUNT)
        