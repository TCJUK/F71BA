import numpy as np
import random
import csv
import string


users = []

def get_campaign():
    return np.random.choice(
                ["push","sms","email","ppc"],
                p=[0.25, 0.25, 0.25,0.25]
                ) 


def get_product():
    return np.random.choice(
                        ["Beauty", "Clothing", "Electronics", "Sport", "Home"],
                        p=[0.2, 0.2, 0.2, 0.2, 0.2]
                    )

def get_campaigns(success):
    campaigns = ["","","",""]
    for i in range(4):
        if i+1 == success[2]:
            campaigns[i]=success[0]
        else:
            this_camp=get_campaign()
            while this_camp == success[0]:
                this_camp=get_campaign()
            campaigns[i]=this_camp
    return campaigns
    



def get_location():
    return np.random.choice(
                ["Online","London","Manchester","Glasgow"],
                p=[0.25, 0.25, 0.25, 0.25]
                )

def generate_random_string(length=1):
    characters = string.ascii_lowercase + string.digits  # a-z, A-Z, 0-9
    return ''.join(random.choices(characters, k=length))


men=[get_campaign(),get_product(),random.randint(2,3)]
women=[get_campaign(),get_product(),random.randint(2,3)]
campaigns=get_campaigns(women)

grow_decline=[get_product(),get_product()]
while grow_decline[0] == grow_decline[1]:
    grow_decline[1] = get_product()

locations=[get_location(),get_location()]
while locations[0] == locations[1]:
    locations[1] = get_location()

file_suffix_m=campaigns[0][-1]+campaigns[1][-1]+campaigns[2][-1]+campaigns[3][-1]
file_suffix_w=women[0][-1]+women[1][-1]+str(women[2])
file_suffix_g=grow_decline[0][-1]+grow_decline[1][-1]
file_suffix_l=locations[0][-1]+locations[1][-1]
file_suffix=generate_random_string()+file_suffix_m+generate_random_string()+file_suffix_w+generate_random_string()+file_suffix_g+generate_random_string()+file_suffix_l+generate_random_string()


for i in range(1277, 2001):
    user_id = f"C{i}"
    gender = random.choice(["male", "female"])
    age = random.randint(16, 66)
    location = np.random.choice(
        ["Online", "London", "Manchester", "Glasgow"],
        p=[0.65, 0.2, 0.1, 0.05]
    )
    category = np.random.choice(
        ["N/A", "Bronze", "Silver", "Gold"],
        p=[0.6, 0.25, 0.1, 0.05]
    )
    users.append({
        "cid": user_id,
        "gender": gender,
        "age": age,
        "location": location,
        "category": category
    })

