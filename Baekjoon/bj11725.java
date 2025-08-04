// 11725 트리의 부모 찾기
// 트리 자료구조를 사용해야하나?

package Baekjoon;

import java.io.*;
import java.util.*;

// // node 클래스 작성
// class Node {
//     int data;
//     Node left;
//     Node right;

//     public Node(int data){
//         this.data = data;
//         this.left = null;
//         this.right = null;
//     }
// }

// // tree 클래스 작성
// class BinaryTree {
//     Node rootnode;

//     BinaryTree(){
//         this.rootnode = null;
//     }

//     BinaryTree(Node rootNode) {
//         this.rootnode = rootNode;
//     }
// }

// 트리 구조를 사용해보려고했으나, 탐색이나 삽입등 너무 비효율적이라서 인접리스트로 트리를 관리

public class bj11725 {
    static public void DFS(int p){
        if (graph[p] == null){  // 리프노드인 경우
            return;
        } else {
            for(int i : graph[p]){
                if (visited[i] == false) {
                    visited[i] = true;
                    answer_parents[i] = p;
                    DFS(i);
                }
            }
        }

        return;
    }

    static ArrayList<Integer>[] graph;
    static boolean[] visited;
    static int[] answer_parents;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        visited = new boolean[n + 1];
        answer_parents = new int[n + 1];
        
        // 인접리스트를 저장할 array
        graph = new ArrayList[n + 1];
        for(int i = 1; i <= n; i++){
            graph[i] = new ArrayList<>();
        }

        for(int i = 0; i < n - 1; i++) {
            // 정점 입력 받기
            StringTokenizer st = new StringTokenizer(br.readLine());
            int v1 = Integer.parseInt(st.nextToken());
            int v2 = Integer.parseInt(st.nextToken());

            // 인접리스트 연결(무방향)
            graph[v1].add(v2);
            graph[v2].add(v1);
        }

        // DFS로 graph 탐색
        DFS(1);

        for(int i = 2; i < n + 1; i++){
            System.out.println(answer_parents[i] +" ");
        }
        
    }
}
