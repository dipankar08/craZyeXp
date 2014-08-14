package com.example.fibnative;

import android.util.Log;

public class FibLib {
	  
	    private static final String TAG = "DD_JAVA";

		public static long fibJR(long n){
			return n<=0?0:n==1?1: fibJR(n-1)+fibJR(n-2);
		}
		public native static long fibNR(long n);
		
		public static long fibJI(long n){
			Log.d(TAG,"fibJI("+n+")");
			long f1 = 0;
			long f2 = 1;
			long fn;
			for(long i = 2;i<= n;i++){
				fn = f1 + f2;
				f1 = f2;
				f2 = fn;
			}
			return f2;
		}
		public native static long fibNI(long n);		
		
		static{
			System.loadLibrary("com_example_fibnative_FibLib");
		}
}
