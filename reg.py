import re

text_file = open("Image_to_text.txt", "r")

# read whole file to a string
data = text_file.read()

#find pattern in our ID Card
num = re.search('[A-Z][A-Z][A-Z][A-Z][A-Z][0-9][0-9][0-9][0-9][A-Z]', data)
s = num.span()
temp = data[s[0]:s[1]]

#find name in the file
name = re.search('Name', data)
r = name.span()

father = re.search('Father', data)
r1 = father.span()

a =int(r[0])+4
b =int(r1[0])
text = data[a:b] + temp

print(text)

#store the found data inside Employee_Data.txt file
text_output = open('Employee_Data.txt', 'w', encoding='utf-8')
text_output.write(text)
text_output.close()










# close file
text_file.close()


