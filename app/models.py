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

# class Review:

#     all_reviews = []

#     def __init__(self,news_name,title,imageurl,review):
#         self.news_name = news_name
#         self.description = description
#         self.category = category
#         self.review = review


#     def save_review(self):
#         Review.all_reviews.append(self)


#     @classmethod
#     def clear_reviews(cls):
#         Review.all_reviews.clear()

#     @classmethod
#     def get_reviews(cls,name):

#         response = []

#         for review in cls.all_reviews:
#             if review.news_name == name:
#                 response.append(review)

#         return response