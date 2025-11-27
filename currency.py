import resources
import requests
from bs4 import BeautifulSoup

def currency_code(country: str) -> str:
    request = requests.get(f"https://taxsummaries.pwc.com/glossary/currency-codes/")
    bs4Object = BeautifulSoup(request.content, "html.parser")

    listOfCells = bs4Object.find_all("td")
    for cell in listOfCells:
        if cell.text in country:
            return listOfCells[listOfCells.index(cell) + 1].text

@resources.cache
def currency_conversion(country1: str,
                        country2: str,
                        value: int) -> str:
    country1 = currency_code(country1)
    country2 = currency_code(country2)
    request = requests.get(f"https://www.xe.com/currencyconverter/convert/?Amount={value}&From={country1}&To={country2}")
    print(f"https://www.xe.com/currencyconverter/convert/?Amount={value}&From={country1}&To={country2}")
    bs4Object = BeautifulSoup(request.content, "html.parser")

    conversion = (bs4Object.find_all("span", attrs={"class": "amount-input flex items-center whitespace-nowrap"})[1].text + 
        bs4Object.find_all("input", attrs={"class": "m-0 box-content self-stretch border-none bg-transparent p-0 focus:shadow-none focus:outline-none"})[1].get("value"))
    return " " + conversion + " "

countries = [
    "Albania", "Algeria", "Angola", "Argentina",
    "Armenia", "Australia", "Austria", "Azerbaijan",
    "Bahamas", "Bahrain", "Bangladesh", "Barbados",
    "Belarus", "Belgium", "Bermuda", "Bolivia",
    "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei Darussalam",
    "Bulgaria", "Cabo Verde", "Cambodia", "Cameroon, Republic of",
    "Canada", "Cayman Islands", "Chad", "Chile",
    "China, People’s Republic of", "Colombia", "Congo, Democratic Republic of the", "Congo, Republic of",
    "Costa Rica", "Croatia", "Cyprus", "Czech Republic",
    "Denmark", "Dominican Republic", "Ecuador", "Egypt",
    "El Salvador", "Equatorial Guinea", "Estonia", "Ethiopia",
    "Fiji", "Finland", "France", "Gabon",
    "Georgia", "Germany", "Ghana", "Gibraltar",
    "Greece", "Greenland", "Guatemala", "Guernsey, Channel Islands",
    "Guyana", "Honduras", "Hong Kong SAR", "Hungary",
    "Iceland", "India", "Indonesia", "Iraq",
    "Ireland", "Isle of Man", "Israel", "Italy",
    "Ivory Coast (Cote d'Ivoire)", "Jamaica", "Japan", "Jersey, Channel Islands",
    "Jordan", "Kazakhstan", "Kenya", "Korea, Republic of",
    "Kosovo", "Kuwait", "Kyrgyzstan", "Lao PDR",
    "Latvia", "Lebanon", "Liberia, Republic of", "Libya",
    "Liechtenstein", "Lithuania", "Luxembourg", "Macau SAR",
    "Madagascar", "Malawi", "Malaysia", "Maldives, Republic of",
    "Malta", "Mauritania", "Mauritius", "Mexico",
    "Moldova", "Mongolia", "Montenegro", "Morocco",
    "Mozambique", "Myanmar", "Namibia, Republic of", "Netherlands",
    "New Caledonia", "New Zealand", "Nicaragua", "Nigeria",
    "North Macedonia", "Norway", "Oman", "Pakistan",
    "Palestinian territories", "Panama", "Papua New Guinea", "Paraguay",
    "Peru", "Philippines", "Poland", "Portugal",
    "Puerto Rico", "Qatar", "Romania", "Russian Federation",
    "Rwanda", "Saint Lucia", "Saudi Arabia", "Senegal",
    "Serbia", "Singapore", "Slovak Republic", "Slovenia",
    "South Africa", "Spain", "Sri Lanka", "Swaziland",
    "Sweden", "Switzerland", "Taiwan", "Tajikistan",
    "Tanzania", "Thailand", "Timor-Leste", "Trinidad And Tobago",
    "Tunisia", "Turkey", "Turkmenistan", "Uganda",
    "Ukraine", "United Arab Emirates", "United Kingdom", "United States",
    "Uruguay", "Uzbekistan, Republic of", "Venezuela", "Vietnam",
    "Zambia", "Zimbabwe"
]
