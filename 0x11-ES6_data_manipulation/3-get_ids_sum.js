export default function getStudentIdsSum(listStudents) {
  let output = 0;

  if (Array.isArray(listStudents))
    output = listStudents.reduce((sum, student) => {
      return sum + student.id;
    }, 0);

  return output;
}
