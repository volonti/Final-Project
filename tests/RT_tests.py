from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import pytest
from test_data import *


def test_design(open_login_page):
    # Проверяем, что страница разделена на 2 части
    assert pytest.driver.find_element(By.ID, 'page-left')
    assert pytest.driver.find_element(By.ID, 'page-right')
    # Проверяем, что кнопки Номер, Почта, Логин, Лицевой счет, поле Логина, поле Пароль находятся в левой части
    assert pytest.driver.find_element(By.XPATH, '//section[@id="page-left"]//div[@id="t-btn-tab-phone"]')
    assert pytest.driver.find_element(By.XPATH, '//section[@id="page-left"]//div[@id="t-btn-tab-mail"]')
    assert pytest.driver.find_element(By.XPATH, '//section[@id="page-left"]//div[@id="t-btn-tab-login"]')
    assert pytest.driver.find_element(By.XPATH, '//section[@id="page-left"]//div[@id="t-btn-tab-ls"]')
    assert pytest.driver.find_element(By.XPATH, '//section[@id="page-left"]//input[@id="username"]')
    assert pytest.driver.find_element(By.XPATH, '//section[@id="page-left"]//input[@id="password"]')
    # Проверяем, что Логотип и вспомогательная информация находятся в правой части
    assert pytest.driver.find_element(By.XPATH,
                                      '//section[@id="page-right"]//div[@class="what-is-container__logo-container"]')
    assert pytest.driver.find_element(By.XPATH, '//section[@id="page-right"]//div[@class="what-is"]')


def test_tab_phone(open_login_page):
    # Нажимаем на таб Телефон
    pytest.driver.find_element(By.ID, 't-btn-tab-phone').click()

    # Проверяем, что таб в соответствии с ТЗ называется "Номер", проверка осуществляется по телефону и паролю и
    # присутствуют поля для ввода телефона и пароля. Остальные элементы формы не прописаны в ТЗ, но также проверяются
    assert pytest.driver.find_element(By.ID, 't-btn-tab-phone').text == 'Номер'
    assert pytest.driver.find_element(By.XPATH, '//input[@id="username"]')
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Мобильный телефон"]')
    assert pytest.driver.find_element(By.XPATH, '//input[@id="password"]')
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Пароль"]')
    assert pytest.driver.find_element(By.XPATH, '//img[@class="rt-captcha__image"]')
    assert pytest.driver.find_element(By.XPATH, '//div[@class="rt-captcha__reload-con"]')
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Символы"]')
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Введите символы с картинки"]')
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Запомнить меня"]')
    assert pytest.driver.find_element(By.XPATH,
                                      '//span[@class="rt-checkbox__shape rt-checkbox__shape--circular '
                                      'rt-checkbox__shape--orange"]')
    assert pytest.driver.find_element(By.ID, 'forgot_password')
    assert pytest.driver.find_element(By.ID, 'kc-login')


def test_tab_email(open_login_page):
    # Нажимаем на таб Почта
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    pytest.driver.implicitly_wait(10)
    # Проверяем, что таб в соответствии с ТЗ называется "Почта", проверка осуществляется по Логину и Паролю и
    # присутствуют поля для ввода почты и пароля. Остальные элементы формы не прописаны в ТЗ, но также проверяются
    assert pytest.driver.find_element(By.ID, 't-btn-tab-mail').text == 'Почта'
    assert pytest.driver.find_element(By.XPATH, '//input[@id="username"]')
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Логин"]')
    assert pytest.driver.find_element(By.XPATH, '//input[@id="password"]')
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Пароль"]')
    assert pytest.driver.find_element(By.XPATH, '//img[@class="rt-captcha__image"]')
    assert pytest.driver.find_element(By.XPATH, '//div[@class="rt-captcha__reload-con"]')
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Символы"]')
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Введите символы с картинки"]')
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Запомнить меня"]')
    assert pytest.driver.find_element(By.XPATH,
                                      '//span[@class="rt-checkbox__shape rt-checkbox__shape--circular '
                                      'rt-checkbox__shape--orange"]')
    assert pytest.driver.find_element(By.ID, 'forgot_password')
    assert pytest.driver.find_element(By.ID, 'kc-login')


