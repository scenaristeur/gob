class Brain:
    def __init__(self, config, width="pas connu", color="red"):
        self.config = config
        self.width = width
        self.color = color
        self.connexion = self.connect(self.config)


    def connect(self, config):
        print(f"{config['name']} : Connexion ... {config['type']}")
        if config['type'] == "memgpt":
            import gob.memGPTBrain as memGPTBrain
            mB =memGPTBrain.memGPTBrain(config)
            mB.connect()
            return mB
        if config['type'] ==   "dummy":
            print("dummy")

        else:
            raise ValueError(f"{config['name']} : Unknown type of brain")