import java.net.ServerSocket;

public class randomport {
    public static void main(String[] args)throws Throwable {
        System.out.println("generate random port number :");
        ServerSocket ss=new ServerSocket(0);
        System.out.println("this server runs on port :"+ss.getLocalPort());
    }
}
