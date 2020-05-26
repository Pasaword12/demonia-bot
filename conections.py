import psycopg2

def conection():
    conexion = psycopg2.connect(host="ec2-52-202-22-140.compute-1.amazonaws.com", database="dcg08u6k2bq4tt", user="yoznmodhjzkeid", password="b6493d7605a047550f9b6aa54b430732033dad49be4c8591f1a865c401d726cd")
    cur = conexion.cursor()
    cur.execute("select url from memes")
    respuesta = ''
    for url in cur.fetchall() :
        respuesta= url
    conexion.close()
    #print(type(respuesta))
    #print(respuesta[0])
    return respuesta
conection()