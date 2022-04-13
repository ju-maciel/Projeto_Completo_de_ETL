from conector_postgres import Conectar
import pandas as pd
import numpy as np

    
if __name__ == '__main__':
    
    ### Local
    # conexao = Conectar(host='localhost', database='operadora2', user='postgres',password='ROOT')
    ### Nuvem
    conexao = Conectar(host='34.151.208.93', database='operadora2', user='postgres',password='ROOT')

    
    # Leitura do arquivo
    ### Local
    #df = pd.read_csv(r'C:\Users\admin\Desktop\operadoras2\Meu_Municipio_Acessos.csv', sep=';', encoding = 'utf-8')
    ### Nuvem
    df = pd.read_csv(r'gs://pasta-scripts/operadoras2/Meu_Municipio_Acessos.csv', sep=';', encoding = 'utf-8')
    #print(df)
    
    
    # print(df.columns)
    # renomeando colunas 
    df.columns=['Ano', 'Mes', 'Acessos', 'Servico', 'Densidade', 'Cod_IBGE', 'Municipio', 'UF', 'Nome_UF', 'Regiao', 'Cod_nacional'] 
    # print(df.columns)
    
    # excluindo colunas
    df = df.drop(columns=['Densidade', 'Nome_UF', 'Cod_nacional']) 
    
    
    # tamanho do dataframe [0]linhas[1]colunas
    # df.shape
    
    # verificação de dados faltantes
    # df.info()
    
    # verificação de dados nulos
    # print(df.isnull().sum())
    
    # substituir nulos por 0
    # df.fillna(0, inplace = True) 
    
    
    # iteração para inserção (1º opção de inserção pelo DF(lento, para cada coluna iterar item por item pelo index))
    # lista = []
    # for i in df.index:
    #     #print(df['Ano'][i])
    #     x = (df['Ano'][i], df['Mes'][i], df['Acessos'][i], df['Servico'][i], df['Cod_IBGE'][i], df['Municipio'][i], df['UF'][i], df['Regiao'][i])
    #     lista.append(x)
    #     #print(lista)
    # lista = str(lista)[1:-1] 
    # print(lista)
  
      
    # print(df)
    
    # transformando df em array para inserção mais eficiente          
    array = np.array(df)
  
    # iteração 
    lista = []
    for i in array:
        #print(i)
        x = (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])  #linhas de inserção 
        lista.append(x)
    # print(lista)
    lista = str(lista)[1:-1]  #excluindo colchetes
        
    
    # inserção por array
    conexao.inserir_array('operadora', 'Ano, Mes, Acessos, Servico, Cod_IBGE, Municipio, UF, Regiao', lista)
            
            
            
            
            
            
            
    # testes
    # cada i é uma linha do array
    # variavel x = cada valor da linha, pelo FOR uma linha de cada vez, pego cada valor e coloco dentro do parenteses separando por ,
    # lista = str(lista)[1:-1] # excluindo o item 0 e -0 da string (quero que a string comece do index 1 até -1) excluindo os [] que atrapalha na inserção
    # print(array) 
    # print (array[1])
    # print('=============')
    # print(df['Ano'][0])   
    # print(df.Ano[0]) 
    # print('===============')
    # print(i[2])
    
 
 
 
 
 
 
 
 
   
    
   
            
 
        
