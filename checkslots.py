import requests
import datetime
from datetime import date
from decouple import config

def checkSlots(log):
    numberOfDaysToLook = int(config('NUMBER_OF_DAYS_TO_LOOK'))
    currentDate = date.today()
    while numberOfDaysToLook > 0:
        url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict"
        params = {'district_id': config('DISTRICT_ID'), 'date': str(currentDate.strftime("%d-%m-%Y"))}
        if config('SEARCH_BY_PIN').lower() == 'true':
            url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin"
            params = {'pincode': config('PIN_CODE'), 'date': str(currentDate.strftime("%d-%m-%Y"))}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
        }
        responseReceived = False
        response = ''
        attemptCount = 5
        while not responseReceived and attemptCount > 0:
            response = requests.request("GET", url, headers=headers, params=params)
            if response.status_code == 200:
                responseReceived = True
            else:
                attemptCount -= 1
            if attemptCount == 0:
                log.info('Cowin API is not reachable at the moment')
        if response.status_code == 200:
            data = response.json()
            if len(data['centers']) > 0:
                log.info(f"Total centers found: {len(data['centers'])} | Date: {currentDate.strftime('%d-%m-%Y')}")
                for center in data['centers']:
                    for session in center['sessions']:
                        if session['available_capacity'] > 0:
                            log.info(f"Session available at: {center['name']} [{center['pincode']}] on {currentDate.strftime('%d-%m-%Y')}")
                            log.info(f"Avaliable Capacity: {session['available_capacity']} | Age Limit: {session['min_age_limit']} | Vaccine: {session['vaccine']}")
                            # add notification code here
                        else:
                            if config('NOTIFY_FULL_CENTERS').lower() == 'true':
                                log.info(f"Center full at: {center['name']} [{center['pincode']}] | Date: {currentDate.strftime('%d-%m-%Y')}")
                    
        currentDate += datetime.timedelta(days=1)
        numberOfDaysToLook -= 1


