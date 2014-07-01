package corejava;

public class Variable_Commandline {

    public static void var_func(int i, String j, int ... ks ){
    	System.out.println(i);
    	System.out.println(j);
    	for (int x: ks){
    		System.out.println(x);
    	}
    }
	
	public static void main(String[] args) {
		System.out.println(args.length);
		
		for ( String x : args){
			System.out.println(x);	
		}
		
		var_func(10,"Dipankar",1,2,3,4,5);

	}

}
