import requests
r = requests.post("https://api.pushover.net/1/messages.json", data = {
  "token": "xxxxxxxxxxxxxxxxxxxxxxxx",
  "user": "xxxxxxxxxxxxxxxxxxxxxxxxx",
  "message": "Security Camera"
},
files = {
  "attachment": ("Front.jpg", open("C:\BlueIris\Alerts\Front.jpg", "rb"), "image/jpeg")
})
print(r.text)
