import java.io.File;

public class sps7988_lab01 {
	// Get the size of the directory
	private static long directorySize(File path) {
		// initializing directorySum to zero
		long directorySum = 0;
		// getting the list of files from the path using listFiles()
		File[] listFiles = path.listFiles();
		int c = listFiles.length;
		// iterating over directory element
		for (int i = 0; i < c; i++) {
			// checking whether each element is a directory or not
			// using recursion to get the size of all files in that folder
			if (listFiles[i].isDirectory()) {
				directorySum = directorySum+ directorySize(listFiles[i]);
				
			}
			// if its not a directory, add the size to the directorySum
			else {
				directorySum = directorySum+ listFiles[i].length();
			}
		}
		// return the sum od directories and files
		return directorySum;
	}

	public static void main(String[] args) {
		// get the current working folder using "."
		File filePath = new File(".");
		// storing the final result in the size variable
		long size = directorySize(filePath);
		System.out.println("Total size in bytes:"+ size +" Bytes");
	}
}
