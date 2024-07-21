# API: https://memgpt.readme.io/reference/get_all_users_admin_users_get
# rest python client https://memgpt.readme.io/docs/admin-client#rest-python-client

from memgpt import Admin, create_client
import yaml
import os
import time
import json

config_directory = "config/memgpt/"
if not os.path.exists(config_directory):
    os.makedirs(config_directory)


class memGPTBrain:
    def __init__(self, config, width="pas connu", color="red"):
        self.config = config
        self.width = width
        self.color = color

    def connect(self):
        # TODO add tools & add data sources

        self.admin = Admin(
            base_url=self.config['endpoint'], token=self.config['admin_token'])
        self.User()
        self.client = create_client(
            base_url=self.config['endpoint'], token=self.api_key)
        # agent = {
        # "config": {
        #     "name": "MyCustomAgent",
        #     "preset": "memgpt_chat",
        #     "human": "cs_phd",
        #     "persona": "sam_pov"
        # }
        # }

        self.human = self.Human()
        self.persona = self.Persona()
        # self.tools = self.createTools()
        # self.data_sources = self.createDataSources()
        self.agent_state = self.Agent()
        print("Agent", self.agent_state.id, type(self.agent_state.id))


#         message = {
#   "agent_id": "e7a192e6-f9a3-4f60-9e7c-1720d3d207ef",
#   "message": "what's the meaning of life? someone told me it's 42...",
#   "stream": "true",
#   "role": "user"
# }
        # print("AGENT STATE", self.agent)
        self.agents = self.client.list_agents().agents
        print("Agents", type(self.agents), self.agents[0]['id'])
        message = "Quel est le sens de la vie ? Qu'elqu'un m'a dit que c'était 42..."
        

        # BUG !!       
        # there is a bug with agent_id, should be self.agent_state.id
        response =self.sendMessage(self.agents[0]['id'],message)
        print(f"RESPONSE : {response}")

    def Human(self):
        # https://github.com/cpacker/MemGPT/blob/634c642aef290f8648636a3ac23a973d3a20ae17/memgpt/client/client.py#L501
        try:
            # eventually update the description
            human = self.client.get_human(self.config['human_name'])
            print("Human exists", human)
            return human
        except:
            return self.client.create_human(
                name=self.config['human_name'],
                human=self.config['human_description'])

    def Persona(self):
        try:
            # eventually update the description
            persona = self.client.get_persona(self.config['persona_name'])
            print("Persona exists", persona)
            return persona
        except:
            return self.client.create_persona(
                name=self.config['persona_name'],
                persona=self.config['persona_description'],
            )

    def Agent(self):

        # agent = {
        #     "config": {
        #         "name": "my_agent",
        #         "preset": "memgpt_chat",
        #         "human": self.human.human_id,
        #         "persona": self.persona.persona_id,

        #     }
        # }

        # self.agents = self.client.list_agents()

        # print("\n###########agents\n###########") 
        # for agent in self.agents:
        #     ag = json.loads(json.dumps(agent))
        #     print(ag)
        #     # if agent.name == self.config['agent_name']:
        #     #     return agent



        # agent = {
        #     "name": self.config['agent_name'],
        #     "human_name": self.config['human_name'],
        #     "human": self.config['human_description'],
        #     "persona_name": self.config['persona_name'],
        #     "persona": self.config['persona_description'],
        #     "model": "memgpt-openai",
        #     "function_names": "append_to_text_file,archival_memory_insert,archival_memory_search,conversation_search,conversation_search_date,core_memory_append,core_memory_replace,http_request,message_chatgpt,pause_heartbeats,read_from_text_file,send_message"
        # },
        # "user_id": self.client['user_id']
# https://github.com/cpacker/MemGPT/blob/634c642aef290f8648636a3ac23a973d3a20ae17/memgpt/server/rest_api/agents/index.py#L93
        return self.client.create_agent(
            #user_id=self.user_id,
            name= self.config['agent_name'],
            tools= ["append_to_text_file",
            "archival_memory_insert",
            "archival_memory_search",
            "conversation_search",
            "conversation_search_date",
            "core_memory_append",
            "core_memory_replace",
            "http_request",
            "message_chatgpt",
            "pause_heartbeats",
            "read_from_text_file",
            "send_message"],
            metadata={
                "human":self.config['human_name'],
                "persona":self.config['persona_name'],
            }
        )

    # def createTools(self):
    #     return self.client.create_tools(
    #         agent_id=self.agent.agent_id
    #     )

    # def createDataSources(self):
    #     return self.client.create_data_sources(
    #         agent_id=self.agent.agent_id

    def sendMessage(self, agent_id, message):
        # message_data = {
        #     "agent_id": self.agent_state.id,
        #     "message": "what's the meaning of life? someone told me it's 42...",
        #     "stream": "true",
        #     "role": "user"
        # }
        # self.client.send_message(agent_id=self.agent_state.name, message=message)
        return self.client.user_message(
            agent_id=agent_id,
            message=message,
        )

    def User(self):
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
            print(f"Utilisateur Exists : {user_info}")
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
