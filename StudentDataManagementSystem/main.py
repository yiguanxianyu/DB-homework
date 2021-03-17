import func
import StudentData


def main():

    dataSet = StudentData.studentData()

    func.readFromFile(dataSet)

    while 1:

        i = func.showWelcomeScreen()

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
            func.saveToFile(dataSet)
            return


if __name__ == "__main__":
    main()
