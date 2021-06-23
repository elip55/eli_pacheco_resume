
# HELLO WORLD!  Welcome to my resume in python!  

#  - VISION - 
# -----------------------
# MyVision1 =  to showcase coding skills while sending a resume simultaneously.
# MyVision2 =  to make the file simple enough to run without ANY elaborate python libraries.
# MyVision3 =  to write an (almost) universal output file; for the sake of convenience.
# MyVision4 =  to make a template simple enough for anyone with basic programming experience to edit and utilize
# NOTE: This program MUST be executed in python3.x which can be downloaded at: https://www.python.org

# - INSTRUCTIONS -
# -----------------------
# TODO: Be aware of the directory(file) you are in.
# Simply run this program in the chosen directory.
# Once the program is interpreted and executed, a .txt document will be written locally as my resume.
# The .txt document will be written into the directory in which it is interpreted.

# skills are displayed first in the code for ease of editing
def skills(): 
    # creating a token for proficiency measurement
    token = '* '
    # initialize the skills string
    skill_string = "Professional Skills | Proficiency"
    skill_string += '\n---------------------------------\n'
    # profesional skills as a list
    prof_skills_list = ['Teamwork', 'Creativity', 'Client Development', 'Professional Communication', 
                        'Adaptation & Collaboration', 'Time Management','Microsoft Office Suite', 
                        'macOS', 'Windows', 'iOS', 'Android OS']
    proficiency_list1 = [5,5,5,5,5,5,5,5,5,5,5,4]
    professional_skills_dict = dict(zip(prof_skills_list, proficiency_list1))
    for skill, proficiency in professional_skills_dict.items():
        skill_string += f'\t{skill} | {token*proficiency}\n'
    skill_string += '\n'
    # add technical skills string
    skill_string += "Technical Skills | Proficiency"
    skill_string += '\n---------------------------------\n'
    # technical skills as a list
    tech_skill_list = ['git & GitHub', 'jupyter lab' 'Unix Shell (bash & zsh)', 'Python',  'Computer Science',
                'Operating Systems', 'Advanced Mathematics', 'Creativity', 'Code Optimization', 
                'Regex', 'YAML files', 'C/C++', 'MATLAB', 'SOLIDWORKS']
    # proficiency measurement, as a list, corresponding directly to the above skills
    proficiency_list2 = [5,4,4,3,3,3,3,3,3,3,2,2,2,2] # NOTE: these two lists MUST be equal in length
    # combine the two lists into key:pair
    tech_skills_dict = dict(zip(tech_skill_list, proficiency_list2))
    for skill, proficiency in tech_skills_dict.items():
        skill_string += f'\t{skill} | {token*proficiency}\n'
    return skill_string

# classes for ease of editing
class HeaderInfo:
    
    def __init__(self, name, location, pn, email):
        self.name = name
        self.location = location
        self.pn = pn
        self.email = email
    
    def build_header_string(self):
        info = f'\n\t{self.name}\n\t{self.location}\n\t{self.pn}\n\t{self.email}\n\n' # create the header string
        return info

# Input the header information as strings reflecting the __init__ constructor
header = HeaderInfo('Eli Pacheco', 'Albuquerque, NM', '(505)321-5922', 'eli.pacheco55@outlook.com')

class EducationInfo:
    # education institutions can be easily added or deleted in the __init__ constructor and function
    def __init__(self, school1, degree1, grad_year1, gpa1, 
                       school2, degree2, grad_year2, gpa2):
        # school 1
        self.school1 = school1
        self.degree1 = degree1
        self.grad_year1 = grad_year1
        self.gpa1 = gpa1
        # school2 (most recent)
        self.school2 = school2
        self.degree2 = degree2
        self.grad_year2 = grad_year2
        self.gpa2 = gpa2
    
    def build_edu_string(self):
        # initialize education string and school dictionaries
        edu_string = 'EDUCATION:\n' 
        edu_string += '---------\n'
        school_two = {}
        school_one = {}
        # most recent school on top for formatting purposes
        school_two[self.school2] = self.degree2 
        school_two['Expected Grad Date'] = self.grad_year2
        school_two['GPA'] = self.gpa2
        for key,value in school_two.items(): # use 'for' loop to add key:value into education string neatly
            edu_string += f'\t{key}: {value}\n' # format the string here to make dictionary less complex
            edu_string += '\t'
            if key == 'GPA':
                edu_string += '\n'
        # add first school into dictionary
        school_one[self.school1] = self.degree1
        school_one['Graduated'] = self.grad_year1
        school_one['GPA'] = self.gpa1
        for key,value in school_one.items(): # use 'for' loop to add key:value into education string neatly
            edu_string += f'\t{key}: {value}\n' # format the string here to make dictionary less complex
            edu_string += '\t'
            if key == 'GPA':
                edu_string += '\n'
        return edu_string

