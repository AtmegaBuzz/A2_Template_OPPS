
class User:
   
   __p = 31
   __mod = 100000007
   
   def __init__(self,id_=-1,username="",password=""):
      
      self.id = id_
      self.username = username
      self.password = self.encryption(self.__mod,self.__p,password)
      

   @staticmethod
   def encryption(mod,p,password):
      p_power = 1
      hash_value = 0

      for char in password:
         hash_value = (hash_value + (ord(char)-ord('a')+1)*p_power) % mod
         p_power = p_power * p % mod
      return hash_value

   def login(self):
      pass

   def generate_unique_user_id(self):
      pass

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
      return "{};;;{};;;{}".format(self.id,self.username,self.password)


