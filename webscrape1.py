#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 11:17:51 2022

@author: ranishah
"""

import requests 
from bs4 import BeautifulSoup

#request from job site
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

#use beautiful soup as our parser 
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
job_elements = results.find_all("div", class_="card-content")

#next few lines were used earlier when testing things out, commented out now, ignore
#print(page.text)
#print(results.prettify())
#print(job_elements)
# for job_element in job_elements:
#     title_element = job_element.find("h2", class_="title")
#     company_element = job_element.find("h3", class_="company")
#     location_element = job_element.find("p", class_="location")
#     print(title_element.text)
#     print(company_element.text)
#     print(location_element.text)
#     print()


#here we will focus on user input
#get the input
keyword = input('Enter a keyword to search for in job title: ')
print(keyword)

#find jobs that include user input
key_jobs = results.find_all(
    "h2", string=lambda text: keyword in text.lower()
)
num_jobs = len(key_jobs)
print('There are %s %s jobs with %s in them \n' %(num_jobs, keyword, keyword))

print('Here they are: ')

#show the jobs that have the keyword in a formatted manner
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    #if it has it, then print. otherwise don't
    if ((title_element.text.lower()).find(keyword)) != -1:
        #stuff
        print(title_element.text)
        print(company_element.text)
        print(location_element.text)
        print()
    