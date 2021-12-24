export default function updateStudentGradeByCity(
  listStudents,
  city,
  newGrades,
) {
  return listStudents
    .filter((student) => student.location === city)
    .map((student) => {
      const [grade] = newGrades.filter(
        (gradeData) => gradeData.studentId === student.id,
      );

      return { ...student, grade: grade ? grade.grade : 'N/A' };
    });
}
