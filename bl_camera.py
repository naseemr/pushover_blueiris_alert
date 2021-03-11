import requests
r = requests.post("https://api.pushover.net/1/messages.json", data = {
  "token": "xxxxxxxxxxxxxxxxxxxxxxxx",
  "user": "xxxxxxxxxxxxxxxxxxxxxxxxx",
  "message": "Security Camera"
},
files = {
  "attachment": ("bl_camera_name.jpg", open("C:\BlueIris\Alerts\bl_camera_name.jpg", "rb"), "image/jpeg")
})
print(r.text)
