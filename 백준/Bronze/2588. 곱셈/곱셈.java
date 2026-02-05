import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;


public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String strA = br.readLine();
        String strB = br.readLine();
        int a = Integer.parseInt(strA);
        int b = Integer.parseInt(strB);
        
        br.close();
        
        StringBuilder sb = new StringBuilder();
        
        sb.append(a * (b%10));
        sb.append('\n');
        
        sb.append(a * ((b%100)/10));
        sb.append('\n');
        
        sb.append(a * (b/100));
        sb.append('\n');
        
        sb.append(a * b);
        
        System.out.println(sb);
        
    }
}