import requests

url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/recent"

headers = {
        'x-rapidapi-key': '8cf6521a06msh2e1499b6f52c2b6p19f978jsn71b595fbe7fa',
		'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com'
}
response = requests.get(url, headers=headers)
print(response.json())
  
