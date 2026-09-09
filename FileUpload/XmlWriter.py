import xml.etree.ElementTree as ET

user = ET.Element("user")

ET.SubElement(user, "id").text = "101"

ET.SubElement(user, "name").text = "Avadhut"

ET.SubElement(user, "salary").text = "100000"

skills = ET.SubElement(user, "skills")

ET.SubElement(skills, "skill").text = "Python"
ET.SubElement(skills, "skill").text = "FastAPI"
ET.SubElement(skills, "skill").text = "AWS"

tree = ET.ElementTree(user)

tree.write(
    "D:\\Python\\Python-Sample\\FileUpload\\uploads\\user.xml",
    encoding="utf-8",
    xml_declaration=True
)