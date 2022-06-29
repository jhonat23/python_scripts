"""Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line."""

if __name__ == '__main__':
    students_list = []
    new_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students_list.append([name, score])

    min_grade = min(students_list, key= lambda x: x[1])[1]
    for i in range(_ + 1):
        if students_list[i][1] != min_grade:
            new_list.append(students_list[i])

    new_list.sort(key=lambda x: x[0])

    for j in range(len(new_list)):
        if new_list[j][1] == min(new_list, key= lambda x: x[1])[1]:
            print(new_list[j][0])