# Functional Programming Exercise

This exercise is designed to test your functional programming skills. The goal is to create several sets of numbers using inputtable array and perform various operations on them without using any form of `for` loop, including iterators. Your code is expected to not have side effects.

## Instructions

1. Start with an array called `inputtable` that has numbers between 1 and 10.
2. Use `inputtable` to create the following sets:
   a. Set of multiples of 5 between 1 and 51. Name it `fiveTable`, and print the contents to the console.
   b. Set of multiples of 13 between 1 and 131. Name it `thirteenTable`, and print the contents to the console.
   c. Set of squares of the numbers in `inputtable`. Name it `squaresTable`, and print the contents to the console.
3. Get (and then print) the odd multiples of 5 between 1 and 100 (i.e., 5, 15, ...).
4. Get (and then print) the sum of even multiples of 7 between 1 and 100 (i.e., find the multiples and then sum them: 14 + 28 + ...).
5. Use currying to rewrite the following function:
```
function cylinder_volume(r, h){ 
    var volume = 3.14 * r * r * h; 
    return volume; 
} 
```
a. Use `r = 5` and `h = 10` to call your curried function.
b. Reuse the function from part ‘a’ but use `h = 17`.
c. Reuse the function from part ‘a’ but use `h = 11`.
6. Use the `makeTag` function to take advantage of closures to wrap content with HTML tags, specifically show an HTML table consisting of a table row that has at least one table cell/element. You can use the console to output your results. The `makeTag` function is defined as follows:
```
makeTag = function(beginTag, endTag){ 
    return function(textcontent){ 
        return beginTag +textcontent +endTag; 
    } 
}
```
Example output for #6:
```
<table> 
<tr> 
<th>Firstname</th> 
<th>Lastname</th> 
<th>Age</th> 
</tr> 
<tr> 
<td>Jill</td> 
<td>Smith</td> 
<td>50</td> 
</tr> 
<tr> 
<td>Eve</td> 
<td>Jackson</td> 
<td>94</td> 
</tr> 
</table> 
```
Note that the `<th>` tag is optional. Please do not use this data, but substitute your own values for the contents of the cells.
7. Do the ‘generic’ version of questions 3 and 4, meaning the target multiple must not be hard coded; hint: we studied closures and currying. This means you should be able to use the same code to handle multiple scenarios, for example: first odd multiples of 11 and then even multiples of 3 (still in the range 1 to 100). Your code should allow the grader to combine a chosen multiple along with the choice of odd/even without writing any code.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