def test_tab_login(open_login_page):
    # Нажимаем на таб Логин
    pytest.driver.find_element(By.ID, 't-btn-tab-login').click()
    pytest.driver.implicitly_wait(10)
    # Проверяем, что таб в соответствии с ТЗ называется "Логин", проверка осуществляется по Почте и Паролю,
    # и присутствуют поля для ввода логина и пароля. Остальные элементы формы не прописаны в ТЗ, но также проверяются
    assert pytest.driver.find_element(By.ID, 't-btn-tab-login').text == 'Логин'
    assert pytest.driver.find_element(By.XPATH, '//input[@id="username"]')
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Электронная почта"]')
    assert pytest.driver.find_element(By.XPATH, '//input[@id="password"]')
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Пароль"]')
    assert pytest.driver.find_element(By.XPATH, '//img[@class="rt-captcha__image"]')
    assert pytest.driver.find_element(By.XPATH, '//div[@class="rt-captcha__reload-con"]')
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Символы"]')
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Введите символы с картинки"]')
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Запомнить меня"]')
    assert pytest.driver.find_element(By.XPATH,
                                      '//span[@class="rt-checkbox__shape rt-checkbox__shape--circular '
                                      'rt-checkbox__shape--orange"]')
    assert pytest.driver.find_element(By.ID, 'forgot_password')
    assert pytest.driver.find_element(By.ID, 'kc-login')


def test_tab_ls(open_login_page):
    # Нажимаем на таб Лицевой счет
    pytest.driver.find_element(By.ID, 't-btn-tab-ls').click()
    pytest.driver.implicitly_wait(10)
    # Проверяем, что таб в соответствии с ТЗ называется "Лицевой счет", проверка осуществляется по Лицевому счету и
    # Паролю, и присутствуют поля для ввода логина и пароля. Остальные элементы формы не прописаны в ТЗ,
    # но также проверяются
    assert pytest.driver.find_element(By.ID, 't-btn-tab-ls').text == 'Лицевой счет'
    assert pytest.driver.find_element(By.XPATH, '//input[@id="username"]')
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Лицевой счёт"]')
    assert pytest.driver.find_element(By.XPATH, '//input[@id="password"]')
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Пароль"]')
    assert pytest.driver.find_element(By.XPATH, '//img[@class="rt-captcha__image"]')
    assert pytest.driver.find_element(By.XPATH, '//div[@class="rt-captcha__reload-con"]')
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Символы"]')
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Введите символы с картинки"]')
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Запомнить меня"]')
    assert pytest.driver.find_element(By.XPATH,
                                      '//span[@class="rt-checkbox__shape rt-checkbox__shape--circular '
                                      'rt-checkbox__shape--orange"]')
    assert pytest.driver.find_element(By.ID, 'forgot_password')
    assert pytest.driver.find_element(By.ID, 'kc-login')


def test_autochange_tab_phone(open_login_page):
    # Нажимаем на таб Почта
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    pytest.driver.implicitly_wait(10)
    # Вводим номер телефона
    pytest.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(valid_phone)
    # Нажимаем на поле Пароль
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').click()
    # Проверяем, что таб переключился на логин по номеру телефона
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Мобильный телефон"]')


def test_autochange_tab_email(open_login_page):
    # Нажимаем на таб Телефон
    pytest.driver.find_element(By.ID, 't-btn-tab-phone').click()
    pytest.driver.implicitly_wait(10)
    # Вводим валидный емейл
    pytest.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(valid_email)
    # Нажимаем на поле Пароль
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').click()
    # Проверяем, что таб переключился на логин по mail
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Электронная почта"]')


