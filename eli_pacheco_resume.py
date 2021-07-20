
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
        edu_string += '----------\n'
        grad_school = {}
        undergrad = {}
        # most recent school on top for formatting purposes
        grad_school[self.school2] = self.degree2 
        grad_school['Expected Grad Date'] = self.grad_year2
        grad_school['GPA'] = self.gpa2
        for key,value in grad_school.items(): # use 'for' loop to add key:value into education string neatly
            edu_string += f'\t{key}: {value}\n' # format the string here to make dictionary less complex
            edu_string += '\t'
            if key == 'GPA':
                edu_string += '\n'
        # add first school into dictionary
        undergrad[self.school1] = self.degree1
        undergrad['Graduated'] = self.grad_year1
        undergrad['GPA'] = self.gpa1
        for key,value in undergrad.items(): # use 'for' loop to add key:value into education string neatly
            edu_string += f'\t{key}: {value}\n' # format the string here to make dictionary less complex
            edu_string += '\t'
            if key == 'GPA':
                edu_string += '\n'
        return edu_string

# input education experience as strings, integers, and floats
# most recent on bottom, reflecting the __init__ constructor
edu = EducationInfo('New Mexico State University', 'BA, Digital Media', 2015, 3.2,
                    'University of New Mexico', 'MS, Computer Science', 2024, 3.67)
class Certificates:
    # initialize certificate actions
    def __init__(self, cert1, desc1, year1, fact1):
        self.cert1 = cert1
        self.desc1 = desc1
        self.year1 = year1
        self.fact1 = fact1
        
    def build_cert_string(self):
        # initialize cert string
        cert_string = 'CERTIFICATES:\n'
        cert_string += '-------------\n'
        # initiate dictionary
        certificate1 = {}
        facts = [self.fact1]
        certificate1[self.cert1] = self.desc1
        certificate1['Attained'] = self.year1
        for key, value in certificate1.items():
            cert_string += f'\t{key}: {value}\n'
            cert_string += '\t'
        # create list for facts on certificates
        facts = [self.fact1]
        for i in facts:
            cert_string += f'\t- {i}\n'
        cert_string += '\n'
        return cert_string

cert = Certificates('Google IT support', 'Professional Certificate', 2021, 'Technical Support Fundamentals')

class ProfessionalExperience:
    # initiate professional experience actions
    def __init__(self, co_title1, pro_action1, pro_action2, pro_action3, pro_action4,
                       co_title2, pro_action5, pro_action6, pro_action7, pro_action8, pro_action9, 
                       co_title3, pro_action10, pro_action11, pro_action12, pro_action13, pro_action14, pro_action15):
        # first company
        self.co_title1 = co_title1
        self.pro_action1 = pro_action1
        self.pro_action2 = pro_action2
        self.pro_action3 = pro_action3
        self.pro_action4 = pro_action4
        # second company
        self.co_title2 = co_title2
        self.pro_action5 = pro_action5
        self.pro_action6 = pro_action6
        self.pro_action7 = pro_action7
        self.pro_action8 = pro_action8
        self.pro_action9 = pro_action9
        # third company
        self.co_title3 = co_title3
        self.pro_action10 = pro_action10
        self.pro_action11 = pro_action11
        self.pro_action12 = pro_action12
        self.pro_action13 = pro_action13
        self.pro_action14 = pro_action14
        self.pro_action15 = pro_action15
    # function to build professional block
    def build_prof_string(self):
        # initialize the professional experience string
        prof_string = 'PROFESSIONAL EXPERIENCE:\n'
        prof_string += '------------------------\n'
        prof_string += f'\t{self.co_title3}\n'
        prof_string += f'\t\t{self.pro_action10}\n\t\t{self.pro_action11}\n\t\t{self.pro_action12}\n\t\t{self.pro_action13}\n\t\t{self.pro_action14}\n\t\t{self.pro_action15}'
        prof_string += f'\n\n'
        prof_string += f'\t{self.co_title2}\n'
        prof_string += f'\t\t{self.pro_action5}\n\t\t{self.pro_action6}\n\t\t{self.pro_action7}\n\t\t{self.pro_action8}\n\t\t{self.pro_action9}'
        prof_string += '\n\n'
        prof_string += f'\t{self.co_title1}\n'
        prof_string += f'\t\t{self.pro_action1}\n\t\t{self.pro_action2}\n\t\t{self.pro_action3}\n\t\t{self.pro_action4}'
        prof_string += '\n\n'
        return prof_string

