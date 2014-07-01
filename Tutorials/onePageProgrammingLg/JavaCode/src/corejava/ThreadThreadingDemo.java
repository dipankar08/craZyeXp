package corejava;

class ThreadUsingThreading extends Thread{
	public Thread t;
	ThreadUsingThreading(String name){
		t = new Thread(this,name);
		this.setName(name);
	}
	public void start(){
		System.out.println( t.getName() +": Starting ");
		t.start();
	}
	synchronized public void callme() throws InterruptedException{
		System.out.println( t.getName() +": callMe Start ");
		Thread.sleep(10000);
		System.out.println( t.getName() +": callMe Start ");
		
	}
	public void run(){
		System.out.println(t.getName() +": Running ");
		try{
			for(int i=0;i<10;i++)
			{
			System.out.println(t.getName() +":"+i);
			Thread.sleep(100); /*1000 ms */
			}
			callme();
		}catch(InterruptedException e){
			System.out.println(t.getName() +" getting Interupt "+e.getMessage());
		}
		System.out.println(t.getName() +": Completd ");	
	}
	public Thread getThread(){
		return t;
	}
	
}

public class ThreadThreadingDemo {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
	 
		Thread t= Thread.currentThread();
		t.setName("Main");
		System.out.println( t.getName() +": Starting ");
		
		ThreadUsingThreading t1 = new ThreadUsingThreading("First");
		t1.start();
		ThreadUsingThreading t2 = new ThreadUsingThreading("Second");
		t2.start();

		/* Crete 10 class  */
		Thread  tlist[] = new Thread[3];
		for (int i=0;i<3;i++){
			tlist[i] = new ThreadUsingThreading("tList"+i);
			tlist[i].start();
		}
		
		System.out.println(t.getName() +": Running ");
		try{
			for(int i=0;i<10;i++)
			{
			System.out.println(t.getName() +":"+i);
			Thread.sleep(10); /*1000 ms */
			}
		}catch(InterruptedException e){
			System.out.println(t.getName() +" getting Interupt "+e.getMessage());
		}
		
		for (int i=0;i<3;i++){
			System.out.println(tlist[i].getName() +" is Alive? "+tlist[i].isAlive());
		}
		try {
			for (int i =0;i<3;i++){	tlist[i].join();}
			t1.join();t2.join();
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		
		for (int i=0;i<3;i++){
			System.out.println(tlist[i].getName() +" is Alive? "+tlist[i].isAlive());
		}
		System.out.println(t.getName() +": Completd ");	
	}

}
