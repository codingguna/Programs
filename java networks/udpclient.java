import java.io.*;
import java.net.*;
class udpclient
{
    public static void main(String[] args) throws Throwable
    {
        try
        {
            int i=0;
            byte[] b = new byte[1024];
            DatagramSocket soc = new DatagramSocket(2000);
            FileInputStream fi = new FileInputStream("C:\\Users\\gs400\\vs programs\\python\\hi.py");
            while(fi.available()!=0) {
            b[i]=(byte)fi.read(); i++;
        }
            fi.close();
            soc.send(new DatagramPacket(b,i,InetAddress.getByName("localhost"),1000));

        } catch(Exception e)
        {
            System.out.println("error :"+e);
        }System.out.println("File sent Scussfully..");
    }
}

