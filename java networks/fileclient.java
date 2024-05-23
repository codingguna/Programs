import java.io.*;
import java.net.*;
import java.util.*;
public class fileclient
{
    public static void main(String[] args)throws Throwable
    {
        try
        {
            String str;
            Socket soc = new Socket(InetAddress.getLocalHost(),8000);
            Scanner socin = new Scanner(new InputStreamReader(soc.getInputStream()));
            if((str = socin.next()) != null) {
            System.out.println("The content of the file is"); System.out.println(str);
            System.out.println("The file is received successfully");
        }
        }
        catch(Exception e)
        {
            System.out.println("Error: " + e);
        }
    }
}
