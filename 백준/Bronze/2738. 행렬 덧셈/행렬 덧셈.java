import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[][] matrix = new int[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                matrix[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                // matrix[i][j]에는 이미 A의 값이 들어있음
                // 거기에 방금 읽은 B의 값을 더해서 StringBuilder에 추가
                int sum = matrix[i][j] + Integer.parseInt(st.nextToken());
                sb.append(sum).append(" ");
            }
            sb.append("\n"); // 한 행이 끝나면 줄바꿈
        }

        // 4. 최종 결과 한 번에 출력
        System.out.print(sb);
    }
}
