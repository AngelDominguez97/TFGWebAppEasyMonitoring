from datetime import datetime

class Utils: 

    @staticmethod 
    def getActualDateTime():
        now = datetime.now()
        # dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        return now

    @staticmethod 
    def getGbByBytes(numberByte):
        numberGb = round((((int(numberByte) / 1024) / 1024) / 1024), 2)
        return numberGb