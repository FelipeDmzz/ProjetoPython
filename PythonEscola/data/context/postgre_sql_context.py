import psycopg2

class Postgre_Sql_Context:

    Parametros_conexao = None
    conexao = None
    cursor = None

    def __init__(self):
        self.Parametros_conexao = {
            'host' : "127.0.0.1",
            'port' : "5432",
            'database' : "Escola",
            'user' : "postgres",
            'password' : "26042005"

        }
    def conectar (self):
        try:
            self.conexao = psycopg2.connect(
                host = self.Parametros_conexao.get('host'),
                port = self.Parametros_conexao.get('port'),
                database = self.Parametros_conexao.get('database'),
                user = self.Parametros_conexao.get('user'),
                password = self.Parametros_conexao.get('password')
            )
        except Exception as e:
            print(f"Não foi possível conectar-se ao banco de dados")
            print(f"Erro > {e}")

    def desconectar(self):
        if self.conexao is not None:
            self.conexao.close()

    def executar_query_sql(self, query):
        self.cursor = self.conexao.cursor()

        self.cursor.execute(query)

        rows = self.cursor.fetchall()

        self.cursor.close()

        return rows

    def executar_uptade_sql(self, query):
        self.cursor = self.conexao.cursor()

        self.cursor.execute(query)

        self.conexao.commit()

        self.cursor.close()


