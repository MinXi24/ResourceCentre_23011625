class Item():
<<<<<<< HEAD
=======

>>>>>>> 737a8e9a586429d7951a2262179bbede525dfe84
    def __init__(self, assetTag, description):
        self._assetTag = assetTag
        self._description = description
        self._dueDate = ""
        self._isAvailable = True
<<<<<<< HEAD
=======

>>>>>>> 737a8e9a586429d7951a2262179bbede525dfe84
    
    def getAssetTag(self):
        return self._assetTag
    
    def getDescription(self):
        return self._description
<<<<<<< HEAD
    
    def getDueDate(self):
        return self._dueDate
    
=======
    def getDueDate(self):
        return self._dueDate
>>>>>>> 737a8e9a586429d7951a2262179bbede525dfe84
    def getIsAvailable(self):
        if self._isAvailable:
            return "Yes"
        else:
            return "No"
<<<<<<< HEAD

    def setDueDate(self, dueDate):
        self._dueDate = dueDate

=======
 
    def setDueDate(self, dueDate):
        self._dueDate = dueDate
>>>>>>> 737a8e9a586429d7951a2262179bbede525dfe84
    def setIsAvailable(self, isAvailable):
        self._isAvailable = isAvailable

    def __str__(self):
<<<<<<< HEAD
        return "{:<10}{:<30}{:<10}{:<12}".format(
                        self.getAssetTag(), self.getDescription(), 
                        self.getIsAvailable(), self.getDueDate() )
    
     
=======
        return "{:<10}{:<30}{:<10}{:<12}".format( 
                        self.getAssetTag(), self.getDescription(),  
                        self.getIsAvailable(), self.getDueDate()  )
>>>>>>> 737a8e9a586429d7951a2262179bbede525dfe84
