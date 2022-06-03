from selenium import webdriver

class Sel_Mod:
    def __init__(self, workflow, user):
        self.driver = webdriver.Chrome()  # В дальнейшем надо поменять Хром, чтобы сохранялась кроссплатфоменность
        self.workflow = workflow
        self.user = user

    def go_to_URL(self, url):
        self.driver.get(url)

    def set_data(self, parameter_value, element):
        element.send_keys(parameter_value)

    def get_element_by_name(self, name):
        return self.driver.find_element_by_name(name)

    def get_element_by_class(self, class_name):
        return self.driver.find_element_by_class_name(class_name)

    def get_element_by_id(self, id):
        return self.driver.find_element_by_id(id)

    def get_element_by_css(self, css):
        return self.driver.find_element_by_css_selector(css)

    def get_element_by_xpath(self, type, span):
        return self.driver.find_element_by_xpath(f"//{type}[.='{span}']")


    def click_buttom(self, element):
        element.click()
