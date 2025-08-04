// 투포인터 문제
// n개의 서로다른 양의정수가 주어졌을때, a1 + a2 = x를 만족하는 수의 개수 찾기
// 쌍이기 때문에 중복을 허용하지 않음


// 9
// 5 12 7 10 9 1 2 3 11
// 13

// 12, 1
// 10, 3
// 2, 11 



package Baekjoon;

import java.io.*;
import java.util.*;

public class bj3273 {
    public static void main(String[] args) throws IOException {
        // 입력부, 시간복잡도 O(n)
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        //String to int
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int[] num = new int[n];     // java에서는 char, int 똑같나?
        int num_i = 0;
        while (st.hasMoreTokens()) {
            num[num_i] = Integer.parseInt(st.nextToken());
            num_i += 1;     // index 추가하는거 빼먹지 말 것
        }

        int x = Integer.parseInt(br.readLine());

        // 투포인터 사용
        int answer = 0;

        // 중첩 루프에서 O(n^2)의 시간복잡도를 가진다.
        // 바깥루프 n, 안쪽 루프 n, n-1, n-2 , ... , 1 이므로 n(n-1)/2
        // 올바른 투포인터 접근법 : 정렬된 배열에서 접근 > 모든 투포인터가 정렬된 것 배열에서 접근해야하는가?
        // for(int k = 0; k < n; k++){
        //     int i = k ;
        //     int j = n - 1;

        //     // 이미 하나의 수가 x보다 큰 경우
        //     if (num[i] > x){
        //         continue;
        //     }

        //     while(i < j){
        //         if (num[i] + num[j] == x){
        //             answer += 1;
        //             break;
        //         }
        //         j -= 1;
        //     }
        // }

        // 정렬을 활용한 투포인터
        Arrays.sort(num);   // 정렬을 사용 O(nlogn)

        int i = 0;
        int j = n - 1;

        while(i < j){
            int result = num[i] + num[j];
            if (result == x){
                i += 1;
                j -= 1;
                answer += 1;
            } else if (result > x){
                j -= 1;
            } else {
                i += 1;
            }
        }
        
        System.out.println(answer);
        
    }
}