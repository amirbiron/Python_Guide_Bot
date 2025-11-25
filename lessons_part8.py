# -*- coding: utf-8 -*-
"""
מסלול A: Web Scraping & Automation
שיעורים 36-40 - מסלול התמחות באיסוף מידע מהרשת
"""

LESSONS_PART8 = {
    36: {
        'title': '🌐 מסלול A.1: BeautifulSoup - התחלה',
        'content': r'''
ברוכים הבאים למסלול Web Scraping! 🕷️

🎯 <b>מה נלמד במסלול הזה?</b>
• BeautifulSoup - פרסור HTML
• Selenium - אתרים דינמיים
• Requests - קבלת דפים
• אוטומציה - שליחת הודעות
• פרויקט: Price Tracker מלא!

---

📦 <b>התקנה:</b>
<code>pip install requests beautifulsoup4 lxml</code>

🌍 <b>הבסיס - קבלת דף:</b>
<code>import requests
from bs4 import BeautifulSoup

# קבלת דף:
url = "https://example.com"
response = requests.get(url)
html = response.text

# יצירת soup:
soup = BeautifulSoup(html, 'lxml')
print(soup.prettify())</code>

🔍 <b>חיפוש אלמנטים - שיטות:</b>

<b>1. find() - מציאה ראשונה:</b>
<code>from bs4 import BeautifulSoup

html = """
<html>
    <h1>כותרת ראשית</h1>
    <p class="intro">פסקה ראשונה</p>
    <p class="content">פסקה שנייה</p>
    <p class="content">פסקה שלישית</p>
</html>
"""

soup = BeautifulSoup(html, 'lxml')

# מציאת h1 ראשון:
h1 = soup.find('h1')
print(h1.text)  # כותרת ראשית

# מציאת p עם class:
intro = soup.find('p', class_='intro')
print(intro.text)  # פסקה ראשונה

# מציאת p ראשון:
first_p = soup.find('p')
print(first_p.text)  # פסקה ראשונה</code>

<b>2. find_all() - כל ההתאמות:</b>
<code># כל ה-p:
all_p = soup.find_all('p')
for p in all_p:
    print(p.text)

# כל ה-p עם class='content':
content_p = soup.find_all('p', class_='content')
print(len(content_p))  # 2

# הגבלה - רק 2 ראשונים:
first_two = soup.find_all('p', limit=2)</code>

<b>3. select() - CSS Selectors:</b>
<code># כל ה-p:
all_p = soup.select('p')

# לפי class:
intro = soup.select('.intro')

# לפי id:
header = soup.select('#header')

# מורכב:
content_in_div = soup.select('div.container > p.content')</code>

🎯 <b>גישה לאטריביוטים:</b>
<code>html = """
<a href="https://example.com" id="link1" class="external">
    לחץ כאן
</a>
<img src="image.jpg" alt="תמונה יפה">
"""

soup = BeautifulSoup(html, 'lxml')

# גישה ל-href:
link = soup.find('a')
print(link['href'])        # https://example.com
print(link.get('href'))    # https://example.com (בטוח יותר)
print(link['class'])       # ['external']
print(link.text)           # לחץ כאן

# גישה ל-src:
img = soup.find('img')
print(img['src'])          # image.jpg
print(img.get('alt'))      # תמונה יפה</code>

📊 <b>דוגמה מציאותית - חדשות:</b>
<code>import requests
from bs4 import BeautifulSoup

def scrape_headlines():
    url = "https://news.ycombinator.com"
    
    # Headers להראות כמו דפדפן:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    
    # מציאת כותרות:
    headlines = soup.select('.titleline > a')
    
    print("📰 כותרות עדכניות:\n")
    for i, headline in enumerate(headlines[:10], 1):
        title = headline.text
        link = headline.get('href', '')
        
        # תיקון לינקים יחסיים:
        if not link.startswith('http'):
            link = f"https://news.ycombinator.com/{link}"
        
        print(f"{i}. {title}")
        print(f"   🔗 {link}\n")

scrape_headlines()</code>

🔗 <b>חילוץ לינקים:</b>
<code>import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

# כל הלינקים:
links = soup.find_all('a')

print("🔗 לינקים בדף:\n")
for link in links:
    href = link.get('href')
    text = link.text.strip()
    
    if href and text:
        print(f"{text}: {href}")</code>

🖼️ <b>חילוץ תמונות:</b>
<code>images = soup.find_all('img')

print("🖼️ תמונות בדף:\n")
for img in images:
    src = img.get('src')
    alt = img.get('alt', 'ללא תיאור')
    
    if src:
        # תיקון URL יחסי:
        if not src.startswith('http'):
            src = f"https://example.com{src}"
        
        print(f"{alt}: {src}")</code>

📋 <b>חילוץ טבלאות:</b>
<code>html = """
<table>
    <tr>
        <th>שם</th>
        <th>גיל</th>
        <th>עיר</th>
    </tr>
    <tr>
        <td>אמיר</td>
        <td>25</td>
        <td>תל אביב</td>
    </tr>
    <tr>
        <td>דני</td>
        <td>30</td>
        <td>ירושלים</td>
    </tr>
</table>
"""

soup = BeautifulSoup(html, 'lxml')
table = soup.find('table')

# חילוץ שורות:
rows = table.find_all('tr')

for row in rows:
    cells = row.find_all(['td', 'th'])
    data = [cell.text.strip() for cell in cells]
    print(' | '.join(data))</code>

💪 <b>דוגמה מתקדמת - גילוי מחירים:</b>
<code>import requests
from bs4 import BeautifulSoup
import time

def scrape_product_prices(url):
    """גילוי מחירי מוצרים באתר"""
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'lxml')
        
        # חיפוש מחירים (תלוי באתר):
        products = []
        
        # דוגמה - אתר אי-קומרס:
        items = soup.select('.product-item')
        
        for item in items:
            name_elem = item.select_one('.product-name')
            price_elem = item.select_one('.product-price')
            
            if name_elem and price_elem:
                name = name_elem.text.strip()
                price = price_elem.text.strip()
                
                products.append({
                    'name': name,
                    'price': price
                })
        
        return products
    
    except requests.exceptions.RequestException as e:
        print(f"שגיאה: {e}")
        return []

# שימוש:
products = scrape_product_prices("https://example-shop.com")

for product in products:
    print(f"{product['name']}: {product['price']}")</code>

⚡ <b>טיפול בשגיאות:</b>
<code>import requests
from bs4 import BeautifulSoup

def safe_scrape(url):
    """Scraping בטוח עם טיפול בשגיאות"""
    try:
        # Timeout חשוב!
        response = requests.get(url, timeout=10)
        
        # בדיקת סטטוס:
        response.raise_for_status()
        
        # פרסור:
        soup = BeautifulSoup(response.text, 'lxml')
        
        return soup
        
    except requests.exceptions.Timeout:
        print("⏰ השרת לא עונה - timeout")
        return None
    
    except requests.exceptions.HTTPError as e:
        print(f"❌ שגיאת HTTP: {e}")
        return None
    
    except requests.exceptions.ConnectionError:
        print("🔌 אין חיבור לאינטרנט")
        return None
    
    except Exception as e:
        print(f"⚠️ שגיאה לא צפויה: {e}")
        return None

# שימוש:
soup = safe_scrape("https://example.com")
if soup:
    # עבוד עם הנתונים
    pass</code>

🎨 <b>ניקוי טקסט:</b>
<code>from bs4 import BeautifulSoup

html = """
<div>
    <p>  טקסט עם    רווחים מיותרים  </p>
    <p>עוד <span>טקסט</span> מעורב</p>
</div>
"""

soup = BeautifulSoup(html, 'lxml')

# .text - כל הטקסט:
div = soup.find('div')
print(div.text)  # יש רווחים מיותרים

# .get_text() עם אפשרויות:
text = div.get_text(separator=' ', strip=True)
print(text)  # טקסט נקי

# .stripped_strings - איטרטור:
for string in div.stripped_strings:
    print(f"- {string}")</code>

🔄 <b>Scraping מרובה עמודים:</b>
<code>import requests
from bs4 import BeautifulSoup
import time

def scrape_multiple_pages(base_url, max_pages=5):
    """Scrape כמה עמודים"""
    all_data = []
    
    for page in range(1, max_pages + 1):
        url = f"{base_url}?page={page}"
        print(f"📄 גולש לעמוד {page}...")
        
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        
        # חילוץ נתונים...
        items = soup.select('.item')
        all_data.extend([item.text for item in items])
        
        # המתן בין בקשות (חשוב מאוד!):
        time.sleep(2)
    
    return all_data

data = scrape_multiple_pages("https://example.com/products")</code>

⚠️ <b>חוקי Web Scraping:</b>

✅ <b>כן:</b>
• בדוק את robots.txt
• שלח headers תקינים
• המתן בין בקשות (2-3 שניות)
• כבד את תנאי השימוש
• בקש רשות אם צריך

❌ <b>לא:</b>
• אל תעמיס על השרת
• אל תשתמש בנתונים באופן לא חוקי
• אל תעקוף מנגנוני אבטחה
• אל תתחזה לבוט רשמי

📚 <b>טיפים חשובים:</b>

1. **תמיד בדוק אם יש API** - זה עדיף!
2. **השתמש ב-headers** - להראות כמו דפדפן
3. **טפל בשגיאות** - האינטרנט לא יציב
4. **המתן בין בקשות** - נימוס!
5. **שמור נתונים מקומית** - אל תבקש שוב
6. **תעד את הקוד** - תשכח מה עשית

🎯 <b>תרגיל מעשי:</b>
<code>"""
צור scraper שמחלץ:
1. כותרת הדף
2. כל הכותרות (h1, h2, h3)
3. כל הלינקים החיצוניים
4. מספר התמונות בדף

ושומר הכל ל-JSON
"""

import requests
from bs4 import BeautifulSoup
import json

def analyze_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    
    # כותרת:
    title = soup.find('title')
    
    # כותרות:
    headings = []
    for tag in ['h1', 'h2', 'h3']:
        for heading in soup.find_all(tag):
            headings.append({
                'level': tag,
                'text': heading.text.strip()
            })
    
    # לינקים חיצוניים:
    external_links = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        if href.startswith('http') and url not in href:
            external_links.append(href)
    
    # תמונות:
    images_count = len(soup.find_all('img'))
    
    result = {
        'title': title.text if title else 'אין כותרת',
        'headings': headings,
        'external_links': list(set(external_links)),
        'images_count': images_count
    }
    
    return result

# שימוש:
data = analyze_page("https://example.com")

# שמירה ל-JSON:
with open('page_analysis.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ הניתוח נשמר!")</code>

💡 <b>בשיעור הבא:</b>
נלמד Selenium - לאתרים עם JavaScript ואינטראקציה מתקדמת!
''',
        'exercise': {
            'question': """מה יודפס?

html = '<p class="text">שלום</p><p>עולם</p>'
soup = BeautifulSoup(html, 'lxml')
result = soup.find('p', class_='text')
print(result.text)""",
            'options': ['שלום', 'עולם', 'שלום עולם', 'None'],
            'correct_answer': 'שלום',
            'explanation': 'נכון! 🎯 find() מחזיר את האלמנט הראשון שמתאים, במקרה הזה ה-p הראשון עם class="text"'
        }
    },
    
    37: {
        'title': '🤖 מסלול A.2: Selenium - אתרים דינמיים',
        'content': r'''
עכשיו נלמד לעבוד עם אתרים שמשתמשים ב-JavaScript! 🚀

🎯 <b>למה Selenium?</b>
BeautifulSoup רואה רק HTML סטטי. אתרים מודרניים משתמשים ב-JavaScript לטעינת תוכן. Selenium מדמה דפדפן אמיתי!

📦 <b>התקנה:</b>
<code># Selenium:
pip install selenium

# WebDriver Manager (מומלץ!):
pip install webdriver-manager</code>

🌐 <b>התחלה בסיסית:</b>
<code>from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# יצירת דפדפן:
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

# גלישה לדף:
driver.get("https://example.com")

# הצגת כותרת:
print(driver.title)

# קבלת HTML:
html = driver.page_source
print(html)

# סגירה:
driver.quit()</code>

🔍 <b>מציאת אלמנטים:</b>

<code>from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://example.com")

# לפי ID:
element = driver.find_element(By.ID, "username")

# לפי Name:
element = driver.find_element(By.NAME, "email")

# לפי Class:
element = driver.find_element(By.CLASS_NAME, "btn-primary")

# לפי CSS Selector:
element = driver.find_element(By.CSS_SELECTOR, ".container > p")

# לפי XPath:
element = driver.find_element(By.XPATH, "//button[@type='submit']")

# כל האלמנטים:
elements = driver.find_elements(By.TAG_NAME, "a")

driver.quit()</code>

⌨️ <b>אינטראקציה עם אלמנטים:</b>

<code>from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.google.com")

# מציאת שדה חיפוש:
search_box = driver.find_element(By.NAME, "q")

# הקלדה:
search_box.send_keys("Python tutorial")

# Enter:
search_box.send_keys(Keys.RETURN)

# המתן לטעינה:
import time
time.sleep(2)

# לחיצה על כפתור:
button = driver.find_element(By.ID, "submit-btn")
button.click()

# ניקוי שדה:
search_box.clear()

# קבלת טקסט:
text = button.text
print(text)

# קבלת אטריביוט:
href = button.get_attribute("href")

driver.quit()</code>

⏰ <b>Waits - המתנות חכמות:</b>

<b>1. Implicit Wait:</b>
<code>from selenium import webdriver

driver = webdriver.Chrome()

# המתן עד 10 שניות לכל אלמנט:
driver.implicitly_wait(10)

driver.get("https://example.com")

# אם האלמנט לא מיידי, Selenium ימתין:
element = driver.find_element(By.ID, "dynamic-content")

driver.quit()</code>

<b>2. Explicit Wait (מומלץ!):</b>
<code>from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://example.com")

try:
    # המתן עד שהאלמנט מופיע:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myElement"))
    )
    element.click()
    
    # המתן עד שהאלמנט ניתן ללחיצה:
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "submit"))
    )
    button.click()
    
except Exception as e:
    print(f"שגיאה: {e}")

driver.quit()</code>

📸 <b>צילום מסך:</b>
<code>from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://example.com")

# צילום מסך:
driver.save_screenshot("screenshot.png")

# או של אלמנט ספציפי:
element = driver.find_element(By.ID, "content")
element.screenshot("element.png")

driver.quit()</code>

🔄 <b>גלילה:</b>
<code>from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://example.com")

# גלילה למטה:
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# גלילה לאלמנט:
element = driver.find_element(By.ID, "footer")
driver.execute_script("arguments[0].scrollIntoView();", element)

# גלילה אינסופית (כמו Instagram):
import time
SCROLL_PAUSE_TIME = 2

# גובה דף נוכחי:
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # גלילה למטה:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    # המתן לטעינה:
    time.sleep(SCROLL_PAUSE_TIME)
    
    # גובה חדש:
    new_height = driver.execute_script("return document.body.scrollHeight")
    
    # אם לא השתנה - סיימנו:
    if new_height == last_height:
        break
    
    last_height = new_height

driver.quit()</code>

🎭 <b>Headless Mode - רקע בלי חלון:</b>
<code>from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# הגדרות:
options = Options()
options.add_argument('--headless')  # ללא חלון
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)
driver.get("https://example.com")

print(driver.title)
driver.quit()</code>

🍪 <b>עבודה עם Cookies:</b>
<code>from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://example.com")

# הוספת cookie:
driver.add_cookie({
    'name': 'user_token',
    'value': 'abc123'
})

# קבלת כל ה-cookies:
cookies = driver.get_cookies()
print(cookies)

# קבלת cookie ספציפי:
token = driver.get_cookie('user_token')

# מחיקת cookie:
driver.delete_cookie('user_token')

# מחיקת הכל:
driver.delete_all_cookies()

driver.quit()</code>

🔄 <b>טאבים וחלונות:</b>
<code>from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://example.com")

# פתיחת טאב חדש:
driver.execute_script("window.open('');")

# מעבר בין טאבים:
tabs = driver.window_handles

driver.switch_to.window(tabs[0])  # טאב ראשון
print(driver.title)

driver.switch_to.window(tabs[1])  # טאב שני
driver.get("https://google.com")

# סגירת טאב:
driver.close()

# חזרה לטאב ראשון:
driver.switch_to.window(tabs[0])

driver.quit()</code>

💪 <b>דוגמה מקיפה - חיפוש ב-Google:</b>
<code>from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def google_search(query):
    """חיפוש ב-Google וחילוץ תוצאות"""
    
    driver = webdriver.Chrome()
    
    try:
        # גלישה ל-Google:
        driver.get("https://www.google.com")
        
        # קבלת שדה החיפוש:
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        
        # חיפוש:
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)
        
        # המתן לתוצאות:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "search"))
        )
        
        # חילוץ תוצאות:
        results = driver.find_elements(By.CSS_SELECTOR, "div.g")
        
        print(f"🔍 תוצאות חיפוש עבור: {query}\n")
        
        for i, result in enumerate(results[:5], 1):
            try:
                title_elem = result.find_element(By.TAG_NAME, "h3")
                link_elem = result.find_element(By.TAG_NAME, "a")
                
                title = title_elem.text
                link = link_elem.get_attribute("href")
                
                if title and link:
                    print(f"{i}. {title}")
                    print(f"   {link}\n")
            
            except:
                continue
        
    except Exception as e:
        print(f"שגיאה: {e}")
    
    finally:
        driver.quit()

# שימוש:
google_search("Python tutorials")</code>

🎯 <b>דוגמה - Scraping דינמי:</b>
<code>from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

def scrape_dynamic_content(url):
    """Scrape אתר עם תוכן דינמי"""
    
    driver = webdriver.Chrome()
    
    try:
        driver.get(url)
        
        # המתן שהתוכן ייטען:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "product"))
        )
        
        # גלילה למטה לטעינת תוכן נוסף:
        for _ in range(3):
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )
            time.sleep(2)
        
        # קבלת HTML:
        html = driver.page_source
        
        # שימוש ב-BeautifulSoup לפרסור:
        soup = BeautifulSoup(html, 'lxml')
        
        # חילוץ מוצרים:
        products = []
        for item in soup.select('.product'):
            name = item.select_one('.product-name')
            price = item.select_one('.product-price')
            
            if name and price:
                products.append({
                    'name': name.text.strip(),
                    'price': price.text.strip()
                })
        
        return products
        
    finally:
        driver.quit()

# שימוש:
products = scrape_dynamic_content("https://example-shop.com")

for product in products:
    print(f"{product['name']}: {product['price']}")</code>

⚙️ <b>הגדרות מתקדמות:</b>
<code>from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()

# Headless:
options.add_argument('--headless')

# גודל חלון:
options.add_argument('--window-size=1920,1080')

# User Agent:
options.add_argument('user-agent=Mozilla/5.0 ...')

# השבתת images (מהיר יותר):
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)

# השבתת התראות:
options.add_argument('--disable-notifications')

# מצב פרטיות:
options.add_argument('--incognito')

driver = webdriver.Chrome(options=options)
driver.get("https://example.com")

driver.quit()</code>

📚 <b>Selenium vs BeautifulSoup:</b>

<b>BeautifulSoup:</b>
✅ מהיר
✅ פשוט
✅ נמוך משאבים
❌ רק HTML סטטי

<b>Selenium:</b>
✅ JavaScript
✅ אינטראקציה
✅ דפדפן אמיתי
❌ איטי
❌ צורך במשאבים

💡 <b>מתי להשתמש במה?</b>
• אתר פשוט ללא JS? BeautifulSoup
• תוכן נטען ב-JS? Selenium
• צריך ללחוץ/למלא טפסים? Selenium
• מהירות חשובה? BeautifulSoup

🎯 <b>טיפים חשובים:</b>

1. **תמיד סגור את הדפדפן** - driver.quit()
2. **השתמש ב-Waits** - אל תסמוך על time.sleep()
3. **Headless לפרודקשן** - חוסך משאבים
4. **try-finally** - לוודא סגירה
5. **הקטן את גודל הדף** - תמונות, CSS לא נחוץ

💡 <b>בשיעור הבא:</b>
נלמד לשלוח התראות אוטומטיות (Telegram, Email) כשמשהו משתנה!
''',
        'exercise': {
            'question': """מה יקרה בקוד הזה?

driver = webdriver.Chrome()
driver.get("https://example.com")
element = driver.find_element(By.ID, "button")
element.click()
# driver.quit() חסר!

מה הבעיה?""",
            'options': [
                'שגיאת תחביר',
                'הדפדפן יישאר פתוח ולא ייסגר',
                'האלמנט לא יימצא',
                'הקוד יעבוד מצוין'
            ],
            'correct_answer': 'הדפדפן יישאר פתוח ולא ייסגר',
            'explanation': 'נכון! 🎯 driver.quit() חיוני לסגירת הדפדפן. בלעדיו, הדפדפן יישאר פתוח ברקע וצורך משאבים'
        }
    },
    
    38: {
        'title': '📬 מסלול A.3: שליחת התראות אוטומטיות',
        'content': r'''
עכשיו נלמד לשלוח התראות כשמשהו משתנה! 🔔

🎯 <b>מה נלמד?</b>
• שליחת הודעות Telegram
• שליחת Email
• התראות SMS
• אינטגרציה עם Scraping

📦 <b>התקנה:</b>
<code>pip install python-telegram-bot requests</code>

---

<b>📱 חלק 1: Telegram Bot</b>

🤖 <b>יצירת בוט:</b>
1. פתח את @BotFather בטלגרם
2. שלח `/newbot`
3. תן שם לבוט
4. קבל Token

<b>שליחת הודעה פשוטה:</b>
<code>import requests

def send_telegram_message(message, bot_token, chat_id):
    """שליחת הודעה לטלגרם"""
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    
    data = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML"
    }
    
    response = requests.post(url, data=data)
    return response.json()

# שימוש:
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
CHAT_ID = "YOUR_CHAT_ID_HERE"

send_telegram_message(
    "🔔 התראה: המחיר ירד!",
    BOT_TOKEN,
    CHAT_ID
)</code>

💡 <b>איך למצוא Chat ID?</b>
<code>import requests

def get_chat_id(bot_token):
    """קבלת Chat ID"""
    url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
    response = requests.get(url)
    data = response.json()
    
    if data['result']:
        chat_id = data['result'][0]['message']['chat']['id']
        return chat_id
    
    return None

# שימוש:
# 1. שלח הודעה לבוט
# 2. הרץ את הפונקציה
chat_id = get_chat_id("YOUR_BOT_TOKEN")
print(f"Your Chat ID: {chat_id}")</code>

📸 <b>שליחת תמונה:</b>
<code>import requests

def send_telegram_photo(photo_path, caption, bot_token, chat_id):
    """שליחת תמונה לטלגרם"""
    url = f"https://api.telegram.org/bot{bot_token}/sendPhoto"
    
    with open(photo_path, 'rb') as photo:
        files = {'photo': photo}
        data = {
            'chat_id': chat_id,
            'caption': caption
        }
        
        response = requests.post(url, files=files, data=data)
    
    return response.json()

# שימוש:
send_telegram_photo(
    "screenshot.png",
    "📸 צילום מסך של המוצר",
    BOT_TOKEN,
    CHAT_ID
)</code>

📄 <b>שליחת קובץ:</b>
<code>def send_telegram_document(file_path, bot_token, chat_id):
    """שליחת קובץ לטלגרם"""
    url = f"https://api.telegram.org/bot{bot_token}/sendDocument"
    
    with open(file_path, 'rb') as file:
        files = {'document': file}
        data = {'chat_id': chat_id}
        
        response = requests.post(url, files=files, data=data)
    
    return response.json()

# שימוש:
send_telegram_document(
    "prices.csv",
    BOT_TOKEN,
    CHAT_ID
)</code>

---

<b>📧 חלק 2: Email</b>

📬 <b>שליחת Email פשוט:</b>
<code>import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email, from_email, password):
    """שליחת Email"""
    
    # יצירת הודעה:
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    
    # הוספת תוכן:
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        # התחברות ל-Gmail:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        
        # שליחה:
        server.send_message(msg)
        server.quit()
        
        print("✅ Email נשלח!")
        return True
        
    except Exception as e:
        print(f"❌ שגיאה: {e}")
        return False

# שימוש:
send_email(
    subject="התראת מחיר",
    body="המחיר של המוצר ירד ל-99₪!",
    to_email="recipient@example.com",
    from_email="your@gmail.com",
    password="your_app_password"
)</code>

📎 <b>Email עם קובץ מצורף:</b>
<code>from email.mime.base import MIMEBase
from email import encoders
import smtplib

def send_email_with_attachment(subject, body, to_email, 
                                from_email, password, filename):
    """Email עם קובץ מצורף"""
    
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    
    # תוכן:
    msg.attach(MIMEText(body, 'plain'))
    
    # קובץ מצורף:
    with open(filename, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
    
    encoders.encode_base64(part)
    part.add_header(
        'Content-Disposition',
        f'attachment; filename= {filename}'
    )
    
    msg.attach(part)
    
    # שליחה:
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        server.send_message(msg)
        server.quit()
        
        print("✅ Email עם קובץ נשלח!")
        
    except Exception as e:
        print(f"❌ שגיאה: {e}")

# שימוש:
send_email_with_attachment(
    subject="דו\"ח מחירים",
    body="מצורף הדו\"ח",
    to_email="recipient@example.com",
    from_email="your@gmail.com",
    password="your_app_password",
    filename="report.pdf"
)</code>

---

<b>🔔 חלק 3: אינטגרציה עם Scraping</b>

💪 <b>Price Tracker - מעקב מחירים:</b>
<code>import requests
from bs4 import BeautifulSoup
import time

class PriceTracker:
    def __init__(self, url, target_price, bot_token, chat_id):
        self.url = url
        self.target_price = target_price
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.last_price = None
    
    def get_price(self):
        """חילוץ מחיר מהאתר"""
        try:
            response = requests.get(self.url)
            soup = BeautifulSoup(response.text, 'lxml')
            
            # חיפוש מחיר (תלוי באתר):
            price_elem = soup.select_one('.price')
            
            if price_elem:
                # ניקוי המחיר:
                price_text = price_elem.text.strip()
                price = float(price_text.replace('₪', '').replace(',', ''))
                return price
            
            return None
            
        except Exception as e:
            print(f"שגיאה בחילוץ: {e}")
            return None
    
    def send_alert(self, message):
        """שליחת התראה"""
        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
        data = {
            "chat_id": self.chat_id,
            "text": message,
            "parse_mode": "HTML"
        }
        requests.post(url, data=data)
    
    def check_price(self):
        """בדיקת מחיר ושליחת התראה"""
        current_price = self.get_price()
        
        if current_price is None:
            return
        
        # התראה על ירידת מחיר:
        if current_price <= self.target_price:
            message = f"""
🎉 <b>המחיר ירד!</b>

💰 מחיר נוכחי: {current_price}₪
🎯 מחיר יעד: {self.target_price}₪

🔗 <a href="{self.url}">לחץ כאן לקנייה</a>
"""
            self.send_alert(message)
            print(f"✅ התראה נשלחה! מחיר: {current_price}₪")
        
        # התראה על שינוי מחיר:
        elif self.last_price and current_price != self.last_price:
            change = current_price - self.last_price
            emoji = "📈" if change > 0 else "📉"
            
            message = f"""
{emoji} <b>המחיר השתנה!</b>

💰 מחיר קודם: {self.last_price}₪
💰 מחיר נוכחי: {current_price}₪
📊 שינוי: {change:+.2f}₪
"""
            self.send_alert(message)
        
        self.last_price = current_price
    
    def start_monitoring(self, interval=3600):
        """התחל מעקב (בדיקה כל שעה)"""
        print(f"🔍 מתחיל מעקב אחרי: {self.url}")
        
        while True:
            self.check_price()
            print(f"⏰ ממתין {interval} שניות...")
            time.sleep(interval)

# שימוש:
tracker = PriceTracker(
    url="https://example-shop.com/product",
    target_price=99,
    bot_token="YOUR_BOT_TOKEN",
    chat_id="YOUR_CHAT_ID"
)

# בדיקה חד-פעמית:
tracker.check_price()

# או מעקב מתמיד:
# tracker.start_monitoring(interval=3600)  # כל שעה</code>

📊 <b>Stock Tracker - מעקב מניות:</b>
<code>import requests
import time

class StockTracker:
    def __init__(self, symbol, bot_token, chat_id):
        self.symbol = symbol
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.last_price = None
    
    def get_stock_price(self):
        """קבלת מחיר מניה (דוגמה - צריך API אמיתי)"""
        try:
            # API לדוגמה (יש להחליף באמיתי):
            url = f"https://api.example.com/stock/{self.symbol}"
            response = requests.get(url)
            data = response.json()
            
            return data['price']
            
        except Exception as e:
            print(f"שגיאה: {e}")
            return None
    
    def send_alert(self, message):
        """שליחת התראה"""
        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
        data = {
            "chat_id": self.chat_id,
            "text": message,
            "parse_mode": "HTML"
        }
        requests.post(url, data=data)
    
    def check_stock(self):
        """בדיקת מניה"""
        current_price = self.get_stock_price()
        
        if current_price and self.last_price:
            change_percent = ((current_price - self.last_price) / self.last_price) * 100
            
            # התראה על שינוי משמעותי (מעל 5%):
            if abs(change_percent) >= 5:
                emoji = "🚀" if change_percent > 0 else "📉"
                
                message = f"""
{emoji} <b>שינוי משמעותי ב-{self.symbol}!</b>

💰 מחיר קודם: ${self.last_price:.2f}
💰 מחיר נוכחי: ${current_price:.2f}
📊 שינוי: {change_percent:+.2f}%
"""
                self.send_alert(message)
        
        self.last_price = current_price

# שימוש:
tracker = StockTracker(
    symbol="AAPL",
    bot_token="YOUR_BOT_TOKEN",
    chat_id="YOUR_CHAT_ID"
)

tracker.check_stock()</code>

🎯 <b>Web Monitor - ניטור שינויים באתר:</b>
<code>import requests
from bs4 import BeautifulSoup
import hashlib

class WebMonitor:
    def __init__(self, url, bot_token, chat_id):
        self.url = url
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.last_hash = None
    
    def get_content_hash(self):
        """קבלת hash של תוכן הדף"""
        try:
            response = requests.get(self.url)
            soup = BeautifulSoup(response.text, 'lxml')
            
            # חילוץ התוכן הרלוונטי:
            content = soup.select_one('.main-content')
            
            if content:
                text = content.get_text(strip=True)
                # יצירת hash:
                return hashlib.md5(text.encode()).hexdigest()
            
            return None
            
        except Exception as e:
            print(f"שגיאה: {e}")
            return None
    
    def send_alert(self):
        """שליחת התראה על שינוי"""
        message = f"""
🔔 <b>הדף השתנה!</b>

האתר {self.url} עודכן עם תוכן חדש!

<a href="{self.url}">צפה בשינויים</a>
"""
        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
        data = {
            "chat_id": self.chat_id,
            "text": message,
            "parse_mode": "HTML"
        }
        requests.post(url, data=data)
    
    def check_changes(self):
        """בדיקת שינויים"""
        current_hash = self.get_content_hash()
        
        if current_hash:
            if self.last_hash and current_hash != self.last_hash:
                self.send_alert()
                print("✅ הדף השתנה! התראה נשלחה")
            else:
                print("ℹ️ אין שינויים")
            
            self.last_hash = current_hash

# שימוש:
monitor = WebMonitor(
    url="https://example.com/announcements",
    bot_token="YOUR_BOT_TOKEN",
    chat_id="YOUR_CHAT_ID"
)

monitor.check_changes()</code>

⏰ <b>הרצה מתוזמנת עם schedule:</b>
<code>import schedule
import time

# התקנה: pip install schedule

def job():
    """המשימה שתרוץ"""
    tracker.check_price()
    print("✅ בדיקה הושלמה")

# תזמון:
schedule.every(1).hours.do(job)      # כל שעה
schedule.every().day.at("09:00").do(job)  # כל יום ב-9:00
schedule.every().monday.at("10:00").do(job)  # כל שני ב-10:00

print("⏰ Scheduler מופעל!")

while True:
    schedule.run_pending()
    time.sleep(60)  # בדוק כל דקה</code>

📚 <b>טיפים חשובים:</b>

✅ **כן:**
• שמור credentials ב-.env
• טפל בשגיאות
• הוסף logging
• בדוק limits של API
• המתן בין בקשות

❌ **לא:**
• אל תשמור טוקנים בקוד
• אל תשלח spam
• אל תעמיס על השרת
• אל תבדוק כל שנייה

💡 <b>בשיעור הבא:</b>
נבנה פרויקט מלא - Price Tracker עם UI ו-Database!
''',
        'exercise': {
            'question': """מה הסיבה הנפוצה ביותר לכשל בשליחת Telegram message?

send_telegram_message("שלום", bot_token, chat_id)""",
            'options': [
                'Bot Token שגוי',
                'Chat ID שגוי',
                'אין חיבור לאינטרנט',
                'כל התשובות נכונות'
            ],
            'correct_answer': 'כל התשובות נכונות',
            'explanation': 'נכון! 🎯 כל 3 הסיבות יכולות לגרום לכשל. חשוב לבדוק: Token תקין, Chat ID נכון, וחיבור אינטרנט פעיל'
        }
    },
    
    39: {
        'title': '🎯 מסלול A.4: פרויקט - Price Tracker מלא',
        'content': r'''
בואו נבנה Price Tracker מקצועי! 💰

🎯 <b>מה נבנה?</b>
• מעקב אחרי מחירי מוצרים
• שמירה במסד נתונים
• היסטוריית מחירים
• גרפים
• התראות אוטומטיות

📦 <b>התקנה:</b>
<code>pip install requests beautifulsoup4 lxml
pip install matplotlib
pip install schedule</code>

---

<b>📁 מבנה הפרויקט:</b>
<code>price_tracker/
├── tracker.py          # הלוגיקה הראשית
├── database.py         # ניהול DB
├── scraper.py          # Scraping
├── notifier.py         # התראות
├── visualizer.py       # גרפים
├── config.py           # הגדרות
└── main.py            # נקודת כניסה</code>

---

<b>📄 config.py - הגדרות:</b>
<code>import os
from dotenv import load_dotenv

load_dotenv()

# Telegram:
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

# Database:
DB_NAME = 'prices.db'

# Scraping:
CHECK_INTERVAL = 3600  # שעה
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'

# Price alerts:
PRICE_DROP_THRESHOLD = 0.05  # 5% ירידה</code>

---

<b>🗄️ database.py - מסד נתונים:</b>
<code>import sqlite3
from datetime import datetime

class PriceDatabase:
    def __init__(self, db_name='prices.db'):
        self.db_name = db_name
        self.init_db()
    
    def init_db(self):
        """יצירת טבלאות"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            
            # טבלת מוצרים:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    url TEXT UNIQUE NOT NULL,
                    target_price REAL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # טבלת מחירים:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS prices (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_id INTEGER,
                    price REAL NOT NULL,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (product_id) REFERENCES products (id)
                )
            """)
            
            conn.commit()
    
    def add_product(self, name, url, target_price=None):
        """הוספת מוצר"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            
            try:
                cursor.execute("""
                    INSERT INTO products (name, url, target_price)
                    VALUES (?, ?, ?)
                """, (name, url, target_price))
                
                conn.commit()
                return cursor.lastrowid
            
            except sqlite3.IntegrityError:
                print("המוצר כבר קיים")
                return None
    
    def add_price(self, product_id, price):
        """הוספת מחיר"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            
            cursor.execute("""
                INSERT INTO prices (product_id, price)
                VALUES (?, ?)
            """, (product_id, price))
            
            conn.commit()
    
    def get_product_by_url(self, url):
        """קבלת מוצר לפי URL"""
        with sqlite3.connect(self.db_name) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT * FROM products WHERE url = ?
            """, (url,))
            
            row = cursor.fetchone()
            return dict(row) if row else None
    
    def get_all_products(self):
        """קבלת כל המוצרים"""
        with sqlite3.connect(self.db_name) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            cursor.execute('SELECT * FROM products')
            
            return [dict(row) for row in cursor.fetchall()]
    
    def get_price_history(self, product_id, limit=30):
        """היסטוריית מחירים"""
        with sqlite3.connect(self.db_name) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT * FROM prices
                WHERE product_id = ?
                ORDER BY timestamp DESC
                LIMIT ?
            """, (product_id, limit))
            
            return [dict(row) for row in cursor.fetchall()]
    
    def get_latest_price(self, product_id):
        """מחיר אחרון"""
        history = self.get_price_history(product_id, limit=1)
        return history[0] if history else None</code>

---

<b>🕷️ scraper.py - Scraping:</b>
<code>import requests
from bs4 import BeautifulSoup
from config import USER_AGENT

class ProductScraper:
    def __init__(self):
        self.headers = {'User-Agent': USER_AGENT}
    
    def scrape_price(self, url):
        """חילוץ מחיר מ-URL"""
        try:
            response = requests.get(
                url,
                headers=self.headers,
                timeout=10
            )
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'lxml')
            
            # נסה סלקטורים שונים:
            selectors = [
                '.price',
                '.product-price',
                '[class*="price"]',
                '#price',
            ]
            
            for selector in selectors:
                price_elem = soup.select_one(selector)
                if price_elem:
                    return self.parse_price(price_elem.text)
            
            print("לא נמצא מחיר")
            return None
            
        except Exception as e:
            print(f"שגיאה ב-scraping: {e}")
            return None
    
    def parse_price(self, price_text):
        """ניקוי והמרת מחיר"""
        import re
        
        # הסרת כל מה שלא ספרות או נקודה:
        clean = re.sub(r'[^\d.]', '', price_text)
        
        try:
            return float(clean)
        except ValueError:
            return None</code>

---

<b>📬 notifier.py - התראות:</b>
<code>import requests
from config import BOT_TOKEN, CHAT_ID

class Notifier:
    def __init__(self, bot_token=BOT_TOKEN, chat_id=CHAT_ID):
        self.bot_token = bot_token
        self.chat_id = chat_id
    
    def send_message(self, message):
        """שליחת הודעה"""
        if not self.bot_token or not self.chat_id:
            print("⚠️ Telegram לא מוגדר")
            return False
        
        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
        
        data = {
            'chat_id': self.chat_id,
            'text': message,
            'parse_mode': 'HTML'
        }
        
        try:
            response = requests.post(url, data=data)
            return response.status_code == 200
        except Exception as e:
            print(f"שגיאה בשליחה: {e}")
            return False
    
    def send_price_alert(self, product_name, old_price, new_price, url):
        """התראת שינוי מחיר"""
        change = new_price - old_price
        percent = (change / old_price) * 100
        
        emoji = "📉" if change < 0 else "📈"
        
        message = f"""
{emoji} <b>שינוי מחיר!</b>

🏷️ <b>{product_name}</b>

💰 מחיר קודם: {old_price:.2f}₪
💰 מחיר נוכחי: {new_price:.2f}₪
📊 שינוי: {change:+.2f}₪ ({percent:+.2f}%)

🔗 <a href="{url}">לחץ לצפייה</a>
"""
        
        return self.send_message(message)
    
    def send_target_reached(self, product_name, price, target_price, url):
        """התראה על הגעה למחיר יעד"""
        message = f"""
🎉 <b>הגעת למחיר יעד!</b>

🏷️ <b>{product_name}</b>

💰 מחיר נוכחי: {price:.2f}₪
🎯 מחיר יעד: {target_price:.2f}₪

🔗 <a href="{url}">קנה עכשיו!</a>
"""
        
        return self.send_message(message)</code>

---

<b>📊 visualizer.py - גרפים:</b>
<code>import matplotlib.pyplot as plt
from datetime import datetime

class PriceVisualizer:
    def create_price_chart(self, history, product_name):
        """יצירת גרף מחירים"""
        if not history:
            print("אין נתונים")
            return None
        
        # חילוץ נתונים:
        timestamps = [datetime.fromisoformat(h['timestamp']) 
                      for h in reversed(history)]
        prices = [h['price'] for h in reversed(history)]
        
        # יצירת גרף:
        plt.figure(figsize=(12, 6))
        plt.plot(timestamps, prices, marker='o', linewidth=2)
        
        plt.title(f'היסטוריית מחירים - {product_name}', 
                  fontsize=16, pad=20)
        plt.xlabel('תאריך', fontsize=12)
        plt.ylabel('מחיר (₪)', fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        # שמירה:
        filename = f'price_chart_{product_name}.png'
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.close()
        
        return filename</code>

---

<b>🎯 tracker.py - הלוגיקה הראשית:</b>
<code>from database import PriceDatabase
from scraper import ProductScraper
from notifier import Notifier
from config import PRICE_DROP_THRESHOLD

class PriceTracker:
    def __init__(self):
        self.db = PriceDatabase()
        self.scraper = ProductScraper()
        self.notifier = Notifier()
    
    def add_product(self, name, url, target_price=None):
        """הוספת מוצר למעקב"""
        product_id = self.db.add_product(name, url, target_price)
        
        if product_id:
            print(f"✅ {name} נוסף למעקב!")
            
            # בדיקה ראשונית:
            self.check_product(url)
        
        return product_id
    
    def check_product(self, url):
        """בדיקת מחיר של מוצר"""
        product = self.db.get_product_by_url(url)
        
        if not product:
            print("מוצר לא נמצא")
            return
        
        # Scrape מחיר:
        current_price = self.scraper.scrape_price(url)
        
        if current_price is None:
            print("לא הצלחתי לחלץ מחיר")
            return
        
        print(f"💰 {product['name']}: {current_price}₪")
        
        # שמירה ב-DB:
        self.db.add_price(product['id'], current_price)
        
        # בדיקת התראות:
        self.check_alerts(product, current_price)
    
    def check_alerts(self, product, current_price):
        """בדיקת התנאים להתראות"""
        last_price_record = self.db.get_latest_price(product['id'])
        
        # אם יש מחיר קודם:
        if last_price_record:
            old_price = last_price_record['price']
            
            # חישוב שינוי:
            change = current_price - old_price
            percent_change = abs(change / old_price)
            
            # התראה על שינוי משמעותי:
            if percent_change >= PRICE_DROP_THRESHOLD:
                self.notifier.send_price_alert(
                    product['name'],
                    old_price,
                    current_price,
                    product['url']
                )
        
        # התראה על הגעה למחיר יעד:
        if product['target_price']:
            if current_price <= product['target_price']:
                self.notifier.send_target_reached(
                    product['name'],
                    current_price,
                    product['target_price'],
                    product['url']
                )
    
    def check_all_products(self):
        """בדיקת כל המוצרים"""
        products = self.db.get_all_products()
        
        print(f"\n🔍 בודק {len(products)} מוצרים...\n")
        
        for product in products:
            self.check_product(product['url'])
            
            # המתן בין בדיקות:
            import time
            time.sleep(2)
        
        print("\n✅ סיימתי לבדוק את כל המוצרים!")
    
    def get_price_history(self, product_name):
        """קבלת היסטוריה"""
        products = self.db.get_all_products()
        
        product = next((p for p in products 
                       if p['name'] == product_name), None)
        
        if not product:
            print("מוצר לא נמצא")
            return []
        
        return self.db.get_price_history(product['id'])</code>

---

<b>▶️ main.py - הרצה:</b>
<code>from tracker import PriceTracker
from visualizer import PriceVisualizer
import schedule
import time

def main():
    tracker = PriceTracker()
    visualizer = PriceVisualizer()
    
    # הוספת מוצר:
    tracker.add_product(
        name="iPhone 15",
        url="https://example-shop.com/iphone-15",
        target_price=3000
    )
    
    tracker.add_product(
        name="MacBook Pro",
        url="https://example-shop.com/macbook",
        target_price=8000
    )
    
    # בדיקה ידנית:
    # tracker.check_all_products()
    
    # תזמון אוטומטי:
    schedule.every(1).hours.do(tracker.check_all_products)
    
    print("⏰ Tracker פועל! בודק כל שעה...")
    
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()</code>

---

<b>📊 שימוש בגרפים:</b>
<code>from tracker import PriceTracker
from visualizer import PriceVisualizer

tracker = PriceTracker()
visualizer = PriceVisualizer()

# קבלת היסטוריה:
history = tracker.get_price_history("iPhone 15")

# יצירת גרף:
chart_file = visualizer.create_price_chart(history, "iPhone 15")

print(f"✅ גרף נוצר: {chart_file}")</code>

---

💡 <b>שיפורים אפשריים:</b>

1. **Web Interface** - Flask/FastAPI
2. **רב-משתמשים** - כל אחד מעקב משלו
3. **מקורות מרובים** - השוואת מחירים
4. **מסנן זול ביותר** - ממיין לפי מחיר
5. **Export ל-Excel** - דוחות
6. **API** - גישה חיצונית
7. **Docker** - deployment קל

🎯 <b>זהו! פרויקט מלא ומקצועי!</b>
''',
        'exercise': {
            'question': """למה חשוב לשמור היסטוריית מחירים במסד נתונים?""",
            'options': [
                'כדי לדעת מתי לקנות',
                'כדי ליצור גרפים',
                'כדי לזהות מגמות',
                'כל התשובות נכונות'
            ],
            'correct_answer': 'כל התשובות נכונות',
            'explanation': 'נכון! 🎯 היסטוריה מאפשרת החלטות חכמות, ויזואליזציה, וזיהוי דפוסים של ירידות/עליות מחירים'
        }
    },
    
    40: {
        'title': '🎓 מסלול A.5: סיכום ואתגרים',
        'content': r'''
סיימנו את מסלול Web Scraping! 🎉

🎯 <b>מה למדנו?</b>

<b>1. BeautifulSoup</b> 🌐
✅ find() ו-find_all()
✅ CSS Selectors
✅ חילוץ טקסט ואטריביוטים
✅ ניקוי נתונים

<b>2. Selenium</b> 🤖
✅ דפדפן אוטומטי
✅ אינטראקציה עם אלמנטים
✅ JavaScript support
✅ Waits חכמים
✅ Screenshots

<b>3. התראות</b> 📬
✅ Telegram Bot
✅ Email
✅ אינטגרציה עם scraping

<b>4. פרויקט מלא</b> 💰
✅ Price Tracker
✅ Database
✅ גרפים
✅ תזמון

---

<b>🏆 אתגרים לתרגול:</b>

<b>אתגר #1: News Aggregator</b>
צור בוט שאוסף חדשות מכמה אתרים ושולח סיכום יומי.

<b>דרישות:</b>
• גילוי מ-3+ אתרי חדשות
• שמירה במסד נתונים
• הסרת כפילויות
• שליחת התראה יומית
• גרף של נושאים פופולריים

<b>טיפ:</b>
<code>from collections import Counter

# ספירת מילות מפתח:
keywords = ['Python', 'AI', 'Bitcoin', 'Python', 'AI']
counter = Counter(keywords)
print(counter.most_common(3))
# [('Python', 2), ('AI', 2), ('Bitcoin', 1)]</code>

---

<b>אתגר #2: Real Estate Monitor</b>
מעקב אחרי דירות חדשות באתר נדל"ן.

<b>דרישות:</b>
• גילוי דירות חדשות
• פילטרים (מחיר, גודל, עיר)
• התראה על דירות מתאימות
• שמירת מועדפים
• חישוב ממוצע מחירים

<b>טיפ:</b>
<code>def matches_criteria(apartment, criteria):
    """בדיקה אם דירה מתאימה"""
    if apartment['price'] > criteria['max_price']:
        return False
    
    if apartment['rooms'] < criteria['min_rooms']:
        return False
    
    if apartment['city'] != criteria['city']:
        return False
    
    return True</code>

---

<b>אתגר #3: Job Listings Tracker</b>
מעקב אחרי משרות חדשות.

<b>דרישות:</b>
• גילוי משרות מ-LinkedIn/Indeed
• פילטרים לפי מילות מפתח
• התראה על משרות רלוונטיות
• שמירת משרות מעניינות
• סטטיסטיקות (שכר ממוצע, מיקום)

---

<b>אתגר #4: Social Media Monitor</b>
מעקב אחרי פוסטים על נושא מסוים.

<b>דרישות:</b>
• חיפוש מילות מפתח
• ניתוח סנטימנט (חיובי/שלילי)
• גרף מגמות לאורך זמן
• התראה על פוסטים ויראליים

<b>טיפ - ניתוח סנטימנט פשוט:</b>
<code>def simple_sentiment(text):
    """ניתוח סנטימנט בסיסי"""
    positive_words = ['good', 'great', 'awesome', 'excellent']
    negative_words = ['bad', 'terrible', 'awful', 'poor']
    
    text_lower = text.lower()
    
    pos_count = sum(word in text_lower for word in positive_words)
    neg_count = sum(word in text_lower for word in negative_words)
    
    if pos_count > neg_count:
        return 'positive'
    elif neg_count > pos_count:
        return 'negative'
    else:
        return 'neutral'

# שימוש:
text = "This product is awesome and great!"
print(simple_sentiment(text))  # positive</code>

---

<b>אתגר #5: E-commerce Comparison</b>
השוואת מחירים בין אתרי קניות.

<b>דרישות:</b>
• חיפוש מוצר באתרים שונים
• השוואת מחירים
• התראה על המחיר הזול ביותר
• טבלת השוואה
• גרף מגמות מחירים

<b>טיפ:</b>
<code>def find_best_deal(products):
    """מציאת העסקה הטובה ביותר"""
    sorted_products = sorted(products, 
                            key=lambda p: p['price'])
    
    best = sorted_products[0]
    
    print(f"🎯 העסקה הטובה ביותר:")
    print(f"   {best['name']}")
    print(f"   {best['price']}₪")
    print(f"   {best['store']}")
    
    return best</code>

---

<b>📚 משאבים להמשך:</b>

<b>תיעוד:</b>
• BeautifulSoup: https://www.crummy.com/software/BeautifulSoup/
• Selenium: https://selenium-python.readthedocs.io/
• Requests: https://requests.readthedocs.io/

<b>כלים נוספים:</b>
• <b>Scrapy</b> - Framework מקצועי
• <b>Playwright</b> - חלופה ל-Selenium
• <b>Puppeteer</b> - דרך Python
• <b>APIs</b> - עדיף תמיד!

<b>למידה נוספת:</b>
• Real Python - Web Scraping Tutorials
• ScrapingBee Blog
• Reddit: r/webscraping

---

<b>⚠️ תזכורת חשובה:</b>

<b>חוקי Web Scraping:</b>
✅ בדוק robots.txt
✅ שלח headers תקינים
✅ המתן בין בקשות
✅ כבד את תנאי השימוש
✅ אל תעמיס על שרתים

<b>אתיקה:</b>
• אל תשתמש בנתונים לרעה
• כבד פרטיות
• אל תעקוף אבטחה
• בקש רשות אם לא בטוח

---

<b>🎉 מזל טוב!</b>

סיימת את מסלול Web Scraping!

עכשיו אתה יודע:
• לאסוף מידע מהאינטרנט
• לבנות מערכות מעקב
• לשלוח התראות
• לבנות פרויקטים מלאים

<b>המשך לתרגל!</b>
כל מומחה התחיל כמתחיל 💪

<b>מסלולים נוספים מחכים:</b>
• מסלול B: Data Basics (Pandas + Matplotlib)
• מסלול C: Build Your Own Bot

---

<b>🚀 Keep Coding!</b>
''',
        'exercise': {
            'question': """איזה כלי הכי מתאים לכל משימה?

1. אתר פשוט עם HTML סטטי
2. אתר עם JavaScript ולחיצות
3. צריך API?""",
            'options': [
                '1=BeautifulSoup, 2=Selenium, 3=Requests',
                '1=Selenium, 2=BeautifulSoup, 3=Requests',
                '1=Requests, 2=Selenium, 3=BeautifulSoup',
                '1=BeautifulSoup, 2=Requests, 3=Selenium'
            ],
            'correct_answer': '1=BeautifulSoup, 2=Selenium, 3=Requests',
            'explanation': 'מעולה! 🎯 BeautifulSoup לHTML פשוט, Selenium לJS ואינטראקציה, Requests לקריאת API. כל כלי למשימה הנכונה!'
        }
    },
}
