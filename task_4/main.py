strok = str(input("Введите строку для поиска: ")).strip().lower()
with open(r"C:\Users\user\Desktop\Лабы и тп\ИПО\lr6\task_4\text.txt", "r", encoding="utf-8") as text:
    lines = text.readlines()
    found_lines = []
    for num, line in enumerate(lines):
        cleanline = strok.strip()
        if strok in cleanline.lower():
            found_lines.append(strok)
    print(found_lines)
