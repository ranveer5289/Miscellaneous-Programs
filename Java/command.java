import java.io.*;
import java.util.*;
class command

{
        public static void main(String[] args) throws IOException
        {
               /* String[] command = new String[5];
                command[0] = "cmd";
                command[1] = "/c";
                command[2] = "copy";
                command[3] = "test.java";
                command[4] = "D:\\Cody";*/
               // String command = "cmd /c copy test.java D:";
                String source = "test.java";
                String des = "D:";
                String command = "cmd.exe\t/c\tcopy\t"+source+"\t"+des;
                System.out.println(command);
                Process p = Runtime.getRuntime().exec (command);
                BufferedReader input =new BufferedReader(new InputStreamReader(p.getInputStream()));
                BufferedReader error =new BufferedReader(new InputStreamReader(p.getErrorStream()));
                String line = null;

                while ((line = input.readLine()) != null)
                        System.out.println(line);
                input.close();

                while ((line = error.readLine()) != null)
                        System.out.println(line);
                error.close();







        }

}
