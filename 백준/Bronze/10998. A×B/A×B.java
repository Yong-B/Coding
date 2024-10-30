import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        
        int A = in.nextInt();
        int B = in.nextInt();
        while(A<=0 || A>=10 || B<=0 || B>=10){
            A = in.nextInt();
            B = in.nextInt();
        }
        System.out.print(A*B);
    }
}