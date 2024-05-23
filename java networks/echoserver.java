import java.net.*;
import java.io.*;
import java.util.*;
public class echoserver
{
    public static void main(String[] args) throws Throwable
    {
        String str;
        ServerSocket ss=new ServerSocket(9000);
        Socket soc = ss.accept();
        Scanner socin = new Scanner(new InputStreamReader(soc.getInputStream()));
        PrintStream socout = new PrintStream(soc.getOutputStream());
        System.out.println("Server Ready.	");
        try
        {
            while(true)
            {

                str = socin.nextLine();
                socout.println(str);
            }
        }
        catch(Exception e)
        {
            System.out.println("error"+e);
        }
    }
}