def test_autochange_tab_login(open_login_page):
    # Нажимаем на таб Телефон
    pytest.driver.find_element(By.ID, 't-btn-tab-login').click()
    pytest.driver.implicitly_wait(10)
    # Вводим Логин
    pytest.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(valid_login)
    # Нажимаем на поле Пароль
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').click()
    # Проверяем, что таб переключился на авторизацию по логину
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Логин"]')


def test_autochange_tab_ls(open_login_page):
    # Нажимаем на таб Почта
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    pytest.driver.implicitly_wait(10)
    # Вводим валидный лицевой счет
    pytest.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(valid_ls)
    # Нажимаем на поле Пароль
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').click()
    # Проверяем, что таб переключился на логин по Лицевому счету
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Лицевой счёт"]')


def test_login_with_phone(open_login_page):
    # Нажимаем на таб Телефон
    pytest.driver.find_element(By.ID, 't-btn-tab-phone').click()
    pytest.driver.implicitly_wait(10)
    # Вводим валидный номер телефона
    pytest.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(valid_phone_exist_user)
    # Вводим валидный пароль
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(valid_password)
    # Проверяем, что есть капча и можно ее обновить
    try:
        pytest.driver.find_element(By.XPATH, '//img[@class="rt-captcha__image"]')
        pytest.driver.find_element(By.XPATH, '//div[@class="rt-captcha__reload-con"]').click()
        pytest.driver.implicitly_wait(10)
        # Вводим капчу
        pytest.driver.find_element(By.ID, 'captcha').send_keys(captcha)
        # Нажимаем на кнопку Войти
        pytest.driver.find_element(By.ID, 'kc-login').click()
        pytest.driver.implicitly_wait(10)
    except NoSuchElementException:
        # Нажимаем на кнопку Войти
        pytest.driver.find_element(By.ID, 'kc-login').click()
        pytest.driver.implicitly_wait(10)
    # Проверяем возможность снять галочку в чек-боксе "Запомнить меня"
    pytest.driver.find_element(By.XPATH,
                               '//span[@class="rt-checkbox__shape rt-checkbox__shape--circular '
                               'rt-checkbox__shape--orange"]').click()
    # Проверяем, что мы зашли в личный кабинет
    assert pytest.driver.find_element(By.XPATH, '//h3[text()="Учетные данные"]')


def test_login_phone_with_invalid_phone(open_login_page):
    # Нажимаем на таб Телефон
    pytest.driver.find_element(By.ID, 't-btn-tab-phone').click()
    pytest.driver.implicitly_wait(10)
    # Вводим невалидный номер телефона
    pytest.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(invalid_phone)
    # Вводим валидный пароль
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(valid_password)
    # Проверяем, что есть капча
    try:
        pytest.driver.find_element(By.XPATH, '//img[@class="rt-captcha__image"]')
        # Вводим капчу
        pytest.driver.find_element(By.ID, 'captcha').send_keys(captcha)
        # Нажимаем на кнопку Войти
        pytest.driver.find_element(By.ID, 'kc-login').click()
        pytest.driver.implicitly_wait(10)
    except NoSuchElementException:
        # Нажимаем на кнопку Войти
        pytest.driver.find_element(By.ID, 'kc-login').click()
        pytest.driver.implicitly_wait(10)

    assert pytest.driver.find_element(By.ID, 'form-error-message').text == 'Неверный логин или пароль'


def test_login_phone_with_invalid_password(open_login_page):
    # Нажимаем на таб Телефон
    pytest.driver.find_element(By.ID, 't-btn-tab-phone').click()
    pytest.driver.implicitly_wait(10)
    # Вводим валидный номер телефона
    pytest.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(valid_phone)
    # Вводим невалидный пароль
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(invalid_password)
    # Проверяем, что есть капча
    try:
        pytest.driver.find_element(By.XPATH, '//img[@class="rt-captcha__image"]')
        # Вводим капчу
        pytest.driver.find_element(By.ID, 'captcha').send_keys(captcha)
        # Нажимаем на кнопку Войти
        pytest.driver.find_element(By.ID, 'kc-login').click()
        pytest.driver.implicitly_wait(10)
    except NoSuchElementException:
        # Нажимаем на кнопку Войти
        pytest.driver.find_element(By.ID, 'kc-login').click()
        pytest.driver.implicitly_wait(10)

    assert pytest.driver.find_element(By.ID, 'form-error-message').text == 'Неверный логин или пароль'


