import java.net.*;
import java.io.*;
import java.util.*;
public class echoclient
{
    public static void main(String[] args) throws Throwable
    {
        String str;
        InetAddress ip = InetAddress.getLocalHost();
        Socket soc = new Socket(ip, 9000);
        Scanner socin = new Scanner(new InputStreamReader(soc.getInputStream()));
        PrintStream socout = new PrintStream(soc.getOutputStream());
        Scanner in = new Scanner(new InputStreamReader(System.in));
        try{
        while(true)
        {
            System.out.print("Client Message:"); str = in.nextLine();
            if(str.equals("bye"))
        {
            break;
        }
            socout.println(str);
            System.out.println("Server Recieved a Message:" + socin.nextLine());
        }
        }
        catch(Exception e)
        {
            System.out.println("error"+e);
        }
    }
}

