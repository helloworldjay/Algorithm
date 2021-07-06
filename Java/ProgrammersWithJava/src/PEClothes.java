import java.util.*;
// https://edu.goorm.io/learn/lecture/41/%EB%B0%94%EB%A1%9C%EC%8B%A4%EC%8A%B5-%EC%83%9D%ED%99%9C%EC%BD%94%EB%94%A9-%EC%9E%90%EB%B0%94-java/lesson/792/set
public class PEClothes {
    public static void main(String[] args) {
//        System.out.println(solution(5, new int[] {2, 4}, new int[] {1, 3, 5}));
        System.out.println(solution(7, new int[] {2, 3, 4}, new int[] {1, 2, 3, 6}));
    }
    public static int solution(int n, int[] lost, int[] reserve) {
//        Set<Integer> lost_set = new HashSet(Arrays.asList(lost));
//        Set<T> mySet = Set.of(someArray); Java 9+
//        var lost_set = Set.of(Arrays.stream(lost)); // Java 10+
        Set<Integer> lost_set = new HashSet<>();
        Set<Integer> reserve_set = new HashSet<>();
//        Set<Integer> temp_set = ; 깊은 복사 안됨
        for (int person : lost) {
            if (!Arrays.stream(reserve).anyMatch(i -> i == person)) {
                lost_set.add(person);
            }
        }
//        lost_set.stream().forEach(System.out::println);
        for (int person: reserve) {
            if (!Arrays.stream(lost).anyMatch(i -> i == person)) {
                reserve_set.add(person);
            }
        }
        for (int reversePerson : reserve_set) {
            if (lost_set.contains(reversePerson-1)) {
                lost_set.remove(reversePerson-1);
            } else if (lost_set.contains(reversePerson+1)) {
                lost_set.remove(reversePerson+1);
            }
        }
        return n - lost_set.size();
    }
}
