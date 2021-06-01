
# HELLO WORLD!  Welcome to my resume in python!  

#  - VISION - 
# -----------------------
# MyVision1 =  to showcase my coding skills while sending a resume simultaneously.
# MyVision2 =  to make the file simple enough to run without ANY elaborate python libraries. 
# MyVision3 =  to write an (almost) universal file for the sake of convenience.
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

# Input the necessary information to build the header string
header = HeaderInfo('Eli Pacheco', 'Albuquerque, NM', '(505)321-5922', 'eli.pacheco55@outlook.com')

class EducationInfo:
    
    def __init__(self, school2, degree2, grad_year2, gpa2, school1, degree1, grad_year1, gpa1):
        self.school2 = school2
        self.degree2 = degree2
        self.grad_year2 = grad_year2
        self.gpa2 = gpa2
        
        self.school1 = school1
        self.degree1 = degree1
        self.grad_year1 = grad_year1
        self.gpa1 = gpa1
    
    def build_edu_string(self):
        schooldict = {}
        # education experience in key:value pairs
        schooldict[f'{self.school2}'] = f'{self.degree2}'
        schooldict['\tExpected Grad Date'] = f'{self.grad_year2}'
        schooldict['\tCurrent GPA'] = f'{self.gpa2}'
        schooldict[f'{self.school1}'] = f'{self.degree1}'
        schooldict['\tGraduated'] = f'{self.grad_year1}'
        schooldict['\tGPA'] = f'{self.gpa1}'
        # education string
        # education string
        edu_string = 'EDUCATION:\n'
        for key,value in schooldict.items(): # use 'for' loop to add key:value into education string neatly
            edu_string += f'\t{key}: {value}\n'
            if key == '\tCurrent GPA':
                edu_string += '\n'
        edu_string += '\n'
        return edu_string

# input necessary information to build the education string
edu = EducationInfo('University of New Mexico', 'BS, Computer Science', '2023', '3.67',
                    'New Mexico State University', 'BA, Digital Media', '2015', '3.2')

class InternInfo:
    
    def __init__(self, co_title1, action1, action2, action3, action4):
        self.co_title1 = co_title1
        self.action1 = action1
        self.action2 = action2
        self.action3 = action3
        self.action4 = action4
        
    def build_intern_string(self):
        intern_string = 'INTERNSHIPS AND CAREER EXPERIENCE:\n' # write title 
        intern_string += f'\t{self.co_title1}\n' 
        intern_string += f'\t\t{self.action1}\n\t\t{self.action2}\n\t\t{self.action3}\n\t\t{self.action4}\n\n' # finish Apple experience string 
        return intern_string
    
# input necessary intern information
intern = InternInfo('Apple - Firmware & Software Engineering, Jan 2021 - June 2021',
                     '- Work closely with developers to write and adapt tools, in python, to help firmware teams read through logs more efficiently.',
                     '- Systematically troubleshoot hardware, using proprietary applications, to delve into systems and correct behavior.',
                     '- Use git and GitHub to create, edit, and push local branches to the remote repo.',
                     '- Build and maintain strong professional relationships with several teams to achieve a common goal.')


class ProfessionalInfo:
    
    def __init__(self, co_title1, action1, action2, action3, co_title2, action4, action5, action6):
        self.co_title1 = co_title1
        self.action1 = action1
        self.action2 = action2
        self.action3 = action3
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
with open('eli_pacheco_resume.txt', 'w') as w: # with open for optimization 
    w.write(write_header) # write header string
    w.write(write_education) # write education string 
    w.write(write_intern) # write intern string
    w.write(write_prof) # write professional experience 
    w.write(skill_string) # write skills

# I am open to any and all feedback: eli.pacheco55@outlook.com
# I will be writing the C++ version soon! 