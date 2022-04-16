import wbdata
import datetime
import pandas as pd

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
    
    return sorted_df

def all_nations():
    countries = wbdata.search_countries('')
    df = pd.DataFrame(countries)
    df.drop(['iso2Code', 'incomeLevel', 'lendingType', 'region', 'adminregion'], axis=1, inplace=True)
    return df



