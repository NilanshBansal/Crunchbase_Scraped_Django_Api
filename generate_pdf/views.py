from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
import random
import requests
from random import randint
from time import sleep
import warnings
import urllib
import pdfkit 
from django.template.loader import get_template

warnings.filterwarnings("ignore", category=UserWarning, module="bs4")

# def index(request):
#     return HttpResponse('CRUNCHBASE PDF!')

def home(request):
    query = request.GET['query']


    userAgents = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0)",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64)",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko)"
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko)",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko)",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko)",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko)",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko)",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko)",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko)",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko)",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko)",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko)",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko)",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko)",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko)",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko)",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko)",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko)"
    ]

    html_headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br, sdch',
        'Connection': 'keep-alive',
        'User-Agent': random.SystemRandom().choice(userAgents)
    }

    no = randint(1,2)
    # url = 'https://www.crunchbase.com/v4/data/entities/organizations/' + urllib.parse.quote_plus(query) + '?field_ids=%5B%22identifier%22,%22layout_id%22,%22facet_ids%22,%22title%22,%22short_description%22,%22description%22,%22is_locked%22%5D&layout_mode=view'
    url = 'https://www.crunchbase.com/v4/data/entities/organizations/' + query.replace(' ','-') + '?field_ids=["identifier","layout_id","facet_ids","title","short_description","description","is_locked"]&layout_mode=view'
    print(url)
    r = requests.get(url,headers=html_headers)
    # r = requests.get('http://localhost:8050/render.html?url={}&timeout=50&wait={}'.format(url,no),headers=html_headers,cookies=cookieJar2)
    
    print("\nServer_Headers: ", r.headers)
    print("\nClient_Headers: ", r.request.headers)
    print("\nStatus Code: ", r.status_code)

    # print(r.text)

    # return jsonify({'status':r.status_code,'cookieJar2':str(cookieJar2),'Client_Headers':str(r.request.headers),'Server_Headers':str(r.headers)})

    return HttpResponse(r.text,content_type='application/json')

