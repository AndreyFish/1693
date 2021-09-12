from requests import get, utils
from decimal import Decimal
from re import findall

response = utils.get_unicode_from_response(get("http://www.cbr.ru/scripts/XML_daily.asp"))


def currency_rates(code):
    content = response.split("<Valute ID=")
    for i in content:
        if code.upper() in i:
            return float(i.replace("/", "").split("<Value>")[-2].replace(",", "."))
            # return Decimal(i.replace("/", "").split("<Value")[-2].replace(",", "."))
            # return findall(r"\d*, \d*", i)[0].replace(",", "."))
print(currency_rates("usd"))
print(currency_rates("eur"))
print(currency_rates("UZS"),("Узбекский Сум"))
print(currency_rates("gbp"))