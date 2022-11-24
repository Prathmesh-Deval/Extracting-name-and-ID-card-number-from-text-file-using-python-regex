import re

text_file = open("Image_to_text.txt", "r")

# read whole file to a string
data = text_file.read()

num = re.search('[A-Z][A-Z][A-Z][A-Z][A-Z][0-9][0-9][0-9][0-9][A-Z]', data)
s = num.span()
temp = data[s[0]:s[1]]

name = re.search('Name', data)
r = name.span()

father = re.search('Father', data)
r1 = father.span()

a =int(r[0])+4
b =int(r1[0])
text = data[a:b] + temp

print(text)

text_output = open('Employee_Data.txt', 'w', encoding='utf-8')
text_output.write(text)
text_output.close()

# print(data[int(r[0])+3])
#
# x= data[int(r[0]):int(r[0])+20]
# print(x)








# close file
text_file.close()


