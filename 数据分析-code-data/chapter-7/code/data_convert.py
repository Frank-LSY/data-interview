import pandas as pd
datafile = '../tmp/data_cleaned.xls'
convertedfile = '../tmp/converteddata.xls'

data = pd.read_excel(datafile,encoding='utf-8')

data = data[['LOAD_TIME','FFP_DATE','LAST_TO_END',
             'FLIGHT_COUNT','SEG_KM_SUM','avg_discount']]

new_data = pd.DataFrame()
new_data['L'] = (pd.to_datetime(data['LOAD_TIME'],format='%Y/%m/%d')-pd.to_datetime(data['FFP_DATE'],format='%Y/%m/%d')).dt.days
new_data['R'] = data['LAST_TO_END']
new_data['F'] = data['FLIGHT_COUNT']
new_data['M'] = data['SEG_KM_SUM']
new_data['C'] = data['avg_discount']

new_data.to_excel(convertedfile)