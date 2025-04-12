class Coder:
    def __init__(self, name, language, experience):
        self.__name = name 
        self.language = language
        self.experience = experience  
        
    def getter(self):
        return self.__name.upper()# getter for encapsulated variable name
    
    def set_name(self, name):
        self.__name = name # setter for encapsulted variable name
        
class FrontEndDev(Coder):
    def __init__(self, name, language, experience, framework):
        super().__init__(name, language, experience)
        self.framework = framework
        
    def introduction(self):
        print(f"Hello, I am {self.getter()}. with over {self.experience} years of coding and specializing in {self.language} and {self.framework}.")
        
    def work(self):
        print(f"Building user interfaces using {self.language} and {self.framework}.")

class BackEndDev(Coder):
    def __init__(self, name, language, experience, framework):
        super().__init__(name, language, experience)
        self.framework = framework
        
    def introduction(self):
        print(f"Hello, I am {self.getter()}. with over {self.experience} years of coding and specializing in {self.language} and {self.framework}.")
        
    def work(self):
        print(f"Building server logic and APIs using {self.language} and {self.framework}.")
        
class FullstackDev(Coder):
    def __init__(self, language, framework):
        super().__init__("Anonymous", language, 0)
        self.framework = framework
    def work(self):        
        print(f"Building both front-end and back-end applications using {self.language} and {self.framework}.")
        
#creating instances classes
frontend = FrontEndDev("Derrick", "JavaScript", 3, "React")

backend = BackEndDev("Derrick", "Python", 5, "Django")
fullstack = FullstackDev("Python", "Django")


for coding in [frontend, backend]:
    coding.introduction()
    coding.work()
    print("-------------------------------------")
fullstack.work()
