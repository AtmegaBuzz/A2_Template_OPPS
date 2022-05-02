from User import User

class Student(User):
    def __init__(
        self, 
        id_=-1,
        username="",
        password="",
        user_title="",
        user_image_50x50="",
        user_initials="",
        review_id=-1
        ):
        self.user_title = user_title
        self.user_image_50x50 = user_image_50x50
        self.user_initials = user_initials
        self.review_id = review_id
        super().__init__(id_, username, password)

    def view_courses(self,args=[]):
        pass

    def view_reviews(self,args=[]):
        pass


    def __str__(self) -> str:
        parent_attrs = super().__str__()
        return f"{parent_attrs};;;{self.user_title};;;{self.user_image_50x50};;;{self.user_initials};;;{self.review_id}"