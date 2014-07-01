package corejava;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Vector;
import java.util.Stack;

import java.util.Hashtable;

public class collections {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
	
	/* Creating 5 Studnet object */
		Student s1 = new Student(1, "Dipankar1");
		Student s2 = new Student(2, "Dipankar2");
		Student s3 = new Student(3, "Dipankar3");
		Student s4 = new Student(4, "Dipankar4");
		Student s5 = new Student(5, "Dipankar5");
		
		Student s11 = new Student(1, "Dipankar11");
		
	/* Testing ArrayList ..: Double concept of Arry */
		ArrayList<String> al = new ArrayList<String>();
		al.add("A");al.add("B");al.add("C");System.out.println(al);
		al.add(0,"D");System.out.println(al);
		System.out.println(al.size());
		al.remove(0); System.out.println(al);
		
		String arr[] = new String [al.size()];
		arr = al.toArray(arr);
		for (String i : arr){
			System.out.println(i);
		}
		System.out.println(al.hashCode());
		System.out.println(al.indexOf("X"));	
		
		ArrayList<String> al1 = new ArrayList<String>(al);
		System.out.println(al1);
		al.addAll(al1);
		System.out.println(al);
		al.removeAll(al1);
		System.out.println(al);
	    al = al1;
	    System.out.println(al);
	    /* Accesting via iterator */
	    Iterator<String> itr = al.iterator(); 
	    while(itr.hasNext()){
	    	System.out.println(itr.next());
	    }
	/* Testing Linkedlist : Just like Linked list*/
	    System.out.println("Linkelist:");
	    LinkedList<Student> ll = new LinkedList<Student>();
	    ll.add(s1);ll.add(s2);System.out.println(ll);
	    System.out.println(ll.getFirst() +"+"+ll.getLast());
	    ll.addFirst(s1);ll.removeLast();
	    System.out.println(ll);
	    
	    
	/* Testing  HashSet ... We need a overwrite or equals and hashCode Both in class*/
	    HashSet<Student> hs = new HashSet<Student>();
	    hs.add(s1);hs.add(s2);hs.add(s3);hs.add(s11);System.out.println(hs);
	    System.out.println(hs.contains(s1));
	    
	 /* testing DeQueue */
	    System.out.println("ArrayDQueue");
	    ArrayDeque<Integer> aq = new ArrayDeque<Integer>();
	    /* Move Like <<[ 1,2,3,4] <<< */
	    aq.offer(1);aq.offer(2);aq.offer(3);aq.offer(4); // Insert from End
	    System.out.println(aq);
	    while(aq.peek()!=null){
	    	System.out.println(aq.poll()); //Takeout from Fromt.
	    }
	    
	    /* Move Like >>>[ 1,2,3,4] >>> */
	    aq.push(4);aq.push(3);aq.push(2);aq.push(1);
	    System.out.println(aq);
	    while(aq.peekLast()!=null){
	    	System.out.println(aq.removeLast()); //Takeout from Last.
	    }
	    
	    
	/*  Testing Priority Queue.. You need to imaplemnet CompareTo() Method in the base class */
	    System.out.println("PQ:");
	    PriorityQueue<Student> pq = new PriorityQueue<Student>();
	    pq.add(new Student(100,"Student100")); pq.add(s2);pq.add(s1);pq.add(s3); // add: Adding at End
	    System.out.println(pq);
	    while(pq.peek()!=null){
	    	System.out.println(pq.remove()); //remove : remove at front
	    }
	    
    /* Testing vector: Resizeable arry */
	    Vector<Student> v = new Vector<Student>();
	    v.add(s1);v.add(s2);v.add(s3);v.add(s11);System.out.println(hs);
	    System.out.println(v.size()+" < Size : Capcity >"+v.capacity());
	    System.out.println("1th Item :"+v.get(0));
	/* Testing Stack */
	    System.out.println("Stack Test:");
	    Stack<Student> s = new Stack<Student>();
	    s.push(s1);s.push(s2);s.push(s3);
	    System.out.println(s);
	    System.out.println("Pos to serach:" + s.search(s1));
	    System.out.println("Peek:"+s.peek());
	    while(! s.isEmpty()){
	    	System.out.println(s.pop());
	    }
	    
	 /* Testing HashTable : Similar to  */
	    System.out.println("Hashtable:");
	    Hashtable<Integer,Student> ht = new Hashtable<Integer, Student>();
	    ht.put(1, s1);ht.put(2, s2);ht.put(3, s3);   System.out.println(ht); //PUT
	    System.out.println(ht.get(3)); //GET
	    ht.put(1, s11);System.out.println(ht);//UPDATE
	    System.out.println(ht.keySet()); //get Key SET
	    System.out.println(ht.values());//Get Values
	    System.out.println(ht.entrySet());//Set as a pair
	    
     /* testing HashMap ... */
	    System.out.println("HashMap:");
	    HashMap<Integer,Student> hm = new HashMap<Integer, Student>();
	    hm.put(1, s1);hm.put(2, s2);hm.put(3, s3);   System.out.println(ht); //PUT
	    System.out.println(hm.get(3)); //GET
	    hm.put(1, s11);System.out.println(hm);//UPDATE
	    System.out.println(hm.keySet()); //get Key SET
	    System.out.println(hm.values());//Get Values
	    System.out.println(hm.entrySet());//Set as a pair	    
	 /* Sorted Hash Map */
	    
	 
	 /*Algorithms*/
	    System.out.println("\nAlgorithms:::");
	    ArrayList<Student> arr1 = new ArrayList<Student>();
	    arr1.add(s1);arr1.add(s2);arr1.add(s3);arr1.add(s4);arr1.add(s5);
	    System.out.println("ORG:"+arr1);
	    
	    Collections.reverse(arr1); System.out.println("REV:"+arr1);
	    
	    Collections.shuffle(arr1); System.out.println("SUFF:"+arr1);
	    Collections.sort(arr1); System.out.println("SORT:"+arr1);
	    Comparator<Student > rev = Collections.reverseOrder();
	    Collections.sort(arr1,rev); System.out.println("SORT IN REV:"+arr1);
	    Collections.swap(arr1, 0, 2);System.out.println("SWAP 0-2:"+arr1);
	    System.out.println("MIN:"+Collections.min(arr1));
	    System.out.println("Max:"+Collections.max(arr1));
	    System.out.println("SORT:"+Collections.binarySearch(arr1, s1));
	    Collections.rotate(arr1, 3);
	    System.out.println("RATETE:"+arr1);
	    Collections.replaceAll(arr1, s1, s2);
	    System.out.println("Replace:"+arr1);

	    
	    
	    
	    

	}

}



















