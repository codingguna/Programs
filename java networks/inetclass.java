import java.net.InetAddress;

public class inetclass {
    public static void main(String[] args)throws Throwable {
        InetAddress ip=InetAddress.getLocalHost();
        System.out.println(ip.getAddress());
        System.out.println(ip.getCanonicalHostName());
        System.out.println(ip.getHostAddress());
        System.out.println(ip.getHostName());
        System.out.println(ip.hashCode());
        System.out.println(ip.isAnyLocalAddress());
        System.out.println(ip.isLinkLocalAddress());
        System.out.println(ip.isLoopbackAddress());
        System.out.println(ip.isMCGlobal());
        System.out.println(ip.isMCLinkLocal());
        System.out.println(ip.isSiteLocalAddress());
        System.out.println(ip.isMCNodeLocal());
        System.out.println(ip.isMCOrgLocal());
        System.out.println(ip.isMCSiteLocal());
        System.out.println(ip.isMulticastAddress());
        System.out.println(ip.isReachable(200));
        System.out.println(ip.getClass());

    }
}
