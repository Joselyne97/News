class News:
    '''
    We have created News class to define News Objects
    '''

    def __init__(self,name,description,category,language,country,url):
        self.name =name
        self.description = description
        self.category = category
        self.language = language
        self.country = country
        self.url = url