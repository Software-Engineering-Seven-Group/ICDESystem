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
def get_ticket2(depart,arrive,depart_date,return_date):  #Booking
    headers = {
    'authority': 'flights.booking.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-CN;q=0.7,en-US;q=0.6,en-CA;q=0.5',
    # 'cookie': 'cors_js=1; bkng_sso_ses=e30; bkng_sso_session=e30; _pxvid=0b421438-6efb-11ee-a052-7388906e5dde; _gcl_au=1.1.1694537867.1697775512; _scid=8435e4aa-5977-49a7-b3d3-007afeb39849; FPID=FPID2.2.8kZExm2PpsjJxD0c94meBneQ27rhW3xxmG%2FHaSc894E%3D.1697773500; _pin_unauth=dWlkPU56azRZelV3T1RjdFlUSmxOQzAwWWpZeUxUa3hOVGN0TXpVM1l6aG1ZekF6WkdObA; g_state={"i_p":1697782811769,"i_l":1}; b=%7B%22countLang%22%3A4%7D; cto_bundle=k4dmKF9VQ29idEkyZzlnMEIyeTYzUWIxUHQyWiUyQmxiMVg2WkZmdFUwTmc3UzM2N3M3JTJCM2dHUVcwUzk1SDQ2Tk5pcHZ1UHptd0NOMjFrdG51YUd4TWZQODRBZUpqNEhqZTJtT3J2V2hGUVVwUmlCTlVHTzRxeVl1Nm9pSXYlMkZGMG1rNkpRa0JzRXdxMiUyQkx0QlpONldxUmV0MmQwRTlGRnp2dDVnbVZac05YZlo1VTRyNmdEbHk0UFlOT2JYZVVsQnRqMlBrVGVneTFJVmJOcmVaMGJFTklSOGNvYWcwRzJaZkElMkZvaTIyUkFocUxHYVlOYVdGUlVxRjM1QWZ4dVJwSHkzWThqRA; fsc=s%3A8d3c8e669cf637e38d789c2640be3f44.nH9zt6o9vomB3rNt7rKftWQBI1S%2BLgeLtiSaRHmKKwI; pcm_consent=consentedAt%3D2023-10-28T23%3A53%3A34.330Z%26countryCode%3DCA%26expiresAt%3D2024-04-25T23%3A53%3A34.330Z%26implicit%3Dfalse%26regionCode%3DQC%26regulation%3Dnone%26legacyRegulation%3Dnone%26consentId%3D94c410ff-a7de-416f-9366-1f926d46c0cd%26analytical%3Dtrue%26marketing%3Dtrue; pc_payer_id=66bd1aa9-9e5e-48e3-a7a5-69d284778e96; fsc=s%3A8d3c8e669cf637e38d789c2640be3f44.nH9zt6o9vomB3rNt7rKftWQBI1S%2BLgeLtiSaRHmKKwI; OptanonConsent=implicitConsentCountry=nonGDPR&implicitConsentDate=1697773499873; _sctr=1%7C1698465600000; px_init=1; _gac_UA-116109-18=1.1698683381.Cj0KCQjwqP2pBhDMARIsAJQ0CzoLhOoJ3Vh0iYufCKauO6BhCQb4oHs3kYYcAPyR45922qU36r1IS-YaAoNFEALw_wcB; _gcl_aw=GCL.1698683381.Cj0KCQjwqP2pBhDMARIsAJQ0CzoLhOoJ3Vh0iYufCKauO6BhCQb4oHs3kYYcAPyR45922qU36r1IS-YaAoNFEALw_wcB; bkng_sso_auth=CAIQsOnuTRpy1geofL5GeFwOTn49FbMOHjEkyU2Zr8UK+Mu8YemsK6LNBSN6o0RwR4pn3LphvcdW6+6ZTojfeCcKAmHyaBZQ/tm0FM71kCsZZlq90hicfHEfRgdy9k5Jd/Duo0SDjIx00mSHG0A64Q0prP4gY1nUDPdv; BJS=-; _gid=GA1.2.172711041.1699031482; _gat=1; __gads=ID=cdd1086050d34b5c:T=1697775510:RT=1699031481:S=ALNI_MZ9-p3lIQH4xLCsbUn0zWgNwxno2Q; __gpi=UID=00000d9b23cc8d39:T=1697775510:RT=1699031481:S=ALNI_MZBgDH0-GHAgQo_xmC5hp9Vr0FcCQ; pxcts=02e9c631-7a6c-11ee-8ee6-7dc3ea9b8ff0; bkng_prue=1; _ga=GA1.1.588184741.1697773500; _ga_FPD6YLJCJ7=GS1.1.1699031483.10.0.1699031483.60.0.0; _scid_r=8435e4aa-5977-49a7-b3d3-007afeb39849; _ga_A12345=GS1.1.1699031483.10.0.1699031483.0.0.0; FPLC=ywEQaT6ev95qpQA9OSzAStsQI49xKkLxguOEPR26ThMHkq1c8nbrRU0u3umCr0DEOCNN6C5F%2B34C2MQMPvA1p6wrMMczrGKafijf87aTDT7RLfwoL0Ill3hfVRVIiQ%3D%3D; _px3=8ae5da39abfd778c79b3262b4978c44775410b311da27e5286de99c0c0561214:4PmPved+w5kyGpl3PcbC2VwVl9IvNFM/HdaVO2j0z/mchulZa5cUShDsAZ0F+GfzkJ7IQ/lSVj3ZZDUWAdIedA==:1000:8glhYCuZ1Q7K2OdGIOf1eDjTur2vmvIzwHMJod/1B4fEvIC1aSYialcP4+8s+qYmX8vy5XulXqMftkh4x8o9jGSa5eRwEoCF9bXqJxr1NrAaiJ9yn9Iq6hjlGJsPEKS/dbQ0L031LamG7Z0F8oVncw8yKjVtFn18pGuyXFV03LHmrS/UMhWthP0IIKazzPWbQ+ubEpOUJ0c8a2Wb4TmkbkLuGQPspA61KR/ZaPsh9J0=; _pxde=e6ac48f06ea24df0e2bd22290da717a64249c7a69ddef59b299832516f750149:eyJ0aW1lc3RhbXAiOjE2OTkwMzE0ODI4MzMsImZfa2IiOjAsImlwY19pZCI6W119; _pxhd=87GlHkukrDGQ3oGoKcq1fko5Ofppl8GIifbGFRBMFDhIV1e1d-DRLaCcxcElsa6dFG5oofl-QjrZkjeKEZ9Jog%3D%3D%3A9zIC2HPC7MRn%2FIe2sFRBNwxy85i73gjhy1C8-iwn6HSbMkrr-DnqHgN8vRXFsqUJnlmUyHaZI-ADj9sqAumAH85n3S6hYhiuL-ii4EH7vGE%3D; fasc=11865d29-ab7a-4419-80ff-589622479500; lastSeen=1699031484456; _uetsid=03c040807a6c11ee9ab97d80235d4c0f; _uetvid=36977eb010fa11ee8fc803d00f40c325; bkng=11UmFuZG9tSVYkc2RlIyh9YSvtNSM2ADX0BnR0tqAEmju3Hqww3f4xH5QhNFzz98Twnj8%2Fk9G5AIoy1THTyCYvh%2FCYLJZ9AtpjpGfvsuPzhb7DNrIroP%2BqtZUGGMGLCaAcFjoZSBcZiVYtR9LViao0dTYHGlQ%2FsdbWjNVO%2Bz6qQ1aH1iUzdqPYTipuDUhFx2jM5y5Rgdzoiefu%2BmiNrUNIrw%3D%3D',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    }

    params = {
        'type': 'ROUNDTRIP',
        'adults': '1',
        'cabinClass': 'ECONOMY',
        'children': '',
        'from': depart,
        'to': arrive,
        'fromCountry': 'CA',
        'toCountry': 'CA',
        'depart': depart_date,
        'return': return_date,
        'sort': 'BEST',
        'travelPurpose': 'leisure',
        'enableVI': '1',
        'enableDiscounts': 'cug',
    }

    response = requests.get('https://flights.booking.com/api/flights/', params=params, headers=headers)
    return response.json()
def get_tickets_list(depart,arrive,depart_date,return_date):
    searchId = get_searchId(depart,arrive,depart_date,return_date)
    result = get_Ticket(searchId)
    return result


def format_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60

    formatted_time = f"{hours:2d}h {minutes:2d}m"
    return formatted_time
def get_tickets_list2(depart,arrive,depart_date,return_date):
    result_list=get_ticket2(depart,arrive,depart_date,return_date)
    resultIds = result_list['flightOffers']
    result_list=[]
    for i in range(len(resultIds)):
        try:
            each = resultIds[i]
            legs_list = each['segments']
            price = each['priceBreakdown']['totalRounded']['units']
            bookingurl = 'https://flights.booking.com/checkout/ticket-type/' + each['token']
            Depart_city = legs_list[0]['departureAirport']['cityName']
            Arrive_city = legs_list[0]['arrivalAirport']['cityName']
            for j,aa in enumerate(legs_list):
                legs_list[j]['totalTime']=format_seconds(aa['totalTime'])
            result_dict = {
                'Depart_city': Depart_city,
                'Arrive_city': Arrive_city,
                'depart_date': depart_date,
                'return_date': return_date,
                'price': price,
                'bookingurl': bookingurl,
                'legs_list': legs_list
            }
            result_list.append(result_dict)
            print(result_dict)
        except:
            pass
    return result_list
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
    aa=get_tickets_list2('YTO','YMQ','2023-11-29','2023-12-11')
    print(aa)
    # searchId=get_searchId('YTO','YMQ','2023-10-29','2023-11-11')
    # result=get_Ticket(searchId)
    # resultIds=result['resultIds']
    # for i in range(1,len(resultIds)):
    #     try:
    #         each = result['results'][resultIds[i]]
    #         legs = each['legs']
    #         legs_list = [i['segments'][0] for i in legs]
    #         fees = each['optionsByFare']
    #         bookingurl = 'https://www.ca.kayak.com' + fees[0]['options'][0]['url']
    #         price = fees[0]['options'][0]['fees']['rawPrice']
    #         result_dict = {
    #             'depart':'YTO',
    #             'arrive':'YMQ',
    #             'depart_date':'2023-11-27',
    #             'return_date':'2023-11-30',
    #             'price':price,
    #             'bookingurl':bookingurl,
    #             'legs_list':legs_list
    #         }
    #         print(result_dict)
    #     except:pass


