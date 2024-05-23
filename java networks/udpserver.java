import java.net.*;
import java.util.*;
class udpserver
{
    public static void main(String[] args) throws Throwable
    {
        try
        {
            byte[] b = new byte[1024];
            Scanner in=new Scanner(System.in);
            DatagramSocket dsoc = new DatagramSocket(1000);
            while(true) {
                DatagramPacket dp = new DatagramPacket(b,b.length);
                dsoc.receive(dp);
                System.out.println(new String(dp.getData(),0,dp.getLength()));
                System.out.println("The recieved file successfully");
                System.out.print("do you want to exit enter y or n :");
                String s=in.nextLine();
                if (s.equals("y")){
                    break;
                }
            }
        }
        catch(Exception e)
        {
            System.out.print("error:"+e);
        }
    }
}