def get_pdf(request):
    query = request.GET['query']
    
    userAgents = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0)",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64)",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko)"
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko)",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko)",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko)",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko)",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko)",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko)",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko)",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko)",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko)",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko)",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko)",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko)",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko)",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko)",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko)",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko)"
    ]

    html_headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br, sdch',
        'Connection': 'keep-alive',
        'User-Agent': random.SystemRandom().choice(userAgents)
    }

    no = randint(1,2)
    # url = 'https://www.crunchbase.com/v4/data/entities/organizations/' + urllib.parse.quote_plus(query) + '?field_ids=%5B%22identifier%22,%22layout_id%22,%22facet_ids%22,%22title%22,%22short_description%22,%22description%22,%22is_locked%22%5D&layout_mode=view'
    url = 'https://www.crunchbase.com/v4/data/entities/organizations/' + query.replace(' ','-') + '?field_ids=["identifier","layout_id","facet_ids","title","short_description","description","is_locked"]&layout_mode=view'
    
    print(url)
    r = requests.get(url,headers=html_headers)
    # r = requests.get('http://localhost:8050/render.html?url={}&timeout=50&wait={}'.format(url,no),headers=html_headers,cookies=cookieJar2)
    
    print("\nServer_Headers: ", r.headers)
    print("\nClient_Headers: ", r.request.headers)
    print("\nStatus Code: ", r.status_code)

    # print(r.text)
    final_json = json.loads(r.text)
    # return jsonify({'status':r.status_code,'cookieJar2':str(cookieJar2),'Client_Headers':str(r.request.headers),'Server_Headers':str(r.headers)})

    obj = {}
    try: 
        obj["title"] = final_json['properties']['title']
    except:
        obj["title"] = None
    try:
        obj["founded"] = final_json['cards']['overview_fields']['founded_on']['value']
    except:
        obj["founded"] = None
    try: 
        obj["hq"] = final_json['cards']['overview_image_description']['location_identifiers'][0]['value']
    except:
        obj["hq"] = None
    try: 
        obj["ipo_status"] = final_json['cards']['overview_company_fields']['ipo_status']
    except:
        obj["ipo_status"] = None
    try: 
        num_founders = len(final_json['cards']['overview_fields']['founder_identifiers'])
        founders = ""
        for i in range(num_founders):
            founders += final_json['cards']['overview_fields']['founder_identifiers'][i]['value'] + " , "

        founders = founders.rstrip(' ,')
        obj["founders"] = founders
    except:
        obj["founders"] = None    

    try:
        categories = ""
        num_categories = len(final_json['cards']['overview_fields']['categories'])
        for i in range(num_categories):
            categories+=final_json['cards']['overview_fields']['categories'][i]['value'] + " , "

        categories = categories.rstrip(' ,')
        obj['categories'] = categories
    except:
        obj['categories'] = None

    try:
        obj["num_investors"]=final_json['cards']['investors_summary']['num_investors']
    except:
        obj['num_investors'] = None
    
    try:
        obj['company_type'] = final_json['cards']['overview_company_fields']['company_type']
    except:
        obj['company_type'] = None

    try:
        obj['num_funding_rounds'] = final_json['cards']['funding_rounds_summary']['num_funding_rounds']
    except:
        obj['num_funding_rounds'] = None

    try:
        obj["num_employees"] = "~ " + final_json['cards']['owler_fields']['owler_employee_count']
    except:
        obj['num_employees'] = None

    try:
        obj["total_equity_funding"] = "$" + str(final_json['cards']['funding_rounds_summary']['funding_total']['value_usd']) + " in " + str(final_json['cards']['funding_rounds_summary']['num_funding_rounds']) + " rounds"
    except:
        obj['total_equity_funding'] = None

    try:
        obj["competitor"] = final_json['cards']['owler_image_list'][0]['competitor_identifier']['value']
    except:
        obj['competitor'] = None

    try:
        obj["competitor_revenue"] = "$ " + str(final_json['cards']['owler_image_list'][0]['competitor_revenue']['value_usd'])
    except:
        obj['competitor_revenue'] = None
    

    try:
        obj["short_description"] = final_json['properties']['short_description']
    except:
        obj['short_description'] = None
    
    try:
        obj["revenue"] = "$" + str(final_json['cards']['owler_summary']['owler_revenue']['value_usd'])
    except:
        obj['revenue'] = None

    try:
        obj["ceo_score"] = final_json['cards']['owler_fields']['owler_ceo_score']
    except:
        obj['ceo_score'] = None

    try:
        obj["no_of_webvisits_latest_month"] = final_json['cards']['similarweb_rank_headline']['similarweb_visits_latest_month']
    except:
        obj['no_of_webvisits_latest_month'] = None

    try:
        obj["no_of_news_articles"] = str(final_json['cards']['news_headline']['num_articles']) + " articles"
    except:
        obj['no_of_news_articles'] = None

    try:
        obj["website"] = final_json['cards']['overview_fields2']['website']['value']
    except:
        obj['website'] = None

    try:
        obj["twitter"] = final_json['cards']['overview_fields2']['twitter']['value']
    except:
        obj['twitter'] = None

    try:
        obj["linkedin"] = final_json['cards']['overview_fields2']['linkedin']['value']
    except:
        obj['linkedin'] = None
    
    try:
        obj["facebook"] = final_json['cards']['overview_fields2']['facebook']['value']
    except:
        obj['facebook'] = None

    try:
        obj["contact_email"] = final_json['cards']['overview_fields2']['contact_email']
    except:
        obj['contact_email'] = None

    try:
        obj["contact_no"] = final_json['cards']['overview_fields2']['phone_number']
    except:
        obj['contact_no'] = None



    t = get_template('pdf_template.html')
    html = t.render(obj)
    config = pdfkit.configuration(wkhtmltopdf='/app/bin/wkhtmltopdf')
    pdf = pdfkit.from_string(html, False, configuration=config)
    response = HttpResponse(pdf,content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename=' + obj['title'] + '.pdf'
    response['Content-Disposition'] = 'inline; filename=' + obj['title'] + '.pdf'


    return response




