import java.io.*;
import java.net.*;
import java.util.*;
public class pingserver
{
    public static void main(String[] args) throws Throwable
    {
        String str;
        int i;
        System.out.println("Ping Server");
        ServerSocket ss = new ServerSocket(9999);
        Socket soc = ss.accept();
        Scanner socin = new Scanner(new InputStreamReader(soc.getInputStream()));
        PrintStream socout = new PrintStream(soc.getOutputStream());
        try {
        for(i = 0; i < 4; i++)
        {
            str = socin.nextLine();
            System.out.println("Pinged by client");
            socout.println(str + " Reply from host:bytes=3<time<1ms TT<=128");
        }
    }
    catch(Exception e)
    {
        System.out.println("Error: " + e);
    }
    }
}

