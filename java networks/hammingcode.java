import java.util.*;
public class hammingcode {
    public static void main(String[] args) {
        int[] d=new int[7];
        int[] p=new int[4];
        int[] c=new int[11];
        int[] r=new int[11];
        int[] pr=new int[4];
        int[] rd=new int[7];
        int[] s=new int[4];
        Scanner in=new Scanner(System.in);
        System.out.print("Enter the 7 digit data code :");
        for(int i=0;i<7;i++){
            d[i]=in.nextInt();}
        System.out.println();
        p[0]=d[0]^d[1]^d[3]^d[4]^d[6];
        p[1]=d[0]^d[2]^d[3]^d[5]^d[6];
        p[2]=d[1]^d[2]^d[3];
        p[3]=d[4]^d[5]^d[6];
        System.out.println("parity bits p1,p2,p3,p4 ="+p[1]+","+p[1]+","+p[2]+","+p[3]);
        System.out.print("complete code is ");
        c[0]=p[0];
        c[1]=p[1];
        c[2]=d[0];
        c[3]=p[2];
        c[4]=d[1];
        c[5]=d[2];
        c[6]=d[3];
        c[7]=p[3];
        c[8]=d[4];
        c[9]=d[5];
        c[10]=d[6];
        for(int i=0;i<11;i++) {
            System.out.print(c[i]+" ");}
        System.out.println("\nEnter the received code :");
        for (int i=0;i<11;i++){
            r[i]=in.nextInt();}
       /* pr[0]=r[0];
        pr[1]=r[1];
        rd[0]=r[2];
        pr[2]=r[3];
        rd[1]=r[4];
        rd[2]=r[5];
        rd[3]=r[6];
        pr[2]=r[7];
        rd[4]=r[8];
        rd[5]=r[9];
        rd[6]=r[10];*/
        s[0]=r[0]^r[2]^r[4]^r[6]^r[8]^r[10];
        s[1]=r[1]^r[2]^r[5]^r[6]^r[9]^r[10];
        s[2]=r[3]^r[4]^r[5]^r[6];
        s[3]=r[7]^r[8]^r[9]^r[10];
        int dec=(s[0])+(s[1]*2)+(s[2]*4)+(s[3]*8);
        if(dec==0){
            System.out.println("\n no errors..");
        }else{
            System.out.println("\nError at "+dec+"th position.");
            if(r[dec-1]==0)
                r[dec-1]=1;
            else
                r[dec-1]=0;
        System.out.print("\nCorrected code is :");
        for (int i=0;i<11;i++) {
            System.out.print(r[i] + " ");}
        }}}