# Covid 19 API

#### Hosted at http://awhite97.pythonanywhere.com/

#### Description: A web application which displays COVID-19 data from an API.


I created this web application as my final project for CS50. I decided I wanted to gain experience using API's whilst developing something relevant.

I used a Corona Virus api to get all of the data displayed. The API I used is found at https://covid19api.com/

The website is a flask application and uses Jinja2 templating.
Each html page and the layout is saved in /templates. Javascript file and CSS file are saved in /static.


## application.py

application.py is the server side program that is used to make calls to the API and generate the web pages.


## /static

js.js - This is the file where I put some javascript functions that were used by multiple pages.

styles.css - This is the ccs file I used for the templates. I did not do much of my own styling as I thought it would be easier to just use bootstrap

## /templates

There are 3 pages to the web application. stats, country and about all of which make use of layout.html as the template.

layout.html - This is what I used for the JINJA2 template. It contains all of the HTML shared by the pages (Nav, footer, etc).

Stats (/templates/stats.html) - This is the main page, it displays the data in a Geochart. It uses the country code from the API to add the data to the correct country.
The colour of the country is dependent on how many new cases were recorded on the previous day. I used a scale of 0 - 5000 (or more) ranging from green to red.
If a country is white this means that no data for that country code was provided by the API.
If you hover over or click on any of the countries a tool tip will be displayed showing the total cases,deaths and recoveries for that country. It also shows how much that increased by in the previous day.

Country (/templates/country.html) - This page displays the daily total stats from the last 100 days for a selected country (Default is the United Kingdom).
I initially wanted to show the daily increase however the only information available from the API was the daily total.
I could have used the daily total from the previous day to calculate the increase however I found that some days the data wasn't updated which caused problems with the graph.
I added a radio button to allow the user to switch between total cases and total deaths. I contemplated displaying both simultaneously however there is significantly more cases than deaths and
therefore the death data was not easily readable.
Some countries don't have any information available while others only have part information available (Normally cases and deaths but not recovered).

About (/templates/about.html) - This is a small page to give some information about the application and why I chose this project.


## Technologies used:
- Python
- HTML
- Javascript
- CSS
- JSON
- Google charts
- JINJA2
- Flask
- Bootstrap
