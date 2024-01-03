from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd


def get_brand(branddriver):
    card = branddriver.find_elements(By.XPATH,'//span[@class="ProductCard__brand"]')
    list=[]
    for i in card:
        value = i.find_element(By.XPATH,'.//span[@class="Text-ds Text-ds--body-3 Text-ds--left Text-ds--neutral-600"]').text
        list.append(value)
    return(list)
    
def get_name(namedriver):
    card = namedriver.find_elements(By.XPATH,'//span[@class="ProductCard__product"]')
    list=[]
    for i in card:
        value = i.find_element(By.XPATH,'.//span[@class="Text-ds Text-ds--body-3 Text-ds--left"]').text
        list.append(value)
    return(list)

def get_links(linkdriver):
    card = linkdriver.find_elements(By.XPATH,'//div[@class="ProductCard"]')
    list=[]
    for i in card:
        value=i.find_element(By.XPATH,'.//a[@class="Link_Huge Link_Huge--secondary"]')
        link=value.get_attribute('href')
        list.append(link)
    return(list)

def get_ingredients(ingredientsdriver):
    try:
        ingredientsdriver.find_element(By.XPATH,'//*[@id="Ingredients"]')
    except:
        return "no ingredients"
    ingredientsdriver.find_element(By.XPATH, '//details[@aria-controls="Ingredients"]').click()
    expand = ingredientsdriver.find_element(By.XPATH, '//details[@aria-controls="Ingredients"]')
    find = expand.find_element(By.XPATH, './/p').text
    return find 


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--log-level=1')


driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.ulta.com/shop/hair/treatment')

load_more = True
while load_more:
    time.sleep(10)
    try:
        driver.find_element(By.XPATH,'//button[@class="Button-ds LoadContent__button Button-ds--compact Button-ds--withHover Button-ds--secondary"]').click()

    except:
        load_more = False

brands = get_brand(driver)
names = get_name(driver)


brand_and_name = []
for i in range(names):
    product = brands[i] + ' ' + names[i]
    brand_and_name.append(product)

links = get_links(driver)

ingredients= []
try:
    for link in links:
        driver.get(link)
        new = get_ingredients(driver)
        ingredients.append(new)
except:
    dict = {'Brand':brands, 'Product':names, 'Ingredients':ingredients, 'Link':links}
    df = pd.DataFrame(dict)
    df.to_csv('table_newest.csv')

dict = {'Brand':brands, 'Product':names, 'Full Product Name':brand_and_name, 'Ingredients':ingredients, 'Link':links}
df = pd.DataFrame(dict)
df.to_csv('table_newest.csv')