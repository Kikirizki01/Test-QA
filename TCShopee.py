import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set path ke ChromeDriver dan Chrome
s = Service("C:\\Program Files (x86)\\chromedriver.exe")
chrome_options = Options()
chrome_options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
chrome_options.add_argument("--disable-notifications")  # Disable notifications

# Inisialisasi WebDriver dengan opsi yang benar
browser = webdriver.Chrome(service=s, options=chrome_options)

# Buka halaman Shopee
browser.get('https://shopee.co.id/buyer/login')
time.sleep(5)

# Isi form login
browser.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/form/div[1]/div[1]/input").send_keys("No.Hp")
time.sleep(5)
browser.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div[2]/form/div[2]/div[1]/input").send_keys("Passsword")
time.sleep(5)

# Klik tombol login
login_button = browser.find_element(By.XPATH, "//button[contains(text(), 'Log in')]")
login_button.click()
time.sleep(20)




