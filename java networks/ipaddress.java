import java.net.InetAddress;

public class ipaddress {
    public static void main(String[] args)throws Throwable {
        System.out.println("displaying host name & ip address");
        InetAddress ip=InetAddress.getLocalHost();
        System.out.println("host name & ip address: "+ip);
        System.out.println("host name :"+ip.getHostName());
        System.out.println("host address :"+ip.getHostAddress());

    }
}
