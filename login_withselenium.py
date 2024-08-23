from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import csv

navegador = webdriver.Chrome()

navegador.get("https://www.saucedemo.com/")
sleep(3)


# ---------- LOGIN -----------

#USER
#encontra local de user
input_user = navegador.find_element(By.XPATH, '//input[@id="user-name"]')
#cola o usuário
input_user.send_keys('standard_user')

sleep(1)

#PASSWORD
#encontra local de user
input_key = navegador.find_element(By.XPATH, '//*[@id="password"]')
#cola o usuário
input_key.send_keys('secret_sauce')

#CLICK em LOGIN
navegador.find_element(By.XPATH, '//*[@id="login-button"]').click()

sleep(3)


# ----- Adicionar ítem no carrinho ------

#Click no produto
navegador.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div').click()
sleep(1)

#Add to cart
navegador.find_element(By.XPATH, '//*[@id="add-to-cart"]').click()
sleep(1)

# ----- Finalizar -----

#Clicar no carrinho
navegador.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
sleep(1)

#Checkout
navegador.find_element(By.XPATH, '//*[@id="checkout"]').click()
sleep(1)

#Informações
input_name = navegador.find_element(By.XPATH, '//*[@id="first-name"]')
input_name.send_keys('Vinicius')
sleep(2)

input_first = navegador.find_element(By.XPATH, '//*[@id="last-name"]')
input_first.send_keys('Paschoal')
sleep(2)

input_CEP = navegador.find_element(By.XPATH, '//*[@id="postal-code"]')
input_CEP.send_keys(12345678)
sleep(2)

navegador.find_element(By.XPATH, '//*[@id="continue"]').click()

#Finaliza
navegador.find_element(By.XPATH, '//*[@id="finish"]').click()

sleep(3)



