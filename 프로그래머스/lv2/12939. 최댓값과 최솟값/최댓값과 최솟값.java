import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public String solution(String s) {
        String[] split = s.split(" ");
        List<Integer> integerList = new ArrayList<>();
        for (String s1 : split) {
            integerList.add(Integer.parseInt(s1));
        }
        return Collections.min(integerList) + " " + Collections.max(integerList);
    }
}