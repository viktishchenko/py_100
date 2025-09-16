datas = [{'city': 'Paris', 'iataCode': 'PAR', 'prices': 54, 'id': 2}, {'city': 'San Francisco', 'iataCode': 'SFO', 'prices': 260, 'id': 9}, {'city': 'Dublin', 'iataCode': 'DBN', 'prices': 378, 'id': 10}]

# {'price': [{'city': 'New York', 'iataCode': 'NYC', 'prices': 240, 'id': 2}, {'city': 'San Francisco', 'iataCode': 'SFO', 'prices': 260, 'id': 3}, {'city': 'Dublin', 'iataCode': 'DBN', 'prices': 378, 'id': 4}]}

# datas = [{'city': 'Paris', 'iataCode': 'PAR', 'prices': 54, 'id': 2}, {'city': 'Frankfurt', 'iataCode': '', 'prices': 42, 'id': 3}, {'city': 'Tokyo', 'iataCode': '', 'prices': 485, 'id': 4}, {'city': 'Hong Kong', 'iataCode': '', 'prices': 551, 'id': 5}, {'city': 'Istanbul', 'iataCode': '', 'prices': 95, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': '', 'prices': 414, 'id': 7}, {'city': 'New York', 'iataCode': '', 'prices': 240, 'id': 8}, {'city': 'San Francisco', 'iataCode': '', 'prices': 260, 'id': 9}, {'city': 'Dublin', 'iataCode': '', 'prices': 378, 'id': 10}]

for data in datas:
  print(f'data>>> {data}')
  if data["iataCode"] == '':
    print('ahlo')