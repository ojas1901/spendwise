import os

import requests
import csv

CURRENCY_API_KEY = '4YOHN3QHDBARIJEX'


def real_time_currency_convert(from_currency, to_currency):
    """
        Queries Alpha Vantage API to find out live currency exchange rates

        :param from_currency: Currency to convert from
        :type: str
        :param to_currency: Currency to convert to
        :type: str
        :return: Live exchange rate from from_currency to to_currency
        :rtype: float
    """
    # importing required libraries

    function = 'CURRENCY_EXCHANGE_RATE'
    # base_url variable store base url

    # main_url variable store complete url
    main_url = f'https://www.alphavantage.co/query?function={function}&from_currency={from_currency}&to_currency={to_currency}&apikey={CURRENCY_API_KEY}'

    req_ob = requests.get(main_url)

    dict_outer_key = "Realtime Currency Exchange Rate"
    dict_inner_key = "5. Exchange Rate"

    result = req_ob.json()[dict_outer_key][dict_inner_key]

    return round(float(result), 2)


def export_to_csv(content, header, path):
    """
    This is a function which helps to export the given content with the given header to csv. It will create a new file
    at the given path

    :param content: list of content
    :type: [[str]]
    :param header: Header List
    :type: [str]
    :param path: Path to save the file
    :type: str
    :return: CSV File
    :rtype: object
    """
    with open(path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(header)
        writer.writerows(content)
    return open(path, 'rb')