def test_login_phone_with_empty_fields(open_login_page):
    # Нажимаем на таб Телефон
    pytest.driver.find_element(By.ID, 't-btn-tab-phone').click()
    pytest.driver.implicitly_wait(10)
    # Оставляем пустым поле Мобильный телефон
    pytest.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys('')
    # Оставляем пустым поле Пароль
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys('')
    # Проверяем, что есть капча
    try:
        pytest.driver.find_element(By.XPATH, '//img[@class="rt-captcha__image"]')
        # Оставляем пустым поле для ввода капчи
        pytest.driver.find_element(By.ID, 'captcha').send_keys('')
        # Нажимаем на кнопку Войти
        pytest.driver.find_element(By.ID, 'kc-login').click()
        pytest.driver.implicitly_wait(10)
    except NoSuchElementException:
        # Нажимаем на кнопку Войти
        pytest.driver.find_element(By.ID, 'kc-login').click()
        pytest.driver.implicitly_wait(10)

    assert pytest.driver.find_element(By.XPATH, '//span[@class="rt-input-container__meta '
                                                'rt-input-container__meta--error"]').text == 'Введите номер телефона '


def test_login_phone_with_long_phone(open_login_page):
    # Нажимаем кнопку Телефон
    pytest.driver.find_element(By.ID, 't-btn-tab-phone').click()
    # Вводим номер телефона, начинающегося с 8 и  больше 12 символов
    pytest.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(long_phone)
    # Проверяем, что в поле только разрешенное количество символов
    assert pytest.driver.find_element(By.XPATH, '//input[@value="79270014500"]')


def test_login_phone_with_short_phone(open_login_page):
    # Нажимаем кнопку Телефон
    pytest.driver.find_element(By.ID, 't-btn-tab-phone').click()
    # Вводим номер телефона из 7 цифр
    pytest.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(short_phone)
    # Нажимаем на поле Пароль
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').click()
    # Проверяем, что появилось сообщение "Неверный формат телефона"
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Неверный формат телефона"]')


def test_login_with_email(open_login_page):
    # Нажимаем на таб Почта
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    pytest.driver.implicitly_wait(10)
    # Вводим валидный емейл
    pytest.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(valid_email)
    # Вводим валидный пароль
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(valid_password)
    # Проверяем, что есть капча и можно ее обновить
    try:
        pytest.driver.find_element(By.XPATH, '//img[@class="rt-captcha__image"]')
        pytest.driver.find_element(By.XPATH, '//div[@class="rt-captcha__reload-con"]').click()
        pytest.driver.implicitly_wait(10)
        # Вводим капчу
        pytest.driver.find_element(By.ID, 'captcha').send_keys(captcha)
        # Нажимаем на кнопку Войти
        pytest.driver.find_element(By.ID, 'kc-login').click()
        pytest.driver.implicitly_wait(10)
    except NoSuchElementException:
        # Нажимаем на кнопку Войти
        pytest.driver.find_element(By.ID, 'kc-login').click()
        pytest.driver.implicitly_wait(10)
    # Проверяем возможность снять галочку в чек-боксе "Запомнить меня"
    pytest.driver.find_element(By.XPATH,
                               '//span[@class="rt-checkbox__shape rt-checkbox__shape--circular '
                               'rt-checkbox__shape--orange"]').click()
    # Проверяем, что мы зашли в личный кабинет
    assert pytest.driver.find_element(By.XPATH, '//h3[text()="Учетные данные"]')


