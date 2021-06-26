import java.util.ArrayList;
import java.util.*;

public class GetPrimeNumber {
    public static void main(String[] args) {
        System.out.println(solution(new int[]{1, 2, 3, 4}));
        System.out.println(isPrime(6));
        System.out.println(isPrime(7));
        System.out.println(isPrime(8));
        System.out.println(isPrime(9));
        Stack<Integer> intStack = new Stack<Integer>();
    }

    public static int solution(int[] nums) {
        ArrayList<Integer> numsSum = new ArrayList<Integer>();
        for (int i = 0; i < nums.length - 2; i++) {
            for (int j = i+1; j < nums.length - 1; j++) {
                for (int k = j+1; k < nums.length; k++) {
                    numsSum.add(nums[i]+nums[j]+nums[k]);
                }
            }
        }
        return numsSum.stream().filter(numberToCheck -> isPrime(numberToCheck)).toArray().length;
    }

    private static boolean isPrime(int numberToCheck) {
        int criterion = (int) Math.sqrt(numberToCheck) + 1;
        for (int i = 2; i < criterion; i++) {
            if (numberToCheck % i == 0) {
                return false;
            }
        }
        return true;
    }
}
