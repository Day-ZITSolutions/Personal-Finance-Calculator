from database.db_utils import execute_query

class User:
    def __init__(self, user_id=None, first_name=None, last_name=None, username=None, email=None, password_hash=None):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password_hash = password_hash

    def create_user(self, first_name, last_name, username, email, password_hash):
        """Creates a new user in the database."""
        query = """
        INSERT INTO users (first_name, last_name, username, email, password_hash)
        VALUES (%s, %s, %s, %s, %s)
        """
        data = (first_name, last_name, username, email, password_hash)
        
        # Execute the insert query
        execute_query(query, data)

        # Now, retrieve the last inserted user ID
        last_id_query = "SELECT LAST_INSERT_ID()"
        last_id_result = execute_query(last_id_query)

        if last_id_result and last_id_result[0]:
            self.user_id = last_id_result[0][0]  # Get the last inserted ID
            self.first_name = first_name
            self.last_name = last_name
            self.username = username
            self.email = email
            self.password_hash = password_hash
            print("User created successfully with ID:", self.user_id)
            return self
        else:
            print("Failed to retrieve the user ID.")
            return False


    @staticmethod
    def get_user_by_username(username):
        """Retrieves a user by username."""
        query = "SELECT * FROM users WHERE username = %s"
        data = (username,)
        user_data = execute_query(query, data)

        if user_data:
            try:
                if user_data:
                    print("User data fetched successfully.")
                    return User(
                        user_id=user_data[0][0],
                        first_name=user_data[0][1],
                        last_name=user_data[0][2],
                        username=user_data[0][3],
                        email=user_data[0][4],
                        password_hash=user_data[0][5]
                    )
                else:
                    print("No user found with the provided username.")
                    return None
            except Exception as e:
                print(f"Error fetching user data: {e}")
                return None
        else:
            print("Failed to execute query or fetch data.")
            return None
