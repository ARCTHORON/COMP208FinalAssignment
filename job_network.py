# Student Name:
# Student ID:
import numpy as np
from numpy.linalg import norm

class Company:
    """ represents a company
    attributes: name (str), location (str)

    example:
    >>>jeff=Company("Flex", "seal")
    self.name="Flex"
    self.location="seal"

    >>>jeff=Company("joe")
    error incorrect arguments

    >>>jeff=Company("jeff", "joe")
    self.name="jeff"
    self.location="joe"
    """

    def __init__(self, comp_name, loc):
        """
        inputs: a string, a string
        outputs: none
        initializing of class
        """
        self.name=str(comp_name)
        self.location=str(loc)#just sets the attrbutes
    
    def __str__(self):
        """
        changes the built in function of str for this class to be 
        the desired ouput

        example: (for test.name=Geroge and test.location=Ohio)
        >>>print(test)
        Company Name:Geroge
        Location:Ohio

        >>>str(test)
        Company Name:Geroge\nLocation:Ohio

        >>>str("not this class")
        "not this class"
        """
        return ("Company Name:"+self.name+"\nLocation:"+self.location)
    
class JobOffer:
    """ represents a job offer
    instance attributes: title (str), company (Company),
    contract (str), salary (float), description (sum

    class attribute: nb_jobs(int)

    example:
    >>>job1=JobOffer("hi", "bye", "fake", 100, "not good")
    self.title="hi"
    self.company="bye
    self.contract="fake"
    self.salary=100
    self.description="not good"
    self.ref=1

    >>>job1=JobOffer("hi", "bye", "fake", 100, "not good")
    self.title="hi"
    self.company="bye
    self.contract="fake"
    self.salary=100
    self.description="not good"
    self.ref=2

    >>>job1=JobOffer("engineer", "bye", "good", 100, "not good")
    self.title="engineer"
    self.company="bye
    self.contract="good"
    self.salary=100
    self.description="not good"
    self.ref=3
    """
    
    nb_jobs=0
    
    def __init__(self, title, comp, contract, salary, description):
        self.title=str(title)
        self.company=comp
        self.contract=str(contract)
        self.salary=float(salary)
        self.description=str(description)
        self.nb_jobs+=1 #increments the reference number
        self.ref=self.nb_jobs
        
    def update_description(self, desc):
        """
        inputs: a string
        outputs:none

        changes the instance attribute description to the provided string

        ex:
        >>>test.update_description("hi")
        test.description="hi"

        >>>test.update_description("9")
        test.description="9"

        >>>test.update_description("this is many words")
        test.description="this is many words"

        """
        self.description=desc
            
    def __str__(self):
        return ("Reference: "+str(self.ref)+ "\nTitle: "+str(self.title)\
        +"\nCompany Name:"+str(self.company.name)+"\nLocation:"+str(\
            self.company.location)\
        +"\nContract: "+str(self.contract)+"\nDescription: "+str(self.description)+\
        "\nSalary: "+str(self.salary))
    
