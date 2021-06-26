import java.util.*;

public class KthNumber {
    public static void main(String[] args) {
        solution(new int[] {1,2}, new int[][] {{1,2}});
    }

    public static int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        for (int i = 0; i < commands.length; i++) {
            int[] subsequence = Arrays.copyOfRange(array, commands[i][0]-1, commands[i][1]);
            Arrays.sort(subsequence);
            answer[i] = subsequence[commands[i][2]-1];
        }
        return answer;
    }
}
