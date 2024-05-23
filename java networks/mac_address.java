import java.net.*;

class mac_address {
    public static void main(String[] args)throws Throwable {
        InetAddress ip =InetAddress.getLocalHost();
        NetworkInterface ni=NetworkInterface.getByInetAddress(ip);
        byte[] b=ni.getHardwareAddress();
        String[] mac=new String[b.length];
        for(int i=0; i <b.length;i++){
            mac[i]=String.format("%02X",b[i]);
        }
        String macaddr=String.join("-",mac);
        System.out.println("ip address : "+ip.getHostAddress());
        System.out.println("mac address : "+macaddr);

    }
}
