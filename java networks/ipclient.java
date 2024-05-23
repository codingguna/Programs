import java.io.PrintStream;
import java.net.InetAddress;
import java.net.Socket;

public class ipclient {
    public static void main(String[] args)throws Throwable {
        InetAddress ip=InetAddress.getLocalHost();
        String s=ip.getHostAddress();
        String s1=ip.getHostName();
        Socket soc=new Socket(s,4000);
        PrintStream socout=new PrintStream(soc.getOutputStream());
        socout.println(ip);
        socout.println("ip address :"+s);
        socout.println("host name :"+s1);

    }
}
