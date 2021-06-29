import java.util.*;
public class DiskController {
    public static void main(String[] args) {
        System.out.println(solution(new int[][] {{0,3},{1,9},{2,6}}));
    }

    public static int solution(int[][] jobs) {
        PriorityQueue<int[]> minHeap = new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return Integer.compare(o1[1]-o1[0], o2[1]-o2[0]);
            }
        });
        Queue<int[]> queue = new LinkedList<>();
        Arrays.stream(jobs).forEach(queue::add);
        minHeap.add(queue.poll());
        int sec = 0;
        int total = 0;
        while (!minHeap.isEmpty()) {
            if (minHeap.peek()[0] > sec) {
                sec = minHeap.peek()[0];
            } else {
                int[] element = minHeap.poll();
                total += (sec-element[0]) + element[1];
                sec += element[1];
            }
            while (true) {
                if (queue.isEmpty()) {
                    break;
                } else if (queue.peek()[0] <= sec) {
                    minHeap.add(queue.poll());
                } else {
                    break;
                }
            }
            if (!queue.isEmpty()) {
                while (queue.peek()[0] <= sec) {
                    minHeap.add(queue.poll());
                }
            }
        }
        return (int) (total / jobs.length);
    }
}
