
/*
1)Start with an array called inputtable. The array should have numbers between 1 and 10. 
*/
function inputtable (end) {
  return Array(end)
    .fill()
    .map((_, i) => i + 1)
}
console.log('inputtable', inputtable(10))
/*
The inputtable function is a JavaScript function that takes a single argument, end. When called, the function creates a new array of integers ranging from 1 to the 
value of end. It does this by using the Array constructor to create an empty array of length end, and then using the fill() method to fill that array with 
undefined values. Finally, the map() method is used to iterate over the array and replace each undefined value with its corresponding index + 1, thus creating an
 array of integers ranging from 1 to end. The resulting array is then returned by the inputtable function.
*/
/*
Output:
inputtable [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
*/


/*
2.a)Set of multiples of 5 between 1 and 51
*/
function fiveTable (end) {
  return Array(end)
    .fill()
    .map((_, i) => i + 1)
    .filter(num => num % 5 === 0 && num != 0)
}
console.log('fiveTable', fiveTable(51))
/*
The fiveTable function is a JavaScript function that takes a single argument, end. When called, the function creates a new array of integers ranging from 1 to end,
 and then filters that array to only include numbers that are divisible by 5 and are not zero. The resulting array is then returned by the fiveTable function.
*/
/*
Output:
fiveTable [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
*/


/*
2.b)Set of multiples of 13 between 1 and 131
*/
function thirteenTable (end) {
  return Array(end)
    .fill()
    .map((_, i) => i + 1)
    .filter(num => num % 13 === 0 && num != 0)
}
console.log('thirteenTable', thirteenTable(131))
/*
The thirteenTable function is a JavaScript function that takes a single argument, end. When called, the function creates a new array of integers ranging from 1 to end,
 and then filters that array to only include numbers that are divisible by 13 and are not zero. The resulting array is then returned by the thirteenTable function.
*/
/*
Output:
thirteenTable [13, 26, 39, 52, 65, 78, 91, 104, 117, 130]
*/


/*
2.c)Set of squares of the numbers in inputtable
*/
//Function definition
function inputtable (end) {
  return Array(end)
    .fill()
    .map((_, i) => i + 1)
}
/*
Here map function iterates over each element of array and performs a callback function on
every valid iteration and maps it to a new array.
*/
function squaresTable (end) {
  return inputtable(end).map(num => Math.pow(num, 2))
}
console.log('squaresTable', squaresTable(10))
/*
Output:
squaresTable [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
*/


/*
3)Odd multiples of 5 between 1 and 100
*/
//Function defination
function oddMultiplesOfFive (end) {
  return Array(end)
    .fill()
    .map((_, i) => i + 1)
    .filter(num => num % 5 === 0 && num % 2 !== 0)
}
console.log('oddMultiplesOfFive', oddMultiplesOfFive(100))
/*
The oddMultiplesOfFive function is a JavaScript function that takes a single argument, end. When called, the function creates a new array of integers ranging
 from 1 to end, and then filters out all numbers that are not odd multiples of 5. The resulting array of odd multiples of 5 is returned by the function, and is 
 also logged to the console using the console.log() statement at the end of the code snippet.
*/
/*
Output:
oddMultiplesOfFive [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]
*/


/*
4) Get (and then print) the sum of even multiples of 7 between 1 and 100
*/
const evenMultiplesOfSeven = Array.from({ length: 101 }, (_, i) => i).filter(
  num => num % 7 === 0 && num % 2 === 0
)
const sumOfMultiplesOfSeven = evenMultiplesOfSeven.reduce(
  (prev, curr) => prev + curr,
  0
)
console.log('sumOfMultiplesOfSeven:', sumOfMultiplesOfSeven)
/*This code creates an array of even multiples of 7 up to and including 100 using Array.from() and filter() methods, and then calculates the sum of those numbers
 using the reduce() method, and logs the result to the console using console.log().*/
/*
Output:
sumOfMultiplesOfSeven: 392
*/


