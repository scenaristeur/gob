# API: https://memgpt.readme.io/reference/get_all_users_admin_users_get
# rest python client https://memgpt.readme.io/docs/admin-client#rest-python-client

from memgpt import Admin
import yaml
import os
import time

config_directory = "config/memgpt/"
if not os.path.exists(config_directory):
    os.makedirs(config_directory)


class memGPTBrain:
    def __init__(self, config, width="pas connu", color="red"):
        self.config = config
        self.width = width
        self.color = color

    def connect(self):
        self.admin = Admin(
            base_url=self.config['endpoint'], token=self.config['admin_token'])

        self.getOrCreateUser()



    def getOrCreateUser(self):
        user_info = None
        user_file = "config/memgpt/"+self.config['user_file']
        user_file_exists = os.path.isfile(user_file)
        if (user_file_exists):
            with open(user_file) as f:
                user_info = yaml.load(f, Loader=yaml.FullLoader)

        if user_info is None:
            response = self.admin.create_user()
            self.user_id = response.user_id  # unique UUID for the user
            self.api_key = response.api_key  # bearer token for authentication
            print(
                f"user created {self.user_id} avec {self.api_key}, and saved to {user_file}")
            self.saveUser()
        else:
            print (f"Utilisateur Exists : {user_info}")
            self.user_id = user_info[0]['user']['login']['user_id']
            self.api_key = user_info[0]['user']['login']['api_key']
            print(f"Utilisateur Exists : {self.user_id} avec {self.api_key}")






    def saveUser(self):
        user_info = [
            {'user': {
                'type': 'memgpt',
                'language': 'python',
                'date': time.time(),
                'login': {
                    'endpoint': self.config['endpoint'],
                    'user_id': str(self.user_id),
                    'api_key': self.api_key,
                }
            }
            }
        ]

        with open("config/memgpt/"+self.config['user_file'], 'w') as yamlfile:
            data = yaml.dump(user_info, yamlfile)
            print("Write successful")