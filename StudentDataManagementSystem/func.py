import os
import json
import encryption
from student import student
from StudentData import studentData


def saveToFile(dataSet):
    f = open('students.dat', 'wb+')
    f.seek(0)
    f.truncate()
    toFile = dict()
    for stuID, stu in dataSet.students.items():
        toFile[stuID] = stu.getAll()

    data = json.dumps(toFile)
    key = input("请输入密码（不超过32位）：")
    ciptext = encryption.encrypt(data, key)
    f.write(ciptext)
    f.close()


def readFromFile(dataSet):
    f = open('students.dat', 'rb')
    ciptext = f.read()
    key = input("请输入密码：")
    data = encryption.decrypt(ciptext, key)
    fromFile = json.loads(data)
    for stuID, tempDict in fromFile.items():

        studentInformation = [
            tempDict["name"], tempDict["id"], tempDict["birthday"],
            tempDict["school"], tempDict["department"]
        ]

        stu = student(studentInformation)
        stu.courses = tempDict["courses"]
        dataSet.students[stuID] = stu

        if stu.name not in dataSet.nameToID:
            dataSet.nameToID[stu.name] = set([stu.id])
        else:
            dataSet.nameToID[stu.name].add(stu.id)

    f.close()


def showWelcomeScreen():

    os.system("cls")
    print("学生管理系统 1.0")
    print("\n0.查看全部学生信息\n")
    print("1. 查询学生信息\t2. 添加学生信息\t3. 修改学生信息\t4. 删除学生信息\n")
    print("5. 查询学生成绩\t6. 添加学生成绩\t7. 修改学生成绩\t8. 删除学生成绩\n")
    print("9. 保存并退出\n")

    while 1:
        returnCode = input("请输入要进行的操作：")

        os.system("cls")
        print("学生管理系统 1.0\n")

        try:
            return int(returnCode)
        except ValueError:
            continue

    return returnCode


def run():
    dataSet = studentData()

    readFromFile(dataSet)

    while 1:

        i = showWelcomeScreen()

        if i == 0:
            dataSet.showAllStudents()

        elif i == 1:
            dataSet.getStudentInformation()

        elif i == 2:
            dataSet.addStudentInformation()

        elif i == 3:
            dataSet.editStudentInformation()

        elif i == 4:
            dataSet.deleteStudentInformation()

        elif i == 5:
            dataSet.getStudentScore()

        elif i == 6:
            dataSet.addStudentScore()

        elif i == 7:
            dataSet.editStudentScore()

        elif i == 8:
            dataSet.deleteStudentScore()

        elif i == 9:
            saveToFile(dataSet)
            return
