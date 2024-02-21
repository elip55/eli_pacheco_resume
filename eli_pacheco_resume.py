
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

class build_strings:

    def __init__(self, v1, v2):
        self.arr = v1
        self.arr2 = v2

    def zip_tie(self):
        # function to make dictionaries
        pass
    def build_header_string(self):
        # first skill is a simple for loop
        header_string = '\n'
        for i in self.arr:
            header_string += f'{i}\n'
        header_string += '\n'
        return header_string
    
    def build_edu_string(self):
        # second skill is utilizing a dictionary
        edu_string = 'EDUCATION\n-------------\n'
        for i,j in self.arr.items():
            edu_string += f'{i} : {j[0]}\n'
            if not j[2]:
                edu_string += f'\tGrad Date: {j[3]}\n'
            else:
                edu_string += f'\tGraduated: {j[3]}\n'
            edu_string += f'\tGPA: {j[1]}\n'
        return edu_string


    def build_pro_string(self):
        pass

# input header info as any desired list of strings
hl = build_strings(['Eli M. Pacheco', 'Las Cruces, NM', '(505)321-5922', 'eli.pacheco55@outlook.com'], 0)
header = build_strings.build_header_string(hl)
el = build_strings({'CU Boulder': ['MS - Data Science', 3.5, False, 2024],
                   'Central New Mexico University': ['AS - Mathematics', 3.25, True, 2023],
                   'New Mexico State University':  ['BA - Creative Media', 3.2, True, 2015]}, 0)
edu = build_strings.build_edu_string(el)

# NOTE:  start experience strings
"""EXPERIENCE STRINGS ARE WORKED ON SEPERATELY, AS THEY CAN BECOME OVERWHELMING IN CODE"""
companies = [0]
r0 = ['Test and perform on console activities involving satellites during launch, early and long-term orbit operations.',
      'Identify areas of concern across multiple systems of hardware and software and troubleshoot solutions in real-time.',
      'Plan and configure communications support while monitoring and reviewing telemetry data.',
      'Advise various teams of failures, degradation, and potential recovery procedures.',
      'Conceive and build PowerShell and UNIX tools to extract, organize and display streams of data efficiently.',
      'Support to varying states of operations, further obtaining certifications to solidify my skills in anomaly response and resolution.']
r1 = ['Diligently monitor overhead vehicle systems for any non-nominal behavior.',
     'Obtained certifications to become highly skilled in anomaly response and resolution.',
     'Apply mission saving solutions across various systems of hardware and software for 24/7 flight operations.',
     'Utilize a wide range of UNIX tools to process, troubleshoot, and apply data effectively.']
r2 = ['With a small team of three, provided complete IT technical support to the entirety of the company in New Mexico, Arizona, California, Florida, and New York.',
      'Using RMM, monitored all iOS and Windows devices in the company.  Confirmed overall health while pushing updates and applications.',
      'To ensure future efficiency, created rubrics for future interns and employees to follow while ramping up in IT.']
r3 = ['Using Python, regular expression and working with a pair programmer, I conceptualized, wrote, and tested a command line tool which parsed through firmware logs and extracted relevant data.  The parsed data would then be written into .txt and .csv files accordingly.',
      'Tasked with optimizing the code, specifically when writing the output files.  Through collaboration, creativity, and time functions in jupyter lab, I tested several different ideas.  I concluded the function optimization by implementing code that was >100% faster than the .csv module.',
      'Systematically troubleshot hardware using several proprietary tools.  I would then report the bugs and identify the behaviors.',
      'All tasks relied heavily on git, GitHub and its commands.  Pulling, testing, editing, and pushing branches for pull requests were carried out daily.  The number of branches on projects ranged from 4 to 100+.']
r4 = ['Responsible for the entirety of the stores inventory being available quickly and efficiently.',
     'Learned advanced selling and professional communication techniques through Apple training. ']
#  NOTE:  end exp strings