import java.io.InputStreamReader;
import java.io.PrintStream;
import java.net.Socket;
import java.util.Scanner;

public class slidingclient {
    public static void main(String[] args) {
        try{
            int str,flag=0;
            int i,j=0;
            String ip;
            Scanner in=new Scanner(new InputStreamReader(System.in));
            System.out.println("entre the ip address :");
            ip=in.nextLine();
            Socket soc=new Socket(ip,5000);
            PrintStream socout=new PrintStream(soc.getOutputStream());
            Scanner socin=new Scanner(new InputStreamReader(soc.getInputStream()));
            System.out.println("entre number of frame number needed:");
            str=Integer.parseInt(in.nextLine());
            socout.println(str);
            while(j<str){
                i=Integer.parseInt(socin.nextLine());
                System.out.println("Received frame no :"+i);
                socout.println(i);
                j++;
            }
        }catch(Exception e){
            System.out.println("error :"+e);
        }
    }
}
