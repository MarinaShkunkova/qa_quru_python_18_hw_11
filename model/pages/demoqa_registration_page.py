import os

from selene import have, command, be
from selene.support.shared import browser

import tests
from model.data.users import User

import allure


class RegistrationPage:

    @allure.step('Открыть страницу с формой регистрации')
    def open(self):
        browser.open('/automation-practice-form')

    @allure.step('Удалить баннеры')
    def remove_banners(self):
        browser.driver.execute_script("$('#RightSide_Advertisement').remove()")
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

    @allure.step('Проскроллить страницу')
    def scroll_page(self):
        browser.element('#submit').perform(command.js.scroll_into_view)

    @allure.step('Указать имя')
    def fill_first_name(self, value):
        browser.element('#firstName').should(be.blank).type(value).click()

    @allure.step('Указать фамилию')
    def fill_last_name(self, value):
        browser.element('#lastName').should(be.blank).type(value).click()

    @allure.step('Указать email')
    def fill_email(self, value):
        browser.element('#userEmail').should(be.blank).type(value).click()

    @allure.step('Указать пол')
    def fill_gender(self):
        browser.element('//label[contains(text(), "Female")]').click()

    @allure.step('Указать мобильный номер')
    def fill_mobile_number(self, value):
        browser.element('#userNumber').should(be.blank).type(value).click()

    @allure.step('Указать дату рождения')
    def fill_date_of_birth(self):
        browser.element("#dateOfBirthInput").click()
        browser.element('.react-datepicker__month-select').click().element('option[value="6"]').click()
        browser.element('.react-datepicker__year-select').click().element('option[value="1980"]').click()
        browser.element('.react-datepicker__day--022').click()

    @allure.step('Указать предмет')
    def fill_subject(self, value):
        browser.element('#subjectsInput').should(be.blank).type(value).press_enter()

    @allure.step('Указать хобби')
    def fill_hobby(self):
        browser.element("label[for='hobbies-checkbox-2']").should(have.exact_text('Reading')).click()

    @allure.step('Загрузить фотографию')
    def upload_picture(self):
        browser.element('#uploadPicture').set_value(
            os.path.abspath(
                os.path.join(os.path.dirname(tests.__file__), 'resources/picture.jpeg')
            )
        )

    @allure.step('Указать адрес')
    def fill_address(self, value):
        browser.element('#currentAddress').should(be.blank).type(value)

    @allure.step('Указать штат')
    def fill_state(self):
        browser.element("#state").click()
        browser.all('[id^="react-select-3-option"]').element_by(have.exact_text('NCR')).click()

    @allure.step('Указать город')
    def fill_city(self):
        browser.element("#city").click()
        browser.all('[id^="react-select-4-option"]').element_by(have.exact_text('Gurgaon')).click()

    @allure.step('Отправить форму')
    def submit(self):
        browser.element('#submit').click()

    def register(self, user: User):
        self.fill_first_name(user.first_name)
        self.fill_last_name(user.last_name)
        self.fill_email(user.email)
        self.fill_gender()
        self.fill_mobile_number(user.mobile_number)
        self.fill_date_of_birth()
        self.fill_subject(user.subject)
        self.fill_hobby()
        self.upload_picture()
        self.fill_address(user.address)
        self.fill_state()
        self.fill_city()
        self.submit()

    @allure.step('Проверить сохраненные данные')
    def should_have_registered(self, user: User):
        browser.element('.table').all('td:nth-child(2)').should(have.texts(
            f'{user.first_name} {user.last_name}',
            user.email,
            user.gender,
            user.mobile_number,
            f'{user.day_of_birth} {user.month_of_birth},{user.year_of_birth}',
            user.subject,
            user.hobby,
            user.picture,
            user.address,
            f'{user.state} {user.city}'.strip()))
