from Libs.config_handler import ConfigHandler

class AppSettings():
    def __init__(self) -> None:
        self.__config_handler = ConfigHandler('config.yml')
        self.token = self.__config_handler.get_value('token')
        self.main_channel_id = self.__config_handler.get_value('main_channel_id')
        self.group_ids = self.__config_handler.get_value('group_ids')
        self.usernames = self.__config_handler.get_value('usernames')