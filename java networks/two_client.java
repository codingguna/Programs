import java.io.*;
import java.net.*;
import java.util.*;
class two_client
{
    public static void main(String args[])throws Throwable
    {
        String str,str1;
        Socket soc = new Socket("LocalHost",8000);
        Scanner socin = new Scanner(new InputStreamReader(soc.getInputStream()));
        PrintStream socOut = new PrintStream(soc.getOutputStream());
        Scanner in = new Scanner(new InputStreamReader(System.in));
        System.out.println("Client Waiting for a Message");
        try
        {
            while(true)
            {
                str = socin.next();
                System.out.println("Server: " + str);
                if(str.equals("bye"))
                {
                    break;
                }
                System.out.print("Client: ");
                str1 = in.next();
                socOut.println(str1);
                if(str1.equals("bye"))
                {
                    break;
                }
            }
        }
        catch(Exception e)
        {
            System.out.println(e);
        }


    }
}
