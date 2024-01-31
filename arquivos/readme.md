Os arquivos desta pasta estão sendo utilizados nas análises ao longo do projeto.

- Arquivos .CSV foram lidos com Python Pandas
    ex:
  
           import Pandas
  
           stores = pd.read_csv('/content/drive/MyDrive/store_sales/stores.csv')

- Arquivos .PKL foram lidos com a biblioteca Pickle
    ex:
  
           import pickle

            with open("df_cleaned.pkl", "rb") as fp:   # Unpickling
            df_cleaned = pickle.load(fp)
