import requests
from bs4 import BeautifulSoup
from time import perf_counter as pc
from multiprocessing import Pool

total_page = 50

def fetch_questions():
    current_page = 1
    while current_page <= total_page:
        url = "https://stackoverflow.com/questions?page={}&sort=votes".format(current_page)
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, 'lxml')
        print(url)
        current_page += 1
        for q in soup.find_all('a', attrs={'class': 'question-hyperlink'}):
            questions.append(q.text.strip())
    print(len(questions))
    with open("questions.txt", 'w', encoding='utf8') as file_handler:
        for question in questions:
            file_handler.write("{}\n".format(question))


if __name__ == '__main__':
    questions = []
    t0 = pc()
    fetch_questions()
    print(pc() - t0)
