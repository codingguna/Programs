import java.io.*;
import java.net.*;
import java.util.*;
public class talkserver
{
    public static void main(String[] args)throws Throwable
    {
        String str1,str2;
        ServerSocket ss= new ServerSocket(9999);
        Socket soc = ss.accept();
        Scanner socin = new Scanner(new InputStreamReader(soc.getInputStream()));
        PrintStream socout = new PrintStream(soc.getOutputStream());
        Scanner in = new Scanner(new InputStreamReader(System.in));
        System.out.println("TALK SERVER");
        System.out.println("	");
        System.out.println("Node Successfully connected..");
        try {
            while(true){
                str1 = socin.nextLine();
                System.out.println("Message Received");
                System.out.println("Message : "+str1);
                str2 = in.nextLine();
                if(str2.equals("bye"))
                {
                    break;
                }
                socout.println(str2);
                socout.flush();
                System.out.println("Message Sent Successfully");
            }
        }
        catch(Exception e)
        {
            System.out.println("error"+e);
        }
    }
}

