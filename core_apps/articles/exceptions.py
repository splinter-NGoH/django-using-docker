from rest_framework.exceptions import APIException


class UpdateArticle(APIException):
    status_code = 403
    default = "Your can't update an article that doesn't belong to you"
    
     