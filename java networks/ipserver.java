import java.io.InputStreamReader;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;

public class ipserver {
    public static void main(String[] args) throws Throwable{
        ServerSocket ss=new ServerSocket(4000);
        Socket soc= ss.accept();
        Scanner in =new Scanner(new InputStreamReader(soc.getInputStream()));
        try{while (true){
            String s=in.nextLine();
            System.out.println(s);
        }}catch(Exception e){
            System.out.println(e);
        }
    }
}
