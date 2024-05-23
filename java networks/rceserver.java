import java.io.InputStreamReader;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;

public class rceserver {
    public static void main(String[] args) throws Throwable{
        ServerSocket ss= new ServerSocket(1000);
        System.out.println("SErver is waiting...");
        Socket soc=ss.accept();
        System.out.println("server is ready");
        Runtime run=Runtime.getRuntime();
        Scanner socin=new Scanner(new InputStreamReader(soc.getInputStream()));
        String str=socin.nextLine();
        System.out.println("the command received :"+str);
        run.exec(str);
        System.out.println("Command executed scussfully");
    }
}
