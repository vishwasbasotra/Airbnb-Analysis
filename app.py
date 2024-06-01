import streamlit as st
import json
from googleapiclient.discovery import build
import pandas as pd
from pymongo import MongoClient
from pymongo.mongo_client import MongoClient
import sqlalchemy as sa
import mysql.connector
from mysql.connector import Error
from streamlit_option_menu import option_menu
import plotly.express as px

f = open('Data/sample_airbnb.json')
airbnbData = json.load(f)

# setting up homepage
st.set_page_config(page_title="AirBNB Analysis", page_icon=':bar_chart:', layout='wide')

# header section
st.title(":red[AirBNB Analysis:]")
vishwas = MongoClient("mongodb+srv://basotra97:aSTR9c!PQ8Fs8o77@cluster0.nvekqq7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = vishwas['AirbnbDB']
main_collection = db.Airbnb_collection

if list(main_collection.find()) == []:
    for i in airbnbData:
        print(i)
        main_collection.insert_one(i)
    st.success('Database Collection uploaded')
    st.balloons()

