Python Web Scraper Project 

This code was written to extract apartment listings data from the apartment website. The code will extract apartment details like rooms, square footage, washer dryer, community name, price, available date. 

The extracted data would then be converted to a pandas df and then written (append) into a csv file

This csv data is extracted into an excel file for analysing the prices based on various factors. Based on the analysis we can determine if the cost makes sense to sign a new lease


Challenges:
    1. Website was dynamic and basic web scraping attempt did not work
    2. Manually running the python script was a little tedious

Solutions
    1. Used selenium python package to automate certain actions leveraging headless browsin
    2. Task Scheduler was used to automate the runs within a certain frequency