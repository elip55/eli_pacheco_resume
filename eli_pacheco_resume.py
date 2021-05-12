
# HELLO WORLD!  Welcome to my resume in python!  
# My vision: to showcase my coding skills while sending a resume simultaneously.
# NOTE: This program MUST be executed in python3.x.
# There are no additional libraries needed. 

# - INSTRUCTIONS -
# -----------------------
# Simply run this program.
# Once the program is compiled and executed, a .txt document will be saved locally as my resume.


# global variables as strings
education = ""
professional_experience = ""
internships = ""
skill_string = ""

# header info
# opted for no function as this info will not change drastically over time
name = 'Eli Pacheco' 
location = 'Albuquerque, NM'
pn = '(505) 321 - 5922'
email = 'eli.pacheco55@outlook.com'
header = f'\n\t{name}\n\t{location}\n\t{pn}\n\t{email}\n\n' # create the header string

# functions for info that may change drastically over the course of a career 
def ed():
    # education info
    global education 
    education = f'EDUCATION:\n'
    schooldict = {'University of New Mexico': 'BS, Computer Science',  # dictionary to store key:value education items
                    'Expected Grad Date': 2023,
                    'Current GPA': 3.67,
                     'New Mexico State University': 'BA, Creative Media',
                     'Graduated': 2015,
                     'GPA': 3.2} 
    for key,value in schooldict.items(): # use 'for' loop to add key:value into education string neatly
        education += f'\t{key}: {value}\n'
        if key == 'Current GPA': # 'if' statement to seperate the two degrees 
            education+= f'\n'
    education += '\n'

def prof():
    global professional_experience
    
    # professional experience Apple
    professional_experience += 'PROFESSIONAL EXPERIENCE:\n\tApple - Operations, 2015-2021\n'
    rtl_action1 = '- Timely receiving and sending thousands of products within the confines of the store.'
    rtl_action2 = '- Adapting to an ever-changing market within hours or minutes to better serve our customers and clients.'
    rtl_action3 = '- Collaborating creative solutions, with a team, to placing a constantly expanding product line into dimensions that remain the same.'
    professional_experience += f'\t\t{rtl_action1}\n\t\t{rtl_action2}\n\t\t{rtl_action3}\n' # create Apple professional experience string 
    
    # professional experience Verizon
    professional_experience += '\tVerizon - Small Business Specialist, 2015\n'
    vzw_experience1 = '- Connected small/medium businesses within our technological ecosystem.'
    vzw_experience2 = '- Conceptualized strategies with a team, aligned appointments, and maintained strong client relationships.'
    vzw_experience3 = '- Learned proprietary software for tracking products and clients'
    professional_experience += f'\t\t{vzw_experience1}\n\t\t{vzw_experience2}\n\t\t{vzw_experience3}\n\n' # create Verizon professional experience string
    # nothing fancy here, open to suggestions.
    
def intern():
    global internships
    # internships and career experience 
    internships += 'INTERNSHIPS AND CAREER EXPERIENCE:\n\tApple - Firmware & Software Engineering, Jan 2021- June 2021\n'
    intern_action1 = '- Work closely with developers to write and adapt tools, in python, to help firmware teams read through logs more efficiently.'
    intern_action2 = '- Systematically troubleshoot hardware, using proprietary applications, to delve into systems and correct behavior.'
    intern_action3 = '- Use Git and GitHub to create, edit, and push local branches to the remote repo.'
    if intern_action1 not in internships: # using 'if' statement to add job responsibilities to string 
        internships += f'\t\t{intern_action1}\n\t\t{intern_action2}\n\t\t{intern_action3}\n\n' # create internships string  

def skills():
    global skill_string
    # technical skills
    skill_string += "\nSkills:\n---------------------\n" # initialize skills string, followed by skills as a list
    skill_list = ['python', 'Computer Science', 'Git', 'GitHub', 'File Generation', 'Operating Systems', 'YAML files', 'Regex', 'Advanced Mathematics', 'Creativity', 'c/c++', 'MATLAB', 'SOLIDWORKS']
    for i in skill_list: # use a 'for' loop to display skills a column 
        if i not in skill_string:
            skill_string += f'\t{i}\n'

# calling functions
ed()
prof()
intern()
skills()

# write the .txt file 
with open('eli_pacheco_resume.txt', 'w') as w: # with open for optimization 
    w.write(header) # write header
    w.write(education) # write education from function
    w.write(internships) # write internships from function 
    w.write(professional_experience) # write professional experience 
    w.write(skill_string) # write skills from function

# I am open to any and all feedback: eli.pacheco55@outlook.com
# Look for the C++ version soon! 