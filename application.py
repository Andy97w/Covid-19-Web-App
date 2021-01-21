#!/usr/bin/python
# -*- coding: utf-8 -*-

"""application.py - Makes use of a Covid 19 API to display information about Covid 19"""

__author__ = 'Andrew White'

import os
import requests
from flask import Flask, render_template, jsonify, request
import datetime

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def stats():

    # Calls getSummary() to get data from API (summary)
    summary = getSummary()

    #formats the global stats to a more readable format
    summary['Global']['TotalConfirmed'] = '{:,}'.format(summary['Global']['TotalConfirmed'])
    summary['Global']['TotalDeaths'] = '{:,}'.format(summary['Global']['TotalDeaths'])
    summary['Global']['TotalRecovered'] = '{:,}'.format(summary['Global']['TotalRecovered'])

    return render_template('stats.html', world=summary['Global'], countries=summary['Countries'])


# Country is an optional argument, if nothing is given United Kingdom will be the default
@app.route('/country', methods=['GET', 'POST'])
def index(country='united-kingdom'):

    # Get the selected country
    if request.method == 'POST':
        country = request.form.get('countries')

    # Calls getCountries() to get data from API (list of all countries)
    countries = getCountries()

    # Calls getCountryStats() with the arguement country to get data from API (100 day stats for selected country )
    stats = getCountryStats(country)

    return render_template('country.html', countries=countries, country=country, stats=stats)


@app.route('/about')
def about():

    return render_template('about.html')

# Request summary from API
def getSummary():

    try:
        response = requests.get('https://api.covid19api.com/summary')
        response.raise_for_status()
    except requests.RequestException:
        return None

   # Return data in JSON format
    return response.json()


# Request list of countries from API
def getCountries():

    try:
        response = requests.get('https://api.covid19api.com/countries')
        response.raise_for_status()
    except requests.RequestException:
        return None

   # Return data in JSON format
    return response.json()


# Request stats from the last 100 days for a specifc country from API
def getCountryStats(country):

    # Calculates yesterdays date to use as the end point and (yesterdays date - 100 days) as the start point. Formats the date to match API requirements
    start = (datetime.datetime.today()
             - datetime.timedelta(days=100)).strftime('%Y-%m-%d')
    end = (datetime.datetime.today()
           - datetime.timedelta(days=1)).strftime('%Y-%m-%d')

    url = 'https://api.covid19api.com/country/' + country + '?from=' + start + '&to=' + end

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return None

   # Return data in JSON format
    return response.json()
