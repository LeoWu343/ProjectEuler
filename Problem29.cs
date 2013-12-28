using System;
using System.Collections.Generic;
public class Problem29 {
    public static int CycleLen(int denom) {
        string foo = ((decimal)1 / (decimal)denom).ToString();
        Console.WriteLine(foo);
        string decPart = foo.Substring(2, foo.Length-2);
        int max = 0;
        for (int start = 0; start < decPart.Length; start++) {
            for (int end = 1; end < decPart.Length-start; end++) {
                string curr = decPart.Substring(start, end);
                int half = curr.Length / 2;
                string fir = curr.Substring(0, half);
                string sec = curr.Substring(half, curr.Length-half);
                Console.WriteLine(fir);
                Console.WriteLine(sec);
                int currLen = fir.Length;
                if (fir == sec && currLen > max) {
                    max = currLen;
                }
            }
        }
        return max;
    }
    public static void Main() {
        Console.WriteLine(CycleLen(999));
        /*int max = 0;
        int maxLen = 0;
        for (int i = 2; i < 1000; i++) {
            int curr = CycleLen(i);
            if (curr > maxLen) {
                max = i;
                maxLen = curr;
            }
            Console.WriteLine(curr);
        }
        Console.WriteLine(max);
        Console.WriteLine(maxLen);*/
    }
}
