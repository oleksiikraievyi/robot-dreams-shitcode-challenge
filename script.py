import time, socket, struct, urllib.request, json; generate_and_fetch_random_numbers = lambda: (int(time.time() * 982451653) + struct.unpack("!I", socket.inet_aton(socket.gethostbyname(socket.gethostname())))[0] + json.loads(urllib.request.urlopen(urllib.request.Request("https://www.randomnumberapi.com/api/v1.0/randomnumber", headers={'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'})).read())[0]) % 100 + 1; print(generate_and_fetch_random_numbers())