from student import student


class _studentData:
    def __init__(self):
        # key是学号，value是Student对象
        self.students = dict()
        # nameToID的value是同一姓名(Student.name)所对应的学号(Student.id)的集合(set)
        self.nameToID = dict()

    def get(self, stuID):
        if stuID in self.students:
            return self.students[stuID]
        else:
            # 学生不存在
            return False

    def add(self, stu):
        # 判断重名
        if stu.name not in self.nameToID:
            self.nameToID[stu.name] = set([stu.id])
        else:
            self.nameToID[stu.name].add(stu.id)

        # key是学号，value是Student对象
        self.students[stu.id] = stu

    def delete(self, stuID):
        """输入学号，删除关于该学生的所有信息"""
        stu = self.students[stuID]

        if len(self.nameToID[stu.name]) == 1:
            # 不重名
            del self.nameToID[stu.name]
        else:
            # 重名
            self.nameToID[stu.name].remove(stuID)

        del self.students[stuID]

    def editName(self, stu, newName):
        """注意这里的大坑"""
        if len(self.nameToID[stu.name]) == 1:
            # 不重名
            del self.nameToID[stu.name]
        else:
            # 重名
            self.nameToID[stu.name].remove(stu.id)

        stu.name = newName

        if stu.name not in self.nameToID:
            self.nameToID[stu.name] = set([stu.id])
        else:
            self.nameToID[stu.name].add(stu.id)

    def editID(self, stu, newID):
        oldID = stu.id
        if len(self.nameToID[stu.name]) == 1:
            # 不重名
            self.nameToID[stu.name] = set([newID])
        else:
            # 重名
            tmpList = list(self.nameToID[stu.name])
            tmpList.remove(oldID)
            self.nameToID[stu.name] = set(tmpList)

        stu.id = newID
        del self.students[oldID]
        self.students[newID] = stu

    def editBirthday(self, stu, newBirthday):
        stu.birthday = newBirthday

    def editSchool(self, stu, newSchool):
        stu.school = newSchool

    def editDepartment(self, stu, newDepartment):
        stu.department = newDepartment


