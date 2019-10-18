from faker import Faker
from bs4 import BeautifulSoup as bs
import random
from random import sample
event_source_link = 'https://www.classicalevents.co.uk/'
import requests
import json
page = requests.get(event_source_link)
fake = Faker()
import csv
import datetime
def get_random_date(year):

    # try to get a date
    try:
        return datetime.datetime.strptime('{} {}'.format(random.randint(1, 366), year), '%j %Y')

    # if the value happens to be in the leap year range, try again
    except ValueError:
        get_random_date(year)

user_names = [fake.name() for _ in range(0,100)] #point
user_addresses = [fake.address() for _ in range(0,100)] #point
user_ages = [random.randint(18, 80) for _ in range(0,100)] #point
concert_types = ['Jazz', 'Musical', 'Opera', 'Classical Rock', 'Violin', 'Orchestra', 'Piano', 'Folk', 'Country'] # point
soup = bs(page.content, 'html.parser')
eles = (soup.find_all(class_="title"))
concert_name_list= ([e.h2.a.span.text for e in eles]) # point
performers = [fake.name() for _ in range(len(concert_name_list))] # point
email = [] # point
for name in user_names:
    split_name = name.split(' ')
    user_email = split_name[0]+split_name[1]+'@gmail.com'
    email.append(user_email)

registered_date = [str(get_random_date(random.randint(2011, 2019))) for _ in range(0,100)]
registered_date = [date.split(' ')[0] for date in registered_date] #point

user_revenue_as_client = [random.randint(25000,100000) for _ in range(0,100)] #point

concerts_attended = [sample(concert_name_list, random.randint(1,10)) for _ in range(0,100)] #point

user_revenue_as_donor = [random.randint(0,50000) for _ in range(0,100)] #point

# with open('data_clients11.csv', 'w+') as csvfile:
#     filewriter = csv.writer(csvfile, delimiter=',')
#     filewriter.writerow(['Name', 'Email', 'Address', 'Age', 'DateRegistered', 'RevenueAsClient', 'ConcertsAttended', 'RevenueAsDonor'])
#     for i in range(0,100):
#         print(i)
#         filewriter.writerow([user_names[i], email[i], user_addresses[i], user_ages[i], registered_date[i], user_revenue_as_client[i], concerts_attended[i], user_revenue_as_donor[i]])



user = {}
for i in range(0, 100):
    user[user_names[i]] = {}
    user[user_names[i]]['Name'] = user_names[i]
    user[user_names[i]]['Score'] = int(user_revenue_as_donor[i]/(user_revenue_as_donor[i]+user_revenue_as_client[i])*100)
    print(int(user_revenue_as_donor[i]/(user_revenue_as_donor[i]+user_revenue_as_client[i])*100))
    user[user_names[i]]['Email'] = email[i]
    user[user_names[i]]['Address'] = user_addresses[i]
    user[user_names[i]]['Age'] = user_ages[i]
    user[user_names[i]]['DateRegistered'] = registered_date[i]
    user[user_names[i]]['RevenueAsClient'] = user_revenue_as_client[i]
    user[user_names[i]]['ConcertsAttended'] = concerts_attended[i]
    user[user_names[i]]['RevenueAsDonor'] = user_revenue_as_donor[i]

# user_json = json.dumps(user)

print(concert_name_list)

with open('final_user_data_team_6.json', 'w+') as json_file:
  json.dump(user, json_file)

# print(user_json)

def get_concert_list():
    event_source_link = 'https://www.classicalevents.co.uk/'
    page = requests.get(event_source_link)
    soup = bs(page.content, 'html.parser')
    eles = (soup.find_all(class_="title"))
    concert_name_list = ([e.h2.a.span.text for e in eles])  # point
    return concert_name_list