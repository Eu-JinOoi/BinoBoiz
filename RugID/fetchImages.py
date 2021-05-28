#
import pandas as pd
import os
import wget
designCSV = 'products_export.csv'
designRead = pd.read_csv(designCSV)
designArray = designRead['Handle'].unique()
for design in designArray:
    try:
        os.mkdir(os.getcwd() + "\\designs\\"+design)
    except:
        print("Tried but already there")
    designFilter = designRead.loc[designRead['Handle'] == design]
    designFilterArray = designFilter['Image Src'].unique()
    for url in designFilterArray:
        filename = wget.download(url)
        os.rename(filename, os.path.join(os.getcwd(), "designs", design, filename))
        print(filename)