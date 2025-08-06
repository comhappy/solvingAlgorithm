package swexpertacademy;

import java.util.*;
import java.io.*;

// 아 문제 좀 잘읽자!
// 순열을 통한 숫자 카드 계산 후, 비교 함수를 통해 승패 결정

public class p6808 {
    static int T;
    static int[] numbersGYU;   // 규영이가 내는 수
    static boolean[] visited;   // 인영이가 사용할 수 있는 수, false로 표시
    static int[] numbersIN;    // 인영이가 내는 수
    static int[] answer;

    public static void main(String[] args) throws IOException {
        // 입력받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        T = Integer.parseInt(br.readLine());

        for(int t = 1; t < T + 1; t++){
            StringTokenizer st = new StringTokenizer(br.readLine());

            numbersGYU = new int[9 + 1];
            numbersIN = new int[9 + 1];
            visited = new boolean[19];

            // 사용한 숫자 확인
            for(int i = 1; i < 10; i++) {
                numbersGYU[i] = Integer.parseInt(st.nextToken());
                visited[numbersGYU[i]] = true;
            }

            // 순열구하기
            answer = new int[2];
            permutation(1);
            System.out.println("#" + t + " " + answer[0] + " " + answer[1]);
        }
    }

    static void permutation(int index) {
        if (index == 10){    // 9개의 카드를 모두 선택한 경우
            fight();
            return;
        } else {
            for(int i = 1; i < 19; i++){
                if (visited[i] == false){
                    visited[i] = true;
                    numbersIN[index] = i;
                    permutation(index + 1);
                    visited[i] = false;
                } 
            }
        }
    }

    static void fight(){
        // for(int i = 1; i < 10; i++){
        //     System.out.print(numbersIN[i] + " ");
        // }
        // System.out.println();
        
        int[] result = new int[2];

        for(int i = 1; i < 10; i++){
            if (numbersGYU[i] > numbersIN[i]) { // 규영이가 이겼을때
                result[0] += numbersGYU[i] + numbersIN[i];
            } else if (numbersGYU[i] < numbersIN[i]){ // 규영이가 졌을때
                result[1] += numbersGYU[i] + numbersIN[i];
            }
        }

        if (result[0] > result[1]) {
            answer[0] += 1;
        } else if (result[0] < result[1]) {
            answer[1] += 1;
        }

        return;
    }
}
