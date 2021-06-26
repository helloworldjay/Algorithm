import java.util.*;

public class CouldnotFinishRace {
    public static void main(String[] args) {
        solution(new String[] {"leo", "kiki", "eden"}, new String[] {"eden", "kiki"});
    }
    public static String solution(String[] participant, String[] completion) {
        HashMap<String, Integer> map = new HashMap<String, Integer>();
        for (String participantMember : participant) {
            if (map.containsKey(participantMember)) {
                map.put(participantMember, map.get(participantMember)+1);
            } else {
                map.put(participantMember, 1);
            }
        }
        for (String completionMember: completion) {
            if (map.get(completionMember) == 1) {
                map.remove(completionMember);
            } else {
                map.put(completionMember, map.get(completionMember)-1);
            }
        }
        return map.keySet().toArray()[0].toString();
    }
}
