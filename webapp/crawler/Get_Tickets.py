import requests
import re
import json
import time

def get_searchId(depart,arrive,depart_date,return_date):
    headers = {
        'authority': 'www.ca.kayak.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-CN;q=0.7,en-US;q=0.6,en-CA;q=0.5',
        # 'cookie': 'Apache=TES6rw-AAABi3iO_jY-ca-HiYlgw; cluster=4; p1.med.token=TcQeNdGHgnZ8omhV4XoF4Z; p1.med.sid=R-4WM5HxiK9qJAdjWZKCaOV-SThi2cid2yAtvfVj82jK1lL7YGmAix36ykeFFXB0A; kanid=; kanlabel=; kayak=ZRgVLarPBu7BCsgZuvRY; csid=3a4d96a7-1087-4373-b4d2-77b8084517d5; kmkid=AzWZONFPPpczOfKT6SIXRdY; _gcl_au=1.1.977708422.1698534720; _fbp=fb.1.1698534720000.0.83877501037026; _uetsid=6614126075e711ee80b143ab187e5dcf; _uetvid=c31415203bb311ee9d86293a66b74360; mst_ADIrkw=tg_Mb3q7RwZZ-v_-GQtrEfw2aObLBMJHq_utDuzZkmHiDvkLyTrsUQAj4rFHBEeJz8uaG2W8V7ecMn8p9OQ8gQ; kayak.mc=AdqJm5OeHxnyKFL9k2_Bk_wfG061COLqJstDc8VGHwZDtC-67fhoWseLA8kdZQG1gRSmlvCu1q8Th6QfqcHbu45q34XiF_vUvWkvOczIwo0BvOHwodvj7gHCpKQf8hVUmjBUxDjTPfCtzbG041KaM2TtO1z2DbM6a_jmTeMpQF-vkjaOsEgIPOeHgojQdSWeRnMmuMkk5cuvBW02CJ6Jan7HoTIVZytBLt_afuiHE19a0aR4uNMnh4BN31lo06SawHjiCiFE76Zab1etYBzHZ_4A2nB2nJNBNG2ge2WDil9jxKD8fU95tn_OT0xepUWIdgurnhkDS4zpxWO0h1VOo7yYQqdqJH49nYTuAiVNJkJq53x9HSBsHTgXpxEIaNMkBvD5y50gSZ6GX2NWn7bjkoVMUi-AABjtjMEe_TujtI0b; __gads=ID=73819b9a526939f8:T=1698530499:RT=1698536738:S=ALNI_MYPUp5g0Wv_u62onGeU-pOluWGERA; __gpi=UID=00000d9d43481b06:T=1698530499:RT=1698536738:S=ALNI_MYizyZ1B0zDAG-EfLJooBLy36TvpQ; mst_iBfK2g=Ba6adDTujnNUk-Pmyms0km7wqiZWA67vJpmOPbYBujYXFCW4vLFXZmTyH83iNPuOq52hreYJJdkqFLSuJhDOIw; hiddenParamsYMQ-YTO%2F2023-11-27%2F2023-12-04=id=1698536734&page_origin=&src=&searchingagain=&c2s=&po=&personality=&provider=-1&pageType=RP',
        # 'referer': 'https://www.ca.kayak.com/flights/YMQ-YTO/2023-11-27/2023-12-04?sort=bestflight_a',
        'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    }
    url='https://www.ca.kayak.com/flights/{}-{}/{}/{}'.format(depart,arrive,depart_date,return_date)
    response2 = requests.get(url, headers=headers)
    html = response2.text
    # print(html)
    pattern = r'"searchId":"(.*?)","'
    searchId=re.findall(pattern,html)[0]
    return searchId
def get_Ticket(searchId):
    timestamp = str(int(time.time()*1000))
    headers = {
        'authority': 'www.ca.kayak.com',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-CN;q=0.7,en-US;q=0.6,en-CA;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '__gads=ID=73819b9a526939f8:T=1698530499:RT=1698534494:S=ALNI_MYPUp5g0Wv_u62onGeU-pOluWGERA; __gpi=UID=00000d9d43481b06:T=1698530499:RT=1698534494:S=ALNI_MYizyZ1B0zDAG-EfLJooBLy36TvpQ; Apache=TES6rw-AAABi3iO_jY-ca-HiYlgw; cluster=4; p1.med.token=TcQeNdGHgnZ8omhV4XoF4Z; p1.med.sid=R-4WM5HxiK9qJAdjWZKCaOV-SThi2cid2yAtvfVj82jK1lL7YGmAix36ykeFFXB0A; kanid=; kanlabel=; kayak=ZRgVLarPBu7BCsgZuvRY; csid=3a4d96a7-1087-4373-b4d2-77b8084517d5; kmkid=AzWZONFPPpczOfKT6SIXRdY; _gcl_au=1.1.977708422.1698534720; _fbp=fb.1.1698534720000.0.83877501037026; _uetsid=6614126075e711ee80b143ab187e5dcf; _uetvid=c31415203bb311ee9d86293a66b74360; hiddenParamsYMQ-YVR%2F2023-11-27%2F2023-12-04=id=1698536226&page_origin=&src=&searchingagain=&c2s=&po=&personality=&provider=-1&pageType=RP; kayak.mc=AStiqSK56LYvXVy_OI9RK-4qc_BPf7-Bk7f1eEK5IzQ6jR4JR3s2VrFgB9Xt6MzvF0iNWYRW7ysUK0fBnwPIGCBERvfJZXQrsh7cu2eiKd-A1mU6LeUsM1sep0Sd9FyuEUphTrqSEJ66QXiW8MoBrvxxwOR6iXmrRf0K9u_xVs6UOp6uYXzP-V61KKdXNLLgbw4cnfUWMmfeOBqRCXjLHC5Wimvp_kkFHBMoo64xeaiMpqWcGJoWZ5IyhIdnxCsI1YUXGPPspyGBnynQSq2eBc08qMu5kY00ThPwGJQPwws4ukUEoGUWbExdx7e-h0ycZonqDn9PWwYX8d6HA6LIbbuYhaoQwfNUpwyZhWjXbpzmDTfGw0yrtEwXE7_hUkc4qTs7mdnaDHuNt9k1fD8b1Xg; mst_iBfK2g=3AucRJjTrOp5B_shf7Rh_ZvOZnQAQV2Tc1jRItRZJUaFz2EqVbFWY9lvp6KvCA4WYGvquhCE7zK0deuNLTs2XA; mst_ADIrkw=ryNWsSAX-YI-QjTZdS8Opf3VyKFHDwyD_G6nGPGVtF460uCRtID_K97RgeMzfW_oiEwHerTELW97gRdUJEQC4A',
        'origin': 'https://www.ca.kayak.com',
        # 'referer': 'https://www.ca.kayak.com/flights/YMQ-YVR/2023-11-27/2023-12-04',
        'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
        'x-csrf': 'eYJoYVwWs_Z2$IHRGF7YG7ZtlsXjdvk11uEuw18GxsI-PgN0bR4XtlJOyH3$oljl$ZnkvRe57858zis0$DCPdAQ',
        'x-r9-blue-green-version': 'R690d',
        'x-requested-with': 'XMLHttpRequest',
        # 'x-requestid': 'flights#results#ucodf2',
            }
    params = {
        'p': '0',
    }

    data = {
        'searchId': searchId,
        'poll': 'true',
        'pollNumber': '0',
        'applyFilters': 'true',
        'filterState': '',
        'useViewStateFilterState': 'true',
        'pageNumber': '1',
        'watchedResultId': '',
        'append': 'false',
        'sortMode': 'bestflight',
        'ascending': 'true',
        'priceType': 'daybase',
        'requestReason': 'POLL',
        'phoenixRising': 'true',
        'isSecondPhase': 'false',
        'displayAdPageLocations': 'bottom-left,bottom',
        'existingAds': 'false',
        'activeLeg': '-1',
        'hasFilterPreferences': 'false',
        'view': 'list',
        'renderPlusMinusThreeFlex': 'false',
        'renderAirlineStopsMatrix': 'false',
        'requestAlternateFlexDates': 'false',
        'ajaxts': timestamp,
        'scriptsMetadata': '16cQQ14E2E2C2Li1xE7C1Bw5g10C8g1BE1Cg6IBCQ9MB10Dg49g4Bk4E3g3Q1g26U1==',
        'stylesMetadata': '61&77Q3B24C19g25D2CI6BB1B11C2BB10w69C8DQ1Q13I314I79I37,hcE8g1I4C44E6g7I3QICE42I379EiSJ1E5IEmSJ3J1ECJEmSIEmSJEmSJEmSJ1kC2iSJ12ECQI2C1EiSJEk1I1k2EmSJ1E2ECSJEkCJEmS5Ek3CQJEk115C6E14I1CQ1EiCI8E1S1EgS2k149J16E1C38k118ECQI76EiSJ1E19G1BEG1J1kCIECS10CQJ1mQJEmSJEkCIEkSJEmSJEmSJEmQJEGSJEmSJEmSJEmSJEmSJEmSJEkSB1CQJEmSJEmSJ1mQJ4EiSJEmSJEkSBEiSIEmSJ1GQBEkS16JEmSJEmSJEk1JEmSJEEC2g127C1JEmS1EiSIEmSJEk1JEkCBEiSJEkC2CQB1mSI1k3i3gSJ5G2Em2E1C89E12C1JEGCJ1kQ6C2EgC2ECB3JEmSB1g4QJ1E1I10QIEESJEmSJEkS6CSJ1E627CSJEkSBE6B141g11CSJEmSJEmSJEmSJEmSJEmSJEkS4I1k20SB4EiQBE1C6C1',
        'r9version': 'R690d',
    }

    response = requests.post(
        'https://www.ca.kayak.com/s/horizon/flights/results/FlightSearchPoll',
        params=params,
        headers=headers,
        data=data)
    jsondata = response.json()
    json_data = jsondata['bufferedScripts'][0]
    pattern2 = r"R9.redux.dispatch\({ type: 'FlightResultsList.SET_DATA', state:(.*?)\s}\)\s+R9."
    json_ticket_data = re.findall(pattern2, json_data)[0]
    ticket_result=json.loads(json_ticket_data)
    return ticket_result
def get_tickets_list(depart,arrive,depart_date,return_date):
    searchId = get_searchId(depart,arrive,depart_date,return_date)
    result = get_Ticket(searchId)
    return result
def get_imageing(keyword):
    headers = {
    'authority': 'www.ca.kayak.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-CN;q=0.7,en-US;q=0.6,en-CA;q=0.5',
    # 'content-length': '0',
    # 'cookie': 'Apache=TES6rw-AAABi3iO_jY-ca-HiYlgw; cluster=4; p1.med.token=TcQeNdGHgnZ8omhV4XoF4Z; p1.med.sid=R-4WM5HxiK9qJAdjWZKCaOV-SThi2cid2yAtvfVj82jK1lL7YGmAix36ykeFFXB0A; kanid=; kanlabel=; kayak=ZRgVLarPBu7BCsgZuvRY; csid=3a4d96a7-1087-4373-b4d2-77b8084517d5; kmkid=AzWZONFPPpczOfKT6SIXRdY; _gcl_au=1.1.977708422.1698534720; _fbp=fb.1.1698534720000.0.83877501037026; _uetsid=6614126075e711ee80b143ab187e5dcf; _uetvid=c31415203bb311ee9d86293a66b74360; kayak.mc=AQxtwVhgt3bclXkFGrZFPIpj8EWes7AoIhXi4x1b6CyWTZfqMGBguco5dIRibmiTfZ2q32X5yZETyIsfuyGGbUr4ZrHGN081mG7gct3gIq2WCcYPzq5KKm4tXy_RwPj2pkavaNDUGhF6ZudEFvXAqHSjOS5Tx3r0zkkhKiyuACGN65qKjn2P72YSJqAHFl1JW7-muCdsDmAH0pJq34UUclKmLKHK1R6eMdxkvoeW0QKe18lZOqqO45T7qW1OMYL8gASgE4khzhyVvf5dxVUsAe36LGiUy9FFtiNmtlqfbfzK1fi61w4ew7dxLRsStRiZEv9a5chhW30sUw7ac9DHXnRVIVxkxidWcZ7xkaQYRCrhcBEqlIo7Hy5vLKAZzYA6I_YMMRZa0pRf60dNGwN35ejVeWpMzWIaiJyR2FUP1f37; __gads=ID=73819b9a526939f8:T=1698530499:RT=1698540238:S=ALNI_MYPUp5g0Wv_u62onGeU-pOluWGERA; __gpi=UID=00000d9d43481b06:T=1698530499:RT=1698540238:S=ALNI_MYizyZ1B0zDAG-EfLJooBLy36TvpQ; mst_iBfK2g=J8xuYXWVoDcXA95JKfYyWfw2aObLBMJHq_utDuzZkmE7E2VsYGDY3wvRs_iqhemyZusMMKW-qy7TrY4SlHD88Q; mst_ADIrkw=a5lVm-BbvgkXghfdZ9OfgXvA6aZsvq9WQpyfu-w6A6QETbUZb7N2ZBC4RH-ukKProDk9zeJ7gp3cTWcWz2G30Q',
    'origin': 'https://www.ca.kayak.com',
    'referer': 'https://www.ca.kayak.com/flights/YMQ-YTO/2023-11-27/2023-12-04?sort=bestflight_a',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'f': 'j',
        's': '58',
        'where': keyword,
        'lc_cc': 'CA',
        'lc': 'en',
        'sv': '5',
        'cv': 'undefined',
        'c': 'undefined',
        'searchId': 'undefined',
        'v': 'undefined',
    }

    response3 = requests.post('https://www.ca.kayak.com/mvm/smartyv2/search', params=params, headers=headers)
    return response3.json()
if __name__=='__main__':
    searchId=get_searchId('YTO','YMQ','2023-10-29','2023-11-11')
    result=get_Ticket(searchId)
    resultIds=result['resultIds']
    for i in range(1,len(resultIds)):
        try:
            each = result['results'][resultIds[i]]
            legs = each['legs']
            legs_list = [i['segments'][0] for i in legs]
            fees = each['optionsByFare']
            bookingurl = 'https://www.ca.kayak.com' + fees[0]['options'][0]['url']
            price = fees[0]['options'][0]['fees']['rawPrice']
            result_dict = {
                'depart':'YTO',
                'arrive':'YMQ',
                'depart_date':'2023-11-27',
                'return_date':'2023-11-30',
                'price':price,
                'bookingurl':bookingurl,
                'legs_list':legs_list
            }
            print(result_dict)
        except:pass


