from datetime import datetime

class Utils: 

    @staticmethod 
    def getActualDateTime():
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        # dt_string = now.
        return now

    @staticmethod 
    def getMbByBytes(numberKByte):
        numberGb = round(int(numberKByte) * pow(10, -6), 2)
        return numberGb
        

    @staticmethod 
    def getGbByBytes(numberByte):
        numberGb = round(int(numberByte) * pow(10, -9), 2)
        return numberGb

    @staticmethod 
    def getMbBybits(numberbits):
        numberMb = round((int(numberbits) / 8) * pow(10, -6), 2)
        return numberMb