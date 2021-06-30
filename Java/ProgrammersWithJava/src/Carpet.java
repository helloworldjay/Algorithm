public class Carpet {
    public int[] solution(int brown, int yellow) {
        return new int[] { (int) (((brown+4)/2)+Math.sqrt((((brown+4)/2)*((brown+4)/2))-4*(yellow+brown)))/2, (int) (((brown+4)/2)-Math.sqrt((((brown+4)/2)*((brown+4)/2))-4*(yellow+brown)))/2};
    }
}
