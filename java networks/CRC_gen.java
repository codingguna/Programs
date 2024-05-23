import java.io.*;
import java.util.*;
public class CRC_gen {
    public static void main(String[] args) {
        int[] data;
        int[] div;
        int[] diviser;
        int[] rem;
        int[] crc;
        int data_bit,diviser_bit,tot_len,i,j;
        Scanner in=new Scanner(new InputStreamReader(System.in));
        System.out.print("enter number of date bits :");
        data_bit=Integer.parseInt(in.nextLine());
        data=new int[data_bit];
        System.out.println("\nEnter data bits :");
        for(i=0;i<data_bit;i++)
            data[i]=Integer.parseInt(in.nextLine());
        System.out.print("\nEnter the number of Diviser bits :");
        diviser_bit=Integer.parseInt(in.nextLine());
        diviser=new int[diviser_bit];
        System.out.print("\nenter the Diviser bits :");
        for(i=0;i<diviser_bit;i++)
            diviser[i]=Integer.parseInt(in.nextLine());
        System.out.print("\n Data bits are :");
        for (i=0;i<data_bit;i++)
            System.out.print(data[i]);
        System.out.print("\n the Diviser bits are :");
        for(j=0;j<diviser_bit;j++)
            System.out.print(diviser[j]);
        tot_len=data_bit+diviser_bit-1;
        div=new int[tot_len];
        rem=new int [tot_len];
        crc=new int[tot_len];
        for(i=0;i<data.length;i++)
            div[i]=data[i];
        System.out.println("\nDivident after appending 0's :");
        for (i=0;i<div.length;i++)
            System.out.print(div[i]);
        for(j=0;j<div.length;j++)
            rem[j]=div[j];
        rem=divide(div,diviser,rem);
        for(i=0;i<div.length;i++)
            crc[i] = (div[i]^rem[i]);
        System.out.print("\nData bits with CRC code : ");
        for(i=0;i<crc.length;i++)
            System.out.print(crc[i]);

        System.out.println("\nEnter data with CRC code of "+tot_len+" bits : ");
        for(i=0; i<crc.length; i++)
            crc[i]=Integer.parseInt(in.nextLine());
        System.out.print("\nData with CRC bits are : ");
        for(i=0; i< crc.length; i++)
        {
            System.out.print(crc[i]);
        }
        System.out.println();


        for(j=0; j<crc.length; j++)
        {
            rem[j] = crc[j];
        }
        rem = divide(crc, diviser, rem);
        for(i=0;i<rem.length;i++){
            if(rem[i]!=0){
                System.out.println("Message reseived with error!!..");
                break;
            }if(i==rem.length-1){
                System.out.println("No errors found \n Message received Scussfully...");
            }
        }
    }static int[] divide(int div[],int diviser[],int rem[]){
        int i,cur=0;
        while(true){
            for(i=0;i<diviser.length;i++)
                rem[cur+i]=(rem[cur+i]^diviser[i]);
            while(rem[cur]==0 && cur!=rem.length-1)
                cur++;
            if((rem.length-cur)<diviser.length)
                break;

        }return rem;
    }
}