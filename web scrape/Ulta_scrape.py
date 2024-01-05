from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd


def get_brand(branddriver):
    """
    Returns a list of strings with all the brand names of hair products. 'branddriver' is the ChromeDriver corresponding to https://www.ulta.com/shop/hair/treatment
    """
    card = branddriver.find_elements(By.XPATH,'//span[@class="ProductCard__brand"]')
    list=[]
    for i in card:
        value = i.find_element(By.XPATH,'.//span[@class="Text-ds Text-ds--body-3 Text-ds--left Text-ds--neutral-600"]').text
        list.append(value)
    return(list)
    
def get_name(namedriver):
    """
    Returns a list of strings with all the product names of hair products. 'namedriver' is the ChromeDriver corresponding to https://www.ulta.com/shop/hair/treatment
    """
    card = namedriver.find_elements(By.XPATH,'//span[@class="ProductCard__product"]')
    list=[]
    for i in card:
        value = i.find_element(By.XPATH,'.//span[@class="Text-ds Text-ds--body-3 Text-ds--left"]').text
        list.append(value)
    return(list)

def get_links(linkdriver):
    """
    Returns a list of strings with all the links of hair products. 'linkdriver' is the ChromeDriver corresponding to https://www.ulta.com/shop/hair/treatment
    """
    card = linkdriver.find_elements(By.XPATH,'//div[@class="ProductCard"]')
    list=[]
    for i in card:
        value=i.find_element(By.XPATH,'.//a[@class="Link_Huge Link_Huge--secondary"]')
        link=value.get_attribute('href')
        list.append(link)
    return(list)

def get_ingredients(ingredientsdriver):
    """
    Returns a string of the ingredients associated with the product that ChromeDriver 'ingredientsdriver' corresponds with. If no ingredients are found return "no ingredients"
    """
    try:
        ingredientsdriver.find_element(By.XPATH,'//*[@id="Ingredients"]')
        ingredientsdriver.find_element(By.XPATH, '//details[@aria-controls="Ingredients"]').click()
        expand = ingredientsdriver.find_element(By.XPATH, '//details[@aria-controls="Ingredients"]')
        find = expand.find_element(By.XPATH, './/p').text
        return find 
    except:
        return "no ingredients"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--log-level=1')

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.ulta.com/shop/hair/treatment')

#lets the page https://www.ulta.com/shop/hair/treatment load by sleeping for 10 seconds, then clicking on the "load more" button, if it exists. If there is no 
#"load more" button this means all the hair products have been loaded 
load_more = True
while load_more:
    time.sleep(10)
    try:
        driver.find_element(By.XPATH,'//button[@class="Button-ds LoadContent__button Button-ds--compact Button-ds--withHover Button-ds--secondary"]').click()

    except:
        load_more = False

#get the brands, product names, links for each product on the page
brands = get_brand(driver)
names = get_name(driver)
brand_and_name = []
for i in range(names):
    product = brands[i] + ' ' + names[i]
    brand_and_name.append(product)
links = get_links(driver)

#for each product, go to its corresponding link and get the ingredients for each product
ingredients= []
for link in links:
    driver.get(link)
    new = get_ingredients(driver)
    ingredients.append(new)

#compile all the data into a csv file
dict = {'Brand':brands, 'Product':names, 'Full Product Name':brand_and_name, 'Ingredients':ingredients, 'Link':links}
df = pd.DataFrame(dict)
df.to_csv('table_newest.csv')
