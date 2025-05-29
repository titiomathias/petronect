import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

bot = webdriver.Chrome()
bot.maximize_window()
bot.get("https://www.petronect.com.br/irj/portal/anonymous")

# Função para entrar nos iframes
def get_in_iframes(bot):
    WebDriverWait(bot, 30).until(
        EC.frame_to_be_available_and_switch_to_it((By.ID, "contentAreaFrame"))
    )
    print("Entrnando no primeiro iframe do Painel de Oportunidades...")

    WebDriverWait(bot, 30).until(
        EC.frame_to_be_available_and_switch_to_it((By.ID, "isolatedWorkArea"))
    )
    print("Entrnando no segundo iframe do Painel de Oportunidades...")

# Função para sair dos iframes
def get_out_iframes(bot):
    try:
        bot.switch_to.default_content()
        print("Saindo do iframe com sucesso!")
    except Exception as e:
        print(f"Erro ao sair do iframe: {e}")
        bot.save_screenshot('erro_sair_iframe.png')


def download_item(bot, item_name):
    time.sleep(10)
    print(f"Iniciando o download do item: {item_name}")
    abas = bot.window_handles
    print("Abas: ", abas)
    aba_original = bot.current_window_handle
    print("Aba original: ", aba_original)

    bot.switch_to.window(abas[-1])
    print("Mudando para a última aba aberta: ", abas[-1])
    time.sleep(5)

    download_button = WebDriverWait(bot, 30).until(
        EC.presence_of_element_located((By.ID, 'DOWNLOAD_BUTTON'))
    )
    download_button.click()
    print(f"{item_name} baixado com sucesso!")

    time.sleep(5)

    close_button = WebDriverWait(bot, 30).until(
        EC.presence_of_element_located((By.ID, 'CLOSE_BUTTON'))
    )
    close_button.click()

    bot.switch_to.window(aba_original)
    print("Voltando para a aba original: ", aba_original)

bot.implicitly_wait(5)

btn_login = bot.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[3]')
btn_login.click()

username = bot.find_element(By.XPATH, '//*[@id="inputUser"]')
password = bot.find_element(By.XPATH, '//*[@id="inputSenha"]')
login = bot.find_element(By.XPATH, '//*[@id="Continuar"]')

username.send_keys("Lipe_Reis")
password.send_keys("Antoniosporko10")
login.click()

try:
    bot.find_element(By.XPATH, '//*[@id="ltext"]/h4')
    try:
        mail = bot.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/span')
        print("Requer confirmação de identidade, código enviado para o e-mail: ", mail.text)
        bot.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div[3]/form/button[2]').click()
    except Exception as e:
        print("Código já enviado! Aguarde alguns segundos e digite o código recebido no e-mail.")
        time.sleep(3)
        codigo = input(f"Digite o código de confirmação enviado para o e-mail: ")
        input_code = bot.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div[3]/form/div/input')
        input_code.send_keys(codigo)
        bot.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div[3]/form/button[2]').click()
    else:
        codigo = input(f"Digite o código de confirmação enviado para o e-mail: ")
        input_code = bot.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div[3]/form/div/input')
        input_code.send_keys(codigo)
        bot.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div[3]/form/button[2]').click()
except Exception as e:
    print("Não requer confirmação de identidade")
    print("Exceção: ", e)
