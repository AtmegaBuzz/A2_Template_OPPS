class Review:
    
    def __init__(
        self,
        id_=-1,
        content="",
        rating=-1.0,
        course_id=-1
        ) -> None:
        
        self.id = id_
        self.content = content
        self.rating = rating
        self.course_id = course_id

    def find_review_by_id(self,review_id):
        pass

    def find_review_by_keywords(self,keyword):
        pass

    def find_review_by_course_id(self,course_id):
        pass

    def reviews_overview():
        pass

    def __str__(self) -> str:
        return f"{self.id_};;;{self.content};;;{self.rating};;;{self.course_id}"

        
