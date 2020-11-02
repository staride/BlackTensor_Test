import requests
import pandas as pd
import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Twitter
from collections import Counter

# ============================================================
# ==================                     =====================
# ==================         KDD         =====================
# ==================                     =====================
# ============================================================
# class CrowKdd(object):
# def get_url():
# search_keyword = '애플'
# url = f'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={search_keyword}'

# r = requests.get(url)
# req = requests.get('https://search.naver.com/search.naver?where=news&sm=tab_jum&query=셀트리온')
# html = req.text
# soup = BeautifulSoup(html, 'html.parser')
# news_titles = soup.select('.news .type01 li dt a[title]')

# print('new: ', len(news_titles))
# print()
# for title in news_titles:
#     print(title['title'])

# def get_news(n_url):
#     news_detail = []
#     print(n_url)
#     breq = requests.get(n_url)
#     bsoup = BeautifulSoup(breq.content, 'html.parser')

#     title = bsoup.select('h3#articleTitle')[0].text
#     news_detail.append(title)

#     pdate = bsoup.select('.t11')[0].get_text()[:11]
#     news_detail.append(pdate)

#     _text = bsoup.select('#articleBodyContents')[0].get_text().replace('\n', " ")
#     btext = _text.replace("// flash 오류를 우회하기 위한 함수 추가 function _flash_removeCallback() {}", "")

#     news_detail.append(btext.strip())

#     pcompany = bsoup.select('#footer address')[0].a.get_text()
#     news_detail.append(pcompany)

#     return news_detail

#     print(news_detail)

# query = "삼성전자"
# s_date = "2020.04.01"
# e_date = "2018.10.30"
# s_from = s_date.replace(".","")
# e_to = e_date.replace(".","")
# page = 1

# f = open("C:/Users/Admin/VscProject/BlackTensor_Test/" + query + '.csv', 'w', encoding='utf-8')

# while page < 100:

#     print(page)

#     url = "https://search.naver.com/search.naver?where=news&query=" + query + "&sort=1&ds=" + s_date + "&de=" + e_date + "&nso=so%3Ar%2Cp%3Afrom" + s_from + "to" + e_to + "%2Ca%3A&start=" + str(page)

#     header = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
#     }
#     req = requests.get(url,headers=header)
#     print(url)
#     cont = req.content
#     soup = BeautifulSoup(cont, 'html.parser')
    
#     for urls in soup.select("._sp_each_url"):
#         try :
#             if urls["href"].startswith("https://news.naver.com"):
#                 news_detail = get_news(urls["href"])
#                 f.write("{}\t{}\t{}\t{}\n".format(news_detail[1], news_detail[3], news_detail[0],
#                                                       news_detail[2]))
#         except Exception as e:
#             # print(e) 
#             continue
#     page += 10  
# f.close()

# url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=코알라'

# r = requests.get(url)
# html = r.content
# soup = BeautifulSoup(html, 'html.parser')
# titles_html = soup.select('.new_area > a.news_tit')

# for i in range(len(titles_html)):
#     print(i+1, titles_html[i].text)

##################################################################################################################################################

##  HeadLine
# pip install lxml
# import requests
# import pandas as pd
# import codecs
# from bs4 import BeautifulSoup
# class CrowKdd(object):
#     # results = ['']
#     keyword = '삼성전자'
#     def naver_news(self, keyword, order):
#         # tag = ['']
#         results = []
#         # a = ''
        
#         for i in range(20)[1:]:
#             url = r'https://search.naver.com/search.naver?&where=news&query={}&sm=tab_pge&sort={}&&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=287&start={}&refresh_start=0'.format(keyword, order, 10*(i-1)+1)
#             resp = requests.get(url)
#             soup = BeautifulSoup(resp.text, 'lxml')
#         #     article_title = soup.find_all('a', class_ = 'news_tit')
            

#         #     for j in article_title:
#         #         a += j.get_text()
#         # return a




#             # # title_list = soup.select('.news_tit')
#             # title_list = soup.find_all('a', class_ = 'news_tit')

#             # for tag in title_list:
#             # #     # print(tag.text)
#             # #     # df = pd.DataFrame(tag.text)
#             # #     # print(df.head())
#             #     # results.append(tag.text)
#             #     results += tag.get_text()
#         # return results

#             title_list = soup.find_all('a', class_ = 'news_tit')
            

