import java.util.*;
class Solution {
    public int solution(int[] numbers) {
        Arrays.sort(numbers);
        int len = numbers.length;
        int r1 = numbers[len-1] * numbers[len-2];
        int r2 = numbers[0] * numbers[1];
        int answer = (r1>r2) ? r1 : r2;
        return answer;
    }
}