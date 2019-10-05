
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from requests import get
headers = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
myurl = "https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&cityName=Hyderabad"
response = get(myurl, headers=headers)
page_soup = soup(response.text, 'html.parser')
containers = page_soup.findAll('div',{'class':'flex relative clearfix m-srp-card__container'})
container = containers[0]

for container in containers:
    bhk_container = container.findAll('span',{'class':'m-srp-card__title__bhk'})
    bhk = bhk_container[0].text
    
    price_container = container. findAll('span',{'class':'m-srp-card__price'})
    price = price_container[0].text
    
    socity_container = container.findAll('a',{'class':'m-srp-card__link'})
    socity = socity_container[0].text
    
    print(bhk)
    print(price)
    print(socity)


*************************************************************************OUTPUT****************************************************************************************

3 BHK Flat

78.8 Lac
The Art

2 BHK Flat

80 Lac
Bollineni Bion

4 BHK Flat

2.69 Cr
Lansum Etania

2 BHK Flat

65.4 Lac
Civitas

3 BHK Flat

1.06 Cr
Sumadhura Acropolis

2 BHK Flat

63 Lac
Sushines La Grand

3 BHK Flat

71.2 Lac
The Art

3 BHK Flat

91.8 Lac
Patels Bright View

3 BHK Flat

3.35 Cr
Aparna One

3 BHK Flat

77.6 Lac
Visions Cascade Greens

3 BHK Flat

89 Lac
NCC Urban One

3 BHK Flat

1.28 Cr
Vishnu Vistara

3 BHK Flat

1.90 Cr
Dhivya Shree Shakthi

4 BHK Flat

1.80 Cr
Sri Ram Garden By Jains

3 BHK Flat

1.56 Cr
SMR Vinay Iconia

3 BHK Flat

1.04 Cr
Mayfair Apartments

3 BHK Flat

1.35 Cr
Aryamitra Flora

3 BHK Flat

86.2 Lac
Hallmark Vicinia

3 BHK Flat

89.6 Lac
My Space

2 BHK Flat

61.4 Lac
Vazhraa Nirmaan Pushpak

2 BHK Flat

47.8 Lac
Risinia Trendilla

3 BHK Flat

65.6 Lac
Village Pointe

2 BHK Flat

56.6 Lac
Land Mark

2 BHK Flat

46 Lac
Saket Pranamam

2 BHK Flat

33.3 Lac
Rochishmati Noveo Homes

1 BHK Flat

32.9 Lac
Provident Kenworth

3 BHK Flat

1.84 Cr
Dukes Galaxy

3 BHK Flat

82.7 Lac
Shweta Shubham

3 BHK Flat

94.1 Lac
Vertex Panache

2 BHK Flat

47.1 Lac
Prime Solitaire

3 BHK Flat

83.7 Lac
Sukhii 9
?