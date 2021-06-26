import java.util.Stack;
import java.util.*;

public class ImplementFunction {
    public int[] solution(int[] progresses, int[] speeds) {
        int[] days = new int[progresses.length];
        List<Integer> result = new ArrayList<Integer>();
        for (int i = 0; i < progresses.length; i++) {
            if ((100 - progresses[i]) % speeds[i] == 0) {
                days[i] = (100 - progresses[i]) / speeds[i];
            } else {
                days[i] = (int) ((100 - progresses[i]) / speeds[i]) + 1;
            }
        }
//        Arrays.stream(days).forEach(s -> System.out.println(s));
        int criterion = 0;
        for (int i = 0; i < days.length; i++) {
            if (days[criterion] < days[i]) {
                result.add(i - criterion);
                criterion = i;
            }
        }
        result.add(days.length - criterion);
        return result.stream().mapToInt(i -> i).toArray();
    }
}
