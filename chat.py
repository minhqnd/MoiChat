import requests
import json

url = "https://api.simsimi.vn/v1/simtalk"

def send(message):
  payload = {
      "text": message,
      "lc": 'vn'
  }
  headers = {
      'Content-Type': 'application/x-www-form-urlencoded'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  if response.status_code == 200:
      data = json.loads(response.text)
      message = data.get("message")
      print(message)
      return message
  else:
      print("Không thể lấy dữ liệu từ API")
      return "Không thể lấy dữ liệu từ API"