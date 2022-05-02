from random import randint

class User:
   
   __p = 31
   __mod = 100000007
   
   def __init__(self,id_=-1,username="",password=""):
      
      self.id = id_
      self.username = username
      self.password = self.encryption(self.__mod,self.__p,password)
      

   def encryption(self,password):
      p_power = 1
      hash_value = 0

      for char in password:
         hash_value = (hash_value + (ord(char)-ord('a')+1)*p_power) % self.mod
         p_power = p_power * self.p % self.mod
      return hash_value

   def login(self):
      
      core = ['user_admin.txt','user_instructor.txt','user_student.txt']
      role = {
         'user_admin.txt':'Admin',
         'user_instructor.txt':'Instructor',
         'user_student.txt':'Student'
      }
      for _file_ in core:
         with open(_file_,'r') as f:
            users = f.readlines()
         for user in users:
            user_data = user.split(";;;")
            username = user_data[1]
            password = user_data[2]

            if self.username==username and self.password==password:
               return (True,role.get(_file_),f"{self.id};;;{self.username}")
         
         return (False,None,None)


   def generate_unique_user_id(self):
      core = ['user_admin.txt','user_instructor.txt','user_student.txt']
      
      while(True):
         u_id = randint(999999999,10000000000)
         for _file_ in core:
            with open(_file_,'r') as f:
               users = f.readlines()
            for user in users:
               user_data = user.split(";;;")
               user_id = user_data[0]

               if user_id == str(u_id):
                  continue
         
         return u_id


   def extract_info(self):
      print('You have no permission to extract information')

   def view_courses(self):
      print("You have no permission to view courses")

   def view_users(self):
      print("You have no permission to view users")

   def view_reviews(self):
      print("You have no permission to view reviews")

   def remove_data(self):
      print("You have no permission to remove data")
   
   def __str__(self) -> str:
      return f"{self.id};;;{self.username};;;{self.password}"


