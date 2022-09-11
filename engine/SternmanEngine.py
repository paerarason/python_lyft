from engine.engine import Engine
class SternmanEngine:
    __warning_light_on :bool
    def __init__(self,warning_light_on ):
        self.__warning_light_on=warning_light_on
    def needs_service(self):
        return self.warning_light_on