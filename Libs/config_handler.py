import yaml

class ConfigHandler():
    def __init__(self, config_path) -> None:
        self.__config_path = config_path
        with open(self.__config_path, 'r') as file:
            self.__data = yaml.safe_load(file)
    
    def get_value(self, value_name: str) -> any:
            return self.__data[value_name]    