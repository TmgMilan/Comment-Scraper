import requests
from bs4 import BeautifulSoup

def main():
    url = "https://news.ycombinator.com/item?id=45800465"
    request = requests.get(url)
    souped = BeautifulSoup(request.content, "html.parser")

    elements = souped.find_all(class_="ind", attrs={"indent": 0})
    ls = []

    for element in elements:
        siblin = element.find_next_sibling(class_="default")
        child = siblin.find(class_="commtext")
        if not child:
            continue
        ls.append(child.get_text(strip=True))
    
    dks = {"python": 0, "javascript":0}
    for c in ls:
        clower = c.lower().split(" ")
        for item in clower:
            if item in dks:
                dks[item] += 1
    print(dks)

if __name__ == "__main__":
    main()
