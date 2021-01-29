import geopandas as gp
import pandas as pd


os.chdir('path')
geojson = gp.read_file('kuntarajat_2017.geojson')


os.chdir('path')
csv = pd.read_csv('postinumeroluettelo.csv',dtype = str)
csv.loc[csv['kunta'] == 'Maarianhamina - Mariehamn','kunta'] = 'Maarianhamina'

csv_grouped = csv[['kunta','maakunta']].groupby(['kunta','maakunta'], as_index=False).first()


merged = pd.merge(geojson,csv_grouped,left_on='Name', right_on='kunta',how = 'left')
merged = merged.drop(columns =['kunta'])


merged = merged.dissolve(by = 'maakunta')


os.chdir('path to save')

merged.to_file("maakuntarajat.geojson", driver='GeoJSON')