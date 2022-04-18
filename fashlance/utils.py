import wbdata
import datetime
import pandas as pd

def get_data(country):
    get_indicators = ['SP.POP.TOTL', 'SP.DYN.LE00.IN', 
    'SP.DYN.CBRT.IN', 'SP.POP.GROW', 'EN.POP.DNST', 'SP.URB.TOTL.IN.ZS',
    'NY.GDP.MKTP.KD.ZG', 'SE.ADT.LITR.ZS', 'SL.UEM.TOTL.ZS']
    date_date = datetime.datetime(2010, 1, 1), datetime.datetime(2022, 1, 1)

    title = []
    info = []


    for values in get_indicators:
        data = wbdata.get_data(values, country=country, data_date=date_date)
        my_dict = data[0]
        values_view = my_dict.values()
        value_iterator = iter(values_view)
        first_value = next(value_iterator)
        title.append(first_value['value'])

        year = []
        values = []
        df = pd.DataFrame()
        for item in data:
            year.append(item['date'])
            values.append(item['value'])
        df['year'] = year
        df['values'] = values
        sorted_df = df.sort_values(by=['year'], ascending=True)
        info.append(sorted_df)

    new_df = pd.DataFrame()
    new_df['title'] = title
    new_df['info'] = info

    return new_df, title

def all_nations():
    countries = wbdata.search_countries('')
    df = pd.DataFrame(countries)
    df.drop(['iso2Code', 'incomeLevel', 'lendingType', 'region', 'adminregion'], axis=1, inplace=True)
    return df



