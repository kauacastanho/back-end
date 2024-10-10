class AppStatus:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.current_user = None
            cls._instance.language = None
            cls._instance.time_zone = None 
            cls._instance.metric_unit = None
        return cls._instance
    
    def get_language(self):
        return self._instance.language

    def get_time_zone(self):
        return self.time_zone
    
    def get_metric_unit(self):
        return self.metric_unit 

    
class Utils:
    MILHA = 160934 

    @staticmethod
    def converter_para_km(valor):
        appstatus = AppStatus()
        if appstatus.get_metric_unit:
            return valor * Utils.MILHA
        else:
            return valor



appstatus = AppStatus()
utils = Utils()



print(Utils.converter_para_km(6))
print(appstatus.get_metric_unit())