# input education experience as strings, integers, and floats
# most recent on bottom, reflecting the __init__ constructor
edu = EducationInfo('New Mexico State University', 'BA, Digital Media', 2015, 3.2,
                    'University of New Mexico', 'BS, Computer Science', 2023, 3.67)

class InternInfo:
    # initialize intern experience actions
    def __init__(self, intern_co_title1, intern_action1, intern_action2, intern_action3, intern_action4, intern_action5):
        # company 1
        self.intern_co_title1 = intern_co_title1
        self.intern_action1 = intern_action1
        self.intern_action2 = intern_action2
        self.intern_action3 = intern_action3
        self.intern_action4 = intern_action4
        self.intern_action5 = intern_action5
    
    
    def build_intern_string(self):
        # initialize internship string
        intern_string = 'INTERNSHIPS AND CAREER EXPERIENCE:\n'
        intern_string += '----------------------------------\n'
        # input co information
        intern_string += f'\t{self.intern_co_title1}\n' 
        intern_string += f'\t\t{self.intern_action1}\n\t\t{self.intern_action2}\n\t\t{self.intern_action3}\n\t\t{self.intern_action4}\n\t\t{self.intern_action5}\n' 
        intern_string += f'\n'
        return intern_string # return built string for writing

# input intern experience as strings
# most recent on bottom, reflecting the __init__ constructor
intern = InternInfo('Apple - Firmware & Software Engineering, Jan 2021 - June 2021',
                     '- Using regular expression and working with a pair programmer, I conceptualized, wrote, and tested Python tools which parsed through firmware logs and extracted relevant data.\n\t\t  The data would then be written into .txt, .csv, and .vcd files as needed.',
                     '- Tasked with optimizing code, specifically when writing the output files.\n\t\t  Through collaboration, creativity, and time functions in jupyter lab, I tested ideas and implemented code that was 650% faster than the csv module.',
                     '- Systematically troubleshoot hardware, using internally written tools, to delve into systems and correct the behavior. ',
                     '- All tasks relied heavily on git, GitHub and its commands.  Pulling, testing, editing, and pushing branches for pull requests were implemented daily.  The branches on projects ranged from 4 to 100+. ',
                     '- Built and maintained professional relationships to achieve a common goal.  Gaining access to tools to help make our tool more efficient. ')

class ProfessionalInfo:
    # initiate professional experience actions
    def __init__(self, prof_co_title1, prof_action1, prof_action2, prof_action3, 
                       prof_co_title2, prof_action4, prof_action5, prof_action6):
        # company 1
        self.prof_co_title1 = prof_co_title1
        self.prof_action1 = prof_action1
        self.prof_action2 = prof_action2
        self.prof_action3 = prof_action3
        # company 2 (most recent)
        self.prof_co_title2 = prof_co_title2
        self.prof_action4 = prof_action4
        self.prof_action5 = prof_action5
        self.prof_action6 = prof_action6
    
    def build_prof_string(self):
        # initialize the professional experience string
        prof_string = 'PROFESSIONAL EXPERIENCE:\n'
        prof_string += '------------------------\n'
        # build second (most recent) company string
        prof_string += f'\t{self.prof_co_title2}\n'
        prof_string += f'\t\t{self.prof_action4}\n\t\t{self.prof_action5}\n\t\t{self.prof_action6}\n'
        prof_string += '\n'
        
        prof_string += f'\t{self.prof_co_title1}\n'
        prof_string += f'\t\t{self.prof_action1}\n\t\t{self.prof_action2}\n\t\t{self.prof_action3}\n'
        prof_string += '\n'
        return prof_string # return built string for writing

# input professional experience as strings
prof = ProfessionalInfo('Verizon - Small Business Specialist, 2015',
                        '- Connect small/medium businesses within our technological ecosystem.',
                        '- Conceptualize strategies with a team, aligned appointments, and maintain strong client relationships.',
                        '- Learn proprietary software for tracking products and clients.',
                        'Apple - Operations, 2015-2021',
                        '- Timely receiving and sending thousands of products within the confines of the store.',
                        '- Adapt to an ever-changing market within hours or minutes to better serve our customers and clients.',
                        '- Collaborate creative solutions, with a team, to place a constantly expanding product line into dimensions that remain the same.')


# calling functions and utilizing classes
write_header = header.build_header_string()
write_education = edu.build_edu_string()
write_intern = intern.build_intern_string()
write_prof = prof.build_prof_string()
write_skills = skills()

# write the .txt file 
with open('eli_pacheco_resume.txt', 'w') as writer: # with open for optimization 
    writer.write(write_header) # write header string
    writer.write(write_education) # write education string 
    writer.write(write_intern) # write intern string
    writer.write(write_prof) # write professional experience 
    writer.write(write_skills) # write skills

# I am open to any and all feedback: eli.pacheco55@outlook.com
# I will be writing the C++ version soon! 