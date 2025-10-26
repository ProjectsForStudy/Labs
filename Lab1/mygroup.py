groupmates = [
    {
        "name": "Александр",
        "surname": "Семёнов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Георгий",
        "surname": "Скворцов",
        "exams": ["История", "ЭЭиС", "Web"],
        "marks": [3, 5, 4]
    },
    {
        "name": "Георгий",
        "surname": "Скворцов",
        "exams": ["ИС", "КТП", "Информатика"],
        "marks": [5, 3, 4]
    },
    {
        "name": "Елизавета",
        "surname": "Чистякова",
        "exams": ["ИС", "КТП", "Философия"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Вадим",
        "surname": "Иванов",
        "exams": ["ИС", "КТП", "Философия"],
        "marks": [3, 3, 4]
    },
    {
        "name": "Полина",
        "surname": "Пономарёва",
        "exams": ["ИС", "КТП", "Web"],
        "marks": [5, 3, 5]
    },
    {
        "name": "Егор",
        "surname": "Волков",
        "exams": ["ИС", "КТП", "Информатика"],
        "marks": [4, 5, 5]
    },
]

def main():
    # Основная функция
    try:
        # Пользовательский ввод
        MinRating = float(input("Введите минимальный средний балл: "))
        
        # Массив для фильтра
        filtered = []
        
        
        for student in groupmates:
            # Подсчёт среднего балла
            TotalMarks = 0
            for mark in student["marks"]:
                TotalMarks = TotalMarks + mark
            avg = TotalMarks / len(student["marks"])
            
            # Если средний балл выше, студент добавляется в список
            if avg > MinRating:
                filtered.append(student)
        
        # Вывод результата
        print("Студенты со средним баллом выше " + str(MinRating) + ":")
        
        if not filtered:
            print("Не найдено")
        else:
            # Заголовок
            print("Имя" + " " * 13 + "Фамилия" + " " * 9 + "Экзамены" + " " * 22 + "Оценки")
            print("-" * 70)
            
            # Вывод каждого студента
            for student in filtered:
                exams = ", ".join(student["exams"])
                marks = ", ".join(str(m) for m in student["marks"])
                print(student["name"] + " " * (15 - len(student["name"])) + student["surname"] + " " * (15 - len(student["surname"])) + exams + " " * (30 - len(exams)) + marks)
        
        print("Всего студентов: " + str(len(groupmates)))
        print("Отфильтровано: " + str(len(filtered)))
        
    except ValueError:
        print("Ошибка: введите число!")


# Запуск
# проверка, запущен ли скрипт напрямую или импортирован из другого модуля
if __name__ == "__main__":
    main()
