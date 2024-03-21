from flask_app.config.mysqlconnection import connectToMySQL
from .ninja_model import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.nombre  = data['nombre']
        self.created_at  = data['created_at']
        self.updated_at  = data['updated_at']
    
    @classmethod
    def get_all(cls):
        query= ("SELECT * FROM dojos;")
        results = connectToMySQL('esquema_dojo_ninjas').query_db(query)
        dojos = []
        for d in results:
            dojos.append(cls(d))
        return dojos
    
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos(nombre) VALUES(%(nombre)s);"
        print('inserta', query)
        results = connectToMySQL('esquema_dojo_ninjas').query_db(query,data)
        return results

    
