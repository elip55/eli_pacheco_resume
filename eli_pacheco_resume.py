
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
    
    def __init__(self, header_strings):
        self.arr = header_strings
    
    def build_header_string(self):
        header_string = '\n'
        for i in self.arr:
            header_string += f'{i}\n'
        header_string += '\n'
        return header_string


# input header info as any desired list of strings
header_strings = ['Eli M. Pacheco', 'Las Cruces, NM', '(505)321-5922', 'eli.pacheco55@outlook.com']
header = HeaderInfo(header_strings)

class Education:
    # education institutions can be easily added or deleted in the __init__ constructor and function
    def __init__(self, school, degree, graduated, grad_year, gpa):
        # school 1
        self.school = school
        self.degree = degree
        self.graduated = graduated
        self.grad_year = grad_year
        self.gpa = gpa
        
    def build_edu_string(self):
        # initialize education string and school dictionaries
        edu_string = ''
        school = {}
        # Build the string
        school[self.school] = self.degree
        if self.graduated:
            school['Graduated'] = self.grad_year
        else:
            school['Expected Grad Year'] = self.grad_year
        school['GPA'] = self.gpa
        for key,value in school.items(): # use 'for' loop to add key:value into education string neatly
            edu_string += f'\t{key}: {value}\n' # format the string here to make dictionary less complex
            edu_string += '\t'
            if key == 'GPA':
                edu_string += '\n'
        return edu_string

# input education experience as strings, integers, and floats
# school name, degree, graduated?(true/false value), year graduated (or will graduate), GPA
school1 = Education('New Mexico State University', 'BA, Digital Media', True, 2015, 3.2)
school2 = Education('Central New Mexico University', 'AS, Mathematical Sciences', True, 2022, 3.22)
school3 = Education('CU Boulder', 'MS - Data Science', False, 2025, 4.0)


class ProfessionalExperience:
    # initiate professional experience actions
    def __init__(self, company_name, job_title, internship, dates, responsibilities):
        self.co = company_name
        self.title = job_title
        self.intern = internship
        self.dates = dates
        self.block = responsibilities
    
    # function to build professional block
    def build_prof_string(self):
        # initialize the professional experience string
        prof_string = f'{self.co} - {self.title} '
        if self.intern:
            prof_string += '<INTERNSHIP>,'
        prof_string += f'{self.dates}\n'
        for i in self.block:
            prof_string += f'\t- {i}\n'
        prof_string += '\n'
        return prof_string


# NOTE:  I work on job responsibilities first so that i can add the array later

r1 = ['Diligently monitor overhead vehicle systems for any non-nominal behavior.',
     'Obtained certifications to become highly skilled in anomaly response and resolution.',
     'Apply mission saving solutions across various systems of hardware and software for 24/7 flight operations.',
     'Utilize a wide range of UNIX tools to help process and apply data effectively.']
r2 = ['With a small team of three, provided complete IT technical support to the entirety of the company in New Mexico, Arizona, California, Florida, and New York.',
      'Sys admin duties:  Configured new user accounts in Active Directory and on the Domain, assigned software licenses, and reset accounts/passwords.',
      'Initiated new user hardware and software, ensuring an efficient transition into joining the company.',
      'Using RMM, monitored all iOS and Windows devices in the company.  Confirmed overall health while pushing updates and applications.',
      'Responsible for hardware maintenance and upgrades including tower and laptop upgrades.',
      'To ensure future efficiency, created rubrics for future interns and employees to follow while ramping up in IT.']
r3 = ['Using Python, regular expression and working with a pair programmer, I conceptualized, wrote, and tested a command line tool which parsed through firmware logs and extracted relevant data.  The parsed data would then be written into .txt and .csv files accordingly.',
      'Our tool was tested daily, directly in the UNIX shell, checking for software bugs or discrepancies within regex and firmware logs.',
      'Tasked with optimizing the code, specifically when writing the output files.  Through collaboration, creativity, and time functions in jupyter lab, I tested several different ideas.  I concluded the function optimization by implementing code that was >100% faster than the .csv module.',
      'Systematically troubleshot hardware using several proprietary tools.  I would then report the bugs and identify the behaviors.',
      'All tasks relied heavily on git, GitHub and its commands.  Pulling, testing, editing, and pushing branches for pull requests were carried out daily.  The number of branches on projects ranged from 4 to 100+.',
      'Built and maintained professional relationships across engineering, marketing, and business relations teams to achieve a common goal.']

"""set each company's header correctly according to the constructor:
 all should be strings:
 company name, job title, internship (true/false value), dates worked"""
company1 = ProfessionalExperience('Lockheed Martin', 'Vehicle Systems Engineer', False, 'August 2022 - Present', r1)
company2 = ProfessionalExperience('B&D Industries, INC.', 'IT Technician', True, 'Jan 2022 - June 2022', r2)
company3 = ProfessionalExperience('Apple', 'Firmware QA & Software Engineering', True, 'Jan 2021 - June 2021', r3)


class Skills:
    
    def __init__(self, skillset, arr1, arr2):
        self.l1 = arr1
        self.l2 = arr2
        self.skill_title = skillset
        if len(arr1) != len(arr2):
            print('Lists MUST be identical length!\nSee line 138')
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
# thinkg of this as writing your resume, you can organize it however you want right here
write_header = header.build_header_string()
edu_title_block = 'EDUCATION:\n-----------\n' 
write_education1 = school3.build_edu_string()
write_education2 = school2.build_edu_string()
write_education3 = school1.build_edu_string()
prof_title_block = 'PROFESSIONAL EXPERIENCE:\n------------------------\n'
write_company1 = company1.build_prof_string()
write_company2 = company2.build_prof_string()
write_company3 = company3.build_prof_string()
write_tech_skills = tech_skillset.build_skills_string()
write_prof_skills = prof_skillset.build_skills_string()

# write the .txt file 
# change the name of the .txt file as needed
with open('eli_pacheco_resume.txt', 'w') as mywriter: # with open for optimization
    mywriter.write(write_header)
    mywriter.write(edu_title_block)
    mywriter.write(write_education1)
    mywriter.write(write_education2)
    mywriter.write(write_education3)
    mywriter.write(prof_title_block)
    mywriter.write(write_company1)
    mywriter.write(write_company2)
    mywriter.write(write_company3)
    mywriter.write(write_tech_skills)
    mywriter.write(write_prof_skills)

# I am open to any and all feedback: eli.pacheco55@outlook.com