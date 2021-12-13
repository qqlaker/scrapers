from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
from scraper import scrap
from tqdm import tqdm
import threading


def driverinit():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    return driver


def main_page_scrap():
    driver = driverinit()
    driver.get('https://www.registredesactionscollectives.quebec/en/Consulter/RecherchePublique')
    while True:
        try:
            tbody = driver.find_element_by_tag_name('tbody')
            break
        except:
            time.sleep(1)
    driver.find_element_by_class_name('col-md-12.text-right').find_element_by_id('tout-afficher').click()
    links = [[], []]
    trs = tbody.find_elements_by_css_selector("tr[role = 'row']")
    print('links parsing')
    time.sleep(1)
    for tr in tqdm(trs, colour='white'):
        links[0].append(tr.find_element_by_tag_name('a').get_attribute('href'))
    driver.close()
    driver.quit()
    for i in range(len(links[0])):
        links[1].append(links[0][i].split('NoDossier=')[1])
    return links

if __name__ == '__main__':
    t = int(input("Please enter timeout (seconds): "))
    print('starting process')
    time.sleep(1)
    path = "pdf_files"
    if not os.path.isdir(path):
        os.mkdir(path)
    links = main_page_scrap()
    files = os.listdir(path)
    b = True

    print('process data')
    time.sleep(1)
    while b == True:
        for i in range(len(links[1])):
            if links[1][i] not in files:
                print(links[0][i])
                scrap(links[0][i])
        print(f'await {round(t/60, 2)} minutes')
        time.sleep(t)

