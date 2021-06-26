import java.util.*;
public class StockPrice {
    public int[] solution(int[] prices) {
        Stack<int[]> stack = new Stack<>();
        int[] result = new int[prices.length];
        stack.add(new int[]{0, prices[0]});
        for (int i = 1; i < prices.length; i++) {
            while (!stack.isEmpty()) {
                if (stack.peek()[1] > prices[i]) {
                    int[] element = stack.pop();
                    result[element[0]] = i - element[0];
                } else {
                    break;
                }
            }
            if (i == prices.length-1) {
                while (!stack.isEmpty()) {
                    int[] element = stack.pop();
                    result[element[0]] = prices.length - element[0] - 1;
                }
            }
            stack.add(new int[]{i, prices[i]});
        }
        return result;
    }
}