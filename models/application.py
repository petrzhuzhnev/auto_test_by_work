import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select, WebDriverWait

TIME_EXPLICIT_WAIT = 60


class Application:

    def __init__(self, wd):
        self.wd = wd

    @property
    def _wait(self):
        return WebDriverWait(self.wd, TIME_EXPLICIT_WAIT)

    def _wait_implicitly(self, locator):
        self.wd.implicitly_wait(15)
        self._element(locator)

    def open_new_tab(self):
        self.wd.execute_script("window.open('','_blank');")
        self.wd.switch_to.window(self.wd.window_handles[1])

    def _element(self, selector: dict, index=0):
        """
        Общий метод для поиска элементов
        """
        time.sleep(0.4)
        by = None
        if selector[0] == 'css':
            by = By.CSS_SELECTOR
        elif selector[0] == 'xpath':
            by = By.XPATH
        if index == 0:
            element = self.wd.find_element(by, selector[1])
            self.wd.execute_script("arguments[0].scrollIntoView();", element)
        else:
            element = self.wd.find_elements(by, selector[1])
            self.wd.execute_script("arguments[0].scrollIntoView();", element[index])
        return element

    def _elements(self, selector: dict):
        """
        Общий метод для поиска элементов
        """
        time.sleep(0.3)
        by = None
        if selector[0] == 'css':
            by = By.CSS_SELECTOR
        elif selector[0] == 'xpath':
            by = By.XPATH
        self.wd.implicitly_wait(15)
        elements = self.wd.find_elements(by, selector[1])
        return elements

    def _click(self, selector):
        """
        Добавлен метод для работы с кнопками.
        Стандартный метод click из selenium.webdriver не работал
        """
        time.sleep(0.2)
        if isinstance(selector, tuple):
            selector = self._element(selector)
        else:
            selector = selector
        self.wd.execute_script("arguments[0].click();", selector)

    def _click_b(self, selector):
        ActionChains(self.wd).move_to_element(self._element(selector)).click().perform()

    def _input(self, selector, value):
        element = self._element(selector)
        element.clear()
        element.send_keys(value)

    def _wait_element(self, selector):
        return self._wait.until(EC.visibility_of(self._element(selector)))

    def _wait_clickable(self, selector):
        return self._wait.until(EC.element_to_be_clickable(self._element(selector)))

    def _wait_click(self, selector):
        element = self._wait_element(selector)
        self._click(element)

    def _wait_input(self, selector, value):
        element = self._wait_element(selector)
        element.clear()
        element.send_keys(value)

    def wait_url(self, url):
        return self._wait.until(EC.url_contains(url))

    def wait_staleness_of(self, selector):
        return self._wait.until(EC.staleness_of(self._element(selector)))

    def _in_element(self, parent_element, child_element):
        element = self._element(parent_element)
        return element.find_element_by_css_selector(child_element)

    def double_click(self, selector):
        element = self._element(selector)
        actions = ActionChains(self.wd).move_to_element(element)
        actions.double_click(element).perform()

    def is_element_present(self, selector):
        try:
            self._wait_element(selector)
        except NoSuchElementException:
            return False
        return True

    """Метод выбора елеманта с ID пакета"""
    def add_id_element(self, element, packet_id):
        element = list(element)
        element = element[0], element[1] % packet_id
        self.wd.implicitly_wait(7)
        element = self.wd.find_element('css', element[1])
        return element

    @classmethod
    def add_id(cls, element, packet_id):
        element = list(element)
        element = element[0], element[1] % packet_id
        return tuple(element)

    # @classmethod
    # def add_id_now(cls, element, packet_id):
    #     element = list(element)
    #     list_element = []
    #     for i in element:
    #         if i == '%s':
    #             list_element.append(packet_id)
    #         else:
    #             list_element.append(i)
    #     element = ''.join(i for i in list_element)
    #     return tuple(element)

    def menu_select(self, select, value):
        menu = Select(self._element(select))
        menu.select_by_value(value)

    def menu_select_by_index(self, select, value):
        menu = Select(self._element(select))
        menu.select_by_index(value)

    def remove_attribute(self, element_id, name_attribute):
        self.wd.execute_script('document.getElementById("%s").removeAttribute("%s")' % (element_id, name_attribute))
        time.sleep(0.5)

    def remove_attribute_by_css(self, element, name_attribute):
        self.wd.execute_script('document.querySelector("%s").removeAttribute("%s")' % (element, name_attribute))
        time.sleep(0.5)

    def remove_element(self, element_id):
        self.wd.execute_script('document.getElementById("%s").remove()' % element_id)
        time.sleep(0.5)

    def remove_element_by_css(self, element):
        self.wd.execute_script('document.querySelector("%s").remove()' % element)
        time.sleep(0.5)
