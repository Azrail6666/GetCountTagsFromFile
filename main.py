count_tags = 0
count_tags_with_attrs = 0
with open("code.html", 'r') as file:
    file_data = file.read()
    tag = ""
    for char in file_data:
        if char == ">":
            if not "</" in tag:
                count_tags += 1
                if "=" in tag:
                    count_tags_with_attrs += 1
            tag = ""
        else:
            tag += char
print(f"Общее количество тегов: {count_tags}")
print(f"Количество тегов с атрибутами: {count_tags_with_attrs}")