#             for tag in title_list:
#                 # results += tag.get_text()
#                 results.append(tag.text)
#         return results

#     result = naver_news(object, keyword, 1) # 0 = 관련도순, 1 = 최신순, 2 = 오래된 순
#     # print(result)
#     df = pd.DataFrame(result)
#     # print(df)
#     df.columns = ['title']
#     print(df.head())
#     df.to_csv(keyword + '.csv', encoding='utf8')

# '''
# 0   논어, 새로운 가르침에 겁내지 않으려면 그간의 가르침을 실행해야 한다!       
# 1  "전 세계 AI 전문가 모여라"…'삼성 AI 포럼 2020' 온라인 개최
# 2              비트코인 지갑서비스 사업자도 자금세탁방지 의무 부과
# 3                  [연합뉴스 이 시각 헤드라인] - 12:00
# 4   “이건희 회장의 ‘도전 DNA’ 계승… 판도 바꾸는 기업으로 진화하자”
# '''


# =======================================================================================================================================
# from bs4 import BeautifulSoup
# from datetime import datetime
# import requests
# import pandas as pd
# import re

# # title_text = []
# # link_text = []
# # source_text = []
# # date_text = []
# # contents_text = []

# def main():
#     info_main = input("="*50+"\n"+"입력 형식에 맞게 입력해주세요."+"\n"+" 시작하시려면 Enter를 눌러주세요."+"\n"+"="*50)
#     maxpage = input("최대 크롤링할 페이지 수 입력하시오: ")
#     query = input("검색어 입력: ")
#     sort = input("뉴스 검색 방식 입력(관련도순=0 최신순=1 오래된순=2): ") #관련도순=0 최신순=1 오래된순=2
#     s_date = input("시작날짜 입력(2019.01.04):") #2019.01.04
#     e_date = input("끝날짜 입력(2019.01.05):") #2019.01.05
#     crawler(maxpage, query, sort, s_date, e_date)
# main()

# def crawler(maxpage, query, sort, s_date, e_date):
#     s_from = s_date.replace(".","")
#     e_to = e_date.replace(".","")
#     page = 1
#     maxpage_t =(int(maxpage)-1)*10+1 # 11= 2페이지 21=3페이지 31=4페이지 ...81=9페이지 , 91=10페이지, 101=11페이지

#     while page <= maxpage_t:
#         url = "https://search.naver.com/search.naver?where=news&query=" + query + "&sort="+sort+"&ds=" + s_date + "&de=" + e_date + "&nso=so%3Ar%2Cp%3Afrom" + s_from + "to" + e_to + "%2Ca%3A&start=" + str(page)
#         response = requests.get(url)
#         html = response.text

#         #뷰티풀소프의 인자값 지정
#         soup = BeautifulSoup(html, 'html.parser')

#         #태그에서 제목과 링크주소 추출
#         atags = soup.select('.news_tit')
#         for atag in atags:
#             title_text.append(atag.text) #제목
#             link_text.append(atag['href']) #링크주소

#         #신문사 추출
#         source_lists = soup.select('.thumb_box')
#         for source_list in source_lists:
#             source_text.append(source_list.text) #신문사

#         #날짜 추출
#         date_lists = soup.select('.info')
#         for date_list in date_lists:
#             test=date_list.text
#             date_cleansing(test) #날짜 정제 함수사용

#         #본문요약본
#         contents_lists = soup.select('a.api_txt_lines.dsc_txt_wrap')
#         for contents_list in contents_lists:
#             #print('==='*40)
#             #print(contents_list)
#             contents_cleansing(contents_list) #본문요약 정제화

#         #모든 리스트 딕셔너리형태로 저장
#         result= {"date" : date_text , "title":title_text , "source" : source_text ,"contents": contents_text ,"link":link_text }
#         print(page)

#         df = pd.DataFrame(result) #df로 변환
#         page += 10

# #날짜 정제화 함수
# def date_cleansing(test):
#     try:
#         #지난 뉴스
#         #머니투데이 10면1단 2018.11.05. 네이버뉴스 보내기
#         pattern = '\d+.(\d+).(\d+).' #정규표현식
#         r = re.compile(pattern)
#         match = r.search(test).group(0) # 2018.11.05.
#         date_text.append(match)
#     except AttributeError:
#         #최근 뉴스
#         #이데일리 1시간 전 네이버뉴스 보내기
#         pattern = '\w* (\d\w*)' #정규표현식

#         r = re.compile(pattern)
#         match = r.search(test).group(1)
#         #print(match)
#         date_text.append(match)

# #내용 정제화 함수
# def contents_cleansing(contents):
#     first_cleansing_contents = re.sub('<dl>.*?</a> </div> </dd> <dd>', '',
#     str(contents)).strip() #앞에 필요없는 부분 제거
#     second_cleansing_contents = re.sub('<ul class="relation_lst">.*?</dd>', '',
#     first_cleansing_contents).strip()#뒤에 필요없는 부분 제거 (새끼 기사)
#     third_cleansing_contents = re.sub('<.+?>', '', second_cleansing_contents).strip()
#     contents_text.append(third_cleansing_contents)
#     #print(contents_text)


# #엑셀로 저장하기 위한 변수
# RESULT_PATH ='C:/Users/User/Desktop/python study/beautifulSoup_ws/crawling_result/' #결과 저장할 경로
# now = datetime.now() #파일이름 현 시간으로 저장하기

# # 새로 만들 파일이름 지정
# outputFileName = '%s-%s-%s %s시 %s분 %s초 merging.xlsx' % (now.year, now.month, now.day, now.hour, now.minute, now.second)
# df.to_excel(RESULT_PATH+outputFileName,sheet_name='sheet1')
# =======================================================================================================================================

# from bs4 import BeautifulSoup
# import requests

# # url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=삼성전자'
# url = "https://search.naver.com/search.naver?where=news&query=" + query + "&sort="+sort+"&ds=" + s_date + "&de=" + e_date + "&nso=so%3Ar%2Cp%3Afrom" + s_from + "to" + e_to + "%2Ca%3A&start=" + str(page)
# # https://search.naver.com/search.naver?where=news&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&sm=tab_srt&sort=1&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so%3Add%2Cp%3Aall%2Ca%3Aall&mynews=0&refresh_start=0&related=0
# res = requests.get(url)
# html = res.text

# soup = BeautifulSoup(html, 'html.parser')

# title_list = soup.select('.news_tit')

# for tag in title_list:
#     print(tag.text)

# =======================================================================================================================================

# ============================================================
# ==================                     =====================
# ==================    Preprocessing    =====================
# ==================                     =====================
# ============================================================
class CrowDf(object):

    word = []
    noun_list =[]
    positive_word = []
    negative_word = []
    keyword_text = []

    poflag = []
    neflag = []

    file = open('삼성전자.csv', 'r', encoding='UTF8')
    lists = file.readlines()
    file.close()
    # lists
    
    twitter = Twitter()
    morphs = []

    for sentence in lists:
        morphs.append(twitter.pos(sentence))

    # print(morphs)

    pos = codecs.open('positive_words_self.txt', 'rb', encoding='UTF-8')

    while True:
        line = pos.readline()
        line = line.replace('\n', '')
        positive_word.append(line)
        keyword_text.append(line)

        if not line: break
    pos.close()

    neg = codecs.open('negative_words_self.txt', 'rb', encoding='UTF-8')

    while True:
        line = neg.readline()
        line = line.replace('\n', '')
        negative_word.append(line)
        keyword_text.append(line)

        if not line: break
    neg.close()

    # for sentence in morphs : 
    #     for word, text_tag in sentence :
    #         for x in range(len(keyword_text)):
    #             posflag = False
    #             negflag = False

    #             if x < len(positive_word)-1:
    #                 if word.find(keyword_text[x] != -1):
    #                     posflag = True
    #                     print(x, "positive_word?", "테스트 : ", word.find(keyword_text[x]), "비교 단어 : ", keyword_text[x], "인덱스 : ", x, word)
    #                     break
    #             if x > (len(positive_word)-2):
    #                 if word.find(keyword_text[x] != -1):
    #                     negflag = True
    #                     print(x, "negative?","테스트 : ", word.find(keyword_text[i]),"비교단어 : ", keyword_text[i], "인덱스 : ", x, word)
    #                     break

    #                 if posflag == True:
    

    # print(type(positive_word))

 

