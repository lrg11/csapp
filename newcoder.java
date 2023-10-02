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
   