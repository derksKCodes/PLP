# Base class Coder 
class Coder:
    def __init__(self, name, language, experience):
        self.__name = name  # Encapsulated attribute (private)
        self.language = language
        self.experience = experience  
    
    # Getter method to get the private attribute __name
    def getter(self):
        return self.__name.upper()  # Returns the name in uppercase
    
    # Setter method to set the private name attribute
    def set_name(self, name):
        self.__name = name


# Derived class FrontEndDev inherits from Coder
class FrontEndDev(Coder):
    def __init__(self, name, language, experience, framework):
        # super() is used to call the __init__ method of the parent class (Coder)
        # It allows  to reuse the initialization logic from the parent class
        super().__init__(name, language, experience)
        self.framework = framework  # Specific attribute for FrontEndDev

    def introduction(self):
        print(f"Hello, I am {self.getter()}. With over {self.experience} years of coding and specializing in {self.language} and {self.framework}.")

    def work(self):
        print(f"Building user interfaces using {self.language} and {self.framework}.")


# Derived class BackEndDev inherits from Coder
class BackEndDev(Coder):
    def __init__(self, name, language, experience, framework):
        # super() calls the parent class constructor
        super().__init__(name, language, experience)
        self.framework = framework

    def introduction(self):
        print(f"Hello, I am {self.getter()}. With over {self.experience} years of coding and specializing in {self.language} and {self.framework}.")

    def work(self):
        print(f"Building server logic and APIs using {self.language} and {self.framework}.")


# Derived class FullstackDev inherits from Coder
class FullstackDev(Coder):
    def __init__(self, language, framework):
        # This coder has no name and 0 experience (default values provided)
        super().__init__("Anonymous", language, 0)
        self.framework = framework

    def work(self):
        print(f"Building both front-end and back-end applications using {self.language} and {self.framework}.")


# Creating instances of each developer type
frontend = FrontEndDev("Derrick", "JavaScript", 3, "React")
backend = BackEndDev("Derrick", "Python", 5, "Django")
fullstack = FullstackDev("Python", "Django")

# Loop through frontend and backend to show polymorphism
for coding in [frontend, backend]:
    coding.introduction()
    coding.work()
    print("-------------------------------------")

# Fullstack dev work (no introduction because it's not defined in the class)
fullstack.work()
