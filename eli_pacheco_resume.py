
# HELLO WORLD!  Welcome to my resume in python!  
# I am open to any and all feedback: eli.pacheco55@gmail.com
# This program MUST be run with python3 
# 
class bcolors:
    HEADER    = '\033[95m'
    OKBLUE    = '\033[94m'
    OKGREEN   = '\033[92m'
    WARNING   = '\033[93m'
    FAIL      = '\033[91m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC      = '\033[0m'

    
# header
name = 'Eli Pacheco' 
location = 'Albuquerque, NM'
pn = '(505) 321 - 5922'
email = 'eli.pacheco55@outlook.com'
header = f'\t\t{name}\n\t\t{location}\n\t\t{pn}\n\t\t{email}\n\n'

# build education rows education 
school = 'University of New Mexico' 
degree = 'BS, Computer Science'
expected_grad_date = 'Expected grad date: 2023'
GPA = 'Current GPA: 3.67\n'
education = f'{school}: {degree}\n{expected_grad_date}\n{GPA}\n'

# professional experience 
apple_rtl = 'PROFESSIONAL EXPERIENCE:\nApple - Operations, 2015-2021\n'
action_rtl = '- Timely receiving and sending thousands of products within the confines of the store.\n- Adapting to an ever-changing market within hours or minutes to better serve our customers and clients.\n- Collaborating creative solutions, with a team, to placing a constantly expanding product line into dimensions that remain the same.\n'
professional_experience = f'{apple_rtl}{action_rtl}'

#internships and career experience 
apple_fmr = 'INTERNSHIPS AND CAREER EXPERIENCE:\nApple - Firmware, Jan 2021- June 2021\n'
action_fmr = '- Work closely with developers to write and adapt tools, in python, to help firmware teams read through logs more eciently.\n - Systematically troubleshoot hardware, using proprietary applications, to delve into systems and correct behavior.\n - Used git and GitHub to create, edit, and push local branches to the remote repo.\n'
internships = f'{apple_fmr}{action_fmr}'

# technical skills
skill_string = "\nSkills:\n ---------------------"
skill_list = ['python', 'Computer Science', 'Git', 'GitHub', 'Operating Systems', 'Mathematics', 'c/c++', 'MATLAB', 'SOLIDWORKS']
skillset = ""
for i in skill_list:
    if i not in skillset:
        skillset += f'{i}\n'
skills_column = f'{skill_string}\n{skillset}'

w = open('eli_pacheco_resume.txt', 'w')
w.write(header)
w.write(education)
w.write(internships)
w.write(professional_experience)
w.write(skills_column)
w.close()