import requests
import re
from lxml import etree
def get_html(destination):
    headers = {
        'authority': 'www.tripadvisor.ca',
        'accept': 'text/html, */*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-CN;q=0.7,en-US;q=0.6,en-CA;q=0.5',
        'content-type': 'Application/json; charset=utf-8',
        # 'cookie': 'TASameSite=1; TAUnique=%1%enc%3AuDVedQjmD2%2FBYT8Sg7TvTyjGztohMnNyZR91DoldrNQnuvWISCXjiA%3D%3D; TASSK=enc%3AABaQxuTKpwhe%2BHhqH84jVZGrLaNSkxzpdOB%2BSCMuQ3zj7rLGY3Eurw%2FXYiT%2FHydTBCAr5TJp0QEZpjecYtflaKd6KaxzLw%2FWSX58Av4fMRGx2KPMRitg9WAGIleRoXKhIg%3D%3D; _pbjs_userid_consent_data=3524755945110770; _lc2_fpi=b4f42222ff48--01hc8zz1jfsjwndq1wmj7vw51y; pbjs_sharedId=ba277e0e-268f-44d4-8c2c-c930554d9217; _ga=GA1.1.1927087291.1696814041; pbjs_sharedId_cst=zix7LPQsHA%3D%3D; ab.storage.sessionId.6e55efa5-e689-47c3-a55b-e6d7515a6c5d=%7B%22g%22%3A%22080a89bb-7cca-2f31-5031-4a49becc5524%22%2C%22e%22%3A1697498377192%2C%22c%22%3A1697498317192%2C%22l%22%3A1697498317192%7D; ab.storage.deviceId.6e55efa5-e689-47c3-a55b-e6d7515a6c5d=%7B%22g%22%3A%22f42f0884-ac40-e7f7-8546-31ba0f10ac4c%22%2C%22c%22%3A1696814122722%2C%22l%22%3A1697498317193%7D; VRMCID=%1%V1*id.13524*llp.%2F-a_gclid%5C.CjwKCAjw1t2pBhAFEiwA__5F____2D__A__2D__NBuGy5TdnqxNWw24T81LQMna7D8IP5XY3Mn3dZ3HyfhSDTWpIYjYABoCRSsQAvD__5F__BwE-m13524-a_supac%5C.4916380134-a_supag%5C.10827356304-a_supai%5C.671681109586-a_supbk%5C.1-a_supcm%5C.155008344-a_supdv%5C.c-a_supli%5C.-a_suplp%5C.9000411-a_supnt%5C.g-a_supti%5C.kwd__2D__119671122*e.1698778073738; _lr_env_src_ats=true; TATrkConsent=eyJvdXQiOiJTT0NJQUxfTUVESUEiLCJpbiI6IkFEVixBTkEsRlVOQ1RJT05BTCJ9; TADCID=_0eidzqb2RnCtesRABQCCKy0j55CTpGVsECjuwJMq3lXymses9dkE4_x8dwYJAjeATP8AtEiyNTPjCPcnmmtangbMSX-2jzdFUQ; TAAUTHEAT=6Sz9DpmnohDarniJABQCobW21V9oR1-Dg22GNw6BiDkuyka3FNFz-lREfScWTDtoB-GTK0LWXZSEEWmC4AIm3PTX6ku16CD7bocjlw8ZdJh2Ww-231q1W5UOk7dKISpVWx9piN-F3WDXSgJzYH2MHmgyAgTzkChMFMrUY2BSVXaJqGGU9CyUKzQzb6Ll2BbsBUbCjEn1WbNwmmJkrw222Dl7-CiQn6latDQ; __vt=u76NbyA-nfcexfO9ABQCCQPEFUluRFmojcP0P3EgGik1aoyb2VqaBtvXcDc6SLAY2aRGM-r15AdPq0W9_iHDywpaYgv91utUSwlecNVJxCzRg4etCV0uFPA5bAoFTuTwdw6tCo8dYG0xAuIB7WiMDfWhDQ; ServerPool=B; PMC=V2*MS.28*MD.20231008*LD.20231104; TASID=C43E9A3004B542089504B5749BCE68E6; PAC=ALGYBNJN08cD30RJ_VMFg7HHiYF0iYQ1PALowc-LJsCfxF5cJ7SanxBocGTyEF0ulM8zsaIZDnrpsGkixy8k_S_KMYpmzHrP5znIJVkEDD1Qufwc_0mS2PHnx3AWxs-tAw%3D%3D; AMZN-Token=v2FweIBLVVFldDNlQTRGWnNmQ1hBNzNaNWl1dWZHTXhUYXcvMUxxU3ROVUt1ZVVsMVlaK3NjdjM4QUxWcXFTdTh4L3dSa1pPR0hBK1pjWGYrek45NjhQOERkKzlRZFhXd0RJaUxld0tZd3NJR1VoOXJlbmFmanJwZ3N4R0hUdmJXbDhnMGJrdgFiaXZ4GHpLTFVqeHZ2djcxRzc3KzlDMjBmNzcrOf8=; _li_dcdm_c=.tripadvisor.ca; __gads=ID=13099b5bfa4f0e0c:T=1696814042:RT=1699153784:S=ALNI_MawHuox6vljQ1XvZ-2HcpMQjo8YEQ; __gpi=UID=000009fdedac231b:T=1696814042:RT=1699153784:S=ALNI_MbWhgn0AthGBNOwZ2ycDuZkDqV7cw; _lr_sampling_rate=100; TATravelInfo=V2*AY.2023*AM.11*AD.12*DY.2023*DM.11*DD.13*A.2*MG.-1*HP.2*FL.3*DSM.1699153788375*AZ.1*RS.1; __li_idex_cache_e30=%7B%22nonId%22%3A%22DV3uLGPLagWrskAy-6aoli-fU7M9m8McnVM85A%22%2C%22magnite%22%3A%22LIW92P2T-1W-B1A1%22%7D; pbjs_li_nonid=%7B%22nonId%22%3A%22DV3uLGPLagWrskAy-6aoli-fU7M9m8McnVM85A%22%2C%22magnite%22%3A%22LIW92P2T-1W-B1A1%22%7D; pbjs_li_nonid_cst=zix7LPQsHA%3D%3D; SRT=TART_SYNC; TART=%1%enc%3AeoEbmvCankdrKus7Mx84haqKgxXDcW1YVThVYBzRFkuIdRV4C0KB3%2F6M5teXsZDh3Fl6nYPjOm4%3D; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Nov+04+2023+23%3A10%3A06+GMT-0400+(%E5%8C%97%E7%BE%8E%E4%B8%9C%E9%83%A8%E5%A4%8F%E4%BB%A4%E6%97%B6%E9%97%B4)&version=202209.1.0&isIABGlobal=false&hosts=&consentId=0B2EC6E536DF6957E24D1E8FCFE51102&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false; _ga_QX0Q50ZC9P=GS1.1.1699153783.9.1.1699153807.36.0.0; TASession=V2ID.C43E9A3004B542089504B5749BCE68E6*SQ.9*LS.Tourism*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.0B2EC6E536DF6957E24D1E8FCFE51102*FA.1*DF.0*TRA.true*LD.1*EAU.u; TAUD=LA-1696814037674-1*RDD-1-2023_10_08*ARC-41863*HD-683989603-2023_11_19.2023_11_20.155587*VRD-683989604-2023_11_19.2023_11_20*G-683989605-2.1.155587.*VRG-683989606-2.0*ARDD-745346587-2023_11_19.2023_11_20*HDD-2339750610-2023_11_12.2023_11_13*LD-2339797723-2023.11.12.2023.11.13*LG-2339797726-2.1.T.; datadome=SZliGWIkOY33KcwOW~792C2_j8VnXAWitNtmpAeFiptZoakxzfGPawedZ8fG41eGHaBhiJbFjRpq1t_MP05MSTtLpZqpzgdFal8kGT7yQVbJwmNY25MZAoZNb5_itkam; roybatty=TNI1625!AOZUS8xB9T0tqVIs%2B51eFUwy%2BzVqJX2AE3wRYpiP64b3KUOCBaP7MPvvuGXJHSiIwrfP3nzC1%2BUVhF%2FrFZWaiQ1Z6pg2W9uYBVJUC3D%2BJ4YC%2BavpNCBKeZMfHYYazFnbkymoX%2BH7AQgC%2BsxetYvujpNFz3ZP1q%2FN6ln2IDlMs3K8%2C1',
        # 'referer': 'https://www.tripadvisor.ca/Search?searchSessionId=000896991b77c339.ssid&searchNearby=false&q=Montreal&sid=C43E9A3004B542089504B5749BCE68E61699153788841&blockRedirect=true&geo=1&ssrc=A&rf=3',
        'sec-ch-device-memory': '8',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-full-version-list': '"Google Chrome";v="119.0.6045.105", "Chromium";v="119.0.6045.105", "Not?A_Brand";v="24.0.0.0"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'x-puid': '8938f263-fc70-47d2-9ef0-14ffc923f841',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'searchNearby': 'false',
        'q': destination,
        'blockRedirect': 'true',
        'geo': '1',
        'ssrc': 'A',
        'rf': '3',
        'withFilters': 'true',
        'firstEntry': 'true',
    }

    response = requests.get('https://www.tripadvisor.ca/Search', params=params, headers=headers)
    # print(response.text)
    return response.text
