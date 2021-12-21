export default function updateStudentGradeByCity(
  listStudents,
  city,
  newGrades,
) {
  let output = 0;

  if (Array.isArray(listStudents)) {
    output = listStudents
      .filter((student) => {
        return student.location === city;
      })
      .map((student) => {
        const grade =
          newGrades
            .filter((gradeData) => {
              return gradeData.studentId === student.id;
            })
            .map((data) => {
              return data.grade;
            })[0] || 'N/A';

        return { ...student, grade };
      });
  }

  return output;
}
