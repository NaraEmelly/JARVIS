from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from os import getcwd
import os
import time

# ==========================
# CONFIGURAÇÃO DO CHROME
# ==========================

chrome_options = Options()

# Permite acesso automático ao microfone
chrome_options.add_argument("--use-fake-ui-for-media-stream")

# Se quiser ver a janela do Chrome, deixe comentado
# chrome_options.add_argument("--headless=new")

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(
    service=service,
    options=chrome_options
)

# ==========================
# ABRIR HTML LOCAL
# ==========================

website = "file:///" + os.path.abspath("STT/index.html")

print("Abrindo:", website)

driver.get(website)

# ==========================
# ARQUIVO DE SAÍDA
# ==========================

Recog_File = f"{getcwd()}\\input.txt"

# ==========================
# FUNÇÃO DE ESCUTA
# ==========================

def listen():

    print("JARVIS STT iniciado")

    try:

        start_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.ID, "startButton"))
        )

        print("Botão encontrado")

        # Clica automaticamente
        start_button.click()

        print("Escutando...")

        last_text = ""

        while True:

            try:

                output_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "output"))
                )

                current_text = output_element.text.strip()

                if (
                    current_text
                    and current_text != last_text
                    and current_text != "Diga algo..."
                ):

                    last_text = current_text

                    print("Você:", current_text)

                    with open(
                        Recog_File,
                        "w",
                        encoding="utf-8"
                    ) as file:

                        file.write(current_text.lower())

                time.sleep(0.5)

            except Exception as e:
                print("Erro ao ler texto:", e)

    except KeyboardInterrupt:

        print("Encerrado pelo usuário")

    except Exception as e:

        print("Erro:")
        print(e)

    finally:

        driver.quit()