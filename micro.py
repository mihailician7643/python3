import requests
import json

def acces(url):
    answer = requests.get(url)
    data = answer.json()
    return str(data)


def main():
    url = 'https://ionaapp.com/assignment-magic/dk/short/10'
    print(acces(url))
    

if __name__ == '__main__' :
    main()
    




    















