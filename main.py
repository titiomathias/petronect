import time
from selenium import webdriver
from selenium.webdriver.common.by import By

bot = webdriver.Chrome()
bot.get("https://www.petronect.com.br/irj/portal/anonymous")

bot.implicitly_wait(5)

btn_login = bot.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[3]')
btn_login.click()

username = bot.find_element(By.XPATH, '//*[@id="inputUser"]')
password = bot.find_element(By.XPATH, '//*[@id="inputSenha"]')
login = bot.find_element(By.XPATH, '//*[@id="Continuar"]')

username.send_keys("Lipe_Reis")
password.send_keys("Antoniosporko10")
login.click()

time.sleep(220)

try:
    bot.find_element(By.XPATH, '//*[@id="ltext"]/h4')
except Exception as e:
    print("Não requer confirmação de identidade")
else:
    mail = bot.find_element(By.XPATH, '//*[@id="lcontent"]/div[2]/div[2]/div/span')
    print("Requer confirmação de identidade, código enviado para o e-mail: ", mail.text)
    bot.find_element(By.XPATH, '//*[@id="005056931CB01FD08DC9F2FDE4B57C9A"]').click()
finally:
    bot.implicitly_wait(5)
    cotacoes_eletronicas = bot.find_element(By.XPATH, '//*[@id="tabIndex2"]/div[2]/div[2]')
    cotacoes_eletronicas.click()
    bot.implicitly_wait(15)
    desbloquear_sessao = bot.find_element(By.XPATH, '//*[@id="subTabIndex2"]/div[1]')
    desbloquear_sessao.click()
    bot.implicitly_wait(15)
    bot.find_element(By.XPATH, '//*[@id="WD21"]').click()
    bot.implicitly_wait(15)
    bot.find_element(By.XPATH, '//*[@id="WD44"]').click()
    bot.implicitly_wait(15)
    painel_de_oportunidades = bot.find_element(By.XPATH, '//*[@id="subTabIndex1"]/div[1]')

time.sleep(2)

time.sleep(220)


