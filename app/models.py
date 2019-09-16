class News:
    '''
    We have created News class to define News Objects
    '''

    def __init__(self,id,name,description,category,language,country,url):
        self.id = id
        self.name =name
        self.description = description
        self.category = category
        self.language = language
        self.country = country
        self.url = url

class Articles:
   '''
   Articles class to define articles objects
   '''
   def __init__(self,id,author,title,description,url,image):
       self.id = id
       self.author = author
       self.title = title
       self.description = description
       self.url = url
       self.image = image
       

