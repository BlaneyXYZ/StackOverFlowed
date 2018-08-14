import csv

import requests
from bs4 import BeautifulSoup
from time import perf_counter as pc
from multiprocessing.dummy import Pool

total_page = 50
page = 1
questions = []


def fetch_questions(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')
    for q in soup.find_all('a', attrs={'class': 'question-hyperlink'}):
        questions.append(q.text.strip())


if __name__ == '__main__':
    t0 = pc()
    pages = []
    while page <= total_page:
        pages.append("https://stackoverflow.com/questions?page={}&sort=votes".format(page))
        page += 1

    fileName = "questions.txt"
    pool = Pool(10)
    pool.map(fetch_questions, pages)
    with open("questions.txt", 'w', encoding='utf8') as file_handler:
        for question in questions:
            file_handler.write("{}\n".format(question))
    print(pc() - t0)
