package solveAc;

import java.util.*;
import java.io.*;

public class p1018 {	
	public static int checkChess(char[][] chess, int x, int y, char color) {
		// 첫 칸을 color로 칠할때 바꾸는 값을 return
		int cntChess = 0; 
		char[] catColor = {'W', 'B'};
		int correctColorIndex;
		
		if (chess[x][y] != color) {
			//chess[x][y] = color;
			cntChess += 1;
		}
		
		if (color == 'W') {
			correctColorIndex = 0;
		} else {
			correctColorIndex = 1;
		}
		
		// 체스판 탐색
		for(int i = 0; i < 8; i++) {
			int dx = i + x;
			for(int j = 0; j < 8; j++) {
				int dy = j + y;
				
				// 다음 타일이 맞지 않는 경우
				if (chess[dx][dy] != catColor[correctColorIndex]) {
					cntChess += 1;
				}
				correctColorIndex = (correctColorIndex + 1) % 2;
			}
			correctColorIndex = (correctColorIndex + 1) % 2;
		}
		
		return cntChess;
	}
	
	public static void main(String[] args) throws IOException {
		// 입력받기
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		char[][] chess = new char[n][m];
		
		for(int i = 0; i < n; i++) {
			char[] info = br.readLine().toCharArray();
			for(int j = 0; j < m; j++) {
				chess[i][j] = info[j];
			}
		}
		
		// 알고리즘 구현 - 브루트 포스
		// 8 * 8 체스판 탐색, 첫 칸이 w인 경우, 첫 칸이 b인 경우
		// 함수 구현 후 시작점 전달 > return 값은 최소 색칠 칸 수(int)
		int ans = 8 * 8;
		
		for(int i = 0; i < n - 7; i++) {
			for(int j = 0; j < m - 7; j++) {
				int a = checkChess(chess, i, j, 'W');
				int b = checkChess(chess, i, j, 'B');
				
				int result = (a >= b) ? b : a;
				System.out.println(a + ", "+ b);
				
				ans = (ans > result) ? result : ans;
			}
		}
		
		System.out.println(ans);
	}
}
