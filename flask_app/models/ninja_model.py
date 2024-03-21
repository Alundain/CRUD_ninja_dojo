from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self,data):
        self.id = data['id']
        self.first_name  =data['first_name']
        self.last_name  =data['last_name']
        self.age  =data['age']
        self.created_at  =data['created_at']
        self.updated_at  =data['updated_at']
        self.dojos_id = data['dojos_id']
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojos_id) VALUES(%(first_name)s, %(last_name)s, %(age)s,%(dojos_id)s);"
        return connectToMySQL('esquema_dojo_ninjas').query_db(query,data)

    @classmethod
    def get_one_dojo_with_ninjas(cls, data):
        query = "SELECT ninjas.* FROM ninjas WHERE dojos_id = %(id)s;"
        results = connectToMySQL('esquema_dojo_ninjas').query_db(query, data)
        print("Imprime el resultado:", results)
        ninjas = []        
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas