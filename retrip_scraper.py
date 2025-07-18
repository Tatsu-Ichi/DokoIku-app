# retrip_scraper.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def fetch_spots():
    options = Options()
    options.add_argument("--headless")
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    )

    driver = webdriver.Chrome(options=options)
    url = "https://rtrp.jp/locations/383/scenes/20/"
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href*="/spots/"]')))
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    results = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        name = a.text.strip()
        if any(x in name for x in ["もっとみる", "このスポットをみる"]): continue
        if any(x in href for x in ["/reviews/", "/images/"]): continue
        if "/spots/" not in href: continue
        results.append((name, href))

    return results
