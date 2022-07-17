from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    db_name = 'users'

    def __repr__(self):
        return f"\nFirst Name: {self.first_name},\nLast Name: {self.last_name},\n{self.email},\nCreated at: {self.created_at},\nUpdated at: {self.updated_at}\n"
    
    #query database with class method
    @classmethod
    def get_all_users(cls):
        query = "SELECT * from users;"
        results = connectToMySQL(cls.db_name).query_db(query)
        users = []

        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def get_one_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if len(results) == 0:
            return []
        else:
            return results[0]

    @classmethod
    def save_user(cls, data):
        query = "INSERT INTO users ( first_name , last_name , email , created_at , updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , NOW() , NOW() ) "
        return connectToMySQL(cls.db_name).query_db(query, data)

    
    @classmethod
    def edit_user(cls, data):
        query = "UPDATE users SET first_name = %(fname)s, last_name = %(lname)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)


    @classmethod
    def clear_users(cls):
        query = "DELETE from users WHERE id > 0;"
        connectToMySQL(cls.db_name).query_db(query)

    @classmethod
    def delete_one_user(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def reset_ids(cls):
        query = "ALTER TABLE users AUTO_INCREMENT = 1;"
        connectToMySQL('users').query_db(query)