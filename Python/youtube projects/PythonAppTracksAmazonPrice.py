import requests
from bs4 import BeautifulSoup
import smtplib
import time


URL = 'https://www.flipkart.com/adidas-adissage-ss-19-flip-flops/p/itmfd3jeghr7gzwa?pid=SFFFD3JCZCJK8GGG&lid=LST' \
      'SFFFD3JCZCJK8GGGTWOB5J&marketplace=FLIPKART&fm=productRecommendation%2Fsimilar&iid=R%3As%3Bp%3ASFFFHW6WCFZV' \
      'S2BX%3Bl%3ALSTSFFFHW6WCFZVS2BXOEKCBK%3Bpt%3App%3Buid%3A99ac1419-a0a4-5180-fca0-07e1fae80470%3B.SFFFD3JCZCJK8GG' \
      'G.LSTSFFFD3JCZCJK8GGGTWOB5J&ppt=ProductPage&ppn=ProductPage&ssid=rr5oso58gw0000001578423929214&otracker=pp_' \
      'reco_Similar%2BProducts_1_29.productCard.PMU_HORIZONTAL_ADIDAS%2BADISSAGE%2BSS%2B19%2BFlip%2BFlops_SFFF' \
      'D3JCZCJK8GGG.LSTSFFFD3JCZCJK8GGGTWOB5J_productRecommendation%2Fsimilar_0&otracker1=pp_reco_PINNED_productR' \
      'ecommendation%2Fsimilar_Similar%2BProducts_GRID_productCard_cc_1_NA_view-all&cid=SFFFD3JCZCJK8GGG.LSTSFFFD3' \
      'JCZCJK8GGGTWOB5J'


headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 '
                        '(KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}


def check_price():

      page = requests.get(URL, headers=headers)

      soup = BeautifulSoup(page.content, 'html.parser')
      title1 = soup.find(attrs={"class":"_2J4LW6"}).get_text()
      title2 = soup.find(attrs={"class":"_35KyD6"}).get_text()
      price = soup.find(attrs={"class":"_1vC4OE _3qQ9m1"}).get_text()

      price = price.replace(',','')
      converted_price = price[1:]
      converted_price = float(converted_price)

      if converted_price < 1700:
            send_mail()


      print(converted_price)
      print(title1, title2)

def send_mail():
      server = smtplib.SMTP('smtp.gmail.com', 587)
      server.ehlo()
      server.starttls()
      server.ehlo()

      # google two step verification turn on
      # google app password
      server.login('kaira.ankit1234@gmail.com', 'yxmowvvqomupgapr')

      subject = 'Price fell down'
      body = 'Check the amazon link https://www.flipkart.com/adidas-adissage-ss-19-flip-flops/p/itmfd3jeghr7gzwa?pid=SFFFD3JCZCJK8GGG&lid=LST' \
      'SFFFD3JCZCJK8GGGTWOB5J&marketplace=FLIPKART&fm=productRecommendation%2Fsimilar&iid=R%3As%3Bp%3ASFFFHW6WCFZV' \
      'S2BX%3Bl%3ALSTSFFFHW6WCFZVS2BXOEKCBK%3Bpt%3App%3Buid%3A99ac1419-a0a4-5180-fca0-07e1fae80470%3B.SFFFD3JCZCJK8GG' \
      'G.LSTSFFFD3JCZCJK8GGGTWOB5J&ppt=ProductPage&ppn=ProductPage&ssid=rr5oso58gw0000001578423929214&otracker=pp_' \
      'reco_Similar%2BProducts_1_29.productCard.PMU_HORIZONTAL_ADIDAS%2BADISSAGE%2BSS%2B19%2BFlip%2BFlops_SFFF' \
      'D3JCZCJK8GGG.LSTSFFFD3JCZCJK8GGGTWOB5J_productRecommendation%2Fsimilar_0&otracker1=pp_reco_PINNED_productR' \
      'ecommendation%2Fsimilar_Similar%2BProducts_GRID_productCard_cc_1_NA_view-all&cid=SFFFD3JCZCJK8GGG.LSTSFFFD3' \
      'JCZCJK8GGGTWOB5J'

      msg = f'Subject: {subject}\n\n{body}'
      server.sendmail('kaira.ankit1234@gmail.com', 'kairaa74@gmail.com', msg)
      print('HEY EMAIL HAS BEEN SENT')
      server.quit()

while(True):
      check_price()
      time.sleep(86400)

