import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

public class RepeatedDNASequences {
    public static List<String> findRepeatedDnaSequences(String s) {
        HashSet<String> rtn = new HashSet<>();
        if (s.length() <= 10) {
            return new ArrayList<>();
        }
        HashSet<String> hashSet = new HashSet<>();
        for (int i = 0; i < s.length() - 10 + 1; i++) {
            String cur = s.substring(i, i + 10);
            if (hashSet.contains(cur)) {
                rtn.add(cur);
            } else {
                hashSet.add(cur);
            }
        }
        return new ArrayList<>(rtn);
    }

    public static void main(String[] args) {
        ArrayList<String> arrayList = new ArrayList<>(
            Arrays.asList(
                "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
                "AAAAAAAAAAAAA",
                "AAAAAAAAAAA"
            )
        );
        for (String e : arrayList) {
            System.out.println(findRepeatedDnaSequences(e));
        }
    }
}

