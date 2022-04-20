import wbdata
import pandas as pd
import datetime

def get_indicators(abbr):
    indicators = ['SP.POP.TOTL', 'SP.DYN.LE00.IN', 
    'SP.DYN.CBRT.IN', 'SP.POP.GROW', 'EN.POP.DNST', 'SP.URB.TOTL.IN.ZS',
    'NY.GDP.MKTP.KD.ZG', 'SE.ADT.LITR.ZS', 'SL.UEM.TOTL.ZS']
    title = []
    acronym = []

    for values in indicators:
        data = wbdata.get_data(values, country=abbr)
        my_dict = data[0]
        values_view = my_dict.values()
        value_iterator = iter(values_view)
        first_value = next(value_iterator)
        title.append(first_value['value'])
        acronym.append(abbr)

    df = pd.DataFrame()

    df['indicator_id'] = indicators
    df['title'] = title
    df['country'] = acronym

    return df

def all_nations():
    countries = wbdata.search_countries('')
    df = pd.DataFrame(countries)
    df.drop(['iso2Code', 'incomeLevel', 'lendingType', 'region', 'adminregion'], axis=1, inplace=True)
    df.drop(df[df['capitalCity'] == ''].index, inplace=True)
    df.drop(df[df['latitude'] == ''].index, inplace=True)
    df = df.reset_index()
    df.drop(['index'], inplace=True, axis=1)
    return df

def get_data(indicator, country):
    date_date = datetime.datetime(2010, 1, 1), datetime.datetime(2022, 1, 1)
    data = wbdata.get_data(indicator, country=country, data_date=date_date)
    df = pd.DataFrame()
    year = []
    values = []
    for item in data:
        year.append(item['date'])
        values.append(item['value'])
    df['year'] = year
    df['values'] = values
    sorted_df = df.sort_values(by=['year'], ascending=True)
    sorted_df = sorted_df.dropna()
    print(sorted_df)
    year = sorted_df['year'].tolist()
    values = sorted_df['values']
    return year,values



