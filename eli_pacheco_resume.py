
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

# global variables initialized as strings 
edu_string = "" 
prof_string = ""
intern_string = ""
skill_string = ""


# header info
# opted for no function as this info will not change drastically over time
name = 'Eli Pacheco' 
location = 'Albuquerque, NM'
pn = '(505) 321 - 5922'
email = 'eli.pacheco55@outlook.com'
header = f'\n\t{name}\n\t{location}\n\t{pn}\n\t{email}\n\n' # create the header string

# functions for info that may change drastically over the course of a career 

def edu(): # education function
    global edu_string 
    schooldict = {}
    # education experience in key:value pairs
    schooldict['University of New Mexico'] = 'BS, Computer Science'
    schooldict['\tExpected Grad Date'] = 2023
    schooldict['\tCurrent GPA'] = 3.67
    schooldict['New Mexico State University'] = 'BA, Creative Media'
    schooldict['\tGraduated'] = 2015
    schooldict['\tGPA'] = 3.2
    # education string
    edu_string = 'EDUCATION:\n'
    for key,value in schooldict.items(): # use 'for' loop to add key:value into education string neatly
        edu_string += f'\t{key}: {value}\n'
        if key == '\tCurrent GPA':
            edu_string += '\n'
    edu_string += '\n'

def prof(): # professional experience function
    global prof_string
    
    # professional experience Apple
    prof_string += 'PROFESSIONAL EXPERIENCE:\n'
    # Apple professional experience
    prof_string += '\tApple - Operations, 2015-2021\n'
    rtl_action1 = '- Timely receiving and sending thousands of products within the confines of the store.'
    rtl_action2 = '- Adapting to an ever-changing market within hours or minutes to better serve our customers and clients.'
    rtl_action3 = '- Collaborating creative solutions, with a team, to placing a constantly expanding product line into dimensions that remain the same.'
    prof_string += f'\t\t{rtl_action1}\n\t\t{rtl_action2}\n\t\t{rtl_action3}\n\n' # finish Apple professional experience string 
    
    # Verizon professional experience
    prof_string += '\tVerizon - Small Business Specialist, 2015\n'
    vzw_action1 = '- Connected small/medium businesses within our technological ecosystem.'
    vzw_action2 = '- Conceptualized strategies with a team, aligned appointments, and maintained strong client relationships.'
    vzw_action3 = '- Learned proprietary software for tracking products and clients.'
    prof_string += f'\t\t{vzw_action1}\n\t\t{vzw_action2}\n\t\t{vzw_action3}\n\n' # finish Verizon professional experience string
    # NOTE: nothing fancy here, open to suggestions.

def internships(): # internships and career experience function
    global intern_string
    
    # internships and career experience 
    intern_string += 'INTERNSHIPS AND CAREER EXPERIENCE:\n' # write title 
    
    intern_string += '\tSandia National Labs, June 2021 - Present\n'
    sandia_action1 = '*to be written*'
    intern_string += f'\t\t{sandia_action1}\n\n'
    # Apple internship experience 
    intern_string += '\tApple - Firmware & Software Engineering, Jan 2021 - June 2021\n' 
    apl_action1 = '- Worked closely with developers to write and adapt tools, in python, to help firmware teams read through logs more efficiently.'
    apl_action2 = '- Systematically troubleshot hardware, using proprietary applications, to delve into systems and correct behavior.'
    apl_action3 = '- Used git and GitHub to create, edit, and push local branches to the remote repo.'
    if apl_action1 not in intern_string: # use basic 'if' statement to add career experience to intern_string 
        intern_string += f'\t\t{apl_action1}\n\t\t{apl_action2}\n\t\t{apl_action3}\n\n' # finish Apple experience string 

def skills(): # skills function
    global skill_string
    # technical skills
    skill_string += "\nSkills:\n---------------------\n" # initialize skills string, followed by skills as a list
    skill_list = ['Python', 'Unix Shell (bash & zsh)', 'Computer Science', 'git & GitHub', 'Operating Systems', 
                  'YAML files', 'Regex', 'Advanced Mathematics', 'Creativity', 'C/C++', 'MATLAB', 'SOLIDWORKS']
    for skill in skill_list: # use a 'for' loop to display skills in a column 
        skill_string += f'\t{skill}\n'

# calling functions
edu()
prof()
internships()
skills()

# write the .txt file 
with open('eli_pacheco_resume.txt', 'w') as w: # with open for optimization 
    w.write(header) # write header
    w.write(edu_string) # write edu_string from function
    w.write(intern_string) # write intern_string from function 
    w.write(prof_string) # write professional experience 
    w.write(skill_string) # write skills from function

# I am open to any and all feedback: eli.pacheco55@outlook.com
# I will be writing the C++ version soon! 