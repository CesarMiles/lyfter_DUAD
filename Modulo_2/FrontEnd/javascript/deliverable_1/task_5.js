// Entrada
const student = {
	name: "John Doe",
	grades: [
		{name: "math",grade: 80},
		{name: "science",grade: 100},
		{name: "history",grade: 60},
		{name: "PE",grade: 90},
		{name: "music",grade: 98}
	]
}

function getAverage(student) {
	const grades = student.grades.map((element) => {
		return element.grade;
	})
	const sumGrades = grades.reduce((accumulator, currentValue) => {
	return accumulator + currentValue;
	}, 0);
	const average = sumGrades / grades.length;
	return average
}

function getHighest(student) {
	let maxGrade = 0;
	let name = "";

	for (let item of student.grades) {
		if (item.grade > maxGrade) {
			maxGrade = item.grade;
			name = item.name;
		}
	}

	return name; 
}

function getLowest(student) {
	let minGrade = 100;
	let name = "";

	for (let item of student.grades) {
		if (item.grade < minGrade) {
			minGrade = item.grade;
			name = item.name;
		}
	}

	return name; 
}

const result = {
  name: student.name,
  gradeAvg: getAverage(student),
	highestGrade: getHighest(student),
	lowestGrade: getLowest(student)
}

console.log(student)
console.log(result)