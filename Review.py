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

    @classmethod
    def find_review_by_id(cls,review_id):
        
        with open('review.txt','r',encoding='utf-8') as f:
            reviews = f.readlines()
        
        for review in reviews:
            review_data = review.split(";;;")
            __review_id__ = review_data[0]

            if __review_id__==review_id:
                r = Review(*review_data)
                print(r)
                return r
        print("no items found")
        
    @classmethod
    def find_review_by_keywords(cls,keyword):
        if keyword=="": 
            print("keyword cannot be empty") 
            return []
        result = []
        with open('review.txt','r',encoding='utf-8') as f:
            reviews = f.readlines()
        
        for review in reviews:
            review_data = review.split(";;;")
            review_content = review_data[1]

            if keyword==review_content:
                result.append(Review(*review_data))
        print(result)
        return result

    @classmethod
    def find_review_by_course_id(cls,course_id):
        course_id = str(course_id)
        result = []
        with open('review.txt','r',encoding='utf-8') as f:
            reviews = f.readlines()
        
        for review in reviews:
            review_data = review.split(";;;")
            __course_id__ = review_data[-1]

            if __course_id__==course_id:
                result.append(Review(*review_data))
        
        print(result)
        return result

    @classmethod
    def reviews_overview(cls):
        with open('review.txt','r',encoding='utf-8') as f:
            reviews = f.readlines()
            l = len(reviews)
            print(l)
            return l

    def __str__(self) -> str:
        return f"{self.id_};;;{self.content};;;{self.rating};;;{self.course_id}"

        
