import java.net.*;
import java.io.*;
import java.util.*;

public class oneserver {
    public static void main(String[] args) throws Throwable{
        String str;
        ServerSocket ss = new ServerSocket(8000);
        System.out.println("Waiting for Connection...\n");
        Socket soc = ss.accept();
        Scanner in = new Scanner(System.in);
        PrintStream socOut = new PrintStream(soc.getOutputStream());
        Scanner socln=new Scanner(new InputStreamReader(soc.getInputStream()));
        System.out.print("Server ready \n");
        System.out.println("SERVER WILL SEND A MESSAGE TO A CLIENT");
        while(true)
        {
            System.out.println("Enter Message to Send:");
            str = in.next();
             socOut.println(str);
             if(str.equals("bye"))
            {
                break;
            }
             String str1=socln.next();
             System.out.println("message:"+str1);
        }
    }
}