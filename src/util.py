import requests

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
