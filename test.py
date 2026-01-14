import requests
from bs4 import BeautifulSoup

def main():
    url = "https://news.ycombinator.com/item?id=45800465"
    saved = requests.get(url)
    souped = BeautifulSoup(saved.content, "html.parser")


    ls = []
    elements = souped.find_all(class_="ind", attrs={"indent": "0"})
    
    for element in elements:
        sib_elem = element.find_next_sibling(class_="default")
        child_elem = sib_elem.find(class_="commtext")
        
        if not child_elem:
            continue
        ls.append(child_elem.get_text(strip=True))
   
    cuh = {"python": 0, "javascript": 0}

    for bruh in ls:
        bruhl = bruh.lower().split(" ")
        for word in bruhl:
            if word in cuh:
                cuh[word] += 1
    print(cuh)


if __name__ == "__main__":
    main()