def test_login_email_with_invalid_email(open_login_page):
    # Нажимаем на таб Почта
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    pytest.driver.implicitly_wait(10)
    # Вводим невалидный емейл
    pytest.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(invalid_email)
    # Вводим валидный пароль
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(valid_password)
    # Проверяем, что есть капча
    try:
        pytest.driver.find_element(By.XPATH, '//img[@class="rt-captcha__image"]')
        # Вводим капчу
        pytest.driver.find_element(By.ID, 'captcha').send_keys(captcha)
        # Нажимаем на кнопку Войти
        pytest.driver.find_element(By.ID, 'kc-login').click()
        pytest.driver.implicitly_wait(10)
    except NoSuchElementException:
        # Нажимаем на кнопку Войти
        pytest.driver.find_element(By.ID, 'kc-login').click()
        pytest.driver.implicitly_wait(10)

    assert pytest.driver.find_element(By.ID, 'form-error-message').text == 'Неверный логин или пароль'


def test_login_email_with_invalid_password(open_login_page):
    # Нажимаем на таб Почта
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    pytest.driver.implicitly_wait(10)
    # Вводим валидный емейл
    pytest.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(valid_email)
    # Вводим невалидный пароль
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(invalid_password)
    # Проверяем, что есть капча
    try:
        pytest.driver.find_element(By.XPATH, '//img[@class="rt-captcha__image"]')
        # Вводим капчу
        pytest.driver.find_element(By.ID, 'captcha').send_keys(captcha)
        # Нажимаем на кнопку Войти
        pytest.driver.find_element(By.ID, 'kc-login').click()
        pytest.driver.implicitly_wait(10)
    except NoSuchElementException:
        # Нажимаем на кнопку Войти
        pytest.driver.find_element(By.ID, 'kc-login').click()
        pytest.driver.implicitly_wait(10)

    assert pytest.driver.find_element(By.ID, 'form-error-message').text == 'Неверный логин или пароль'


def test_login_email_with_empty_fields(open_login_page):
    # Нажимаем на таб Почта
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    pytest.driver.implicitly_wait(10)
    # Оставляем поле Электронная почта пустым
    pytest.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys('')
    # Оставляем поле Пароль пустым
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys('')
    # Проверяем, что есть капча
    try:
        pytest.driver.find_element(By.XPATH, '//img[@class="rt-captcha__image"]')
        pytest.driver.implicitly_wait(10)
        # Оставляем поле для ввода капчи пустым
        pytest.driver.find_element(By.ID, 'captcha').send_keys('')
        # Нажимаем на кнопку Войти
        pytest.driver.find_element(By.ID, 'kc-login').click()
        pytest.driver.implicitly_wait(10)
    except NoSuchElementException:
        # Нажимаем на кнопку Войти
        pytest.driver.find_element(By.ID, 'kc-login').click()
        pytest.driver.implicitly_wait(10)

    # Проверяем, что появилась подсказка об ошибке ввода
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Введите адрес, указанный при регистрации"]')


def test_login_with_login(open_login_page):
    # Нажимаем кнопку Логин
    pytest.driver.find_element(By.ID, 't-btn-tab-login').click()
    pytest.driver.implicitly_wait(10)
    # Вводим Логин
    pytest.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(valid_login)
    # Вводим валидный пароль
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(valid_password)
    # Проверяем, что есть капча и можно ее обновить
    try:
        pytest.driver.find_element(By.XPATH, '//img[@class="rt-captcha__image"]')
        pytest.driver.find_element(By.XPATH, '//div[@class="rt-captcha__reload-con"]').click()
        pytest.driver.implicitly_wait(10)
        # Вводим капчу
        pytest.driver.find_element(By.ID, 'captcha').send_keys(captcha)
        # Нажимаем на кнопку Войти
        pytest.driver.find_element(By.ID, 'kc-login').click()
        pytest.driver.implicitly_wait(10)
    except NoSuchElementException:
        # Нажимаем на кнопку Войти
        pytest.driver.find_element(By.ID, 'kc-login').click()
        pytest.driver.implicitly_wait(10)
    # Проверяем возможность снять галочку в чек-боксе "Запомнить меня"
    pytest.driver.find_element(By.XPATH,
                               '//span[@class="rt-checkbox__shape rt-checkbox__shape--circular '
                               'rt-checkbox__shape--orange"]').click()
    # Проверяем, что мы зашли в личный кабинет
    assert pytest.driver.find_element(By.XPATH, '//h3[text()="Учетные данные"]')


