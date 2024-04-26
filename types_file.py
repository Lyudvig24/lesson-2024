# import os
# import shutil

# excludeFiles = ['lessons.py','filter_file.txt','weather.py','randomwords.txt']

# def get_file_extension(file_name):
#     if not file_name:
#         return None
#     return file_name.split('.')[-1].lower()

# def file_types():
#     data = {}
#     for fileName in os.listdir('.'):
#         if os.path.isfile(fileName) and fileName not in excludeFiles:
#             type = get_file_extension(fileName)
#             data.setdefault(type,[])
#             data[type].append(fileName)
    
#     for type in data:
#         files = data[type]
#         if os.path.isdir(type) == False:
#             os.makedirs(type)

#         for newFileName in files:
#             shutil.move(newFileName, type + '/' + newFileName)

#     return data
        
# print(file_types())
