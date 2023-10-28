from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import g4f

# Указываем путь к драйверу Chrome
driver_path = "C:/Users/vlady/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Python 3.11/chromedriver-win64/chromedriver.exe"

# Создаем экземпляр сервиса ChromeDriver
service = webdriver.chrome.service.Service(driver_path)

# Запускаем сервис
service.start()

# Создаем экземпляр WebDriver, связанный с сервисом
driver = webdriver.Chrome(service=service)

# Открываем веб-сайт Discord
driver.get("https://discord.com/login")

# Находим поле ввода почты и вводим почту
email_input = driver.find_element(By.NAME, "email")
email_input.send_keys("papap1kap4ik@gmail.com")

# Находим поле ввода пароля и вводим пароль
password_input = driver.find_element(By.NAME, "password")
password_input.send_keys("Sigoh1234@")

# Нажимаем клавишу Enter для отправки формы
password_input.send_keys(Keys.RETURN)

# Дожидаемся, пока меню пользователей загрузится (ждем, пока кнопка меню станет видимой)
wait = WebDriverWait(driver, 10)
menu_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".privateChannels__93473")))

# Перейдите к меню пользователей
menu_link.click()

# Добавляем код для перехода к меню приватных каналов
# Используйте CSS-селектор для поиска элемента навигации по приватным каналам

private_channels_nav = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav[aria-label="Приватні канали"]')))

# Нажмите на элемент навигации по приватным каналам
private_channels_nav.click()

# Дождитесь, пока меню приватных каналов загрузится (может потребоваться время)
time.sleep(10)

# Найдите список пользователей в меню
user_elements = driver.find_elements(By.CSS_SELECTOR, ".privateChannels-oVe7HL .channel-1Shao0")

# Перебирайтесь по пользователям и взаимодействуйте с ними
for user_element in user_elements:
    user_name = user_element.find_element(By.CSS_SELECTOR, ".name-2m3Cms").text

    # Ожидаем появления всплывающего сообщения
    message_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".notice-3X5ZB"))
    )

    message_text = message_element.text

    # Генерируем ответ с помощью GPT-3.5 Turbo API
    g4f_messages = [
        {"role": "user", "content": message_text},
    ]

    g4f_response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=g4f_messages,
        stream=True,
    )

    response_text = g4f_response[-1]["message"]["content"]

    # Нажимаем на всплывающее сообщение, чтобы открыть окно чата
    message_element.click()

    # Ожидаем загрузки окна чата
    chat_window = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".chat-3bRxxu"))
    )

    # Находим элемент поля ввода сообщения в окне чата
    message_input = chat_window.find_element(By.CSS_SELECTOR, ".textArea-12jD-V")

    # Вводим ответ в поле ввода сообщения
    message_input.send_keys(response_text)

    # Нажимаем клавишу Enter для отправки ответа
    message_input.send_keys(Keys.RETURN)

    # Ожидаем появления нового сообщения
    message_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".message-2qnXI6"))
    )

    # Извлекаем текст сообщения
    message_text = message_element.text

    # Находим текстовое поле для ввода сообщения
    message_input = driver.find_element(By.CSS_SELECTOR, ".textArea-12jD-V")

    # Вводим сгенерированный ответ в текстовое поле
    message_input.send_keys(response_text)

    # Нажимаем клавишу Enter для отправки ответа
    message_input.send_keys(Keys.RETURN)

# Вернитесь к начальной странице или закройте меню (в зависимости от ваших потребностей)

input("Нажмите Enter для закрытия браузера...")
