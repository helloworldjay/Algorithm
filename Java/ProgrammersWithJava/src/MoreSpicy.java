import java.util.*;
public class MoreSpicy {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> minHeap = new PriorityQueue<Integer>();
        Arrays.stream(scoville).forEach(minHeap::add);
        int shuffleTime = 0;
        while (minHeap.peek() < K) {
            if (minHeap.size() == 1) {
                return -1;
            }
            shuffleTime++;
            int shuffledElement = minHeap.poll() + minHeap.poll()*2;
            minHeap.add(shuffledElement);
        }
        return shuffleTime;
    }
}
