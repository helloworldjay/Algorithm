import java.util.*;
public class DiskController {
    public int solution(int[][] jobs) {
        PriorityQueue<int[]> maxHeap = new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return - Integer.compare(o1[1], o2[1]);
            }
        });
        Queue<int[]> queue = new LinkedList<>();
        Arrays.stream(jobs).forEach(queue::add);
        maxHeap.add(queue.poll());
        int sec = 0;
        int total = 0;
        while (!maxHeap.isEmpty()) {
            if (!queue.isEmpty()) {
                while (queue.peek()[0] <= sec) {
                    maxHeap.add(queue.poll());
                }
            }
            if (maxHeap.peek()[0] > sec) {
                sec = maxHeap.peek()[0];
            } else {
                int[] element = maxHeap.poll();
                total += (sec-element[0]) + element[1];
                sec += element[1];
            }
            maxHeap.stream().forEach(System.out::println);
        }
        return (int) (total / jobs.length);
    }
}
