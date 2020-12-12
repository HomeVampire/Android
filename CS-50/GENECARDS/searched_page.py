import requests
from bs4 import BeautifulSoup


def searched_page(new_url):
    new_html_content = requests.get(new_url).text
    new_soup = BeautifulSoup(new_html_content, "lxml")
    new_div_content = new_soup.find("div", attrs={"id": "fav-lead1"})

    new_searched_result = new_div_content.find_all("div", attrs={
                                                   "class": "favth-col-lg-10 favth-col-md-10 favth-col-sm-9 favth-col-xs-12 details-field"})
    for i in new_searched_result:
        link = i.find('a', href=True)
        if link is None:
            continue
        else:
            if "https://www.genecards.org/cgi-bin/carddisp.pl?gene=" in str(link):
                final_url = link['href']
                print(final_url)
                import output
                return output.main(final_url)
