from tests.base_test import BaseTest
from pages.registration_page import Registration_protocole
import unittest


class Test_registration(BaseTest):

    def test_correct_registration(self):
        rp = Registration_protocole(self.driver)

        print("zamknij pop-up")
        rp.pop_up_closing()
        #print("zamknij chat")
        #rp.chat_closing()

        print("kliknij w przycisk 'Zaloguj'")
        rp.find_login_btn()
        print("zakceptuj ciaseczka")
        rp.accept_cookies()
        # print("zjedź w dół strony do ikony 'facebook'")
        # rp.click_facebook_btn()
        print("kliknij w 'załóż nowe konto'")
        rp.create_new_account()
        print("uzupełnij pola danymi")
        rp.fill_data()
        print("kliknij 'utwórz konto'")
        rp.create_account()






    def tearDown(self):
        self.driver.quit()

if "__name__" == "__main__":
    unittest.main()