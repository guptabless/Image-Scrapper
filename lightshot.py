import requests
import random
import string

print("-------------------------------------------------------------")
print("------------------------NG-----------------------------------")
print("Usage: Python lightshot.py ")
print("-------------------------------------------------------------")

i = 0
N = 22

input_scrap = int(input("How much image you want to scrap"))

input_path = str(input("Enter the path yo want save those images"))

for i in range(0, input_scrap):

    res = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=N))

    print("The generated random string : " + str(res))
    url_host = 'https://image.prntscr.com/image/' + res + '.png'
    print(url_host)
    myfile_statuscode = requests.get(url_host).status_code
    myfile = requests.get(url_host)
    myfile_str = str(myfile)

    if(myfile_statuscode == 200):
      url = input_path + res + '.png'
      url_str = str(url)
      print("URL",url)
      open(url, 'wb').write(myfile.content)
      i = i + 1
    else:
      print("Image Not Found")



