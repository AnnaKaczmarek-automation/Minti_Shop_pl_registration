from pages.base_page import  BasePage
from locators import registranion_buttons
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

class Registration_protocole(BasePage):

    def pop_up_closing(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "smwpRejectionButton")))
        self.driver.find_element(*registranion_buttons.pop_up_denie_btn).click()

    def chat_closing(self):
        #self.driver.find_element_by_xpath('//div[@class="bhr-chat-launch"]').click()
        closing_chat = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(By.CLASS_NAME,'bhr-chat-launch'))
        closing_chat.perform()

    def accept_cookies(self):#nie mogę zamknać ciasteczek bo chyba chat go przysłania ale chata nie moge w ogóle usunąć
        self.driver.find_element(*registranion_buttons.cookies_btn).click()

        # accepting_cookies = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(By.CLASS_NAME, "fa fa-close"))
        # accepting_cookies.perform()

        # button = self.driver.find_element_by_class_name('fa fa-close')
        # self.driver.implicitly_wait(10)
        # ActionChains(self.driver).move_to_element(button).click(button).perform()


    def find_login_btn(self):
        self.driver.find_element(*registranion_buttons.login_btn).click()

    def click_facebook_btn(self):
        facebook = self.driver.find_element_by_xpath('//a[@class="service_item service_Facebook"]')
        facebook.location_once_scrolled_into_view()



    def create_new_account(self):
        print("zjedż na dół")
        # account_btn = self.driver.find_element_by_xpath('//a[@href="/client-new.php?register"][@class="btn signin-form_register2"]')
        # actions = ActionChains(self.driver)
        # actions.move_to_element(account_btn).perform()
        # self.driver.find(*registranion_buttons.create_new_account_btn).click()
        # time.sleep(3)


        self.driver.find_element(*registranion_buttons.create_new_account_btn).click()
        time.sleep(3)

    # def click_question_btn(self):
    #     #self.driver.find_element(*registranion_buttons.question_btn).click()
    #     question_btn = self.driver.find_element_by_xpath('//a[@class="pull-right ng-binding"]')
    #     Hover = ActionChains(self.driver).move_to_element(question_btn)
    #     Hover.perform()
    #     self.driver.find_element_by_xpath('//a[@class="pull-right ng-binding"]').click()

    def fill_data(self):
        #self.driver.find_element(*registranion_buttons.private_person).click()
        self.driver.find_element(*registranion_buttons.first_name).send_keys("Aleksandra")
        self.driver.find_element(*registranion_buttons.last_name).send_keys("Owczarczak")
        self.driver.find_element(*registranion_buttons.street_and_number).send_keys("Jędrzejowska 34")
        self.driver.find_element(*registranion_buttons.zipcode).send_keys("61-339")
        self.driver.find_element(*registranion_buttons.city).send_keys("Poznań")
        self.driver.find_element(*registranion_buttons.country).send_keys("Poland")
        # self.driver.find_element(*registranion_buttons.poland).click()
        self.driver.find_element(*registranion_buttons.phone_number).send_keys("540278530")
        self.driver.find_element(*registranion_buttons.e_mail).send_keys("aleksandra22@gmail.com")

        # poszukaj jakos css selector. chodzi o ::before
        self.driver.find_element(*registranion_buttons.terms_agreement_btn).click()


        self.driver.find_element(*registranion_buttons.login2_btn).send_keys("Olka007")
        self.driver.find_element(*registranion_buttons.password).send_keys("Olk@4457")
        self.driver.find_element(*registranion_buttons.repeated_password).send_keys("Olk@4457")
        time.sleep(4)

    def create_account(self):
        self.driver.find_element(*registranion_buttons.create_account_btn).click()

