import xml.etree.ElementTree as ET

tree = ET.parse("D:\\Python\\Python-Sample\\FileUpload\\uploads\\user.xml")

root = tree.getroot()

print(root.tag)

print(root.find("id").text)

print(root.find("name").text)

print(root.find("salary").text)

skills = root.find("skills")

for skill in skills:

    print(skill.text)