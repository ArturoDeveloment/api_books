from dotenv import load_dotenv
import os

load_dotenv()


class Config():
    pass

class VariablesEnviroment(Config):
    __HOST = os.getenv("HOST_SV")
    __PORT = os.getenv("PORT_SV")
    __DEBUG = bool(eval(os.getenv("DEBUG_SV").replace(" ", "").capitalize()))
    
    def get_env_sv(self):
        return {
            "host": self.__HOST,
            "port": int(self.__PORT),
            "debug": self.__DEBUG
        }

server =  VariablesEnviroment().get_env_sv()