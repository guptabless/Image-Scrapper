import requests
import random
import string
import bcolors
import sys, argparse

def banner():
    print("""

            ██╗███╗░░░███╗░█████╗░░██████╗░███████╗░██████╗░█████╗░██████╗░░█████╗░██████╗░███████╗██████╗░
            ██║████╗░████║██╔══██╗██╔════╝░██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
            ██║██╔████╔██║███████║██║░░██╗░█████╗░░╚█████╗░██║░░╚═╝██████╔╝███████║██████╔╝█████╗░░██████╔╝
            ██║██║╚██╔╝██║██╔══██║██║░░╚██╗██╔══╝░░░╚═══██╗██║░░██╗██╔══██╗██╔══██║██╔═══╝░██╔══╝░░██╔══██╗
            ██║██║░╚═╝░██║██║░░██║╚██████╔╝███████╗██████╔╝╚█████╔╝██║░░██║██║░░██║██║░░░░░███████╗██║░░██║
            ╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚═════╝░╚══════╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝   
                                                                                                Code by NG          
          """)

if len(sys.argv) > 1:
    banner()
    if ((sys.argv[1] == '-c')| (sys.argv[1] == '-o')):
        try:
            input_scrap = sys.argv[2]
            input_path = sys.argv[4]

            parser = argparse.ArgumentParser()
            parser.add_argument("-c", required=True)
            parser.add_argument("-o", required=True)
            args = parser.parse_args()

            i = 0
            N = 22
            for i in range(0, int(input_scrap)):
                res = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=N))
                url_host = 'https://image.prntscr.com/image/' + res + '.png'
                print(bcolors.OKMSG + 'Generated URL :' + url_host)
                myfile_statuscode = requests.get(url_host).status_code
                myfile = requests.get(url_host)
                myfile_str = str(myfile)

            if (myfile_statuscode == 200):
                url = input_path + res + '.png'
                url_str = str(url)
                print(bcolors.OKMSG + "URL", url)
                open(url, 'wb').write(myfile.content)
                i = i + 1
            else:
                print(bcolors.ERRMSG + "No Images Found")

        except:
            print('Please enter python ImageScraper.py -c <valid domain name> -o <output location where you want to save image>')

    elif ((sys.argv[1] == '-c') | (sys.argv[1] == '--help')):
        print(bcolors.BOLD + 'usage: ImageScraper [-h] -c Count' '\n' 'OPTIONS:' '\n' '-h,--help    '
                             'show this help message and exit' '\n''-c Count,   --count Count' '\n' '-o output    Output where you want to Save image')
    elif (((sys.argv[1] != '-c') | (sys.argv[1] != '-o'))):
        print('Please enter -c <Count> -o <output location>')
else:
    banner()
    print(bcolors.ERR + 'Please select atleast 1 option from (-c,-o) or -h, with valid count and location')