class studentData(_studentData):
    def getStudentInformationByName(self, stuName):
        """返回student对象或False"""
        if stuName not in self.nameToID:
            # 学生不存在
            return False

        else:
            # 学生存在
            # 当前姓名学生对应的学号集合
            stuIDSet = self.nameToID[stuName]

            if len(stuIDSet) != 1:
                # 重名判断
                print(stuName, "对应多个重名学生，请根据学号选择:")
                print(*stuIDSet, sep='\n')
                stuID = input("请输入学号：")
                targetStudent = self.get(stuID)

            else:
                targetStudent = self.get(list(stuIDSet)[0])

            # 返回Student对象
            return targetStudent

    def getStudentInformationByID(self, stuID):
        """返回student对象或False"""
        return self.get(stuID)

    def getStudentInformation(self):

        targetStudent = self.getCurrentStudent()

        if targetStudent is False:
            print("学生不存在！", end='')

        else:
            print("查询成功！")
            print("学生姓名：", targetStudent.name)
            print("学生学号：", targetStudent.id)
            print("学生生日：", targetStudent.birthday)
            print("学生学院：", targetStudent.school)
            print("学生系所：", targetStudent.department)

        n = input("输入1继续查询学生信息，直接按下回车键返回：\n")
        if n == '1':
            self.getStudentInformation()

    def addStudentInformation(self):
        information = []
        print("请输入学生的姓名：")
        information.append(input())
        print("请输入学生的学号：")
        information.append(input())
        print("请输入学生的生日：")
        information.append(input())
        print("请输入学生的学院：")
        information.append(input())
        print("请输入学生的系所：")
        information.append(input())
        stu = student(information)

        self.add(stu)

        print("输入成功！ 输入1继续添加学生信息，按下回车键结束输入：")
        n = input()
        if n == '1':
            self.addStudentInformation()

    def editStudentInformation(self):
        stu = self.getCurrentStudent()

        if stu is False:
            print("学生不存在！输入1重新输入学号或姓名，按下回车键返回:")
            tmp = input()
            if tmp == '1':
                self.editStudentInformation()
            else:
                return

        else:
            print("请输入对应的值：")
            print("  1 修改学生姓名\n  2 修改学生学号\n  3 修改学生生日\n  4 修改学生学院\n  5 修改学生系所")
            n = int(input())

            if n == 1:
                print(f"学生现在的姓名为：{stu.name}，请输入变更后的姓名：")
                newName = input()
                self.editName(stu, newName)
                print("学生姓名变更成功")

            elif n == 2:
                print(f"{stu.name}现在的学号为：{stu.id}，请输入变更后的学号：")
                newID = input()

                if newID in self.students:
                    print("\033[1;31m警告：该学号已存在，强行写入将导致覆盖！ \033[0m")
                    if self.warning():
                        self.editID(stu, newID)
                        print(f"{stu.name}学号变更成功")
                    else:
                        print("变更操作已取消。输入1继续变更，按下回车键退出变更学生信息")
                        n = input()
                        if n == '1':
                            self.editStudentInformation()
                else:
                    self.editID(stu, newID)
                    print(f"{stu.name}学号变更成功")

            elif n == 3:
                print(f"{stu.name}现在的生日为：{stu.birthday}，请输入变更后的生日：")
                newBirthday = input()
                self.editBirthday(stu, newBirthday)
                print(f"{stu.name}生日变更成功")

            elif n == 4:
                print(f"{stu.name}现在的学院为：{stu.school}，请输入变更后的学院：")
                newSchool = input()
                self.editSchool(stu, newSchool)
                print(f"{stu.name}学院变更成功")

            elif n == 5:
                print(f"{stu.name}现在的系所为：{stu.department}，请输入变更后的系所：")
                newDepartment = input()
                self.editDepartment(stu, newDepartment)
                print(f"{stu.name}系所变更成功")

            else:
                print("输入错误")

            ch = input("输入1继续变更，按下回车键退出")
            if ch == '1':
                self.editStudentInformation()
            else:
                return

    def deleteStudentInformation(self):

        string = input("请输入要删除学生的学号或姓名：")
        confrim = input("请再次输入以确认操作：")

        if string == confrim:
            try:
                # 输入了学号
                int(string)
                targetStudent = self.getStudentInformationByID(string)

            except ValueError:
                # 输入了姓名
                targetStudent = self.getStudentInformationByName(string)

            if targetStudent is False:
                # 学生不存在
                print("学生不存在！输入1重新输入学号或姓名，按下回车键返回:")
                tmp = input()
                if tmp == '1':
                    self.deleteStudentInformation()
                else:
                    return

            else:
                # 学生存在
                if self.warning():
                    self.delete(targetStudent.id)
                    n = input("删除成功，输入1继续删除，按下回车键返回：")
                    if n == '1':
                        self.deleteStudentInformation()
                else:
                    print("删除已取消，按下回车键返回")
                    input()
                    return
        else:
            ch = input("两次输入的值不相符！按下回车键重新输入，输入q取消删除：")
            if ch == 'q':
                return
            else:
                self.deleteStudentInformation()

    def getStudentScore(self):

        stu = self.getCurrentStudent()
        if stu is False:
            print("学生不存在！按下回车键返回")
            input()
            return

        print(f"学生{stu.name}的课程和成绩如下：")

        for course in stu.courses:
            print(course, '\t', stu.courses[course])
            # course是课程名，courses[course]是分数

        print("\n输入1继续查询学生成绩，按下回车键结束输入：")
        n = input()
        if n == '1':
            self.getStudentScore()

    def addStudentScore(self):

        stu = self.getCurrentStudent()
        if stu is False:
            print("学生不存在！按下回车键返回")
            input()
            return

        courseName = input("请输入课程名称：")
        courseScore = input("请输入课程成绩：")
        if not stu.addCourse(courseName, courseScore):
            # 若成功添加则返回True，课程已存在返回False
            print("课程已存在，是否覆盖？输入y确认覆盖，n取消覆盖")
            while 1:
                n = input()
                if n == 'y':
                    stu.editCourse(courseName, courseScore)
                    break
                elif n == 'n':
                    break
                else:
                    print("您的输入有误，请重新输入")

        ch = input("输入1继续添加，按下回车键退出")
        if ch == '1':
            self.addStudentScore()
        else:
            return

    def editStudentScore(self):

        stu = self.getCurrentStudent()
        if stu is False:
            print("学生不存在！按下回车键返回")
            input()
            return

        courseName = input("请输入课程名称：")
        if courseName in stu.courses:
            # 已经存在这门课
            print(f"{stu.name}的课程{courseName}当前的成绩是：{stu.courses[courseName]}")
            newScore = input("请输入新的成绩：")
            stu.editCourse(courseName, newScore)
        else:
            # 还不存在这门课
            print(f"{stu.name}的课程中没有这门课！输入成绩以将其添加到课程中。按下回车键退出。")
            newScore = input()
            if newScore != '':
                stu.editCourse(courseName, newScore)

        ch = input("成功！输入1继续变更成绩，按下回车键退出")
        if ch == '1':
            self.editStudentScore()
        else:
            return

    def deleteStudentScore(self):

        stu = self.getCurrentStudent()
        if stu is False:
            print("学生不存在！按下回车键返回")
            input()
            return

        courseName = input("请输入要删除的课程名称：")
        if courseName in stu.courses:
            stu.deleteCourse(courseName)
            print("成功！", end='')
        else:
            print("课程不存在，请核对后重新输入！")

        ch = input("输入1继续删除，按下回车键退出")
        if ch == '1':
            self.deleteStudentScore()
        else:
            return

    def getCurrentStudent(self):
        string = input("请输入学生的学号或姓名：")

        try:
            # 输入了学号
            int(string)
            ts = self.getStudentInformationByID(string)
            # targetStudent
        except ValueError:
            ts = self.getStudentInformationByName(string)

        return ts

    def warning(self):
        while 1:
            print("\033[1;31m警告：此操作是不可逆的，请确认您是否要进行此操作。输入yes确认，输入no取消： \033[0m")
            n = input()
            if n == "yes":
                break
            elif n == "no":
                return False  # 取消

        return True  # 确认

    def showAllStudents(self):
        print("所有学生：")
        for stu in self.students.values():
            print(f"{stu.id}: {stu.name}")

        input("\n按下回车键返回：")
