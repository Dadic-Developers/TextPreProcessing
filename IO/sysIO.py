import json

class sysIO :
    def readFile(self, fileName):

        # Opening JSON file
        f = open(fileName)
        
        # returns JSON object as 
        # a dictionary
        data = json.load(f)
        
        
        
        # Closing file
        f.close()
        return data
    def writeFile (self, data, fileName='/media/daadik/Local Disk/backend/TextPreProcessing/Data/outFile.json'):
        with open(fileName,"w", encoding='utf-8') as jsonfile:
         json.dump(data,jsonfile,ensure_ascii=False)