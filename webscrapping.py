from bs4 import BeautifulSoup
import requests,openpyxl

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'Top 250 Most Reviewed Games'
sheet.append(['Game Rank','Game Name', 'Release Month','Release Year','Reviews on Steam','Rating on Steam'])

try:
    source = 'https://steam250.com/reviews'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',"Accept-Language": "en-US,en;q=0.5"} 
    result = requests.get(source, headers=headers)
    soup = BeautifulSoup(result.text, 'html.parser')
    movies1 = soup.find('div', class_='col1 main ranking')
    moviesList = movies1.find_all('div',id='1')
    for i in range(2,251):
        moviesList.extend(movies1.find_all('div',id=f'{i}'))
    for movie in moviesList:
        rankAndName = movie.find('span',class_='title').text.split(".")
        rank = rankAndName[0]
        name = rankAndName[1]
        releaseMonthAndYear = movie.find('span',class_='date').a.text.split(" ")
        releaseMonth = releaseMonthAndYear[1]
        releaseYear = releaseMonthAndYear[2]
        numOfReviews = movie.find('span',class_='owners').text
        rating = movie.find('span',class_='rating').text.split(" ")[-1]
        print(rank,name,releaseMonth,releaseYear,numOfReviews,rating)
        sheet.append([rank,name,releaseMonth,releaseYear,numOfReviews,rating])
    
except Exception as e:
    print(e)

excel.save('Top 250 Most Reviewed Games on Steam.xlsx')

