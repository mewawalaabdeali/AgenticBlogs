from configparser import ConfigParser

class Config:
    def __init__(self, config_file="./src/ui/uiconfigfile.ini"):
        self.config = ConfigParser()
        self.config.read(config_file)

    def get_usecase_options(self):
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(", ")
    
    def get_pagetitle(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")
    
    def get_model_options(self):
        return self.config["DEFAULT"].get("MODEL_OPTIONS").split(", ")