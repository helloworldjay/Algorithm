import java.util.*;



public class ProgrammersBackEnd {
    public static void main(String[] args) {
        System.out.println(solution1(new int[] {1,3,2,5,4}, 6));
    }

    public static int solution1(int[] d, int m) {
        int boatNumber = 0;
        int boxLeft = m;
        int currentBoxNumber = 1;
        for (int upperBound: d) {
            boatNumber++;
            if (currentBoxNumber > upperBound) {
                currentBoxNumber = 1;
                continue;
            }
            boxLeft -= currentBoxNumber;
            currentBoxNumber *= 2;
            if (boxLeft <= 0) {
                break;
            }
        }
        if (boxLeft <= 0) {
            return boatNumber;
        } else {
            return -1;
        }
    }

    public static int[] solution2(int[] deposit) {
        Stack<Integer> depositStack = new Stack<>();
        for (int transaction : deposit) {
            if (transaction >= 0) {
                depositStack.push(transaction);
            } else {
                while (transaction < 0) {
                    transaction += depositStack.pop();
                }
                if (transaction > 0) {
                    depositStack.push(transaction);
                }
            }
        }
        int[] result = new int[depositStack.size()];
        for (int i = 0; i < result.length; i++) {
            result[i] = depositStack.elementAt(i);
        }
        return result;
    }

    public static int answer = Integer.MAX_VALUE;
    public static int[] parents;

    public int solution3(int n, int[][] wires) {
        for (int i = 0; i < wires.length; i++) {
            dfsSkipParameter(i, n, wires);
        }
        return answer;
    }

    private static void dfsSkipParameter(int skipIndex, int n, int[][] wires) {
        parents = new int[n+1];
        for (int i = 0; i < n + 1; i++) {
            parents[i] = i;
        }

        for (int i = 0; i < wires.length; i++) {
            if (i == skipIndex) {
                continue;
            }
            int[] edge = wires[i];
            int u = edge[0];
            int v = edge[1];

            union(u, v, n);
        }

        // TODO: 각 팀별 개수 세서 정답이랑 비교하기
        Map<Integer, Integer> countMap = new HashMap<>();
        for (int i = 1; i <= n; i++) {
            if (countMap.containsKey(parents[i])) {
                countMap.put(parents[i], countMap.get(parents[i]) + 1);
            } else {
                countMap.put(parents[i], 1);
            }
        }
        Set<Integer> integersSet = countMap.keySet();
        Integer[] array = new Integer[integersSet.size()];
        int k = 0;
        for (Integer i : integersSet) {
            array[k++] = countMap.get(i);
        }
        answer = Math.min(answer, Math.abs(array[0] - array[1]));
    }

    private static void union(int a, int b, int n) {
        a = find(a);
        b = find(b);

        if (a == b) {
            return;
        }

        if (a < b) {
            for (int i = 1; i <= n; i++) {
                if (i != b && parents[i] == b) {
                    parents[i] = a;
                }
            }
            parents[b] = a; //궁긍증: 만약 그렇다면 b의 부하들은 여전히 b를 대장이라고 생각하지 않나?
        } else {
            for (int i = 1; i <= n; i++) {
                if (i != a && parents[i] == a) {
                    parents[i] = b;
                }
            }
            parents[a] = b;
        }
    }

    private static int find(int a) {
        if (a == parents[a]) {
            return a;
        }
        parents[a] = find(parents[a]);
        return parents[a];
    }
}
