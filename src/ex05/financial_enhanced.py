#!/usr/bin/env python3
import sys
import httpx
from bs4 import BeautifulSoup


def get_fin_data(ticker, name_row):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    url = f"https://finance.yahoo.com/quote/{ticker}/financials/?p={ticker.lower()}"
    response = httpx.get(url, headers=headers)
    if  response.status_code == 302:
        raise Exception(f"Wrong Ticker: {ticker}")
    elif response.status_code != 200:
        raise Exception(
            f"Page not found (status code: {response.status_code})")
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find(
        'div', {'class': 'tableContainer yf-9ft13'})
    if not table:
        if (soup.find('div', {'class': 'noData yf-wnifss'})):
            raise Exception(f"Wrong Ticker {ticker}")
        else:
            raise Exception(f"Can't find the table")

    table_body = soup.find('section', {'class': 'finContainer'}).find('div', {'class': 'tableBody'})
    if not table_body:
        raise Exception("Something went wrong :Can't find the table")
    rows = table_body.find_all('div', {'class': 'row'})
    for row in rows:
        children = row.find_all(recursive=False)
        if children[0].text.strip().lower() == name_row.strip().lower():
            result_list = [children[0].text.strip()]
            for child in children[1:]:
                result_list.append(child.text.strip())
            print(tuple(result_list))
            break             
    else:
        raise Exception(f"Not such of row name: {name_row}")
    
                


def finance():
    if len(sys.argv) != 3:
        print("Usage: ./financial.py <ticker> \"<name_row>\"")
    else:
        ticker = sys.argv[1].upper()
        name_row = sys.argv[2]
        try:
            result = get_fin_data(ticker, name_row)
        except Exception as e:
            print(f"Error: {e}")


if __name__ == '__main__':
    finance()
