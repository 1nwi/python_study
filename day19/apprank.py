from selenium import webdriver
from bs4 import BeautifulSoup
import time as t

# 날짜처리 라이브러리
from datetime import datetime

# 엑셀저장 라이브러리
import xlsxwriter

# 이미지 다운로드 처리 라이브러리
import urllib.request as req
from io import BytesIO

# 오늘 날짜 시간
d = datetime.today()

# 파일명
file_name = f'어플일간순위_{d.year}_{d.month}_{d.day}.xlsx'

# 파일 저장 경로
file_save_path = f'D:/isec_spring1/py_study/{file_name}'

# 엑셀 라이브러리 객체 생성
workbook = xlsxwriter.Workbook(file_save_path)

# 엑셀 워크 시트 만들기
worksheet = workbook.add_worksheet()

styles = {
    'bold': True,
    'font_color': 'red',
    'bg_color': 'yellow'
}
cell_format = workbook.add_format(styles)


worksheet.write('A1', '순위', cell_format)
worksheet.write('B1', '썸네일', cell_format)
worksheet.write('C1', '앱명', cell_format)
worksheet.write('D1', '상승률', cell_format)
worksheet.write('E1', '업종대분류', cell_format)
worksheet.write('F1', '업종소분류', cell_format)



# 물리드라이버
browser = webdriver.Chrome('D:/isec_spring1/py_study/chromedriver.exe')

# 브라우저 최대창으로 띄우기
# browser.maximize_window()

# 브라우저 원하는 사이즈로 키우기
browser.set_window_size(1280, 1080)

# 타겟 사이트로 이동
browser.get('https://www.mobileindex.com/mi-chart/top-100/top-apps')

t.sleep(3)
# 현재 페이지 소스코드 불러오기
html = browser.page_source

soup = BeautifulSoup(html, 'html.parser')

############### 핵심로직 ###############

apprank = soup.select('tbody > tr')


for app in apprank:
    app_list = app.select('td')
    
    
    rank = int(app.select_one('.center').text.strip())
    title = app_list[1].text
    rising_rate = app_list[2].text
    main_category = app_list[3].text
    category = app_list[4].text

    img_tag = app.select_one('td.left > span.app-name > img')
    img_src = img_tag['src']

    print(rank)
    print(title)
    print(rising_rate)
    print(main_category)
    print(category)
    print('=' * 60)

    worksheet.write(f'A{rank + 1}', rank)

    img_data = BytesIO(req.urlopen(img_src).read())
    worksheet.insert_image(f'B{rank + 1}', img_src, {'image_data' : img_data})

    worksheet.write(f'C{rank + 1}', title)
    worksheet.write(f'D{rank + 1}', rising_rate)
    worksheet.write(f'E{rank + 1}', main_category)
    worksheet.write(f'F{rank + 1}', category)

browser.close()
workbook.close()

