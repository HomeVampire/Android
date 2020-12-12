import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# TODO: Change "webdriver/chromedriver.exe" with your Chrome driver path.
# driver.minimize_window()    # TODO: Minimize the Chrome Window
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options,
                          executable_path="webdriver/chromedriver.exe")


def main(final_url):
    driver.get(final_url)
    content = driver.page_source
    driver.close()

    final_soup = BeautifulSoup(content, "lxml")

    div_content = final_soup.find(
        "div", attrs={"class": "gc-subsection-inner-wrap"})

    links = div_content.find_all("a")

    # print("The Corrosponding entrez Id:\t", links[1].text)
    return links[1].text
