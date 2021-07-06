import java.util.*;
class JoyStick {
    public int solution(String name) {
        int[] cursorUpDown = new int[name.length()];
        for (int i = 0; i < name.length(); i++) {
            if ((int) name.charAt(i) - (int) 'A' < 13) {
                cursorUpDown[i] = (int) name.charAt(i) - (int) 'A';
            } else {
                cursorUpDown[i] = 26 - ((int) name.charAt(i) - (int) 'A');
            }
        }
        int totalMovement = 0;
        int index = 0;
        while (Arrays.stream(cursorUpDown).sum() != 0) {
            totalMovement += cursorUpDown[index];
            cursorUpDown[index] = 0;
            int rightIndex = 0;
            boolean findedRightIndex = false;
            int leftIndex = 0;
            boolean findedLeftIndex = false;
            for (int i = 1; i < name.length(); i++) {
                if (cursorUpDown[(index + i) % name.length()] != 0 & !findedRightIndex) {
                    rightIndex = i;
                    findedRightIndex = true;
                }
                if (cursorUpDown[(index - i + name.length()) % name.length()] != 0 & !findedLeftIndex) {
                    leftIndex = i;
                    findedLeftIndex = true;
                }
                if (findedLeftIndex & findedRightIndex) {
                    break;
                }
            }
            if (leftIndex < rightIndex) {
                totalMovement += leftIndex;
                index = ((index - leftIndex) + name.length()) % name.length();
            } else {
                totalMovement += rightIndex;
                index = (index + rightIndex) % name.length();
            }
        }
        return totalMovement;
    }
}