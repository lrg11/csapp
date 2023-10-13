import java.util.Scanner;
import java.util.ArrayList; 
// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);  
        String input = scanner.nextLine();  
        String[] strs = input.split(",");  
        int n = strs.length;
        int[] array = new int[n];  
        for (int i = 0; i < n; i++) {  
            array[i] = Integer.parseInt(strs[i]);  
        }  
        scanner.close();  
        int left = 0;
        int right = 0;
        while(right < n) {
            if(array[right] != array[left]) {
                left++;
                array[left] = array[right];
            }
            right ++;
        }

        System.out.println(left + 1);

    }
}



#

import java.util.Scanner;

// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);  
        String input = scanner.nextLine();  
        int start  = -1;

        int maxS = -1;
        int maxE = -1;
        int maxLength = 0;
        for(int i = 0; i < input.length(); i++) {
            if (start == -1 && Character.isDigit(input.charAt(i))){
                start = i;
            } 
            if (start != -1 && !Character.isDigit(input.charAt(i))) {
                if (i - start > maxLength) {
                    maxLength = i - start;
                    maxS = start;
                    maxE = i;
                }
                start = -1;
            }
        }
        if (start != -1) {
            if (input.length() - start > maxLength) {
                    maxLength = input.length() - start;
                    maxS = start;
                    maxE = input.length();
                }
               
        }

        System.out.println(input.substring(maxS, maxE));
    }
}


import java.util.Scanner;
import java.util.regex.Matcher;  
import java.util.regex.Pattern;
// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);  
        String input = scanner.nextLine();  
        String longestNumber = findLongestNumber(input);

        System.out.println(longestNumber);
    }
    public static String findLongestNumber(String input) {  
        String longestNumber = "";  
        Pattern pattern = Pattern.compile("\\d+"); // 匹配连续的数字  
        Matcher matcher = pattern.matcher(input);  
  
        while (matcher.find()) {  
            String number = matcher.group();  
            if (number.length() > longestNumber.length()) {  
                longestNumber = number;  
            }  
        }  
        return longestNumber;  
    }  
}

import java.util.Scanner;

// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        // 注意 hasNext 和 hasNextLine 的区别
        
        int a = in.nextInt();
        int b = in.nextInt();
        if (a / 3 < b) {
            System.out.println(-1);
            return;
        }
        String str1 = "you";  
        //String str2 = "";  
        StringBuilder sb = new StringBuilder();  
        for( int i = 0; i < b; i++)
            sb.append(str1);
        for (int i = 0; i < (a - b * 3); i++)  
        sb.append("o");  
    
        String result = sb.toString();
        System.out.println(result);
        
    }
}


 import java.util.Scanner;  
 
  
   // 注意类名必须为 Main, 不要有任何 package xxx 信息  
  
   public class Main {  
  
       public static void main(String[] args) {  
  
           Scanner in = new Scanner(System.in);  
  
             
  
               long a = in.nextLong();  
  
               long res=0L,j=0;  
  
               long n = a%3;  
  
                 
  
              if (n==0) {  
  
                   res=a/3-1;  
  
                    
  
               } else  {  
  
                    
  
                   res=(a-n)*2/3;  
  
                    
  
               }  
  
                  
  
                System.out.println(res);  
  
            
  
       }  
  
   }  


   import java.math.BigInteger;
 import java.util.Scanner;
 
 // 注意类名必须为 Main, 不要有任何 package xxx 信息
 public class Main {
     private final static int mod = (int) Math.pow(10, 9) + 7;;
     public static void main(String[] args) {
         Scanner in = new Scanner(System.in);
         // 注意 hasNext 和 hasNextLine 的区别
         long count = 0;
         int n = in.nextInt();
         int k = in.nextInt();
         int index = 0;
         long num[] = new long[n];
         int len = 0;
 
          int opx[] = new int[k]; 
 
          // 初始化数据 记录操作数组 转换为正负操作
 
         while (in.hasNextInt()) { 
             if (index < n) {
                 num[index++] = in.nextInt();
             } else {
                 int b = in.nextInt();
                 if (b == 1) {
                     opx[len] = in.nextInt();
                 } else {
                     opx[len] = -in.nextInt();
                 }
                 len++;
             }
         }
         long add = 0;
         long sub = 0;
 
          long current = 0; 
 
          //统一对操作数组进行替换  对于一个数 如果 前面的操作大于0 则可以把前面那一步操作和后面的操作加起来 ，按这个推 ，最后一定只剩下 一次减 和一次加 
         for (int i = 0; i < opx.length; i++) {
             current = (current + opx[i]);
             if (opx[i] < -current) {
                 if (current < 0) {
                     sub = (sub + current);
                     current = 0;
                 }
             }
             add = current;
 
          } 
 
          //遍历数组 如果这个数比总的减去的值还大 那么不为0 所以加起来，如果小于那么肯定为0直接等于最后操作的正数 
         for (int i = 0; i < n; i++) {
             if (num[i] > -sub) {
                 num[i] = num[i]+add+sub ;
             } else {
                 num[i] = add;
             }
             count = (count + num[i]) % mod;
         }
         System.out.println(count);
     }
 
 }

# rotate array
class Solution {
    public void reverse(int[] nums, int left, int right) {
        while (left < right) {
            int temp = nums[left];
            nums[left] = nums[right];
            nums[right] = temp;
            left++;
            right--;
        }
    }
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        int newk = k % n;
        reverse(nums, 0, n - 1);
        reverse(nums, 0, newk - 1);
        reverse(nums, newk, n - 1);
    }
}


class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int []suf_mul = new int[n + 1];
        suf_mul[n] = 1;
        for (int i = n - 1; i >= 0; i--) {
            suf_mul[i] = suf_mul[i + 1] * nums[i];
        }

        int pre = 1;
        int[] ans = new int[n];
        for(int i = 0; i < n; i++){
            ans[i] = pre * suf_mul[i + 1];
            pre *= nums[i];
        }
        return ans;

    }
}