def test_login_with_invalid_login(open_login_page):
    # Нажимаем кнопку Логин
    pytest.driver.find_element(By.ID, 't-btn-tab-login').click()
    pytest.driver.implicitly_wait(10)
    # Вводим невалидный логин
    pytest.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(invalid_login)
    # Вводим валидный пароль
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(valid_password)
    # Проверяем, что есть капча
    try:
        pytest.driver.find_element(By.XPATH, '//img[@class="rt-captcha__image"]')
        # Вводим капчу
        pytest.driver.find_element(By.ID, 'captcha').send_keys(captcha)
        # Нажимаем на кнопку Войти
        pytest.driver.find_element(By.ID, 'kc-login').click()
        pytest.driver.implicitly_wait(10)
    except NoSuchElementException:
        # Нажимаем на кнопку Войти
        pytest.driver.find_element(By.ID, 'kc-login').click()
        pytest.driver.implicitly_wait(10)

    assert pytest.driver.find_element(By.ID, 'form-error-message').text == 'Неверный логин или пароль'


def test_login_with_invalid_password(open_login_page):
    # Нажимаем кнопку Логин
    pytest.driver.find_element(By.ID, 't-btn-tab-login').click()
    pytest.driver.implicitly_wait(10)
    # Вводим валидный логин
    pytest.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(valid_login)
    # Вводим невалидный пароль
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(invalid_password)
    # Проверяем, что есть капча
    try:
        pytest.driver.find_element(By.XPATH, '//img[@class="rt-captcha__image"]')
        # Вводим капчу
        pytest.driver.find_element(By.ID, 'captcha').send_keys(captcha)
        # Нажимаем на кнопку Войти
        pytest.driver.find_element(By.ID, 'kc-login').click()
        pytest.driver.implicitly_wait(10)
    except NoSuchElementException:
        # Нажимаем на кнопку Войти
        pytest.driver.find_element(By.ID, 'kc-login').click()
        pytest.driver.implicitly_wait(10)

    assert pytest.driver.find_element(By.ID, 'form-error-message').text == 'Неверный логин или пароль'


def test_login_with_empty_fields(open_login_page):
    # Нажимаем кнопку Логин
    pytest.driver.find_element(By.ID, 't-btn-tab-login').click()
    pytest.driver.implicitly_wait(10)
    # Оставляем поле Логин пустым
    pytest.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys('')
    # Оставляем поля для ввода пароля пустым
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys('')
    # Проверяем, что есть капча
    try:
        pytest.driver.find_element(By.XPATH, '//img[@class="rt-captcha__image"]')
        # Оставляем поле для ввода капчи пустым
        pytest.driver.find_element(By.ID, 'captcha').send_keys('')
        # Нажимаем на кнопку Войти
        pytest.driver.find_element(By.ID, 'kc-login').click()
        pytest.driver.implicitly_wait(10)
    except NoSuchElementException:
        # Нажимаем на кнопку Войти
        pytest.driver.find_element(By.ID, 'kc-login').click()
        pytest.driver.implicitly_wait(10)

    assert pytest.driver.find_element(By.XPATH, '//span[text()="Введите логин, указанный при регистрации"]')


