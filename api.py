import requests
from calculation import hsical


try:
    def api_info(latitude, longitude):

        # request = requests.get('http://127.0.0.1:8000/')
        # print(request.json())
        '''
        Stages of my URL first one was to see if the file read using the request.json above.
        Second one was where I inserted the latitude and longitude physically had an issue where their was a server error
        till I saw the : infront of my url.
        third and final url was by using .format for latitude and longitude to use float values in main.
        '''
        # url = "http://api.weatherapi.com/v1/forecast.json?key=d14476359b4d4d5cb9a201929230110&q=London&days=3&aqi=no&alerts=no"
        # url = "http://api.weatherapi.com/v1/forecast.json?key=d14476359b4d4d5cb9a201929230110&q=" + latitude + "," + longtitude + "&days=3&aqi=no&alerts=no"
        url = "http://api.weatherapi.com/v1/forecast.json?key=d14476359b4d4d5cb9a201929230110&q={0},{1}&days=3&aqi=no&alerts=no".format(latitude, longitude)
        response = requests.get(url)
        response.raise_for_status()

        # pycharms changed line 23/24 into line 22 but I didn't understand it so stayed with my way

        # weather_data = {'forecast': {}}#
        weather_data = {}
        weather_data['forecast'] = {}
        '''
        Made a for loop with increasing index +1 so that it could show 3 days then went into forecastday directory and 
        looked for each values I needed also it didn't specify so I used the average temperature and humidity
        '''
        index = 1
        for x in response.json()['forecast']['forecastday']:
            weather_data['forecast']['day' + str(index)] = {}
            weather_data['forecast']['day' + str(index)]['date'] = x['date']
            # have to go inside of day to access temp
            weather_data['forecast']['day' + str(index)]['temperature'] = x['day']['avgtemp_c']
            # have to go inside of day to access humidity
            weather_data['forecast']['day' + str(index)]['humidity'] = x['day']['avghumidity']
            # have to go inside of day to access condition
            weather_data['forecast']['day' + str(index)]['weather_condition'] = x['day']['condition']['text']
            # have to go inside of day then calculate the heat stress index
            weather_data['forecast']['day' + str(index)]['heat_stress_index'] = hsical(x['day']['avgtemp_c'], x['day']['avghumidity'])
            # print(weather_data)
            index += 1
            # print(weather_data)
        return weather_data
except requests.exceptions.HTTPError as err:
    # response didn't register because it was inside a function
    #saw that you could do a try catch after creating a function and do something similar below so just did it with exception instead
    response = api_info()
    print('bad status code', response.status_code)
    raise err
    print('program runs normal')






