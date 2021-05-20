import sys

flights = []
f = sys.stdin
for _ in range(int(f.readline())):
  fr, to = f.readline().split()
  flight = {
      "to": to,
      "from": fr
  }
  flights.append(flight)

# flights = [{'to': 'ZRH', 'from': 'AMS'}, {'to': 'NYC', 'from': 'SFO'}, {'to': 'ZRH', 'from': 'NYC'}, {'to': 'ZRH', 'from': 'SFO'}, {'to': 'AMS', 'from': 'SFO'}, {'to': 'AMS', 'from': 'NYC'}, {'to': 'MUC', 'from': 'NYC'}, {'to': 'ZRH', 'from': 'MUC'}]

trips = []
for _ in range(int(f.readline())):
  fr, to = f.readline().split()
  trip = {
      "from": fr,
      "to": to
  }
  trips.append(trip)

# trips = [{'from': 'SFO', 'to': 'ZRH'}, {'from': 'ZRH', 'to': 'SFO'}, {'from': 'AMS', 'to': 'ZRH'}, {'from': 'x', 'to': 'ZRH'}, {'from': 'SFO', 'to': 'y'}, {'from': 'NYC', 'to': 'ZRH'}]
result = []
for trip in trips:
    from_matches = []
    to_matches = []
    trip_result = ''
    for flight in flights:
        if trip["from"] == flight["from"]:
            from_matches.append(flight)
        if trip["to"] == flight["to"]:
            to_matches.append(flight)
    for to in to_matches:
        for f in from_matches:
            if to["from"] == f["to"]:
                trip_result += f["to"] + " "
    result.append(trip_result)
print('\n'.join(result))