def test_login_with_ls(open_login_page):
    # Нажимаем кнопку Лицевой счет
    pytest.driver.find_element(By.ID, 't-btn-tab-ls').click()
    pytest.driver.implicitly_wait(10)
    # Вводим Логин
    pytest.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(valid_ls)
    # Вводим валидный пароль
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(valid_password)
    # Проверяем, что есть капча и можно ее обновить
    try:
        pytest.driver.find_element(By.XPATH, '//img[@class="rt-captcha__image"]')
        pytest.driver.find_element(By.XPATH, '//div[@class="rt-captcha__reload-con"]').click()
        pytest.driver.implicitly_wait(10)
        # Вводим капчу
        pytest.driver.find_element(By.ID, 'captcha').send_keys(captcha)
        # Нажимаем на кнопку Войти
        pytest.driver.find_element(By.ID, 'kc-login').click()
        pytest.driver.implicitly_wait(10)
    except NoSuchElementException:
        # Нажимаем на кнопку Войти
        pytest.driver.find_element(By.ID, 'kc-login').click()
        pytest.driver.implicitly_wait(10)
    # Проверяем возможность снять галочку в чек-боксе "Запомнить меня"
    pytest.driver.find_element(By.XPATH,
                               '//span[@class="rt-checkbox__shape rt-checkbox__shape--circular '
                               'rt-checkbox__shape--orange"]').click()
    # Проверяем, что мы зашли в личный кабинет
    assert pytest.driver.find_element(By.XPATH, '//h3[text()="Учетные данные"]')


def test_login_ls_with_invalid_ls(open_login_page):
    # Нажимаем кнопку Лицевой счет
    pytest.driver.find_element(By.ID, 't-btn-tab-ls').click()
    pytest.driver.implicitly_wait(10)
    # Вводим невалидный лс
    pytest.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(invalid_ls)
    # Вводим валидный пароль
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(valid_password)
    # Проверяем, что есть капча
    try:
        pytest.driver.find_element(By.XPATH, '//img[@class="rt-captcha__image"]')
        # Вводим капчу
        pytest.driver.find_element(By.ID, 'captcha').send_keys(captcha)
        # Нажимаем на кнопку Войти
        pytest.driver.find_element(By.ID, 'kc-login').click()
        pytest.driver.implicitly_wait(10)
    except NoSuchElementException:
        # Нажимаем на кнопку Войти
        pytest.driver.find_element(By.ID, 'kc-login').click()
        pytest.driver.implicitly_wait(10)

    assert pytest.driver.find_element(By.ID, 'form-error-message').text == 'Неверный логин или пароль'


def test_login_ls_with_invalid_password(open_login_page):
    # Нажимаем кнопку Лицевой счет
    pytest.driver.find_element(By.ID, 't-btn-tab-ls').click()
    pytest.driver.implicitly_wait(10)
    # Вводим валидный лс
    pytest.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(valid_ls)
    # Вводим невалидный пароль
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(invalid_password)
    # Проверяем, что есть капча
    try:
        pytest.driver.find_element(By.XPATH, '//img[@class="rt-captcha__image"]')
        # Вводим капчу
        pytest.driver.find_element(By.ID, 'captcha').send_keys(captcha)
        # Нажимаем на кнопку Войти
        pytest.driver.find_element(By.ID, 'kc-login').click()
        pytest.driver.implicitly_wait(10)
    except NoSuchElementException:
        # Нажимаем на кнопку Войти
        pytest.driver.find_element(By.ID, 'kc-login').click()
        pytest.driver.implicitly_wait(10)

    assert pytest.driver.find_element(By.ID, 'form-error-message').text == 'Неверный логин или пароль'


