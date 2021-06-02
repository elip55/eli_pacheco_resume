
# HELLO WORLD!  Welcome to my resume in python!  

#  - VISION - 
# -----------------------
# MyVision1 =  to showcase my coding skills while sending a resume simultaneously.
# MyVision2 =  to make the file simple enough to run without ANY elaborate python libraries.
# MyVision3 =  to write an output file (almost) universal; for the sake of convenience.
# MyVision4 =  to make a template simple enough for anyone with basic programming experience to edit
# NOTE: This program MUST be executed in python3.x.

# - INSTRUCTIONS -
# -----------------------
# Simply run this program locally.
# Once the program is interpreted and executed, a .txt document will be written locally as my resume.
# The .txt document will be saved in the same directory(file) as the saved program. 

# Skills are displayed first in the code for ease of editing
skill_string = ""

def skills(): # skills function
    global skill_string
    # technical skills
    skill_string += "\nSkills:\n---------------------\n" # initialize skills string, followed by skills as a list
    skill_list = ['Python', 'Unix Shell (bash & zsh)', 'Computer Science', 'git & GitHub', 'Operating Systems', 
                  'Code Optimization', 'YAML files', 'Regex', 'Advanced Mathematics', 'Creativity', 'C/C++', 'MATLAB', 
                  'SOLIDWORKS']
    for skill in skill_list: # use a 'for' loop to display skills in a column 
        skill_string += f'\t{skill}\n'

# classes of resume information for anyone to edit easily
class HeaderInfo:
    
    def __init__(self, name, location, pn, email):
        self.name = name
        self.location = location
        self.pn = pn
        self.email = email
    
    def build_header_string(self):
        info = f'\n\t{self.name}\n\t{self.location}\n\t{self.pn}\n\t{self.email}\n\n' # create the header string
        return info

# Input the header information as strings
header = HeaderInfo('Eli Pacheco', 'Albuquerque, NM', '(505)321-5922', 'eli.pacheco55@outlook.com')

class EducationInfo:
    # education options can be easily added or deleted in the __init__ constructor   
    def __init__(self, school1, degree1, grad_year1, gpa1, 
                       school2, degree2, grad_year2, gpa2):
        # school 1
        self.school1 = school1
        self.degree1 = degree1
        self.grad_year1 = grad_year1
        self.gpa1 = gpa1
        # school2
        self.school2 = school2
        self.degree2 = degree2
        self.grad_year2 = grad_year2
        self.gpa2 = gpa2
    
    def build_edu_string(self):
        undergrad_dict = {}
        # if grad school is the same as undergrad, create new dictionary. EX: grad_dict = {}
        # education experience in key:value pairs
        undergrad_dict[f'{self.school2}'] = f'{self.degree2}'
        undergrad_dict['\tExpected Grad Date'] = f'{self.grad_year2}'
        undergrad_dict['\tCurrent GPA'] = f'{self.gpa2}'
        undergrad_dict[f'{self.school1}'] = f'{self.degree1}'
        undergrad_dict['\tGraduated'] = f'{self.grad_year1}'
        undergrad_dict['\tGPA'] = f'{self.gpa1}'
        # initialize education string
        edu_string = 'EDUCATION:\n' 
        for key,value in undergrad_dict.items(): # use 'for' loop to add key:value into education string neatly
            edu_string += f'\t{key}: {value}\n'
            if key == '\tCurrent GPA': #NOTE: will need to edit this condition accordingly 
                edu_string += '\n'
        edu_string += '\n'
        return edu_string

# input education experience as strings, integers, and floats
edu = EducationInfo('New Mexico State University', 'BA, Digital Media', 2015, 3.2,
                    'University of New Mexico', 'BS, Computer Science', 2023, 3.67)

class InternInfo:
    
    def __init__(self, co_title1, action1, action2, action3, action4,
                       co_title2, action5):
        # company 1
        self.co_title1 = co_title1
        self.action1 = action1
        self.action2 = action2
        self.action3 = action3
        self.action4 = action4
        self.co_title2 = co_title2
        self.action5 = action5
        # company 2
        self.co_title2 = co_title2
        self.action5 = action5
    
    def build_intern_string(self):
        # initialize internship string
        intern_string = 'INTERNSHIPS AND CAREER EXPERIENCE:\n'
        # create second company string
        intern_string += f'\t{self.co_title2}\n'
        intern_string += f'\t\t{self.action5}\n'
        intern_string += f'\n'
        # create oldest company string
        intern_string += f'\t{self.co_title1}\n' 
        intern_string += f'\t\t{self.action1}\n\t\t{self.action2}\n\t\t{self.action3}\n\t\t{self.action4}\n' 
        intern_string += f'\n'
        return intern_string # return built string for writing

# input intern experience as strings
intern = InternInfo('Apple - Firmware & Software Engineering, Jan 2021 - June 2021',
                     '- Work closely with developers to write and adapt tools, in python, to help firmware teams read through logs more efficiently.',
                     '- Systematically troubleshoot hardware, using proprietary applications, to delve into systems and correct behavior.',
                     '- Use git and GitHub to create, edit, and push local branches to the remote repo.',
                     '- Build and maintain strong professional relationships with several teams to achieve a common goal.',
                     'Sandia National Labs - Advanced Materials Laboratory, June 2021 - Present',
                      '*to be written*')

class ProfessionalInfo:
    
    def __init__(self, co_title1, action1, action2, action3, 
                       co_title2, action4, action5, action6):
        # company 1
        self.co_title1 = co_title1
        self.action1 = action1
        self.action2 = action2
        self.action3 = action3
        # company 2
        self.co_title2 = co_title2
        self.action4 = action4
        self.action5 = action5
        self.action6 = action6
    
    def build_prof_string(self):
        prof_string = 'PROFESSIONAL EXPERIENCE:\n'
        prof_string += f'\t{self.co_title1}\n'
        prof_string += f'\t\t{self.action1}\n\t\t{self.action2}\n\t\t{self.action3}\n\n'
        prof_string += f'\t{self.co_title2}\n'
        prof_string += f'\t\t{self.action4}\n\t\t{self.action5}\n\t\t{self.action6}\n'
        return prof_string

# input professional experience as strings
prof = ProfessionalInfo('Apple - Operations, 2015-2021',
                        '- Timely receiving and sending thousands of products within the confines of the store.',
                        '- Adapt to an ever-changing market within hours or minutes to better serve our customers and clients.',
                        '- Collaborate creative solutions, with a team, to place a constantly expanding product line into dimensions that remain the same.',
                        'Verizon - Small Business Specialist, 2015',
                        '- Connect small/medium businesses within our technological ecosystem.',
                        '- Conceptualize strategies with a team, aligned appointments, and maintain strong client relationships.',
                        '- Learn proprietary software for tracking products and clients.')


# calling functions and utilizing parent classes
write_header = header.build_header_string()
write_education = edu.build_edu_string()
write_intern = intern.build_intern_string()
write_prof = prof.build_prof_string()
skills()

# write the .txt file 
with open('eli_pacheco_resume.txt', 'w') as writer: # with open for optimization 
    writer.write(write_header) # write header string
    writer.write(write_education) # write education string 
    writer.write(write_intern) # write intern string
    writer.write(write_prof) # write professional experience 
    writer.write(skill_string) # write skills

# I am open to any and all feedback: eli.pacheco55@outlook.com
# I will be writing the C++ version soon! 