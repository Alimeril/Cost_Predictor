from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

def read_car_name(driver,path):
    w = 1
    car_name = ''
    while True:
        try:
            xpath = path + f'/span[{w}]'
            part = driver.find_element(By.XPATH,xpath)
            # Because car name are in persian we reverse add the names.
            car_name = part.text + car_name  
            w += 1
        except NoSuchElementException:
            break
    return car_name

class car_properties():
    def __init__(self):
        self.name = None
        self.year = None
        self.km = None
        self.description = None
        self.price = None

    def read_car(self,driver,path):
        self.name = read_car_name(driver,(path + '/div[2]/p/span'))
        try:
            year_element = driver.find_element(By.XPATH, path + '/div[3]/span[1]')
            self.year = year_element.text.replace(' ','')
        except NoSuchElementException:
            self.year = None
        try:
            km_element = driver.find_element(By.XPATH, path + '/div[3]/span[2]')
            self.km = km_element.text.replace(' ','')
        except NoSuchElementException:
            self.km = None
        try:
            desc_element = driver.find_element(By.XPATH, path + '/div[3]/span[3]')
            self.description = desc_element.text.replace(' ','')
        except NoSuchElementException:
            self.description = None
        try:
            price_element = driver.find_element(By.XPATH, path + '/div[4]/div[2]/span')
            self.price = price_element.text.replace(' ','')
        except NoSuchElementException:
            try:
                price_element = driver.find_element(By.XPATH, path + '/div[5]/div[2]/span')
                self.price = price_element.text.replace(' ','')
            except NoSuchElementException:
                self.price = None

def read_data():
    car_list = []
    driver = webdriver.Safari()
    driver.get("https://bama.ir/car")
    driver.maximize_window()
    time.sleep(5)

    for i in range(100):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(0.8)
    time.sleep(1)

    for i in range(1,401):
        new_car = car_properties()
        new_car.read_car(driver,f'//*[@id="__layout"]/div/div[1]/section/div[2]/div[2]/div[{i}]/a')
        if new_car.name == None:
            continue
        elif new_car.year == None:
            continue
        elif new_car.km == None:
            continue
        elif new_car.description == None:
            continue
        elif new_car.price == None or new_car.price == 'توافقی':
            continue
        else:
            car_list.append(new_car)
    
    return car_list