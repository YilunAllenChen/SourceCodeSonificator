
//I worked on the homework assignment alone, using only course materials.
import java.io.File;
import java.io.IOException;
import java.io.FileNotFoundException;
import java.util.Scanner;

/**
 * A easy-to-use Grep method to search for string in all files in specified
 * directory.
 *
 * @author Yilun Chen
 * @version 1.0.0
 */
public class Grep {

    /**
     * main method.
     *
     * @param args the arguments to be passed in.
     */
    public static void main(String[] args) throws IllegalArgumentException {

        // throws exception if arguments are not valid.
        IllegalArgumentException problem = new IllegalArgumentException(
                "Arguments are not valid. \nBe sure to use: \n    java Grep \"string\" "
                        + "fileName \nor:\n    java Grep -i \"string\" fileName\nor:\n "
                        + "   java Grep \"string\"\nor:\n    java Grep -i \"string\"");
        if (args.length == 3 && !args[0].equals("-i")) {
            System.out.println("1");
            throw problem;
        }

        if (args.length < 1 || args.length > 3) {
            System.out.println("2");
            throw problem;
        }

        // parsing the arguments.
        File src = new File("./");
        boolean sensitive = true;
        String string;
        if (args[0].equals("-i")) {
            sensitive = false;
            string = args[1];
            if (args.length == 3) {
                src = new File("./" + args[args.length - 1]);
            }
        } else {
            string = args[0];
            if (args.length == 2) {
                src = new File("./" + args[args.length - 1]);
            }
        }

        System.out.println(grep(src, string, sensitive));

    }

    /**
     * grep method that browses through all the files and directories
     *
     * @return a string that contains all lines found.
     * @param src       the file/directory to be searched in
     * @param string    the string to be searched for
     * @param sensitive whether this search is case-sensitive.
     */
    public static String grep(File src, String string, boolean sensitive) {
        String toBePrinted = new String();
        if (src.exists() && src.isDirectory()) {
            String[] files = src.list();
            for (String thisString : files) {
                File thisFile = new File(src.toPath() + "/" + thisString);
                String found = grep(thisFile, string, sensitive);
                if (found != null) {
                    toBePrinted = toBePrinted + found;
                }
            }
        } else if (src.exists() && src.isFile()) {
            toBePrinted = searchInFile(src, string, sensitive);
            if (toBePrinted != null) {
                return toBePrinted;
            }
        }
        return toBePrinted;
    }

    /**
     * grep method that browses through all the files and directories
     *
     * @return a string that contains all lines found.
     * @param src    the file/directory to be searched in
     * @param string the string to be searched for
     */

    /**
     * helper function searchInFile that deals with individual files.
     *
     * @return a string that contains all lines that contain the string in this
     *         current
     * @param file      the file/directory to be searched in
     * @param string    the string to be searched for
     * @param sensitive whether this search is case-sensitive.
     */
    public static String searchInFile(File file, String string, boolean sensitive) {
        String toBeReturned = new String();
        try {
            // System.out.println("Searching for: [" + string + "] in [" + file.toPath() +
            // "].");
            if (file.exists() && file.isFile()) {
                Scanner scanner = new Scanner(file);
                int num = 1;
                while (scanner.hasNext()) {
                    String thisLine = scanner.nextLine();
                    if (sensitive) {
                        if (thisLine.contains(string)) {
                            String toBePrinted = new String(file.getCanonicalPath() + ":" + num + ":" + thisLine);
                            toBeReturned = toBeReturned + "\n" + toBePrinted;
                        }
                    } else {
                        String thisLineLow = thisLine.toLowerCase();
                        String stringLow = string.toLowerCase();
                        if (thisLineLow.contains(stringLow)) {
                            String toBePrinted = new String(file.getCanonicalPath() + ":" + num + ":" + thisLine);
                            toBeReturned = toBeReturned + "\n" + toBePrinted;
                        }
                    }
                    num++;
                }
                scanner.close();
            }
        } catch (FileNotFoundException fnfe) {
            System.out.println(fnfe);
        } catch (IOException ioe) {
            System.out.println(ioe);
        }

        if (toBeReturned.isBlank()) {
            return null;
        } else {
            return toBeReturned;
        }
    }

}