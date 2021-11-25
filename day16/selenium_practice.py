

# 셀레늄: 웹 자동화 및 웹의 소스코드를 수집하는 모듈
from selenium import webdriver  # 셀레늄 모듈 로딩
import time as t 


# 크롬 브라우저 물리드라이버 가동
browser = webdriver.Chrome('D:/isec_spring1/py_study/chromedriver.exe')

# 원하는 사이트로 이동
browser.get('https://news.daum.net/society#1')


# 뉴스 1위  : //*[@id="mAside"]/div[1]/ul/li[1]/div/ol[1]/li[1]/strong/a
# 뉴스 2위  : //*[@id="mAside"]/div[1]/ul/li[1]/div/ol[1]/li[2]/strong/a

# 연예 1위  : //*[@id="mAside"]/div[1]/ul/li[2]/div/ol[1]/li[1]/strong/a
#             //*[@id="mAside"]/div[1]/ul/li[2]/div/ol/li[1]/strong/a
#             //*[@id="mAside"]/div[1]/ul/li[2]/div/ol/li[2]/strong/a

# 스포츠 1위: //*[@id="mAside"]/div[1]/ul/li[3]/div/ol[1]/li[1]/strong/a


for m in range(1,4):
    # 뉴스 탭 : //*[@id="mAside"]/div[1]/ul/li[1]/a
    # 연예 탭 : //*[@id="mAside"]/div[1]/ul/li[2]/a
    tab = browser.find_element_by_xpath(f'//*[@id="mAside"]/div[1]/ul/li[{m}]/a')
    tab.click()

    for n in range(1,11):
        if m == 1:

            rank1 = browser.find_element_by_xpath(f'//*[@id="mAside"]/div[1]/ul/li[{m}]/div/ol[1]/li[{n}]/strong/a')
        else: 
            rank1 = browser.find_element_by_xpath(f'//*[@id="mAside"]/div[1]/ul/li[{m}]/div/ol/li[{n}]/strong/a')
        rank1.click()
        t.sleep(1.5)

############################################반복문 3개 돌린 멍청이#################################

# for n in range(1, 11):

#     # 1위 뉴스기사를 클릭
#     rank1 = browser.find_element_by_xpath(f'//*[@id="mAside"]/div[1]/ul/li[1]/div/ol/li[{n}]/strong/a')
#     rank1.click()
#     t.sleep(1)
#     # 2위 뉴스기사 클릭
#     # rank2 = browser.find_elements_by_css_selector('#mAside > div.aside_g.aside_popular > ul > li.on > div > ol > li:nth-child(2) > strong > a')

# entertainments = browser.find_element_by_xpath('//*[@id="mAside"]/div[1]/ul/li[2]/a')
# entertainments.click()

# for n in range(1, 11):
#     entertainments_rank = browser.find_element_by_xpath(f'//*[@id="mAside"]/div[1]/ul/li[2]/div/ol/li[{n}]/strong/a')
#     entertainments_rank.click()
#     t.sleep(1)

# sports = browser.find_element_by_xpath('//*[@id="mAside"]/div[1]/ul/li[3]/a')
# sports.click()

# for n in range(1,11):
#     sports_rank = browser.find_element_by_xpath(f'//*[@id="mAside"]/div[1]/ul/li[3]/div/ol/li[{n}]/strong/a')
#     sports_rank.click()
#     t.sleep(1)


    