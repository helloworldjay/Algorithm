public class GetCenterCharacter {
    public static void main(String[] args) {

    }

    public String solution(String s) {
        int sLength = s.length();
        if (sLength < 3) {
            return s;
        }
        if (sLength % 2 == 0) {
            return s.substring(sLength/2-1, sLength/2 + 1);
        }
        return Character.toString(s.charAt(sLength/2));
    }

}
