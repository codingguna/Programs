import java.net.*;
import java.io.*;
import  java.util.*;

public class slidingserver {
    public static void main(String[] args) throws Throwable{
        try{
            int i,str,p;
            ServerSocket ss=new ServerSocket(5000);
            System.out.println("Server ready ...");
            Socket soc=ss.accept();
            Scanner socin=new Scanner(new InputStreamReader(soc.getInputStream()));
            PrintStream socout=new PrintStream(soc.getOutputStream());
            p=Integer.parseInt(socin.nextLine());
            for (i=0;i<=p;++i){
                System.out.println("Sending frame no : "+i);
                socout.println(i);
                System.out.println("Waiting for acknowledgement ");
                Thread.sleep(2000);
                str=Integer.parseInt(socin.next());
                System.out.println("Received acknowledgement for frame no :"+i+"as"+str);
            }

        } catch(Exception e)
        {
            System.out.println("error :"+e);
        }
    }
}
