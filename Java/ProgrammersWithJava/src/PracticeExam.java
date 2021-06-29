import java.util.*;

public class PracticeExam {
    public static void main(String[] args) {
        System.out.println(solution(new int[] {1,3,2,4,2}));
    }

    public static int[] solution(int[] answers) {
        List<Integer> winners = new ArrayList<>();
        int[] supojas = {1,2,3};
        Map<Integer, int[]> map = new HashMap<>(){{
            put(1, new int[] {1,2,3,4,5});
            put(2, new int[] {2,1,2,3,2,4,2,5});
            put(3, new int[] {3,3,1,1,2,2,4,4,5,5});
        }};
        int maxScore = 0;
        for (int supoja : supojas) {
            int score = getScore(answers, map.get(supoja));
            if (score > maxScore) {
                winners = new ArrayList<>();
                winners.add(supoja);
                maxScore = score;
            } else if (score == maxScore) {
                winners.add(supoja);
            }
        }
        int[] answer = new int[winners.size()];
        for (int i = 0; i < winners.size(); i++) {
            answer[i] = winners.get(i);
        }
        return answer;
    }

    private static int getScore(int[] answers, int[] answerList) {
        int score = 0;
        for (int i = 0; i < answers.length; i++) {
            if ( answerList[i % answerList.length] == answers[i]) {
                score++;
            }
        }
        return score;
    }
}
