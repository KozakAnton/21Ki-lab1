students = {}
# Створення порожнього словника для зберігання студентів та їх оцінок
while True:
    name = input("Ім'я студента (або stop): ")
    if name.lower() == "stop":
        break
    grade = int(input("Оцінка: ")) # Додавання студента до словника (ім'я - ключ, оцінка - значення)
    students[name] = grade

print("Список студентів:",students)

if students: # Перевірка, чи словник не порожній (є хоча б один студент)
    avg = sum(students.values()) / len(students) # Обчислення середнього балу (сума всіх оцінок поділена на кількість студентів)
    print(f"Середній бал: {avg:}")
 # Створення списків студентів за категоріями за їх оцінками:
    excellent = [n for n, g in students.items() if 10 <= g <= 12]
    good = [n for n, g in students.items() if 7 <= g <= 9]
    weak = [n for n, g in students.items() if 4 <= g <= 6]
    failed = [n for n, g in students.items() if 1 <= g <= 3]
# Виведення результатів з кількістю студентів у кожній категорії
    print(f"Відмінники:{len(excellent)}-{excellent}")
    print(f"Хорошисти: {len(good)}-{good}")
    print(f"Відстаючі: {len(weak)}-{weak}")
    print(f"Не здали: {len(failed)}-{failed}")