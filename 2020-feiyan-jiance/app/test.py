import requests

def get_data():
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
    r = requests.get(url).text
    print(r)
    type(r)

if __name__ == "__main__":
    get_data()