/*
5)Use currying to rewrite the function.
*/
/*
With the help of currying we can pass two argument even though the function parameter has only one. It lets you use the first argument for the first function then 
second argument for next function.
*/
function cylinder_volume (r) {
  return function (h) {
    return 3.14 * r * r * h
  }
}
console.log('cylinder_volume(5)(10)', cylinder_volume(5)(10))
console.log('cylinder_volume(5)(17)', cylinder_volume(5)(17))
console.log('cylinder_volume(5)(11)', cylinder_volume(5)(11))
/*
Output:
cylinder_volume(5)(10) 785
cylinder_volume(5)(17) 1334.5
cylinder_volume(5)(11) 863.5
*/


/*
6)Use the following code to take advantage of closures to wrap content with HTML tags, specifically show an HTML table consisting of a table row that has at least
one table cell/element. You can use the console to output your results.
 */
/*
A closure is the combination of a function and the lexical environment within which that function was declared.I have created separate variable executing maketag 
function for different HTMl Tags and created datasets for td and th tags and wrapped it using trTag and finally in the tableTag.
*/
const makeTag = function (beginTag, endTag) {
  return function (textcontent) {
    return beginTag + textcontent + endTag
  }
}
//Defining tags
let tableTag = makeTag('<table>' + '\n', '</table>')
let tdTag = makeTag('<td>', '</td>')
let trTag = makeTag('<tr>' + '\n', '</tr>' + '\n')
let thTag = makeTag('<th>', '</th>')
let FieldTitle1 = thTag('Departments')
let FieldTitle2 = thTag('Number of Students Enrolled')
let allFields = FieldTitle1 + '\n' + FieldTitle2 + '\n'
let sport1 = tdTag('Computer Science')
let students1 = tdTag('500')
let dataSet1 = sport1 + '\n' + students1 + '\n'
let sport2 = tdTag('Industrial')
let students2 = tdTag('200')
let dataSet2 = sport2 + '\n' + students2 + '\n'
let row1 = trTag(allFields)
let row2 = trTag(dataSet1)
let row3 = trTag(dataSet2)
let rowData = row1 + '\n' + row2 + '\n' + row3
let table = tableTag(rowData)
console.log('HTML Table', '\n', table)
/*
HTML Table 
 <table>
<tr>
<th>Departments</th>
<th>Number of Students Enrolled</th>
</tr>
<tr>
<td>Computer Science</td>
<td>500</td>
</tr>
<tr>
<td>Industrial</td>
<td>200</td>
</tr>
</table>
*/


/*
7) Do the ‘generic’ version of questions 3 and 4, meaning the target multiple must not be hard coded.
*/
function getMultiplesOf (multiple) {
  return function (rangeStart, rangeEnd, includeEven) {
    const numbers = Array.from(
      { length: rangeEnd - rangeStart + 1 },
      (_, i) => i + rangeStart
    )
    return numbers.filter(
      num =>
        num % multiple === 0 && (includeEven ? num % 2 === 0 : num % 2 !== 0)
    )
  }
}
// Example usage:
const getOddMultiplesOf11 = getMultiplesOf(11)
const first10OddMultiplesOf11 = getOddMultiplesOf11(1, 100, false).slice(0, 10)
console.log('First 10 odd multiples of 11:', first10OddMultiplesOf11)
const getEvenMultiplesOf3 = getMultiplesOf(3)
const first10EvenMultiplesOf3 = getEvenMultiplesOf3(1, 100, true).slice(0, 10)
console.log('First 10 even multiples of 3:', first10EvenMultiplesOf3)
/*
This code defines a higher-order function getMultiplesOf that returns another function that takes three arguments rangeStart, rangeEnd, and includeEven.
The returned function creates an array of numbers ranging from rangeStart to rangeEnd, and filters out the numbers that are not multiples of the specified multiple. 
If includeEven is true, the function also filters out odd multiples, otherwise it filters out even multiples.
The getMultiplesOf function is then used to create two new functions: getOddMultiplesOf11 and getEvenMultiplesOf3, which respectively return the odd multiples of 11 
and even multiples of 3 within a given range.
The console.log() statements then demonstrate how to use these functions to find the first 10 odd multiples of 11, and the first 10 even multiples of 3, 
within a range of 1 to 100.
*/
/*
Output:
First 10 odd multiples of 11: [ 11, 33, 55, 77, 99 ]
First 10 even multiples of 3: [6, 12, 18, 24, 30,36, 42, 48, 54, 60]
*/
