import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;

public class Printer {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        Queue<Integer> queue = new LinkedList<>();
        Arrays.stream(priorities).forEach(queue::add);
//        queue.stream().forEach(x -> System.out.println(x));
        int count = 1;
        int result = -1;
        while (!queue.isEmpty()) {
            if( Collections.max(queue) == queue.peek()) {
                if (location == 0) {
                    result = count;
                    break;
                } else {
                    count++;
                    queue.poll();
                }
            } else {
                queue.add(queue.poll());
            }
            location = (location - 1 + queue.size())%(queue.size());
        }
        return result;
    }
}
