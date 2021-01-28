# slashes may need to change for MacOS or Linux
f = open("new_file.txt",'w+')
f.write("Here is some text")
f.close()

# slashes may need to change for MacOS or Linux
f = open("new_file2.txt",'w+')
f.write("Here is some text")
f.close()

import zipfile
comp_file = zipfile.ZipFile('comp_file.zip','w')
comp_file.write("new_file.txt",compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('new_file2.txt',compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()
# Extracting from Zip Files
zip_obj = zipfile.ZipFile('comp_file.zip','r')
zip_obj.extractall("extracted_content")

# Using shutil library
import shutil
directory_to_zip='D:\Python Learning 2021\Python Step2'
# Creating a zip archive
output_filename = 'example'
# Just fill in the output_filename and the directory to zip
# Note this won't run as is because the variable are undefined
shutil.make_archive(output_filename,'zip',directory_to_zip)

# Extracting a zip archive
# Notice how the parameter/argument order is slightly different here
shutil.unpack_archive(output_filename,dir_for_extract_result,'zip')