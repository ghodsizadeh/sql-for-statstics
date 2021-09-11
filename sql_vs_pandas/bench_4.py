from memory_profiler import profile


@profile
def run():
    import psycopg2 
    connection = psycopg2.connect(database='stats',user='postgres',password='postgres', host='localhost', port='5435')
    with connection.cursor() as cursor:
        cursor.execute('select activated, count(*) as counter from users group by activated')

        result = cursor.fetchall()
        print(result)




if __name__ == "__main__":
    run()

