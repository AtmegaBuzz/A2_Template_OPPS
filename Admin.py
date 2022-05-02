from User import User
import json 
import glob

class Admin(User):
    
    def __init__(self, id_=-1, username="", password=""):
        super().__init__(id_, username, password)

    def register_admin(self):
        pass

    def extract_course_info(self):
        filename = "data/course_data/raw_data2.txt"
        with open(filename,'r') as f:
            raw_data = f.read()
        course_data = json.loads(raw_data)["unit"]["items"]

        with open('courses.txt','a') as f:
            
            for course in course_data:
                course_id = course.get("id")
                course_title = course.get("title")
                image_100x100 = course.get("image_100x100")
                headline = course.get("headline").replace("\n"," ")
                num_of_subscribers = course.get("num_subscribers")
                avg_rating = course.get("avg_rating")
                course_content_length = course.get("content_info").replace("total hours","")

                f.writelines(f"{course_id};;;{course_title};;;{image_100x100};;;{headline};;;{num_of_subscribers};;;{avg_rating};;;{course_content_length}\n")

                   

    def extract_review_info(self):
        filenames = glob.glob("data/review_data/*.json")

        for filename in filenames: 
            with open(filename,'r') as f:
                raw_data = f.read()

            review_data = json.loads(raw_data)
            reviews = review_data['results']

            with open('review.txt','a') as f:
                
                for review in reviews:
                    course_id = review.get('id')
                    review_content = review.get('content').replace("\n"," ")
                    review_rating = review.get('rating')
                    review_id = review.get('user').get('id')

                    f.write(f"{review_id};;;{review_content};;;{review_rating};;;{course_id}\n")
            
    def extract_students_info(self):
        filenames = glob.glob("data/review_data/*.json")
        for filename in filenames:
            with open(filename,'r') as f:
                raw_data = f.read()      
            
            review_data = json.loads(raw_data)
            reviews = review_data['results']

            with open('user_student.txt','a') as f:
                for review in reviews:
                    user_id = review.get('user').get('id')
                    username = review.get('user').get('name').lower().replace(" ","_")
                    user_title = review.get('user').get('title')
                    user_image = review.get('user').get('image_50x50')
                    user_initials = review.get('user').get('initials')
                    review_id = review.get('id')
                    password = f"{user_initials}{user_id}{user_initials}"

                    f.write(f"{user_id};;;{username};;;{password};;;{user_title};;;{user_image};;;{user_initials};;;{review_id}\n")
                 

    def extract_instructor_info(self):
        filename = "data/course_data/raw_data2.txt"
        with open(filename,'r') as f:
            raw_data = f.read()
        course_data = json.loads(raw_data)["unit"]["items"]

        with open('courses.txt','a') as f:
            
            for course in course_data:
                instrustors = course.get("visible_instructors",[])
                course_id = course.get('id')
                
                 

                for instrustor in instrustors:
                    instrustor_id = instrustor.get("id")
                    username = instrustor.get("title")
                    password = instrustor.get("image_100x100")
                    display_name = instrustor.get("headline").replace("\n"," ")
                    job_title = instrustor.get("num_subscribers")
                    image_100x100 = instrustor.get("avg_rating")
                    course_content_length = instrustor.get("content_info").replace("total hours","")

                    f.writelines(f"{course_id};;;{course_title};;;{image_100x100};;;{headline};;;{num_of_subscribers};;;{avg_rating};;;{course_content_length}\n")

    def extract_info(self):
        self.extract_course_info()
        self.extract_instructor_info()
        self.extract_review_info()
        self.extract_students_info()

    def remove_data(self):
        core_data_files = ['course.txt','review.txt','user_student.txt','user_instructor.txt']
        for core_file in core_data_files:
            with open(core_file,'w') as f:
                f.write("")
        

    def view_courses(self,args=[]):
        pass

    def view_users(self):

        admins = sum(1 for line in open('user_admin.txt'))
        instructors = sum(1 for line in open('user_instructor.txt'))
        students = sum(1 for line in open('user_student.txt'))

        print(f"admins:{admins}, instructors:{instructors}, students:{students}")

    def view_reviews(self,args=[]):
        pass

    def __str__(self) -> str:
        return super().__str__()
        


admin = Admin()
admin.extract_students_info()