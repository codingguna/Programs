import java.io.*;
import java.net.*;
import java.util.*;
public class pingclient
{
    public static void main(String args[]) throws IOException
    {
        int i;
        String str;
        Scanner in = new Scanner(new InputStreamReader(System.in));
        System.out.println("Enter the IP address: ");
        String ip = in.nextLine();
        Socket soc = new Socket(ip, 9999);
        Scanner socin = new Scanner(new InputStreamReader(soc.getInputStream()));
        PrintStream socout = new PrintStream(soc.getOutputStream());
        System.out.println("Pinging " + ip + " with 32 bytes of data");
        try {for (i = 0; i < 4; i++)
        {
            socout.println(ip);
            str = socin.nextLine();
            if (str != null) {
            Thread.sleep(2000);
            System.out.println("Reply from " + str);
        }
        else
        {
            Thread.sleep(2000);
            System.out.println("Request time out");
        }
        }
    }
    catch (Exception e) { System.out.println("Request timed out");
    }
    }
}