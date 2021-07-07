import java.util.*;
public class Pick2AndSum {
    public int[] solution(int[] numbers) {
        Set<Integer> sumSet = new HashSet<>();
        for (int i = 0; i < numbers.length - 1; i++) {
            for (int j = i + 1; j < numbers.length; j++) {
                sumSet.add(numbers[i]+numbers[j]);
            }
        }
        int[] result = new int[sumSet.size()];
        for (int i = 0; i < result.length; i++) {
            result[i] = (int) sumSet.toArray()[i];
        }
        Arrays.sort(result);
        return result;
    }
}
