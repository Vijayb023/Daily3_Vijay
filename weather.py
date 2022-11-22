import streamlit as st
import requests
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import time
from PIL import Image


api_key = [ "b3c7849489d93147a21f33fc9e1171ff" ]

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
url_1 = 'https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={}&lon={}&dt={}&appid={}'


def getweather(city: object)  -> object:
    result = requests.get(url.format(city, api_key))
    if result :
        json = result.json ( )
        st.write(json)
        country = json [ 'sys' ] [ 'country' ]
        temp = json [ 'main' ] [ 'temp' ] - 273.15
        temp_feels = json [ 'main' ] [ 'feels_like' ] - 273.15
        humid = json [ 'main' ] [ 'humidity' ] - 273.15
        icon = json [ 'weather' ] [ 0 ] [ 'icon' ]
        des = json [ 'weather' ] [ 0 ] [ 'description' ]
        res = [ country, round ( temp, 1 ), round ( temp_feels, 1 ),
                humid, icon, des ]

        return res, json
    else :
        print ( "error in search !" )





st.header ( 'Streamlit Weather Report' )




col1, col2 = st.columns ( 2 )

with col1 :
        city_name = st.text_input("Enter city")
        res = getweather ( city_name )
        json = res
        st.success("Weather "+ str(getweather ( city_name )))
        #st.write(x)




