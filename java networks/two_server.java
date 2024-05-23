import java.net.*;
import java.io.*;
import java.util.*;
class two_server
{
    public static void main(String args[]) throws Throwable
    {
        String str, str1;
        ServerSocket ss = new ServerSocket(8000);
        System.out.println("Waiting for Connection...\n");
        Socket soc = ss.accept();
        Scanner socin = new Scanner(new InputStreamReader(soc.getInputStream()));
        PrintStream socout = new PrintStream(soc.getOutputStream());
        Scanner in = new Scanner(new InputStreamReader(System.in));
        System.out.print("Server ready \n");
        try
        {
            while(true)
            {
                System.out.print("Server: ");
                str=in.next();
                socout.println(str);
                if(str.equals("bye"))
                {
                    break;
                }
                str1 = socin.next();
                System.out.println("client :"+str1);
                if(str1.equals("bye"))
                {
                    break;
                }
            }
        }
        catch(Exception e)
        {
            System.out.println("error "+e);
        }
    }
}

