import java.util.*;
public class StockPrice {
    public int[] solution(int[] prices) {
        Stack<Integer> stack = new Stack<>();
        int[] result = new int[prices.length];
        stack.add(0);
        for (int i = 1; i < prices.length; i++) {
            while (!stack.isEmpty()) {
                if (prices[stack.peek()] > prices[i]) {
                    int element = stack.pop();
                    result[element] = i - element;
                } else {
                    break;
                }
            }
            if (i == prices.length-1) {
                while (!stack.isEmpty()) {
                    int element = stack.pop();
                    result[element] = prices.length - element - 1;
                }
            }
            stack.add(i);
        }
        return result;
        // 	실행한 결괏값 [4,0,2,1,0]이(가) 기댓값 [4,3,1,1,0]와(과) 다릅니다.
    }
}