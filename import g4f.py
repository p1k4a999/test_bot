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

    # Ваш код для взаимодействия с пользователем здесь
    # Например, вы можете использовать GPT-3.5 Turbo для отправки сообщений
    g4f_messages = [
        {"role": "user", "content": f"Tell me about yourself, {user_name}"},
    ]

    g4f_response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=g4f_messages,
        stream=True,
    )

    for message in g4f_response:
        print(message['message']['content'], flush=True, end='')

    # Находим элемент поля ввода сообщения
    message_input = driver.find_element(By.CSS_SELECTOR, ".textArea-12jD-V")

    # Вводим сообщение для пользователя
    message_input.send_keys(f"Привет, {user_name}! Как дела?")

    # Нажимаем клавишу Enter для отправки сообщения
    message_input.send_keys(Keys.RETURN)

    # Ожидаем появления всплывающего сообщения
    message_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".notice-3X5ZbR"))
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

    # Находим элемент, отображающий список упоминаний
    mentions_element = driver.find_element(By.CSS_SELECTOR, ".mentionsPopout-2hNoT_")

    # Ожидаем, пока список упоминаний не станет видимым
    WebDriverWait(driver, 10).until(
        EC.visibility_of(mentions_element)
    )

    # Находим все элементы, соответствующие упоминаниям в списке
    mention_elements = mentions_element.find_elements(By.CSS_SELECTOR, ".mention-1Y6aS_")

    # Обрабатываем каждое упоминание в списке
    for mention_element in mention_elements:
        mention_text = mention_element.text

        # Генерируем ответ с помощью GPT-3.5 Turbo API
        g4f_messages = [
            {"role": "user", "content": mention_text},
        ]

        g4f_response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=g4f_messages,
            stream=True,
        )

        response_text = g4f_response[-1]["message"]["content"]

        # Нажимаем на упоминание, чтобы открыть окно чата
        mention_element.click()

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
