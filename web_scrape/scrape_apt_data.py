#######################################################
## Import Packages
#######################################################
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import timezone
import datetime
import pandas as pd
import time
import os


#######################################################
## Headless Browser Web Scraper for Apartment Community
#######################################################

## Declare Variables
# Website url hidden for privacy and security reasons
url = "<website-url>"
page = str()
totalpages = int()

# Browser Options 
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument('--incognito')

## Website Get Request using Selenium
with webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options) as driver: 
	driver.get(url)

	## Print URL, Title
	print("Page URL:", driver.current_url) 
	print("Page Title:", driver.title)
	print("\nExtracting.........")
	
	## Find "Load More" button object to scroll through multiple apartment listings
	loadmore = driver.find_element(By.XPATH, "//button[@class='button-primary load-more']")
	# print(loadmore.text)

	## Load all available pages
	while True:
		try:
			loadmore.click()
			time.sleep(5)
		except Exception as e:
			print(e)
			break
	
	print(f"Load More Clicks Complete")

	## Extract all listed Apartments into a string
	parent_elements = driver.find_elements(By.XPATH, "//div[@class='home-units']") 
	for parent_element in parent_elements: 
		# print(parent_element.text)
		page = page + '\n' + parent_element.text
    
print("Extraction Complete")


#######################################################
## Clean scraped apartment data
#######################################################

# Replace non-relevant lines from string object. Replace 'Learn More' with empty line
page = page.replace('Learn More', '')

# Remove Empty Lines that were replaced in previous step
page = "".join([s for s in page.strip().splitlines(True) if s.strip("\r\n").strip()])

# Write cleaned string to a file
with open("<text_file_location>", "w") as text_file:
    print(f"{page}", file=text_file)


#######################################################
## Convert Cleaned Data to List
#######################################################

# Convert lines in the file to list
df = open('<text_file_location>', "r")
lines = df.readlines()
df.close()

# Remove /n at the end of each item
for index, line in enumerate(lines):
      lines[index] = line.strip()
      
# Print total items in the list
# print(f"Total Items: {len(lines)}")
# print("Note: Total Items should be a multiple of 5 ideally")


#######################################################
## Convert the list to a DF for Analysis
#######################################################

# Variable to index the DF rows
ind = 0
dt = datetime.datetime.now(timezone.utc)

# Define DataFrame
df_result = pd.DataFrame(columns=('property', 'rooms', 'sqft_cost', 'availableon', 'unit', 'datarefutc'))

# Write data into the DF from the list object Lines
for i in range(0, len(lines), 5):
    df_result.loc[ind] = [lines[i], lines[i+1], lines[i+2], lines[i+3], lines[i+4], dt]
    ind+=1

# print(df_result)


#######################################################
## Data Cleaning Operations #1
#######################################################

# Bed Bath as separate columns instead of one
new_lst = df_result["rooms"].tolist()   
# print(f"Original BedBath {new_lst} \n")

# Extract Bedroom number from the column
lst_1 = [x.split(",")[0].replace(" bedroom", "").replace("s", "") for x in new_lst]
lst_1 = [int(x) for x in lst_1]
#print(lst_1)

# Extract Bathroom number from the column
lst_2 = [x.split(",")[1].replace(" bathroom", "").replace("s", "").replace(" ", "") for x in new_lst]
lst_2 = [int(x) for x in lst_2]
#print(lst_2)

# Add new columns to the DF. Separate columns for Bed and Bath
df_result["bed"]=lst_1
df_result["bath"]=lst_2
# print(df_result)


#######################################################
## Data Cleaning Operations #2
#######################################################

# Bed Bath as separate columns instead of one
new_lst = df_result["sqft_cost"].tolist()   
#print(f"\nOriginal SqFt_Cost {new_lst} \n")

lst_1 = [x.split("•")[0].replace(" sq. ft. ", "") for x in new_lst]
lst_1 = [int(x) for x in lst_1]
#print(lst_1)

lst_2 = [x.split("•")[1].replace(" / month", "").replace(" $", "").replace(",","") for x in new_lst]
lst_2 = [int(x) for x in lst_2]
#print(lst_2)

# Add new columns to the DF. Separate columns for SquareFeet and Cost
df_result["sqft"]=lst_1
df_result["cost"]=lst_2
#print(df_result)


#######################################################
## Data Cleaning Operations #3
#######################################################

# Remove extra verbiage from AvailableOn column
new_lst = df_result["availableon"].tolist()   
#print(f"\nOriginal AvailableOn {new_lst} \n")
lst_1 = [x.replace("Available on: ", "").replace("Available", f"9/25/1991") for x in new_lst]
#print(lst_1)

# Remove extra verbiage from Unit column
new_lst = df_result["unit"].tolist()   
#print(f"\nOriginal Unit {new_lst} \n")
lst_2 = [x.replace("Unit ", "") for x in new_lst]
#print(lst_2)

# Assign the cleaned values to the existing column
df_result["availableon"]=lst_1
df_result["unit"]=lst_2
#print(df_result)


#######################################################
## Final DF Cleaning
#######################################################

## Remove combined value columns
df_result.drop(columns=['rooms', 'sqft_cost'], inplace=True)

# ReOrder Columns
df_result = df_result[['property', 'unit', 'sqft', 'bed', 'bath', 'cost', 'availableon', 'datarefutc']]
# print(df_result)


#######################################################
## Dataframe to CSV - Write/Append
#######################################################

# Save the dataframe to a CSV file
# If file does not exist write header else no header 
if not os.path.isfile('<final_csv_file>'):
    df_result.to_csv('<final_csv_file>', mode='w', index=False, header=True)
    print('No such file. Create new file')
else: # else it exists so append without writing the header
    df_result.to_csv('<final_csv_file>', mode='a', index=False, header=False)
    print("File exists. Append to Existing")
   