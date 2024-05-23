import java.net.*;
import java.util.*;
public class Main
{
    public static void main(String[] args)throws Throwable
    {
        System.out.println("Hello world!");
        Enumeration<NetworkInterface> nics = NetworkInterface.getNetworkInterfaces();
        while (nics.hasMoreElements()) {
            NetworkInterface nic = nics.nextElement();
            if (!nic.isLoopback()) {
                Enumeration<InetAddress> inetAddresses = nic.getInetAddresses();
                while (inetAddresses.hasMoreElements()) {
                    InetAddress inetAddress = inetAddresses.nextElement();
                    if (!inetAddress.isLoopbackAddress()) {
                        System.out.println("MAC Address : " + nic.getHardwareAddress());
                    }
                }
            }
        }
    }


}