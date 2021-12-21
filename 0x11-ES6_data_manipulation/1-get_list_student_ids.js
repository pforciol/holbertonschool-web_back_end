export default function getListStudentIds(listStudents) {
  let output = [];

  if (Array.isArray(listStudents))
    output = listStudents.map((student) => {
      return student.id;
    });

  return output;
}
