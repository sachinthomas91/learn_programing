# Python Web Scraper Project 

## Project Overview
This code was written to extract apartment listings data from the apartment website. The code will extract apartment details like rooms, square footage, price, available date. 

The extracted data would then be converted to a pandas df and then written (append) into a csv file. Its main purpose is to track and monitor the prices of leases, aiding in the analysis of market trends and helping users make informed decisions regarding apartment rentals.. Based on the analysis we can determine if the cost makes sense to sign a new lease


Challenges:
   1. Website was dynamic and basic web scraping attempt did not work
   2. Manually running the python script was a little tedious

Solutions
   1. Used selenium python package to automate certain actions leveraging headless browsin
   2. Task Scheduler was used to automate the runs within a certain frequency

## Features
- Scrapes apartment listings, including prices, square footage, number of bedrooms, and availability.
- Saves data in a structured format (CSV) for easy analysis.
- Schedule regular scrapes to monitor price changes over time using windows task scheduler

## Technologies Used
- Python 3
- Python Selenium package
- Python Chrome Driver Manager
- Pandas for data manipulation and export

## Note
This project is intended for educational purposes and personal use. Please respect the website's terms of use and robots.txt file to avoid any legal issues. Always ensure you have permission to scrape the website.

Happy scraping!
