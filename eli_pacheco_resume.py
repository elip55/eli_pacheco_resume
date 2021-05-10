
# HELLO WORLD!  Welcome to my resume in python!  
# I am open to any and all feedback: eli.pacheco55@gmail.com
# This program MUST be run with python3.x.
# Simply run this program.
# Once program is finished, it will write a .txt document for the reader as my resume.

# header info
name = 'Eli Pacheco' 
location = 'Albuquerque, NM'
pn = '(505) 321 - 5922'
email = 'eli.pacheco55@outlook.com'

header = f'\n\t{name}\n\t{location}\n\t{pn}\n\t{email}\n\n' # create the header string

# education info
education = f'EDUCATION:\n'
schooldict = {'University of New Mexico': 'BA, Computer Science'} # key:value pair for UNM:degree
egd = 'Expected grad date: 2023' 
GPA = 'Current GPA: 3.67'
for key,value in schooldict.items(): # use for loop to add key:value into education string 
    education += f'\t{key}: {value}'
education += f'\n\t{egd}\n\t{GPA}\n\n' # create the education string

# professional experience 
professional_experience = 'PROFESSIONAL EXPERIENCE:\n\tApple - Operations, 2015-2021\n'
rtl_action1 = '- Timely receiving and sending thousands of products within the confines of the store.'
rtl_action2 = '- Adapting to an ever-changing market within hours or minutes to better serve our customers and clients.'
rtl_action3 = '- Collaborating creative solutions, with a team, to placing a constantly expanding product line into dimensions that remain the same.'
professional_experience += f'\t\t{rtl_action1}\n\t\t{rtl_action2}\n\t\t{rtl_action3}\n\t\t' # create professional experience string 
# nothing fancy here, open to suggestions.

# internships and career experience 
internships = 'INTERNSHIPS AND CAREER EXPERIENCE:\n\tApple - Firmware, Jan 2021- June 2021\n'
intern_action1 = '- Work closely with developers to write and adapt tools, in python, to help firmware teams read through logs more efficiently.'
intern_action2 = '- Systematically troubleshoot hardware, using proprietary applications, to delve into systems and correct behavior.'
intern_action3 = '- Used git and GitHub to create, edit, and push local branches to the remote repo.'
if intern_action1 not in internships: # using 'if' statement to add job responsibilities to string 
    internships += f'\t\t{intern_action1}\n\t\t{intern_action2}\n\t\t{intern_action3}\n\n' # create internships string 

# technical skills
skill_string = "\nSkills:\n---------------------\n" # initialize skills string, followed by skills as a list
skill_list = ['python', 'Computer Science', 'Git', 'GitHub', 'Operating Systems', 'Mathematics', 'c/c++', 'MATLAB', 'SOLIDWORKS']
for i in skill_list: # use a 'for' loop to display skills a column 
    if i not in skill_string:
        skill_string += f'\t{i}\n'

with open('eli_pacheco_resume.txt', 'w') as w: # with open for optimization 
    w.write(header)
    w.write(education)
    w.write(internships)
    w.write(professional_experience)
    w.write(skill_string)
