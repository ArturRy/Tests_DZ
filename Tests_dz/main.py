import requests
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


def wait_element(browser, delay_seconds=1, by=By.TAG_NAME, value=None):
    return WebDriverWait(browser, delay_seconds).until(
        expected_conditions.presence_of_element_located((by, value))
    )


o = Options()
o.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=o)

courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python",
           "Frontend-разработчик с нуля"]

mentors = [
    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
     "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков",
     "Роман Гордиенко"],
    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
     "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
     "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
     "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
     "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков",
     "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
     "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]


def unique_names(mentors):
    ulist = []
    for name in mentors:
        ulist.extend(name)
    uname = sorted(set(' '.join(ulist).split()[0::2]))
    unamesort = (', '.join((uname)))
    res = f'Уникальные имена преподавателей: {unamesort}'
    return res


def top_3_name(mentors):
    all_name = []
    all_name_list = []
    for name in mentors:
        all_name_list.extend(name)
    for name in mentors:
        all_name.extend(name)
    uname = list(set(' '.join(all_name).split()[0::2]))
    count_list = []
    names = ' '.join(all_name_list).split()[0::2]
    for n in uname:
        if n in names:
            count_list.append([n, names.count(n)])
    sort_list = sorted(count_list, key=lambda x: x[1], reverse=True)
    sname = (sort_list[0:3])
    pname = []
    for name in sname:
        pname.append(name[0] + ': ' + str(name[1]) + ' раз(а)')
    res = ', '.join(pname)
    return res


Some_name = 'Name'


def supernames(mentors, courses):
    mentors_names = []
    for m in mentors:
        course_names = []
        for name in m:
            course_names.append(name.split()[0])
        mentors_names.append(course_names)

    pairs = []

    for id1 in range(len(mentors_names)):
        for id2 in range(len(mentors_names)):
            if id1 == id2: continue

            intersection_set = set(mentors_names[id1]) & set(mentors_names[id2])
            if len(intersection_set) > 0:

                pair = {courses[id1], courses[id2]}

                if pair not in pairs:
                    pairs.append(pair)

                    all_names_sorted = sorted(intersection_set)

                    res = (f"На курсах '{courses[id1]}' и '{courses[id2]}' преподают: {', '.join(all_names_sorted)}")
                    return res


def direct():
    token_y = 'Token'
    directory = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Authorization': token_y}
    params_directory = {'path': f'some_direct',
                        'permanently': 'true'}
    res_del = requests.delete(directory, params=params_directory, headers=headers)
    res_put = requests.put(directory, params=params_directory, headers=headers)
    return res_put


driver.get('https://passport.yandex.ru/auth/add')
input_log_in = wait_element(driver, by=By.CLASS_NAME, value='Textinput-Control')
input_log_in.send_keys('Login')
inter_button = wait_element(driver, by=By.ID, value='passp:sign-in')
inter_button.click()
input_password = wait_element(driver, by=By.ID, value='passp-field-passwd')
input_password.send_keys('Password')
inter_button_2 = wait_element(driver, by=By.ID, value='passp:sign-in')
inter_button_2.click()
status = wait_element(driver, by=By.TAG_NAME, value='title')
print(status.text)

# driver.close()