#==========================================================================================================
    for sentence in morphs : 
        for word, text_tag in sentence :
            for x in positive_word:
                if x == word: 
                    # print(x)
                    poflag.append(x)
                
            for y in negative_word:
                if y == word:
                    neflag.append(y)
                    # print("부정적 :", y)
            # if text_tag in ['Noun'] and ("것" not in word) and ("내" not in word) and ("첫" not in word) and \
            #     ("나" not in word) and ("와" not in word) and ("식" not in word) and ("수" not in word) and \
            #     ("게" not in word) and ("말" not in word):
                #  noun_list.append(word)
                
            # if text_tag in ['Noun'] and ("갑질" not in word) and ("논란" not in word) and ("폭리" not in word) and \
            #     ("허위" not in word) and ("과징금" not in word) and ("눈물" not in word) and ("피해" not in word) and \
            #     ("포화" not in word) and ("우롱" not in word) and ("위반" not in word) and ("리스크" not in word) and \
            #     ("사퇴" not in word) and ("급락" not in word) and ("하락" not in word) and ("폐업" not in word) and \
            #     ("불만" not in word) and ("산재" not in word) and ("닫아" not in word) and ("손해배상" not in word) and \
            #     ("구설수" not in word) and ("적발" not in word) and ("침해" not in word) and ("빨간불" not in word) and \
            #     ("취약" not in word) and ("불명예" not in word) and ("구형" not in word) and ("기소" not in word) and \
            #     ("반토막" not in word) and ("호소" not in word) and ("불매" not in word) and ("냉담" not in word) and \
            #     ("문제" not in word) and ("직격탄" not in word) and ("한숨" not in word) and ("불똥" not in word) and \
            #     ("항의" not in word) and ("싸늘" not in word) and ("일탈" not in word) and ("파문" not in word) and \
            #     ("횡령" not in word) and ("사과문" not in word) and ("여파" not in word) and ("울상" not in word) and \
            #     ("초토화" not in word) and ("급감" not in word) and ("우려" not in word) and ("중단" not in word) and \
            #     ("퇴출" not in word) and ("해지" not in word) and ("일베" not in word) and ("이물질" not in word) and \
            #     ("엉망" not in word) and ("소송" not in word) and ("하락" not in word) and ("매출하락" not in word) and \
            #     ("혐의" not in word) and ("부채" not in word) and ("과징금" not in word) and ("포기" not in word) and \
            #     ("약세" not in word) and ("최악" not in word) and ("손실" not in word) and ("의혹" not in word):
            #     positive_word.append(word)

    #         elif text_tag in ['Noun'] and ("MOU" not in word) and ("제휴" not in word) and ("주목" not in word) and \
    #             ("호응" not in word) and ("돌파" not in word) and ("이목" not in word) and ("수상" not in word) and \
    #             ("입점" not in word) and ("인기" not in word) and ("열풍" not in word) and ("진화" not in word) and \
    #             ("대박" not in word) and ("순항" not in word) and ("유치" not in word) and ("1위" not in word) and \
    #             ("출시" not in word) and ("오픈" not in word) and ("돌풍" not in word) and ("인싸" not in word) and \
    #             ("줄서서" not in word) and ("대세" not in word) and ("트렌드" not in word) and ("불티" not in word) and \
    #             ("진출" not in word) and ("체결" not in word) and ("증가" not in word) and ("기부" not in word) and \
    #             ("신제품" not in word) and ("신상" not in word) and ("최고" not in word) and ("새로운" not in word) and \
    #             ("착한" not in word) and ("신기록" not in word) and ("전망" not in word) and ("협력" not in word) and \
    #             ("역대" not in word) and ("상승" not in word) and ("늘어" not in word) and ("승인" not in word):
    #             negative_word.append(word)

    # print(noun_list)
    
    # count = Counter(noun_list)
    # words = dict(count.most_common())
    # print(words)
    
    # print(positive_word)
    # print(negative_word)
    count_po = Counter(poflag)
    count_ne = Counter(neflag)
    # po_words = count_po.most_common()
    po_words = dict(count_po.most_common())
    ne_words = dict(count_ne.most_common())
    print("긍정적인 단어", po_words)
    # print("긍정적인 단어", positive_word)
    # print(type(po_words))
    print("부정적인 단어", ne_words)
    



# ============================================================
# ==================                     =====================
# ==================       Modeling      =====================
# ==================                     =====================
# ============================================================
# class CrowDto(db.Model):
#     ...
# class CrowDao(StockDto):
#     ...
# class CrowVo(object):
#     ...
# class CrowTf(object):
#     ...
# class CrowAi(object):
#     ...
# ============================================================
# ==================                     =====================
# ==================      Resourcing     =====================
# ==================                     =====================
# ============================================================