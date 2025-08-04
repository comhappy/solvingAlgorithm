package solveAc;

import java.util.*;
import java.io.*;

public class p4581 {
public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		
		for(int t = 0; t < T; t++) {
			char[] a = br.readLine().toCharArray();
			char[] b = new char[a.length];
			
			// 투포인터 사용
			int i = 0;
			int j = a.length - 1;
			int b_index = 0;

			// 투포인터 종료 조건
			while(i <= j) {
				// 앞의 알파벳이 사전적으로 빠른 경우
				if (a[i] < a[j]) {
					b[b_index] = a[i];
					i += 1;
				// 뒤의 알파벳이 사전적으로 빠른 경우
				} else if (a[i] > a[j]){
					b[b_index] = a[j];
					j -= 1;
				// 알파벳이 같은 경우
				} else {
					b[b_index] = a[i];
					
					int ai = i;
					int aj = j;
					boolean isSwitch = false;
					
					while(ai <= aj && (isSwitch == false)) {
						if (a[ai] > a[aj]) {
							j -= 1;
							isSwitch = true;
						} else if (a[ai] < a[aj]) {
							i += 1;
							isSwitch = true;
						} else {
							ai += 1;
							aj -= 1;
						}
					}
					if (isSwitch == false) {
						i += 1;
					}
				}
				b_index += 1;
			}
			
			System.out.print("#" + (t + 1) +" ");
			for(char c : b) {
				System.out.print(c);
			}
			System.out.println();
		}
	}
}

