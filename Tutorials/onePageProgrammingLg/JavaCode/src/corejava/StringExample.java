package corejava;

public class StringExample {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		String s = "Dipankar";
		System.out.println("\nLength is "+s.length());
		System.out.println("\nCatAt is "+s.charAt(0));
		System.out.println("\nIndex is "+s.indexOf('a'));
		System.out.println("\nIndex is "+s.lastIndexOf('a'));
		System.out.println("\nSunStr is "+ s.substring(0,5));
		System.out.println("\nIndex is "+s.replace("D", "DDDDhhh"));

	}

}
