class studentWithoutCourse:
    def __init__(self, si):
        # si for student information
        self.name = si[0]
        self.id = si[1]
        self.birthday = si[2]
        self.school = si[3]
        self.department = si[4]

    def getAll(self):
        """返回包含着学生所有信息的字典"""
        stu = dict()

        stu["name"] = self.name
        stu["id"] = self.id
        stu["birthday"] = self.birthday
        stu["school"] = self.school
        stu["department"] = self.department

        return stu


class student(studentWithoutCourse):
    def __init__(self, si):
        # si for student information
        self.name = "N/A" if (si[0] == '') else si[0]
        self.id = "N/A" if (si[1] == '') else si[1]
        self.birthday = "N/A" if (si[2] == '') else si[2]
        self.school = "N/A" if (si[3] == '') else si[3]
        self.department = "N/A" if (si[4] == '') else si[4]
        self.courses = dict()

    def getAll(self):
        """返回包含着学生所有信息的字典"""
        stu = dict()

        stu["name"] = self.name
        stu["id"] = self.id
        stu["birthday"] = self.birthday
        stu["school"] = self.school
        stu["department"] = self.department
        stu["courses"] = self.courses

        return stu

    def getCourse(self):
        # 返回一个字典
        return self.courses

    def addCourse(self, courseName, score):
        if courseName in self.courses:
            return False  # 课程已存在
        else:
            self.courses[courseName] = score
            return True

    def editCourse(self, courseName, score):
        """编辑课程成绩，如果课程不存在将自动添加课程"""
        self.courses[courseName] = score

    def deleteCourse(self, course):
        del self.courses[course]
