def create_xml(data, name = "new_export"):
    print("Пищу xml")
    xml = '<xml>\n'
    data = data.split("*;***")
    for i in range(len(data) - 1):
        family, name, tel, description = data[i].split(",")
        xml += '<Фамилия>{}</Фамилия>\n'\
            .format(family)
        xml += '<Имя>{}</Имя>\n' \
            .format(name)
        xml += '<Телефон>{}</Телефон>\n' \
            .format(tel)
        xml += '<Описание>{}</Описание>\n' \
            .format(description)
    xml += '</xml>'
    with open("new_export.xml", 'w') as page:
        page.write(xml)
