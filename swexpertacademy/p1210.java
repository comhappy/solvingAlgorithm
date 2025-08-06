package swea1210;

import java.io.*;
import java.util.*;

public class main {
	static int[][] ladder = new int[100][100];

// 재귀로 작성 > stackoverflow 발생 ㄷㄷ
// 반복문으로 작성
//	public static void searchladder(int x, int y) {
//	if (x == 0) {	// 출발지점에 도착한 경우
//		for(int i = 0; i < 100; i++) {
//			if (ladder[0][i] == 1) {
//				startPoint += 1;
//				
//				if (i == x) {	// 정답인 경우
//					return;
//				}
//			}
//		}
//	} else {
//		// 좌우 탐색 후 길이 있는경우 이동
//		if (y - 1 >= 0 && ladder[x][y - 1] == 1)	{ // 좌측 탐색
//			searchladder(x, y - 1);
//		} else if (y + 1 < 100 && ladder[x][y + 1] == 1) {	// 우측 탐색
//			searchladder(x, y + 1);
//		} else {	// 위로 이동
//			searchladder(x - 1, y);
//		}
//	}
//	
//	return;
//}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		for(int t = 0; t < 10; t++) {	
			// 문제번호 입력받기
			int T = Integer.parseInt(br.readLine());
			
			// 사다리 입력 받기
			for(int i = 0; i < 100; i++) {
				StringTokenizer st = new StringTokenizer(br.readLine());
				int j = 0;
				
				while (st.hasMoreTokens()){
					ladder[i][j] = Integer.parseInt(st.nextToken());
					j += 1;
				}
			}
			
//			// 정답 구하기
//			for(int i = 0; i < 100; i++) {
//				if (ladder[99][i] == 2) {
//					searchladder(99, i);
//				}
//			}

			int sx = 99;
			int sy = 99;
			
			// 시작위치 구하기
			for(int i = 0; i < 100; i++) {
				if (ladder[99][i] == 2) {
					sy = i;
					break;
				}
			}
			
			while(sx != 0) {
				if (sy - 1 >= 0 && ladder[sx][sy - 1] == 1) {	// 좌측이동
					sy -= 1;
					
					while(ladder[sx - 1][sy] == 0) {
						sy -= 1;
					}
				} else if (sy + 1 < 100 && ladder[sx][sy + 1] == 1) {	// 우측이동
					sy += 1;
					
					while(ladder[sx - 1][sy] == 0) {
						sy += 1;
					}
					
				} 
				sx -= 1;	
			}
			
			System.out.println("#" + (t + 1) + " " + sy);
			
		}
	}
}
