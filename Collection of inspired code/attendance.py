class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.attendance = {}

    def mark_attendance(self, date, status):
        self.attendance[date] = status

    def get_attendance(self, date):
        return self.attendance.get(date, "Not marked")

class AttendanceSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, name, student_id):
        self.students[student_id] = Student(name, student_id)

    def mark_attendance(self, student_id, date, status):
        student = self.students.get(student_id)
        if student:
            student.mark_attendance(date, status)
        else:
            print(f"Student with ID {student_id} not found.")

    def get_student_attendance(self, student_id, date):
        student = self.students.get(student_id)
        if student:
            return student.get_attendance(date)
        else:
            return "Student not found."

    def get_attendance_summary(self, date):
        summary = []
        for student_id, student in self.students.items():
            status = student.get_attendance(date)
            summary.append(f"{student.name}: {status}")
        return summary

# Example usage
if __name__ == "__main__":
    attendance_system = AttendanceSystem()

    # Add students to the system
    attendance_system.add_student("Shalikram", 1)
    attendance_system.add_student("Rekha", 2)
    attendance_system.add_student("Sagar", 3)
    attendance_system.add_student("Prakash", 4)

    # Mark attendance
    attendance_system.mark_attendance(1, "2024-04-12", "Present")
    attendance_system.mark_attendance(2, "2024-04-12", "Absent")
    attendance_system.mark_attendance(3, "2024-04-12", "Present")
    attendance_system.mark_attendance(4, "2024-04-12", "Present")

    # Get attendance summary
    date = "2024-04-12"
    print(f"Attendance summary for {date}:")
    for line in attendance_system.get_attendance_summary(date):
        print(line)
