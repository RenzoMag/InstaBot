from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from os import system
from time import sleep
import os
import random
from random import choice
import sys


class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.login()

    def random_number_generator(self, x, y):
        global random_number
        random_number = random.randrange((x * 100), (y * 100)) / 100
        return random_number

    def login(self):
        os.system('CLS')
        global cantidad
        cantidad = int(input(CYAN+ "Ingrese cantidad para seguir:"))
        os.system('CLS')
        sleep(0.6)
        print(RED+ "OK!")
        sleep(0.6)
        os.system('CLS')
        global tiempo1
        tiempo1 = int(input(CYAN+ "Ingrese primer digito de la randomización del tiempo:"))
        os.system('CLS')
        sleep(0.6)
        print(RED+ "OK!")
        sleep(0.6)
        os.system('CLS')
        global tiempo2
        tiempo2 = int(input(CYAN+ "Ingrese segundo digito de la randomización del tiempo:"))
        os.system("CLS")
        sleep(0.6)
        print(RED+ "OK!")
        sleep(0.6)
        os.system("CLS")
        global apagado
        apagado = (input(CYAN+ "Apagar computadora luego de la finalizacion del programa: (si / no):"))
        os.system("CLS")
        sleep(0.6)
        print(RED+ "OK!")
        sleep(0.6)
        os.system('CLS')
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )
        sleep(1)
        self.driver.get('https://instagram.com/accounts/login')
        sleep(self.random_number_generator(2, 4))
        self.driver.find_element_by_name('username').send_keys(self.username)
        password_field = self.driver.find_element_by_name('password')
        password_field.send_keys(self.password)
        password_field.send_keys(Keys.RETURN)
        sleep(self.random_number_generator(1, 2))
        os.system('CLS')
        print(RED+ "Logueado")
        sleep(2)
        os.system('CLS')

    def nav_user(self, user):
        sleep(self.random_number_generator(2, 3))
        self.driver.get('https://instagram.com/' + user)

    def follow_user(self, user):
        self.nav_user(user)
        try:
            self.driver.find_element_by_xpath("//*[text()='Seguir']").click()
            print(YELLOW+ user, RED+ "Seguido")
        except:
            pass


    def user_followers(self, user, limit=70):
        self.nav_user(user)
        sleep(self.random_number_generator(2, 4))
        followers_btn = self.driver.find_element_by_xpath(f"//a[contains(@href, '/{user}/followers/')]")
        followers_btn.click()
        sleep(self.random_number_generator(2, 4))
        fBody = self.driver.find_element_by_xpath("//div[@class='isgrP']")
        scroll = 0
        while scroll < 25:
            print("Obteniendo Seguidores...")
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
            scroll += 1
            sleep(1)
        followers_list = []
        for i in range(limit):
            follower = self.driver.find_elements_by_class_name('_0imsa')[i]
            followers_list.append(follower.text)
        os.system('CLS')
        print(YELLOW+"Se seguiran las siguientes cuentas:")
        print(WHITE, followers_list)
        return followers_list

    def follow_users(self, users):
        for user in users:
            self.smart_follow(user)
    
    def smart_follow_check(self, user):
        try:
            self.nav_user(user)
            followers = self.driver.find_element_by_xpath(f'//a[contains(@href, "{user}/followers")]/span')
            string = followers.text
            string = string.replace(',', '')
            Seguidores_num = int(string)
            following = self.driver.find_element_by_xpath(f'//a[contains(@href, "{user}/following")]/span')
            string1 = following.text
            string1 = string1.replace(',', '')
            Seguidos_num = int(string1)
            if Seguidos_num > Seguidores_num:
                return True
            return False
        except:
            pass

    def smart_follow(self, user):
        sleep(self.random_number_generator(tiempo1, tiempo2))
        print(CYAN+f"Espera de: {random_number} segundos")
        self.follow_user(user)

    def follow_user_followers(self, user, limit=50):
        users = self.user_followers(user, limit=cantidad)
        self.follow_users(users)
        if apagado == "si":
            print(VIOLETA+ "Terminado")
            sleep(1)
            os.system("shutdown.exe -s -t 15")
            i = 1
            while i > 0:
                print("Esperando 15 segundos... [/]")
                os.system("cls")
                sleep(0.5)
                print("Esperando 15 segundos... [-]")
                sleep(0.5)
                os.system("cls")
                print("Esperando 15 segundos... [\\]")
                sleep(0.5)
                os.system("cls")
                print("Esperando 15 segundos... [|]")
                sleep(0.5)
                os.system("cls")
                print("Esperando 15 segundos... [/]")
                sleep(0.5)
                os.system("cls")
                print("Esperando 15 segundos... [-]")
                sleep(0.5)
                os.system("cls")
                print("Esperando 15 segundos... [\\]")
                sleep(0.5)
                os.system("cls")
                print("Esperando 15 segundos... [|]")
        elif apagado == "no":
            print(VIOLETA+ "Terminado")
            sleep(5)
            self.driver.quit()
        else:
            print(VIOLETA+ "Terminado")
            sleep(5)
            self.driver.quit()


if __name__ == "__main__":

 YELLOW = '\033[33m'
 CYAN = '\033[36m'
 RED = '\033[31m'
 WHITE = '\033[37m'
 VIOLETA="\033[35m"
 RESET = "\033[39m'WHITE = '\033[30m"




    
 bot = InstagramBot('user', 'password')
    

 l2 = ["accounts"]
 cuentas = random.choice(l2)
 
 
 bot.follow_user_followers(f"{cuentas}")
 
 
 

