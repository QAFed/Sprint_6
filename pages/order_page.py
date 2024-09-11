from selenium.webdriver.common.by import By


class OrderPage:
    name_input = [By.XPATH, '//input[@placeholder="* Имя"]']
    family_input = [By.XPATH, '//input[@placeholder="* Фамилия"]']
    address_input = [By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]']
    metro_station_input = [By.XPATH, '//input[@placeholder="* Станция метро"]']
    tel_number_input = [By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]']
    date_delivery_input = [By.XPATH, '//input[@placeholder="* Когда привезти самокат"]']
    rental_period_dropdown = [By.XPATH, '//div[@class="Dropdown-placeholder" and text()="* Срок аренды"]']
    black_samokat_checkbox = [By.XPATH, '//div[text()="Цвет самоката"]/parent::div//label[text()="чёрный жемчуг"]/input']
    grey_samokat_checkbox = [By.XPATH, '//div[text()="Цвет самоката"]/parent::div//label[text()="серая безысходность"]/input']
    comment_for_courier_input = [By.XPATH, '//input[@placeholder="Комментарий для курьера"]']