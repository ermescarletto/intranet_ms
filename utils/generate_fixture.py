import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json

def obter_dia_festivo(termo):
    # Inicializa o WebDriver do Chrome
    driver = webdriver.Chrome()

    try:
        # Abre o Google e faz a busca
        driver.get('https://www.google.com/')
        campo_busca = driver.find_element(By.NAME, 'q')
        campo_busca.send_keys('dia do ' + termo)
        campo_busca.send_keys(Keys.RETURN)

        # Espera até que os resultados carreguem
        driver.implicitly_wait(10)

        # Encontra e extrai o conteúdo do elemento
        elemento = driver.find_element(By.CLASS_NAME, 'IZ6rdc')
        conteudo = elemento.text

        return conteudo
    except:
        print(f'Elemento não localizado para o cargo{termo}')
    finally:
        # Fecha o navegador
        driver.quit()

with open('utils/cargos.csv') as cargos_csv:
    reader = csv.reader(cargos_csv,delimiter=",")
    cargo_list =  []
    for row in reader:
        
        cargo = {
        "model":"intranet.cargo",
        "pk" : row[0],
        "fields": {
            "descricao" : row[1],
            "dia_festivo" : obter_dia_festivo(row[1])
            }
        }
        cargo_list.append(cargo)
        print(cargo)
    fixture_json = json.dumps(cargo_list)
    arquivo = open('cargos.json', 'w')
    arquivo.write(str(fixture_json))
