
# HELLO WORLD!  Welcome to my resume in python!  
# My vision: to showcase my coding skills while sending a resume simultaneously.
# NOTE: This program MUST be executed in python3.x.
# There are no additional libraries needed. 

# - INSTRUCTIONS -
# -----------------------
# Simply run this program locally.
# Once the program is interpreted and executed, a .txt document will be written locally, as my resume.
# The .txt document will be saved in the same directory as the program. 


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

def edu(): # education function
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

def prof(): # professional experience function
    global professional_experience
    
    # professional experience Apple
    professional_experience += 'PROFESSIONAL EXPERIENCE:\n\tApple - Operations, 2015-2021\n'
    rtl_action1 = '- Timely receiving and sending thousands of products within the confines of the store.'
    rtl_action2 = '- Adapting to an ever-changing market within hours or minutes to better serve our customers and clients.'
    rtl_action3 = '- Collaborating creative solutions, with a team, to placing a constantly expanding product line into dimensions that remain the same.'
    professional_experience += f'\t\t{rtl_action1}\n\t\t{rtl_action2}\n\t\t{rtl_action3}\n\n' # create Apple professional experience string 
    
    # professional experience Verizon
    professional_experience += '\tVerizon - Small Business Specialist, 2015\n'
    vzw_action1 = '- Connected small/medium businesses within our technological ecosystem.'
    vzw_action2 = '- Conceptualized strategies with a team, aligned appointments, and maintained strong client relationships.'
    vzw_action3 = '- Learned proprietary software for tracking products and clients'
    professional_experience += f'\t\t{vzw_action1}\n\t\t{vzw_action2}\n\t\t{vzw_action3}\n\n' # create Verizon professional experience string
    # NOTE: nothing fancy here, open to suggestions.

def intern(): # internship and career experience function
    global internships
    # internships and career experience 
    internships += 'INTERNSHIPS AND CAREER EXPERIENCE:\n' # Begin internship string 

    internships += '\tSandia National Labs - Advanced Materials Laboratory Science, June 2021 - Present\n'

    internships += '\tApple - Firmware & Software Engineering, Jan 2021- June 2021\n'
    apl_action1 = '- Work closely with developers to write and adapt tools, in python, to help firmware teams read through logs more efficiently.'
    apl_action2 = '- Systematically troubleshoot hardware, using proprietary applications, to delve into systems and correct behavior.'
    apl_action3 = '- Use Git and GitHub to create, edit, and push local branches to the remote repo.'
    if apl_action1 not in internships: # using 'if' statement to add job responsibilities to string 
        internships += f'\t\t{apl_action1}\n\t\t{apl_action2}\n\t\t{apl_action3}\n\n' # create internships string  

def skills(): # skills function
    global skill_string
    # technical skills
    skill_string += "\nSkills:\n---------------------\n" # initialize skills string, followed by skills as a list
    skill_list = ['python', 'Computer Science', 'Git', 'GitHub', 'File Generation', 'Operating Systems', 'YAML files', 'Regex', 'Advanced Mathematics', 'Creativity', 'C/C++', 'MATLAB', 'SOLIDWORKS']
    for i in skill_list: # use a 'for' loop to display skills in a column 
        skill_string += f'\t{i}\n'

# calling functions
edu()
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
# I will be writing the C++ version soon! 