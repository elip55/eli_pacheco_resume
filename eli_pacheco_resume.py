
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

    def __init__(self, header_strings):
        self.arr = header_strings
    
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




# input header info as any desired list of strings
hl = build_strings(['Eli M. Pacheco', 'Las Cruces, NM', '(505)321-5922', 'eli.pacheco55@outlook.com'])
header = build_strings.build_header_string(hl)
el = build_strings({'CU Boulder': ['MS - Data Science', 3.5, False, 2024],
                   'Central New Mexico University': ['AS - Mathematics', 3.25, True, 2023],
                   'New Mexico State University':  ['BA - Creative Media', 3.2, True, 2015]})
edu = build_strings.build_edu_string(el)
