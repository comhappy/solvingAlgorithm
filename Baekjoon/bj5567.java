package Baekjoon;


// 결혼식
// 인접리스트 구성 후 상근이 기준으로 DFS or BFS하면 끝
// java에서 인접리스트 구성방법
// 1. ArrayList<Integer>[] (ArrayList의 배열)
// 2. ArrayList<ArrayList<Integer>> (ArrayList의 ArrayList)
// 3. Map<Integer, List<Integer>> (맵과 리스트의 조합)

// DFS로 풀어보기 > 방문관리 배열(visited)만 사용하면 되는 경우가 생김
//     1
//    / \
//   2   3      트리구조가 왼쪽과 같은경우
//  / \ / \     1-2-4, 1-2-5, 1-3-5, 1-3-6 경로로 DFS하는데 이때, 2, 3, 5가 중복됨
// 4   5   6    이것을 해결하기 위해 counted 배열 선언 후 첫방문때만 answer += 1;

// BFS로도 풀어보자...

import java.util.*;
import java.io.*;

public class bj5567 {
    static int n;
    static int m;
    static boolean[] visited;
    static boolean[] counted;
    static ArrayList<Integer>[] adjlist;
    static int answer;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());

        visited = new boolean[n + 1];   // 노드 방문관리 배열
        counted = new boolean[n + 1];   // 중복을 막기위한 배열

        // 1번 방법사용
        adjlist = new ArrayList[n + 1];

        for(int i = 0; i < n + 1; i++){
            adjlist[i] = new ArrayList<>();
        }

        for(int i = 0; i < m; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            // 인접리스트 추가, 무방향 그래프
            adjlist[a].add(b);
            adjlist[b].add(a);
        }

        // DFS를 활용하면 시간초과 > 왜? 순환그래프가 존재해서? > 그러면 BFS로 풀어야하나?
        // 그냥 문제를 잘못 이해한거같은디 > 친구와 친구의 친구만 초대 > depth가 1인 경우 + depth가 2인 경우
        // 이 경우 DFS로는 못푸나?
        // DFS를 활용하여 동기 수 구하기
        answer = 0;
        DFS(1, 0);
        System.out.println(answer - 1);
    }

    public static void DFS(int index, int depth){
        if (visited[index] == true || depth == 3){
            return;
        } else{
            visited[index] = true;

            // 첫방문
            if (counted[index] == false){
                answer += 1;
                counted[index] = true;
            }

            for(int i : adjlist[index]){
                DFS(i, depth + 1);
            }

            visited[index] = false;
        }

        return;
    }

}
