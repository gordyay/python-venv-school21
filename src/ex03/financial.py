#!/usr/bin/env python3
import sys
import requests
from bs4 import BeautifulSoup
import time


def get_fin_data(ticker, name_row):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    url = f"http://finance.yahoo.com/quote/{ticker}/financials/?p={ticker.lower()}"
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(
            f"Page not found (status code: {response.status_code})")
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find(
        'div', {'class': 'tableContainer yf-9ft13'})
    if not table:
        raise Exception("Table not found")

    table_container = soup.find('section', {'class': 'finContainer'})
    if not table_container:
        raise Exception("Таблица не найдена.")
    # Получаем заголовки столбцов
    columns = []
    header_row = table_container.find('div', {'class': 'D(tbr)'})
    if header_row:
        column_headers = header_row.find_all('div', {'class': 'Ta(c)'})
        for header in column_headers[1:]:  # Первый элемент - пустой
            columns.append(header.get_text(strip=True))

    # Ищем нужную строку
    rows = table_container.find_all('div', {'data-test': 'fin-row'})
    for row in rows:
        row_title = row.find('div', {'class': 'Va(m)'})
        if row_title and row_title.get_text(strip=True).lower() == name_row.lower():
            values = row.find_all('div', {'data-test': 'fin-col'})
            formatted_values = [value.get_text(strip=True) for value in values]
            return columns, formatted_values
    # rows = table_body.find_all('div', {'class': 'row'})
    # for row in rows:
    #     children = row.find_all(recursive=False)
    #     for child in children:
    #         print(child)


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
