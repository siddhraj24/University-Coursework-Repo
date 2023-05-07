## DirectorySize

This repository contains implementations of a program that calculates the total size (in bytes) of all files in the current directory and all sub-directories. The program has been implemented in Python, Java, and C.

## Python Implementation
The Python implementation is contained in the file `sps7988_lab01.py`. It uses the `os` module to recursively iterate through the directory tree and the `os.path.getsize()` method to calculate the size of each file. The total size is stored in a variable and printed to the console at the end of the program.

To run the Python implementation, simply navigate to the directory containing the `sps7988_lab01.py` file and run the command `python sps7988_lab01.py`.

## Java Implementation
The Java implementation is contained in the file `sps7988_lab01.java`. It uses the `java.io.File` class to recursively iterate through the directory tree. The total size is stored in a variable and printed to the console at the end of the program.

To run the Java implementation, navigate to the directory containing the `sps7988_lab01.java` file and run the following commands:
```
javac sps7988_lab01.java
java sps7988_lab01
```

## C Implementation
The C implementation is contained in the file `sps7988_lab01.c`. It uses the `dirent.h` header file to recursively iterate through the directory tree and the `sys/stat.h` header file to calculate the size of each file. The total size is stored in a variable and printed to the console at the end of the program.

To run the C implementation, navigate to the directory containing the `sps7988_lab01.c` file and run the following commands:
```
gcc sps7988_lab01.c -o sps7988_lab01
./sps7988_lab01
```

Note: The `gcc` command is used to compile the C code and the `-o` flag specifies the name of the output file. In this case, the output file is named `sps7988_lab01`. The `./sps7988_lab01` command is used to run the compiled program.

## Conclusion
This repository demonstrates how the same program can be implemented in multiple programming languages. By comparing the different implementations, we can gain insight into the strengths and weaknesses of each language and choose the best language for a given task.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
