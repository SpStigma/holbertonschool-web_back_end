export default function updateStudentGradeByCity(array, city, newGrades) {
  if (!Array.isArray(array)) {
    return [];
  }
  const newArray = array.map((student) => {
    if (student.location === city) {
      const matchingGrade = newGrades.find((grade) => grade.studentId === student.id);

      if (matchingGrade) {
        return {
          ...student,
          grade: matchingGrade.grade,
        };
      }
      return {
        ...student,
        grade: 'N/A',
      };
    }
    return student;
  });

  return newArray;
}
