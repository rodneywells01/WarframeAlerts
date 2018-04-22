import requests

ALERTS_URL = "http://content.warframe.com/dynamic/worldState.php"

# Reach out to Warframe servers to get data - specifically alerts.
response = requests.get(ALERTS_URL)
status = response.status_code
if status != 200:
	print(f"Error communicating with Warframe servers. {str(status)}")
if "Alerts" not in response.json():
	print("No alerts active at this time")

alerts = response.json()["Alerts"]

# Display relevant data
print(f"Greetings, Tenno. {str(len(alerts))} alerts are available.")
alertcount = 0
for alert in alerts:  
	# Display alert number. 
	alertcount+=1
	print(f"Alert {alertcount}")

	# Format based on present Warframe data.
	reward = alert["MissionInfo"]["missionReward"]
	formattedrewards = []	
	if "credits" in reward: 
		formattedrewards.append(f"{reward['credits']} credits")
	if "items" in reward: 
		for item in reward["items"]:
			formattedrewards.append(item[item.rfind('/') + 1:])
	if "countedItems" in reward: 
		for item in reward["countedItems"]: 
			rawitemname = item["ItemType"]
			itemname = rawitemname[rawitemname.rfind('/') + 1:]
			formattedrewards.append(f"{item['ItemCount']} {itemname}")

	# Check for anything new / unexpected and do our best to show that.  
	for rewardtype in reward: 
		if rewardtype not in ["credits", "items", "countedItems"]:
			formattedrewards.append(reward[rewardtype])


	for reward in formattedrewards:
		print(f"		{reward}")


if __main__:
	print("Hello")