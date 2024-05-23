import java.io.*;
import java.util.*;
class ShortestPath
{
    public static void main(String args[]) throws IOException
    {
        int n,s,d,i,j;
        int y=0, sd=9999;
        int[] in = new int[10];
        int[][] m = new int[5][5];
        int[] dis = new int[10];
        int[] path = new int[10];
        Scanner a = new Scanner(System.in);
        System.out.println("****** SHORTEST PATH ROUTING ******\n");
        System.out.print("Enter the No of Vertex:");
        n = Integer.parseInt(a.nextLine());
        System.out.println("");
        System.out.print("Enter the Source Vertex:");
        s = Integer.parseInt(a.nextLine());
        System.out.println("");
        System.out.print("Enter the Destination Vertex:");
        d = Integer.parseInt(a.nextLine());
        System.out.println("");
        for(i=1;i<n;i++)
        {
            j=1;
            while(j<n)
            {
                System.out.print("\nEnter the distance between [" +i+ "," +(j+1)+"]:");
                m[i][j+1] = Integer.parseInt(a.nextLine());
                m[j+1][i] = m[i][j+1];
                j++;
            }
        }
        for(i=1;i<=n;i++)
        {
            in[i] = 0;
            dis[i] = m[s][i];
            if(m[s][i]!=0)
                path[i] = s;
        }
        in[s] = 1;
        dis[s] = 0;
        for(i=2;i<n;i++)
        {
            for(j=1;j<=n;j++)
            {
                if(in[j]==0)
                {
                    if(dis[j]<sd)
                    {
                        sd=dis[j];
                        y=j;
                    }
                }
            }
            in[y]=1;
            for(j=1;j<=n;j++)
            {
                if((in[j]==0)&&(m[y][j]!=0))
                {
                    if((dis[y]+m[y][j])<dis[j])
                    {
                        dis[j]=dis[y]+m[y][j];
                        path[j]=y;
                    }
                }
            }
        }
        i=d;
        System.out.print("\n");
        System.out.println("The Shortest Path is : \n");
        System.out.print(" "+d);
        while(path[i]!=s)
        {
            System.out.print("-----> " +path[i]);
            i=path[i];
        }
        System.out.print("---	> ");
        System.out.println(s);
        System.out.print("\n");
        System.out.println("Distance of the Shortest Path is "+dis[d]);
    }
}