class Candidate:
    """ represents a candidate
    attributes: first_name (str), last_name(str), open_to_work (int)
    email (str), skills (str)

    """
    def __init__(self, first, last, ope, email, skills):
        """
        inputs: a string, a string, an integer(0 or 1), 
        a string of a valid email, a string
        outputs:none

        initialises the class
        """
        self.first_name=str(first)
        self.last_name=str(last)
        self.open_to_work=int(ope)
        self.set_email(email)
        temp_skill=(str(skills).lower())
        self.skills=temp_skill
        
    def get_skills_list(self):
        """
        input: none
        output: a list of skills

        converts the string self.skills into a list
        with delimeter "-"
        then returns the list

        example: 
        with self.skills="joe"
        >>>self.get_skills_list()
        ["joe"]

        with self.skills="joe-joe"
        >>>self.get_skills_list()
        ["joe", "joe"]

        with self.skills="joe joe"
        >>>self.get_skills_list()
        ["joe joe"]
        """
        temp=self.skills
        temp=temp.split("-")#splits
        for x in range(len(temp)):
            temp[x]=str(temp[x]).strip()#removes spaces
        return temp
    
    def set_email(self, email):
        """
        imput: a string of an email
        output: none

        sets the instance attribute self.email to the 
        value of email if it is valid

        example:
        >>>self.set_email("fakeemail@haha")
        "Error in Class Candidate: Email format error:"\
        "missing/too many @ and .com occurences"

        >>>self.set_email(67)
        "Error in Class Candidate: The input email should"\
        "be a string"

        >>>self.set_email("realemail@true.com")
        self.email="realemail@true.com"
        """
        mail=email
        if type(mail)!=str:#the type error check
            raise TypeError("Error in Class Candidate: The input email should"\
                             "be a string")
        counter_at=0
        for x in range(len(email)):
            if email[x]=="@":
                counter_at+=1
        counter_com=0
        length=len(email)
        if len(email)<4:
            raise ValueError("Error in Class Candidate: Email format error:"\
                            "missing/too many @ and .com occurences")
        if email[length-4]=="." and email[length-3]=="c":
            if email[length-2]=="o" and email[length-1]=="m":
                counter_com=1
        if (counter_com==0) or (counter_at!=1):#if either are wrong
            raise ValueError("Error in Class Candidate: Email format error:"\
                            "missing/too many @ and .com occurences")
        self.mail=email
        
    def add_skill(self, skill):
        """
        imput: a string 
        output: none

        adds the new skill string to the pre existing string
        at self.skills
        """
        try:
            skill=skill.lower()#makes lowercase
            self.skills=self.skills+"-"+skill#adds skill thats choppable
        except:
            raise ValueError("Error in Class Candidate: The input skill should"\
                             "be a string")#in case it goes wrong
    
class JobNetwork:
    
    def __init__(self, jobs, candidates):
        self.jobs_list=jobs
        self.candidate_list=candidates
        
    def find_job_per_ref(self, reference):
        for x in range(len(self.jobs_list)):
            if ((self.jobs_list)[x]).ref==reference:
                return self.jobs_list[x]
        return 0#if its not there
    
    def skills_in_job(self, candidate):
        temp_list=Candidate.get_skills_list(candidate)
        new_dict={}#dictionary to fkill
        for x in range(len(self.jobs_list)):
            new_dict[self.jobs_list[x]]=[]
            for x in range(len(temp_list)):#i kinda run out of room in next line
                if lower(temp_list[x]) in (self.jobs_list[x].title).lower() or\
                   lower(temp_list[x])in(self.jobs_list[x].title).lower():
                    new_dict[self.jobs_list[x].ref].append(1)
                else:#just adding to the new dictionary
                    new_dict[self.jobs_list[x].ref].append(0)
        return new_dict#returning it
                    
    def compute_similarity(self, candidate_list, job_list):
        candidate_vector=np.array(candidate_list)
        job_vector=np.array(job_list)
        return np.dot(candidate_vector, job_vector)/((\
        np.linalg.norm(job_vector)*\
        np.linalg.norm(candidate_vector)))#plugging in the formula
        
    def compute_similarity_all(self, candidate):
        skills= [1]*len(Candidate.get_skills_list(candidate.skills))
        skill_dict=self.skills_in_job(candidate)
        new_dict={}
        for key in skill_dict.keys():#does it for all of them
            new_dict[key]=self.compute_similarity(skills, skill_dict.get(key))
        return new_dict
    
    def recommend_job(self, candidate):
        compatibility=self.compute_similarity_all(candidate)
        return max(compatibility)#finds highest one
            
    def print_recommended_job(self, candidate):
        key=self.recommend_job(candidate)
        print(self.find_job_per_ref(key))#prints the recommendation
    
    
        
        
