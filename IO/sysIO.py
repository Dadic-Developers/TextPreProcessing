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
    def writeFile (self, data, fileName):
        with open(fileName, 'w') as f:
            print >> f, data
        # f = open(fileName, "w")
        # f.write(data)
        # f.close()
        # with open(fileName, "w") as outfile:
        #      json.dump(data, outfile)