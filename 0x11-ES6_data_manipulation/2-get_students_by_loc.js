export default function getStudentsByLocation(listStudents, city) {
  let output = [];

  if (Array.isArray(listStudents))
    output = listStudents.filter((student) => {
      return student.location === city;
    });

  return output;
}