def test_ls_with_empty_fields(open_login_page):
    # Нажимаем кнопку Лицевой счет
    pytest.driver.find_element(By.ID, 't-btn-tab-ls').click()
    pytest.driver.implicitly_wait(10)
    # Поле для ввода лицевого счета оставляем пустым
    pytest.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys('')
    # Поле дла ввода пароля оставляем пустым
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys('')
    # Проверяем, что есть капча
    try:
        pytest.driver.find_element(By.XPATH, '//img[@class="rt-captcha__image"]')
        # Поле для ввода капчи оставляем пустым
        pytest.driver.find_element(By.ID, 'captcha').send_keys('')
        # Нажимаем на кнопку Войти
        pytest.driver.find_element(By.ID, 'kc-login').click()
        pytest.driver.implicitly_wait(10)
    except NoSuchElementException:
        # Нажимаем на кнопку Войти
        pytest.driver.find_element(By.ID, 'kc-login').click()
        pytest.driver.implicitly_wait(10)

    # Проверяем, что появилась подсказка об ошибке ввода
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Введите номер вашего лицевого счета"]')


def test_btn_terms_of_use(open_login_page):
    # Нажимаем кнопку Пользовательское соглашение
    pytest.driver.find_element(By.XPATH, '//a[text()="пользовательского соглашения"]').click()
    # Переключаемся на новую вкладку
    window_after = pytest.driver.window_handles[1]
    pytest.driver.switch_to.window(window_after)
    # Проверяем, что произошла переадресация на страницу Публичная оферта
    assert pytest.driver.find_element(By.XPATH, '//title[text()="User agreement"]')


def test_btn_forgot_password(open_login_page):
    # Нажимаем кнопку 'Забыл пароль'
    pytest.driver.find_element(By.ID, 'forgot_password').click()
    pytest.driver.implicitly_wait(10)
    # Проверяем, что переадресация на страницу восстановления пароля
    assert pytest.driver.find_element(By.XPATH, '//h1[text()="Восстановление пароля"]')


def test_btn_registration(open_login_page):
    pytest.driver.find_element(By.ID, 'kc-register').click()
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == 'Регистрация'


def test_social_providers(open_login_page):
    # Нажимаем на значок ВКонтакте
    pytest.driver.find_element(By.XPATH, '//a[@id="oidc_vk"]').click()
    pytest.driver.implicitly_wait(10)
    # Проверяем, что открылась авторизация через ВК
    assert pytest.driver.find_element(By.XPATH, '//body[@class="VK oauth_centered"]')
    # Возвращаемся на форму авторизации
    pytest.driver.get('https://b2c.passport.rt.ru')
    # Нажимаем на значок Одноклассники
    pytest.driver.find_element(By.XPATH, '//a[@id="oidc_ok"]').click()
    pytest.driver.implicitly_wait(10)
    # Проверяем, что открылась авторизация через ОК
    assert pytest.driver.find_element(By.XPATH, '//div[@id="hook_Block_OAuth2Login"]')
    # Возвращаемся на форму авторизации
    pytest.driver.get('https://b2c.passport.rt.ru')
    # Нажимаем на значок Mail.ru
    pytest.driver.find_element(By.XPATH, '//a[@id="oidc_mail"]').click()
    # Проверяем, что открылась авторизация через Mail
    assert pytest.driver.find_element(By.XPATH, '//div[@class="auth-dialog"]')
    # Возвращаемся на форму авторизации
    pytest.driver.get('https://b2c.passport.rt.ru')
    # Нажимаем на значок Google
    pytest.driver.find_element(By.XPATH, '//a[@id="oidc_google"]').click()
    # Проверяем, что открылась авторизация через Google
    assert pytest.driver.find_element(By.XPATH, '//body[@class="nyoS7c UzCXuf EIlDfe"]')
    # Возвращаемся на форму авторизации
    pytest.driver.get('https://b2c.passport.rt.ru')
    # Нажимаем на значок Яндекс
    pytest.driver.find_element(By.XPATH, '//a[@id="oidc_ya"]').click()
    # Проверяем, что открылась авторизация через Яндекс
    assert pytest.driver.find_element(By.XPATH, '//div[@class="passp-flex-wrapper"]')



