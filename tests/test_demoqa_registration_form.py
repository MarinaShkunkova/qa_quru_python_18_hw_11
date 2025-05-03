from model.data.users import user
from model.pages.demoqa_registration_page import RegistrationPage
import allure
from allure_commons.types import Severity


@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "shkunkova")
@allure.feature("Дженкинс")
@allure.story("Создание задачи в дженкинс")
@allure.link("https://github.com", name="Testing")
def test_registers_user(setup_browser):
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.scroll_page()
    registration_page.register(user)
    registration_page.should_have_registered(user)