# input intern experience as strings
# most recent on bottom, reflecting the __init__ constructor
# NOTE: using \n\t\t for longer actions is recommended
prof = ProfessionalExperience('Apple - Specialist, November 2015 – January 2019',
                        '- Learned advanced selling and professional communication techniques through Apple training.',
                        '- Met and exceeded quotas in sales, business connections, customer satisfaction, and attachments for each quarter.',
                        '- Worked in understanding operating systems across devices and companies to suggest the perfect solutions for customers and clients.',
                        '- Introduced businesses to tech solutions including hardware, software, cloud platforms, accessories and Apple services.',
                        'Apple - Operations, January 2019 - January 2021',
                        '- Received and shipped thousands of products within the confines of the store.',
                        '- Adapted to a constantly changing product line within hours, or minutes, to better serve our customers and clients.',
                        '- Shipments were received at all hours of the day, every day.  Skills in time management and task prioritization were necessary to delegate tasks accordingly.',
                        '- Collaborated creative solutions, with a team, to place a constantly expanding product line into dimensions that remain the same.',
                        '- Using simple mathematics, I devised a strategy to utilize every inch of possible space, in the bays, while the iPhone product line grew by 300 percent.\n\t\t  This allowed us to efficiently have product readily available while eliminating the necessity to build more shelves for the expansion.\n\t\t  This led to an increase in the floorspace area for more shipments, products, and physical movement.',
                        'Apple - Firmware QA & Software Engineering "Internship", January 2021 - June 2021',
                        '- Using Python, regular expression and working with a pair programmer, I conceptualized, wrote, and tested a command line tool which parsed through firmware logs and extracted relevant data.\n\t\t  The parsed data would then be written into .txt and .csv files accordingly.',
                        '- Our tool was tested daily, directly in the UNIX shell, checking for software bugs or discrepancies within regex and firmware logs.',
                        '- Tasked with optimizing the code, specifically when writing the output files.\n\t\t  Through collaboration, creativity, and time functions in jupyter lab, I tested several different ideas.\n\t\t  I concluded the function optimization by implementing code that was 100-500 percent faster than the csv module.',
                        '- Systematically troubleshot hardware using several proprietary tools.  I would then report the bugs and identify the behaviors.\n\t\t  This meant a working understanding of circuits, electronic symbols, and general computer science.',
                        '- All tasks relied heavily on git, GitHub and its commands.  Pulling, testing, editing, and pushing branches for pull requests were carried out daily.\n\t\t  The number of branches on projects ranged from 4 to 100+.',
                        '- Built and maintained professional relationships across engineering, marketing, and business relations teams to achieve a common goal.')

class TechnicalSkills:
    
    def __init__(self, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5
        self.s6 = s6
        self.s7 = s7
        self.s8 = s8
        self.s9 = s9
        self.s10 = s10
        self.s11 = s11
        self.s12 = s12
        self.s13 = s13
        
    def build_tech_skills_string(self):
        # token for visual proficiency
        token = '* '
        # initialize the skills string
        tech_skill_string = "Technical Skills | Proficiency"
        tech_skill_string += '\n---------------------------------\n'
        # profesional skills as a list
        prof_skills_list = [self.s1, self.s2, self.s3, self.s4, self.s5, self.s6, 
                            self.s7, self.s8, self.s9, self.s10, self.s11, self.s12, self.s13]
        proficiency_list1 = [4,4,4,3,3,3,3,3,3,3,2,2,2] #NOTE: These integers directly reflect skills, length must identical
        technical_skills_dict = dict(zip(prof_skills_list, proficiency_list1))
        for skill, proficiency in technical_skills_dict.items():
            tech_skill_string += f'\t{skill} | {token*proficiency}\n'
        tech_skill_string += '\n'
        return tech_skill_string

# input skills as strings
technical_skills = TechnicalSkills('git and GitHub', 'jupyter lab', 'Unix shell', 'Python', 'Troubleshooting', 'Computer Science', 'Operating Systems', 
                                    'Advanced Mathematics', 'SSH Authentication Keys', 'regex', 'YAML', 'SOLIDWORKS', 'MATLAB')

class ProfessionalSkills:
    
    def __init__(self, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5
        self.s6 = s6
        self.s7 = s7
        self.s8 = s8
        self.s9 = s9
        self.s10 = s10
        self.s11 = s11
        self.s12 = s12
        self.s13 = s13
    
    def build_prof_skills_string(self):
        token = '* '
        # initialize the skills string
        prof_skill_string = "Professional Skills | Proficiency"
        prof_skill_string += '\n---------------------------------\n'
        # profesional skills as a list
        prof_skills_list = [self.s1, self.s2, self.s3, self.s4, self.s5, self.s6, 
                            self.s7, self.s8, self.s9, self.s10, self.s11, self.s12, self.s13]
        proficiency_list1 = [5,5,5,5,5,5,5,5,5,5,4,5,3] #NOTE: These integers directly reflect skills, length must identical
        professional_skills_dict = dict(zip(prof_skills_list, proficiency_list1))
        for skill, proficiency in professional_skills_dict.items():
            prof_skill_string += f'\t{skill} | {token*proficiency}\n'
        prof_skill_string += '\n'
        return prof_skill_string

# input skills as strings
prof_skills = ProfessionalSkills('Teamwork', 'Customer Service', 'Creativity', 'Task Prioritization', 'Client Development', 'Professional Communication', 
                    'Adaptation & Collaboration', 'Time Management', 'Microsoft Office Suite', 'macOS', 'Windows', 'iOS', 'Android OS')

# calling functions and utilizing classes
write_header = header.build_header_string()
write_education = edu.build_edu_string()
write_certificates = cert.build_cert_string()
write_prof = prof.build_prof_string()
write_tech_skills = technical_skills.build_tech_skills_string()
write_prof_skills = prof_skills.build_prof_skills_string()

# write the .txt file 
# change the name of the .txt file as needed
with open('eli_pacheco_resume.txt', 'w') as writer: # with open for optimization 
    writer.write(write_header) # write header string
    writer.write(write_education) # write education string 
    writer.write(write_certificates)
    writer.write(write_prof) # write professional experience 
    writer.write(write_tech_skills)
    writer.write(write_prof_skills) # write skills

# I am open to any and all feedback: eli.pacheco55@outlook.com