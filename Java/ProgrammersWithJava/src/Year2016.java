import java.util.*;
public class Year2016 {
    public String solution(int a, int b) {
        String[] dates = new String[] {"FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"};
        int[] days = new int[] {0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30};
        return dates[(Arrays.stream(Arrays.copyOfRange(days, 0, a)).sum()+b-1)%7];
    }
}
