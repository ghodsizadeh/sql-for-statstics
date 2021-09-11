from memory_profiler import profile


@profile
def run():
    import pandas as pd
    import psycopg2 
    connection = psycopg2.connect(database='stats',user='postgres',password='postgres', host='localhost', port='5435')
    with connection.cursor() as cursor:
        cursor.execute('select id, activated from users')
        df = pd.DataFrame(cursor.fetchall(), 
        columns = ['id', 'activated']
        )
        

    result = df.groupby('activated').count()




if __name__ == "__main__":
    run()

