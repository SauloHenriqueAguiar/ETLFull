from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# Configurar opções do Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')

# Configurar o caminho do Chromedriver
chrome_driver_path = 'C:\\Users\\user\\wbscraping\\chromedriver-win64\\chromedriver.exe'

# Configurar o driver do Chrome
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)


driver.get("https://www.amazon.com/-/es/s?k=libros&language=es&qid=1694366636&ref=sr_pg_1")

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_all_elements_located((By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")))

body = driver.find_element(By.TAG_NAME, "body")
for _ in range(5):  # Scroll down multiple times
    body.send_keys(Keys.END)
    sleep(2)  # Esperar para carregar novos produtos

names = driver.find_elements(By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")
prices_whole = driver.find_elements(By.XPATH, "//span[@class='a-price-whole']")
prices_fraction = driver.find_elements(By.XPATH, "//span[@class='a-price-fraction']")

print(len(prices_whole), len(prices_fraction), len(names))

namesText = [name.text for name in names]

pricesList = []
for i in range(len(prices_whole)):
    whole = prices_whole[i].text
    fraction = prices_fraction[i].text if i < len(prices_fraction) else '00'
    price = whole + '.' + fraction
    pricesList.append(price)

print("Nomes dos produtos:")
print(namesText)
print("Preços dos produtos:")
print(pricesList)

driver.quit()
