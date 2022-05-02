from User import User

class Instructor(User):
    
    def __init__(
        self, 
        id_=-1,
        username="",
        password="",
        display_name="",
        job_title="",
        image_100x100="",
        course_id_list=[]
        ):
        self.display_name = display_name
        self.job_title = job_title
        self.image_100x100 = image_100x100
        self.course_id_list = course_id_list
        super().__init__(id_, username, password)

    def view_courses(self,args=[]):
        pass

    def view_reviews(self,args=[]):
        pass

    def __str__(self) -> str:
        parent_attrs = super().__str__()
        return f"{parent_attrs};;;{self.display_name};;;{self.job_title};;;{self.image_100x100};;;123123–323–32–3123–3123"


