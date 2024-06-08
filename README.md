# Airbnb Analysis

## Introduction 

* This project aims to analyze Airbnb data using MongoDB Atlas, perform data cleaning and preparation, develop interactive geospatial visualizations, and create dynamic plots to gain insights into pricing variations, availability patterns, and location-based trends.

![Intro GUI](https://github.com/vishwasbasotra/Airbnb-Analysis/blob/main/demo.png)

## Airbnb Dashboard Link: https://public.tableau.com/app/profile/vishwas.basotra/viz/AirbnbAnalysis_17178195358750/Dashboard1?publish=yes

## Project Overview
* BizCardX is a user-friendly tool for extracting information from business cards. The tool uses OCR technology to recognize text on business cards and extracts the data into an SQL database after classification using regular expressions. Users can access the extracted information using a GUI built using Streamlit. The BizCardX application is a simple and intuitive user interface that guides users through uploading the business card image and extracting its information. The extracted information would be displayed clean and organised, and users could easily add it to the database with a click of a button. Further, the data stored in the database can be easily read, updated and deleted by the user as per the requirement.

## Developer Guide 

### 1. Tools install

* VS Code.
* Jupyter notebook.
* Python 3.11.0 or higher.
* MySQL
* Git

### 2. Requirement Libraries to Install

* pip install pandas numpy os json requests subprocess mysql.connector sqlalchemy pymysql streamlit plotly.express

### 3. Import Libraries
* import pandas as pd
* import easyocr
* import mysql.connector
* import sqlalchemy
* from sqlalchemy import create_engine

**Dashboard libraries**
* import streamlit as st
* import plotly.express as px
