import requests
from bs4 import BeautifulSoup

def main():
    url = "https://news.ycombinator.com/item?id=45800465"
    blobData = requests.get(url)
    souped = BeautifulSoup(blobData.content, "html.parser")
    

    ls1 = []
    elements = souped.find_all(class_="ind", attrs={"indent" : "0"})
    for element in elements:
        sib_elem = element.find_next_sibling(class_="default")
        child_elem = sib_elem.find(class_="commtext")

        if not child_elem:
            continue
        ls1.append(child_elem.get_text(strip=True))

    keywords = {"python": 0, "javascript": 0}

    

    for item in ls1:
        ls = item.lower().split(" ")
        for word in ls:
            if word in keywords:
                keywords[word] += 1
    
    print(keywords)
    


if __name__ == "__main__":
    main()
