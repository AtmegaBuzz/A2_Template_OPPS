
class Course:
    
    def __init__(
        self,
        course_id=-1,
        course_title="",
        course_image_100x100="",
        course_headline="",
        course_num_subscribers=-1,
        course_avg_rating=-1.0,
        course_content_length=-1        
        ) -> None:

        self.course_id = course_id 
        self.course_title = course_title 
        self.course_image_100x100 = course_image_100x100
        self.course_headline = course_headline
        self.course_num_subscribers = course_num_subscribers
        self.course_avg_rating = course_avg_rating
        self.course_content_length = course_content_length

    def find_course_by_title_keyword(self,keyword):
        pass

    def find_course_by_id(self,course_id):
        pass

    def find_course_by_instructor_id(self,instructor_id):
        pass

    def courses_overview(self):
        pass        

    def __str__(self):
        return f"{self.course_id};;;{self.course_title};;;{self.course_image_100x100};;;{self.course_headline};;;{self.course_num_subscribers};;;{self.course_avg_rating};;;{self.course_content_length}"
