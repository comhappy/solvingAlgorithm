package solveAc;

// max n = 10,000

import java.util.*;
import java.io.*;

public class p1436 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		
		int i;
		int ind = 0;
		for(i = 666; ind != n; i++) {
			String num = Integer.toString(i);
			
			if(num.contains("666")) {
				ind += 1;
			}
		}
		
		System.out.println(i - 1);
	}
}