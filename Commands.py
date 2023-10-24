# Импортируем библиотеки
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
import time
import datetime
import requests
from dotenv import load_dotenv

# Создаём класс, который будем вызывать в main
class Commands:
    # Создаём метод, который будет сохранять скриншот оценок
    @staticmethod
    def marks():
        load_dotenv()
        # Инициализируем браузер гугл для работы автономного ПО
        url = "https://sgo.rso23.ru/"
        driver = webdriver.Chrome(executable_path="E:\\ProektTgBot\\chromedriver.exe")
        login = os.getenv('LOGIN')
        password = os.getenv('PASSWORD')
        try:
            # Переходим на сайт СГО
            driver.get(url)
            driver.maximize_window()
            time.sleep(2)
            # Выбираем регион, тип школы, саму школу
            region = driver.find_element(by=By.ID, value="provinces")
            region.click()
            value = driver.find_element(By.XPATH, value="//*[@id='provinces']/option[7]")
            value.click()
            time.sleep(1)
            type_school = driver.find_element(by=By.XPATH, value="//*[@id='funcs']")
            type_school.click()
            value = driver.find_element(by=By.XPATH, value="//*[@id='funcs']/option[3]")
            value.click()
            time.sleep(1)
            school = driver.find_element(by=By.XPATH, value="//*[@id='schools']")
            school.click()
            value = driver.find_element(by=By.XPATH, value="//*[@id='schools']/option[22]")
            value.click()
            time.sleep(1)
            # Вводим Логин и Пароль в поля
            login_enter = driver.find_element(by=By.XPATH, value='//*[@id="message"]/div/div/div[8]/input')
            login_enter.send_keys(login)
            time.sleep(1)
            password_enter = driver.find_element(by=By.XPATH, value='//*[@id="message"]/div/div/div[9]/input')
            password_enter.send_keys(password)
            time.sleep(1)
            # Нажимаем кнопку Войти
            enter = driver.find_element(by=By.XPATH, value='//*[@id="message"]/div/div/div[12]/a/span')
            enter.click()
            time.sleep(5)
            if driver.current_url == "https://sgo.rso23.ru/asp/SecurityWarning.asp":
                driver.implicitly_wait(5)
                enter = driver.find_element(by=By.XPATH,
                                            value='/html/body/div[1]/div/div/div[2]/div/div[4]/div/div/div/div/button[2]')
                enter.click()
            driver.implicitly_wait(5)
            # Переходим до вкладки 'отчёт об успеваемости и посещаемости'
            otchet = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[4]/nav/ul/li[3]/a')
            otchet.click()
            time.sleep(1)
            otchet_vhod = driver.find_element(by=By.XPATH, value='//*[@id="ReportsList"]/tbody/tr[7]/td[2]/a')
            otchet_vhod.click()
            driver.implicitly_wait(5)
            build_otchet = driver.find_element(by=By.XPATH, value='//*[@id="buttonPanel"]/div/button[1]')
            build_otchet.click()
            time.sleep(5)
            # Прокручиваем страницу до таблицы
            driver.execute_script("window.scrollTo(0, 350)")
            time.sleep(1)
            # Делаем скриншот страницы
            driver.save_screenshot("screenshot.png")
            time.sleep(1)
            # Выходим из СГО
            exit = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/ul/li[3]/a/span[2]')
            exit.click()
            driver.implicitly_wait(5)
            really_exit = driver.find_element(by=By.XPATH,
                                              value='/html/body/div[5]/div[2]/div/div[3]/div/div/button[1]')
            really_exit.click()
            # Инициализируем сделанный ранее скриншот, далее обрезаем его и сохраняем обрезанный скриншот
            img = Image.open('screenshot.png')
            area = (50, 200, 1360, 740)
            cropped_image = img.crop(area)
            cropped_image.save('screenshot_cropped.png')
        # В случае ошибки, выводит ошибку
        except Exception as ex:
            print(ex)
        finally:
            # Закрываем браузер
            time.sleep(5)
            driver.close()
            driver.quit()

    # Создаём метод для расписания
    @staticmethod
    def timetable():
        # Создаю расписание
        data = {
            1: {
                "Школа": {
                    "1": "8:00 - 8:40 География ",
                    "2": "8:55 - 9:35 Математика",
                    "3": "9:50 - 10:30 Литература",
                    "4": "10:45 - 11:25 Английский язык",
                    "5": "11:35 - 12:15 Информатика",
                    "6": "12:25 - 13:05 Информатика"
                },
                "Цтриго": {
                    "1": "16:50 - 18:10 Математика"
                }
            },
            2: {
                "Школа": {
                    "1": "8:00 - 8:40 Обществознание ",
                    "2": "8:55 - 9:35 Математика",
                    "3": "9:50 - 10:30 История",
                    "4": "10:45 - 11:25 Индивидуальный проект",
                    "5": "11:35 - 12:15 Физика",
                    "6": "12:25 - 13:05 Физкультура",
                    "7": "13:15 - 14:05 Кубановедение"
                },
                "Цтриго": {
                    "1": "15:20 - 16:40 Программирование",
                    "2": "16:50 - 18:10 Системное администрирование"
                }
            },
            3: {
                "Школа": {
                    "1": "8:00 - 8:40 Математика ",
                    "2": "8:55 - 9:35 Математика",
                    "3": "9:50 - 10:30 Физика",
                    "4": "10:45 - 11:25 Химия",
                    "5": "11:35 - 12:15 История",
                    "6": "12:25 - 13:05 Английский язык"
                },
                "Цтриго": {
                    "1": "15:20 - 17:25 Физика"
                }
            },
            4: {
                "Школа": {
                    "1": "8:00 - 8:40 Индивидуальный проект ",
                    "2": "8:55 - 9:35 Математика",
                    "3": "9:50 - 10:30 Физика",
                    "4": "10:45 - 11:25 Математика",
                    "5": "11:35 - 12:15 Обществознание",
                    "6": "12:25 - 13:05 Физкультура"
                },
                "Цтриго": {
                    "1": "Нет занятий"
                }
            },
            5: {
                "Школа": {
                    "1": "8:00 - 8:40 Физика ",
                    "2": "8:55 - 9:35 Литература",
                    "3": "9:50 - 10:30 Биология",
                    "4": "10:45 - 11:25 Английский язык",
                    "5": "11:35 - 12:15 Физкультура",
                    "6": "12:25 - 13:05 Математика"
                },
                "Цтриго": {
                    "1": "16:50 - 18:10 Системное администрирование"
                }
            },
            6: {
                "Школа": {
                    "1": "8:00 - 8:40 Информатика ",
                    "2": "8:55 - 9:35 Информатика",
                    "3": "9:50 - 10:30 Физика",
                    "4": "10:45 - 11:25 ОБЖ",
                    "5": "11:35 - 12:15 Русский язык",
                    "6": "12:25 - 13:05 Литература"
                },
                "Цтриго": {
                    "1": "14:35 - 16:40 Физика",
                    "2": "17:35 - 18:55 Математика"
                }
            },
            7: {
                "Школа": {
                    "1": "Нет занятий"
                },
                "Цтриго": {
                    "1": "Нет занятий"
                }
            }
        }
        # Преобразование из формата json в вид сообщения
        otvet = f"Школа:\n"
        for i in data[datetime.datetime.today().isoweekday()]["Школа"]:
            otvet = otvet + f"{data[datetime.datetime.today().isoweekday()]['Школа'][i]}\n"
        otvet = otvet + f"\nЦТРиГО:\n"
        for i in data[datetime.datetime.today().isoweekday()]['Цтриго']:
            otvet = otvet + f"{data[datetime.datetime.today().isoweekday()]['Цтриго'][i]}\n"
        return otvet

    # Создаём метод для погоды
    @classmethod
    def weather(cls):
        # Получаем токен для погоды
        open_weather_token = "50fad483f0d646f791e9fb5b82950a52"
        # Емоджи для разных видов погоды
        code_to_smile = {
            "Clear": "Ясно \U00002600",
            "Clouds": "Облачно \U00002601",
            "Rain": "Дождь \U00002614",
            "Drizzle": "Дождь \U00002614",
            "Thunderstorm": "Гроза \U000026A1",
            "Snow": "Снег \U0001F328",
            "Mist": "Туман \U0001F32B"
        }
        town = "sochi"
        # Получаем данные о погоде в Сочи в формате json
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={town}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        # Сохраняем значения
        city = data["name"]
        cur_weather = data["main"]["temp"]
        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])
        # Сохраняем в переменную все полученные данные
        otvet = f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n" \
                f"Погода в городе: {city}\nТемпература: {cur_weather}C° {wd}\n" \
                f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n" \
                f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n" \
                f"***Хорошего дня!***"
        # Возвращаем переменную
        return otvet

    # Создаём метод отвечающий за курс валют
    @classmethod
    def valute(cls):
        # Сохраняем данные о курсах валлют с ЦБ РФ
        data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
        # Преобразовываем полученные данные в сообщение
        otvet = f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n" \
                f"Курс валлют:\n\n"f"Валлюта: {data['Valute']['USD']['Name']} 💵\n" \
                f"Номинал: {data['Valute']['USD']['Nominal']}\n" \
                f"Стоимость в рублях: {data['Valute']['USD']['Value']}\n\n" \
                f"Валлюта: {data['Valute']['EUR']['Name']} 💶\n" \
                f"Номинал: {data['Valute']['EUR']['Nominal']}\n" \
                f"Стоимость в рублях: {data['Valute']['EUR']['Value']}"
        # Возваращем преобразованные данные
        return otvet