finally:
    # Cotações Eletrônicas
    bot.implicitly_wait(15)
    cotacoes = bot.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/div/table/tbody/tr/td/table[1]/tbody/tr/td[1]/div/div/div[3]/div[2]/div[2]')
    cotacoes.click()
    time.sleep(5)
    cotacoes.click()
    print("Cotações Eletrônicas acessadas com sucesso!")
    bot.implicitly_wait(15)

    # Desbloquear Sessão
    bot.implicitly_wait(15)
    bot.find_element(By.XPATH, '//*[@id="subTabIndex2"]/div[1]').click()
    print("Entrando na aba de desbloqueio de sessão...")
    bot.implicitly_wait(30)

    get_in_iframes(bot)

    try:
        executar = WebDriverWait(bot, 30).until(
            EC.presence_of_element_located((By.ID, 'WD21'))
        )
        executar.click()
        print("Botão Executar encontrado e clicado com sucesso!")
    except Exception as e:
        print(f"Erro ao interagir com elementos dentro do iframe: {e}")
        bot.save_screenshot('erro_iframe.png')
    finally:
        get_out_iframes(bot)
    
    try:
        WebDriverWait(bot, 30).until(
            EC.frame_to_be_available_and_switch_to_it((By.ID, "URLSPW-0"))
        )

        confirmar = WebDriverWait(bot, 30).until(
            EC.presence_of_element_located((By.ID, 'WD44'))
        )

        confirmar.click()
        print("Botão Confirmar encontrado e clicado com sucesso!")
    except Exception as e:
        print(f"Erro ao interagir com elementos dentro do iframe: {e}")
        bot.save_screenshot('erro_iframe.png')
    finally:
        get_out_iframes(bot)

    # Painel de Oportunidades
    bot.implicitly_wait(15)
    bot.find_element(By.XPATH, '//*[@id="subTabIndex1"]/div[1]').click()

    get_in_iframes(bot)

    try:
        input_number = WebDriverWait(bot, 30).until(
            EC.presence_of_element_located((By.ID, 'WD024B'))
        )
        input_number.click()
        print("Campo de entrada encontrado com sucesso!")
        time.sleep(10)
        input_number.click()
        print("Cliclou a segunda vez no campo de entrada!")
        time.sleep(2)
        input_number.send_keys("7004461738")
        print("Enviou os dados no input")

        time.sleep(5)

        search_button = WebDriverWait(bot, 30).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/table/tbody/tr/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/table/tbody/tr[3]/td/div[1]/div/table/tbody/tr/td/span/span/table/tbody/tr/td/span/span[2]/table/tbody/tr/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div/span[1]'))
        )
        search_button.click()
        print("Botão de pesquisa encontrado e clicado com sucesso!")

        time.sleep(5)

        first_result = WebDriverWait(bot, 30).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/table/tbody/tr/td/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/table/tbody/tr[3]/td/div[1]/div/table/tbody/tr/td/span/span/table/tbody/tr/td/span/span[4]/table/tbody/tr/td/span/span[1]/div/div/div/span/span/table/tbody/tr[2]/td/div/table/tbody/tr/td/div/table/tbody/tr/td[1]/table/tbody/tr[2]/td[2]'))
        )
        first_result.click()
        print("Primeiro resultado encontrado e clicado com sucesso!")

        time.sleep(15)  
    except Exception as e:
        print(f"Erro ao interagir com elementos dentro do iframe: {e}")
        bot.save_screenshot('erro_iframe.png')
    finally:
        get_out_iframes(bot)


    # Baixar PDF e ZIP
    
    get_in_iframes(bot)

    try:
        link_to_pdf = WebDriverWait(bot, 30).until(
            EC.presence_of_element_located((By.ID, 'WD20'))
        )
        link_to_pdf.click()

        # Download do PDF
        download_item(bot, "PDF")

        get_out_iframes(bot)
        get_in_iframes(bot)

        print("Seguindo para notas e anexos...")
        notas_e_anexos = WebDriverWait(bot, 30).until(
            EC.presence_of_element_located((By.ID, 'WD44-title'))
        )
        notas_e_anexos.click()
        print("Notas e Anexos acessados com sucesso!")

        time.sleep(5)

        # Link para o arquivo ZIP
        print("Procurando pelo link do arquivo ZIP...")
        link_to_zip = WebDriverWait(bot, 30).until(
            EC.presence_of_element_located((By.ID, 'WD0176'))
        )
        link_to_zip.click()
        print("Link para o arquivo ZIP encontrado e clicado com sucesso!")

        # Download do ZIP
        download_item(bot, "ZIP")
    except Exception as e:
        print(f"Erro ao interagir com elementos dentro do iframe: {e}")
        bot.save_screenshot('erro_iframe.png')
    finally:
        get_out_iframes(bot)
        bot.find_element(By.XPATH, '//*[@id="subTabIndex1"]/div[1]').click()

print("Fechando o navegador...")
time.sleep(1000)


