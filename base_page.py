class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self._verify_page()
        print("sprawdzam")

    def _verify_page(self):
        return