def Data_process(html_text,destination):
    html = etree.HTML(html_text)
    location_list = html.xpath( '//div[@data-widget-type="LOCATIONS" and @class="ui_column is-12 content-column result-card"]')
    result_list=[]
    for location in location_list:
        try:
            title = location.xpath('.//*[@class="result-title"]/span/text()')[0]
            address = location.xpath('.//*[@class="address-text"]/text()')[0]
            img_style = location.xpath('.//*[@class="aspect  is-shown-at-desktop"]/div/@style')[0]
            img_url = re.findall('url\((.*?)\);', img_style)[0]
            review_snipeet = location.xpath('.//*[@class="review-snippet"]/text()')[0]
            tag = location.xpath('.//*[@class="thumbnail-overlay-tag"]/text()')[0]
            url_str = location.xpath('.//*[@class="result-title"]/@onclick')[0]
            html_links = re.findall(r"'(\/[^\s']*)'", url_str)[0]
            result_dict={
                'destination':destination,
                'title':title,
                'address':address,
                'img_url':img_url,
                'review_snipeet':review_snipeet,
                'tag':tag,
                'html_link':'https://www.tripadvisor.ca'+html_links
            }
            result_list.append(result_dict)
        except:pass
    return result_list
def get_destination_result(destination):
    html1 = get_html(destination)
    result = Data_process(html1, destination)
    return result
if __name__=='__main__':
    html1=get_html('Montreal')
    result=Data_process(html1,'Montreal')
    # print(result)