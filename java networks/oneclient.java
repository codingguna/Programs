import java.io.*; import java.net.*;
import java.util.Scanner;
class oneclient
{
    public static void main(String args[]) throws Throwable
    {
        String str;
        Socket soc = new Socket("localhost",8000);
        Scanner in= new Scanner(new InputStreamReader(soc.getInputStream()));
        System.out.println("CLIENT WAITING FOR A MESSAGE FROM THE SERVER");
        PrintStream socout=new PrintStream(soc.getOutputStream());
        try
        {
            while(true)
            {
                str = in.next();
                System.out.println("Message Received: " + str);
                if(str.equals("bye"))
            {
                break;
            }
                socout.println(str);
            }
        }
        catch(Exception e)
        {
            System.out.println("Error "+e);
        }
    }
}

