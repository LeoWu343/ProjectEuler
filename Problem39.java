import java.util.HashMap;
public class Problem39 {
    public static void main(String[] args) {
        HashMap<Integer, Integer> record = new HashMap<Integer, Integer>();
        for (int i = 1; i < 1000; i++) {
            for (int j = 1; j < 1000; j++) {
                double z = Math.sqrt(Math.pow(i, 2) + Math.pow(j, 2));
                if (z % 1 != 0) {
                    continue;
                }
                if (i + j <= z || j + z <= i || i + z <= j) {
                    continue;
                }
                int key = i + j + (int)z;
                if (record.containsKey(key)) {
                    record.put(key, record.get(key) + 1);
                } else {
                    record.put(key, 1);
                }
            }
        }
        int max = 0;
        int ind = 0;
        for (int i = 1; i < 1000; i++) {
            Integer curr = record.get(i);
            if (curr != null && curr > max) {
                max = curr;
                ind = i;
            }
        }
        System.out.println(ind);
        System.out.println(max);
    }
}
