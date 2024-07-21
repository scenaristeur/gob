default_config="./config/first.yaml"


def getConfig(config):
    import yaml

    with open(config, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            raise

def showBrain(brain):
    print(brain['name'])