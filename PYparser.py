# Импортируем необходимые библиотеки
import requests
from bs4 import BeautifulSoup
import html5lib
import shutil 


#Часть кода , отвечающая за переход на следуюющую страницу
count = 1
while count <= 10 :                                  #Тут стоит указать конечную страницу для парса
	url = "http://baskino.me/new/page/" + str(count)        

	page = requests.get(url).text

	soup = BeautifulSoup(page , 'lxml')

	divs = soup.findAll('div' , {'class' : "shortpost"})



#Основное тело парсера

	def find_content():
		
		for div in divs:
			div_title = div.find('div' , {'class':"posttitle"})    # Находим в html коде необходимое
			link_text = div_title.find('a').text                   # Выбираем из <a> весь текст(тут у нас название фильма)
			div_date = div.find('div', {'class':"rinline"})        
			date_text = div_date.text                              # Тут у нас дата загрузки фильма на сайт
			div_release = div.find('div', {'class':"linline"})      
			release_text =  div_release.text                        # Тут дата выхода фыльма
			
			print ("Название фильма: " + link_text)                 # Выводим в консоль название фильма,
			print (date_text)                                       #дату появления на сайте
			print("Появился на сайте: " + release_text)             # и дату релиза фильма
			
			img = div.find('div' , {'class' : 'postcover'})             
			img_src = img.find('img').get('src')                    # Находим картинку(постер) фильма
			
            #Часть кода , отвечающая за загрузку постеров з названием фильма у формате .jpg в одну директорию с вашим кодом
			src = img_src
			response  = requests.get(src , stream = True)
			with open(link_text.replace('/' , '').replace('?' , '') + '.jpg' , 'wb') as out_file:
				shutil.copyfileobj(response.raw , out_file)
			del response	
		
			
	count +=1
	
	print (find_content())                                


