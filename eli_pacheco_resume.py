
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
# -----------------------

# the order of classes are as follows: 
# header
# education
# certificates
# internships and career experience
# professional experience
# technical skills
# professional skills
# edit each class as needed

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
header = HeaderInfo('Eli Pacheco', 'Las Cruces, NM', '(505)321-5922', 'eli.pacheco55@outlook.com')

class EducationInfo:
    # education institutions can be easily added or deleted in the __init__ constructor and function
    def __init__(self, school1, degree1, grad_year1, gpa1, 
                       school2, degree2, grad_year2, gpa2,
                       school3, degree3, grad_year3, gpa3):
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
        # school3 (most recent)
        self.school3 = school3
        self.degree3 = degree3
        self.grad_year3 = grad_year3
        self.gpa3 = gpa3
        
    def build_edu_string(self):
        # initialize education string and school dictionaries
        edu_string = 'EDUCATION:\n' 
        edu_string += '----------\n'
        school2 = {}
        school1 = {}
        school3 = {}
        # Build the string
        school3[self.school3] = self.degree3
        school3['Expected Graduation'] = self.grad_year3
        school3['GPA'] = self.gpa3
        # most recent school on top for formatting purposes
        for key,value in school3.items(): # use 'for' loop to add key:value into education string neatly
            edu_string += f'\t{key}: {value}\n' # format the string here to make dictionary less complex
            edu_string += '\t'
            if key == 'GPA':
                edu_string += '\n'
        for key,value in school2.items(): # use 'for' loop to add key:value into education string neatly
            edu_string += f'\t{key}: {value}\n' # format the string here to make dictionary less complex
            edu_string += '\t'
            if key == 'GPA':
                edu_string += '\n'
        # add second school into dictionary
        school2[self.school2] = self.degree2 
        school2['Graduated'] = self.grad_year2
        school2['GPA'] = self.gpa2
        for key,value in school2.items(): # use 'for' loop to add key:value into education string neatly
            edu_string += f'\t{key}: {value}\n' # format the string here to make dictionary less complex
            edu_string += '\t'
            if key == 'GPA':
                edu_string += '\n'
        # add first school into dictionary
        school1[self.school1] = self.degree1
        school1['Graduated'] = self.grad_year1
        school1['GPA'] = self.gpa1
        for key,value in school1.items(): # use 'for' loop to add key:value into education string neatly
            edu_string += f'\t{key}: {value}\n' # format the string here to make dictionary less complex
            edu_string += '\t'
            if key == 'GPA':
                edu_string += '\n'
        return edu_string

# input education experience as strings, integers, and floats
# most recent on bottom, reflecting the __init__ constructor
edu = EducationInfo('New Mexico State University', 'BA, Digital Media', 2015, 3.2,
                    'Central New Mexico University', 'AS, Mathematical Sciences', 2022, 3.22,
                    'CU Boulder', 'MS - Data Science', 2024, 'N/A' )
class Certificates:
    # initialize certificate actions
    def __init__(self, cert1, desc1, year1, fact1):
        self.cert1 = cert1
        self.desc1 = desc1
        self.year1 = year1
        self.fact1 = fact1


class ProfessionalExperience:
    # initiate professional experience actions
    def __init__(self, co_title1, pro_action1, pro_action2, pro_action3, pro_action4, pro_action5, pro_action6,
                       co_title2, pro_action1a, pro_action2a, pro_action3a, pro_action4a, pro_action5a,
                       co_title3, pro_action1b, pro_action2b, pro_action3b):
        # first company
        self.co_title1 = co_title1
        self.pro_action1 = pro_action1
        self.pro_action2 = pro_action2
        self.pro_action3 = pro_action3
        self.pro_action4 = pro_action4
        self.pro_action5 = pro_action5
        self.pro_action6 = pro_action6
        # second company
        self.co_title2 = co_title2
        self.pro_action1a = pro_action1a
        self.pro_action2a = pro_action2a
        self.pro_action3a = pro_action3a
        self.pro_action4a = pro_action4a
        self.pro_action5a = pro_action5a
        # third company
        self.co_title3 = co_title3
        self.pro_action1b = pro_action1b
        self.pro_action2b = pro_action2b
        self.pro_action3b = pro_action3b
    
    
    # function to build professional block
    def build_prof_string(self):
        # initialize the professional experience string
        prof_string = 'PROFESSIONAL EXPERIENCE:\n'
        prof_string += '------------------------\n'
        prof_string += f'\t{self.co_title3}\n'
        prof_string += f'\t\t{self.pro_action1b}\n\t\t{self.pro_action2b}\n\t\t{self.pro_action3b}\n'
        prof_string += '\n'
        prof_string += f'\t{self.co_title2}\n'
        prof_string += f'\t\t{self.pro_action1a}\n\t\t{self.pro_action2a}\n\t\t{self.pro_action3a}\n\t\t{self.pro_action4a}\n\t\t{self.pro_action5a}\n\t\t'
        prof_string += '\n'
        prof_string += f'\t{self.co_title1}\n'
        prof_string += f'\t\t{self.pro_action1}\n\t\t{self.pro_action2}\n\t\t{self.pro_action3}\n\t\t{self.pro_action4}\n\t\t{self.pro_action5}\n\t\t{self.pro_action6}'
        prof_string += '\n\n'
        return prof_string

