import java.io.*;
import java.net.*;
import java.util.*;

public class rceclient {
    public static void main(String[] args)throws Throwable {
        Socket soc=new Socket("localhost",1000);
        Scanner in=new Scanner(new InputStreamReader(System.in));
        PrintStream socout=new PrintStream(soc.getOutputStream());
        System.out.println("enter command calculator/notepad ;");
        String str=in.nextLine();
        socout.println(str);
    }
}
