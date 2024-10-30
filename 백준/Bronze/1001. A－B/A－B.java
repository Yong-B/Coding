import java.util.Scanner;
 
public class Main {
    public static void main(String[] args){
        
        Scanner scan = new Scanner(System.in);
        int A = scan.nextInt();
        int B = scan.nextInt();
   
        while(A<=0 || A>=10 || B<=0 || B>=10) {
            A = scan.nextInt();
            B = scan.nextInt();            
        }
        
        System.out.println(A-B);
    }
}