prof = ProfessionalExperience(
                        'Apple - Firmware QA & Software Engineering <Internship>, Jan 2021 - June 2021',
                        '- Using Python, regular expression and working with a pair programmer, I conceptualized, wrote, and tested a command line tools which parsed through firmware logs and extracted relevant data.\n\t\t  The parsed data would then be written into .txt and .csv files accordingly.',
                        '- Our tool was tested daily, directly in the UNIX shell, checking for software bugs or discrepancies within regex and firmware logs.',
                        '- Tasked with optimizing the code, specifically when writing the output files.\n\t\t  Through collaboration, creativity, and time functions in jupyter lab, I tested several different ideas.\n\t\t  I concluded the function optimization by implementing code that was 100-500 percent faster than the csv module.',
                        '- Systematically troubleshot hardware using several proprietary tools.  I would then report the bugs and identify the behaviors.\n\t\t  This meant a working understanding of circuits, electronic symbols, and general computer science.',
                        '- All tasks relied heavily on git, GitHub and its commands.  Pulling, testing, editing, and pushing branches for pull requests were carried out daily.\n\t\t  The number of branches on projects ranged from 4 to 100+.',
                        '- Built and maintained professional relationships across engineering, marketing, and business relations teams to achieve a common goal.',
                        'B&D Industries, Inc. - IT Technician <Internship>, Jan 2022 - May 2022', 
                        '- With a small team of three, provided complete IT technical support to the entirety of the company in New Mexico, Arizona, California, Florida, and New York.',
                        '- Preliminary sys admin duties, configuring all new user accounts in Active Directory and on the Domain.',
                        '- Initiated all new user hardware and software, ensuring an efficient transition into joining the company.',
                        '- Using RMM, monitored all iOS and Windows devices in the company ensuring updates, overall health, and necessary applications.',
                        '- Responsible for hardware maintenance and upgrades including tower, laptop, and network upgrades.',
                        'Lockheed Martin - Vehicle Systems Engineer, August 2022 - Present',
                        '- Diligently monitor vehicle systems for any non-nominal behavior, applying time-sensitive solutions across various systems of hardware and software.',
                        '- Collaborate with a cross-country and diverse team to achieve resolutions for complex engineering problems.',
                        '- Utilize a wide range of UNIX tools to help process and apply data effectively.')

class Skills:
    
    def __init__(self, skillset, arr1, arr2):
        self.l1 = arr1
        self.l2 = arr2
        self.skill_title = skillset
        if len(arr1) != len(arr2):
            print('Lists MUST be identical length!')
            exit()
        
    def build_skills_string(self):
        token = '* '
        # initialize the skills string
        prof_skill_string = f"{self.skill_title} | Proficiency"
        prof_skill_string += '\n---------------------------------\n'
        # profesional skills as a list
        prof_skills_list = self.l1
        proficiency_list1 = self.l2 #NOTE: These integers directly reflect skills, length must be identical
        professional_skills_dict = dict(zip(prof_skills_list, proficiency_list1))
        for skill, proficiency in professional_skills_dict.items():
            prof_skill_string += f'\t{skill} | {token*proficiency}\n'
        prof_skill_string += '\n'
        return prof_skill_string

# first input titles of each list
tech_title = 'Technical Skills'
prof_title = 'Professional Skills'
# then input skills as a list of strings
tech_list = ['Mathematics', 'git and GitHub', 'jupyter lab', 'Unix shell', 'Troubleshooting', 'Systems Engineering', 'Aerospace Solutions', 'Anomaly Response', 'SSH', 'Python']
prof_list = ['Teamwork', 'Client Development', 'Creativity', 'Task Prioritization', 'Professional Communication', 'Adaptation & Collaboration', 'Time Management', 'Microsoft Office Suite', 'macOS', 'Windows' ]
# enter proficienty as a list of integers
tech_proficiency = [5,4,4,4,4,4,3,3,3,3]
prof_proficiency = [5,5,5,5,5,5,5,4,4,4]
# finally, use the class Skills
tech_skillset = Skills(tech_title, tech_list, tech_proficiency)
prof_skillset = Skills(prof_title, prof_list, prof_proficiency)

# calling functions and utilizing classes
write_header = header.build_header_string()
write_education = edu.build_edu_string()
write_prof = prof.build_prof_string()
write_tech_skills = tech_skillset.build_skills_string()
write_prof_skills = prof_skillset.build_skills_string()

# write the .txt file 
# change the name of the .txt file as needed
with open('eli_pacheco_resume.txt', 'w') as mywriter: # with open for optimization
    mywriter.write(write_header)
    mywriter.write(write_education)
    mywriter.write(write_prof)
    mywriter.write(write_tech_skills)
    mywriter.write(write_prof_skills)

# I am open to any and all feedback: eli.pacheco55@outlook.com