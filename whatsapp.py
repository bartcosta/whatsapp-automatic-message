from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

import time

to = input('Pra quem voce deseja enviar a mensagem? ')
message = input('Insira a mensagem: ')

navegador = webdriver.Chrome(ChromeDriverManager().install())

try:
	navegador.get("https://web.whatsapp.com")

	time.sleep(10)

	navegador.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]').send_keys(to + Keys.RETURN)

	navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message + Keys.RETURN)
    
finally:
    navegador.quit()

