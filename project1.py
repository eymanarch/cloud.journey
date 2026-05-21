import requests
import json

response=requests.get("https://api.github.com/users/eymanarch")
data=response.json()

profile={
	"login": data["login"],
	"public_repos": data["public_repos"],
	"bio" : data["bio"]
}

try:
	with open("profile.json", "w") as f:
		json.dump(profile,f, indent=4)
	print("saved")
except:
	print("it is not accessible")
