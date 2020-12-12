import requests
from bs4 import BeautifulSoup
import searched_page


def main():
    tag = input("Enter Your gene Id:\t")
    url = "https://reactome.org/content/query?q=" + tag

    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "lxml")

    div_content = soup.find("div", attrs={"id": "fav-lead1"})

    if "No results found" in str(div_content.find("h3")):
        print("Your gene Id is wrong try again...")
    else:
        searched_result = str(div_content.find(
            "div", attrs={"id": "search-results"}).a['href'])

        result = searched_page.searched_page(searched_result.replace(
            "./detail", "https://reactome.org/content/detail"))

        print("The Corrosponding entrez Id:\t", result)


main()
