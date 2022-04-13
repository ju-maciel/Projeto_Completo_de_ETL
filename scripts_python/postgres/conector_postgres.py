import psycopg2

class Conectar:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        
        
    def conectar(self):
        conect = psycopg2.connect(host=self.host, database=self.database, user=self.user,password=self.password)
        return conect
    
    def executar(self, query):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute(query)
        cursor.close()
        con.commit()
        return 'Acao Feita!'
    
    def selecionar(self, query):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute(query)
        resultado = cursor.fetchall()
        return resultado

    def inserir_array(self, table, parametros, valores):
        query = f"INSERT INTO {table} ({parametros}) VALUES {valores}" 
        self.executar(query) 
        #print(query) # escolher printar query, comentar o executar query (pra visualizar como está inserindo no banco)
        
   