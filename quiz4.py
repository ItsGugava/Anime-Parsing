import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint

file = open("animes.csv", "w", newline="\n", encoding="utf-8")
file_obj = csv.writer(file)
file_obj.writerow(["Name", "Amount of episodes", "Duration", "Rating"])
for i in range(0, 251, 50):
    url = f"https://myanimelist.net/topanime.php?limit={i}"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    content = soup.find("div", class_="pb12")
    animes = content.find_all("tr", class_="ranking-list")
    for anime in animes:
        name = anime.h3.a.text
        information = anime.find("div", class_="information di-ib mt4")
        each_details = information.text.strip().split("\n")
        amount_of_episodes = each_details[0]
        duration = each_details[1].strip()
        rating = anime.find("div", class_="js-top-ranking-score-col di-ib al").text
        file_obj.writerow([name, amount_of_episodes, duration, rating])
    sleep(randint(5,15))
