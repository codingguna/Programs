import java.io.*;
import java.net.*;
import java.util.*;
public class fileserver
{
    public static void main(String[] args)throws Throwable
    {
        try
        {
            String str;
            ServerSocket ss = new ServerSocket(8000);
            Socket soc = ss.accept();
            System.out.println("Server Listening.	");
            System.out.println("Connection frame: " + soc);//192.168.5.48
            PrintStream socout = new PrintStream(soc.getOutputStream());
            Scanner in = new Scanner(new InputStreamReader(System.in));
            System.out.println("Enter the text file name");
            String filename = in.nextLine();
            File fi = new File(filename);
            if(fi.exists()) {
            BufferedReader fileIn = new BufferedReader(new FileReader(filename));
            while((str = fileIn.readLine()) != null){
            socout.println(str);
        }
            System.out .println("The file send successfully");
        }
        else
        {
            System.out.println("File not exists");
        }
        } catch(Exception e)
        {
            System.out.println("Error: " + e);
        }
    }
}
//C:\Users\gs400\vs programs\python\hi.py