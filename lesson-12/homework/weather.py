from bs4 import BeautifulSoup


with open('weather.html', 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')
days = {}

rows = soup.find("tbody").find_all("tr")
for row in rows:
    cols = row.find_all("td") 
    day = cols[0].text.strip()
    temperature = cols[1].text.strip()
    condition = cols[2].text.strip()
    days[day] = {"Temperature": temperature, "Condition": condition}


print(days)

max_temperature = max(int(days[day]["Temperature"].replace("°C", "")) for day in days)
print(max_temperature)

sunny_days = [day for day in days if days[day]["Condition"] == "Sunny"]
print(sunny_days)

average_temperature = sum(int(days[day]["Temperature"].replace("°C", "")) for day in days) / len(days)
print(average_temperature)