# Write the data to a CSV file
csv_file_path = "/home/tcj1/Teaching/F71BA/Code/users_{0}.csv".format(file_suffix)
with open(csv_file_path, mode="w", newline="") as csv_file:
    fieldnames = ["cid", "gender", "age", "location", "category"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(users)

print(f"Data written to {csv_file_path}")



def get_user_info(users):
    customer = np.random.randint(0, 724)
    return users[customer] #if 0 <= customer < len(users) else None


marketing=[]
sales=[]
for week in range(1, 5):
    for sale in range(900):
        user = get_user_info(users)
        #print(user)
        Marketing=False
        day=random.randint(1,7)
        if user['category'] == "N/A":
            no_items=np.random.choice(
                [1,2,3],
                p=[0.65, 0.25, 0.1]
                )   
        elif user['category'] == "Bronze":
            no_items=np.random.choice(
                [1,2,3],
                p=[0.45, 0.4, 0.15]
                )
        elif user['category'] == "Silver":
            no_items=np.random.choice(
                [1,2,3,4],
                p=[0.25, 0.3, 0.25, 0.2]
                ) 
        elif user['category'] == "Gold":
            no_items=np.random.choice(
                [1,2,3,4],
                p=[0.15, 0.35, 0.3, 0.2]
                )       

        for i in range(no_items):    

            loc=user['location']
            if user['gender'] == "female":
                if user['age'] < 20:
                    item = np.random.choice(
                        ["Beauty", "Clothing", "Electronics", "Sport", "Home"],
                        p=[0.4, 0.3, 0.05, 0.15, 0.1]
                    )
                elif user['age'] < 30:
                    item = np.random.choice(
                        ["Beauty", "Clothing", "Electronics", "Sport", "Home"],
                        p=[0.3, 0.4, 0.05, 0.05, 0.2]
                    )
                elif user['age'] < 40:
                    item = np.random.choice(
                        ["Beauty", "Clothing", "Electronics", "Sport", "Home"],
                        p=[0.3, 0.3, 0.05, 0.05, 0.3]
                    )
                elif user['age'] < 60:
                    item = np.random.choice(
                        ["Beauty", "Clothing", "Electronics", "Sport", "Home"],
                        p=[0.25, 0.3, 0.05, 0.05, 0.35]
                    )
                else:
                    item = np.random.choice(
                        ["Beauty", "Clothing", "Electronics", "Sport", "Home"],
                        p=[0.25, 0.3, 0.05, 0.05, 0.35]
                    )
            else:
                if user['age'] < 20:
                    item = np.random.choice(
                        ["Beauty", "Clothing", "Electronics", "Sport", "Home"],
                        p=[0.2, 0.4, 0.15, 0.25, 0.00]
                    )
                elif user['age'] < 30:
                    item = np.random.choice(
                        ["Beauty", "Clothing", "Electronics", "Sport", "Home"],
                        p=[0.3, 0.4, 0.15, 0.1, 0.05]
                    )
                elif user['age'] < 40:
                    item = np.random.choice(
                        ["Beauty", "Clothing", "Electronics", "Sport", "Home"],
                        p=[0.1, 0.3, 0.2, 0.1, 0.3]
                    )
                elif user['age'] < 60:
                    item = np.random.choice(
                        ["Beauty", "Clothing", "Electronics", "Sport", "Home"],
                        p=[0.05, 0.2, 0.25, 0.1, 0.4]
                    )
                else:
                    item = np.random.choice(
                        ["Beauty", "Clothing", "Electronics", "Sport", "Home"],
                        p=[0.0, 0.2, 0.3, 0.1, 0.4]
                    )
                
            if week ==2 and item == grow_decline[0] and random.randint(0,3)>2:
                item = grow_decline[1]          
            if week ==3 and item == grow_decline[0] and random.randint(0,3)>=2:
                item = grow_decline[1]          
            if week ==4 and item == grow_decline[0] and random.randint(0,3)>=1:
                item = grow_decline[1]

            if week==women[2] and user['location'] == "Online" and item != women[1] and random.randint(0,3)>=1:
                item = women[1]
                Marketing=True
                marketing.append({
                "campaign": women[0],
                "date": "202502{0:02d}".format((week-1)*7+day),
                "cid": user['cid'],
                "open": 1,
                "ct": 1,
                "sale": 1
                })
            elif user['location'] == "Online" and random.randint(0,3)>=2:
                Marketing=True
                marketing.append({
                "campaign": campaigns[week-1],
                "date": "202502{0:02d}".format((week-1)*7+day),
                "cid": user['cid'],
                "open": 1,
                "ct": 1,
                "sale": 1
                })


            if week>=2 and user['location'] == locations[0]  and random.randint(0,3)>=2:
                loc = locations[1]
            if week>=3 and user['location'] == locations[0]  and random.randint(0,3)>=1:
                loc = locations[1]

            rnd=np.random.binomial(n=40, p=0.25)/10.
            if item == "Beauty":
                value = rnd*20-0.01
            elif item == "Clothing":                
                value = rnd*50-0.01
            elif item == "Electronics":
                value = rnd*50-0.01
            elif item == "Sport":
                value = rnd*40-0.01
            else:
                value = rnd*60-0.01

            sales.append({
                "date": "202502{0:02d}".format((week-1)*7+day),
                "category": item,
                "value": value,
                "location": loc,
                "cid": user['cid']
            })







# Write the data to a CSV file
csv_file_path = "/home/tcj1/Teaching/F71BA/Code/sales_{0}.csv".format(file_suffix)
with open(csv_file_path, mode="w", newline="") as csv_file:
    fieldnames = ["date", "category", "value", "location", "cid"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(sales)
print(f"Data written to {csv_file_path}")

def threshold_check(c):
    u = random.uniform(0, 1)
    return int(u > 1.-c)

for i in range(10000):

    user_id = "C{0:04d}".format(random.randint(1277, 2000))
    week=random.randint(1,4)
    day=random.randint(1,7)



    camp=campaigns[week-1]
    if camp=="push":
        crit=[0.7,0.3,0.1]
    elif camp=="sms":
        crit=[0.3,0.5,0.05]
    elif camp=="email": 
        crit=[0.4,0.6,0.1]
    else:
        crit=[0.2,0.4,0.01]

    sale=0
    #o=threshold_check(crit[0])
    o=1
    if o==1:    
        ct=threshold_check(crit[1])
    else:
        ct=0
        sale=0  
    
    marketing.append({
                "campaign": camp,
                "date": "202502{0:02d}".format((week-1)*7+day),
                "cid": user_id,
                "open": o,
                "ct": ct,
                "sale": 0
            })
    
# Write the data to a CSV file
csv_file_path = "/home/tcj1/Teaching/F71BA/Code/marketing_{0}.csv".format(file_suffix)
with open(csv_file_path, mode="w", newline="") as csv_file:
    fieldnames = ["campaign", "date", "cid", "open", "ct", "sale"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(sorted(marketing, key=lambda x: x['date']))
print(f"Data written to {csv_file_path}")