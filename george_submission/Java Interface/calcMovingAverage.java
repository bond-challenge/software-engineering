package com.bondbrand.challenge.test;
 
import java.util.LinkedList;
import java.util.Queue;

public interface FinalDataStructure {
    void addElement(float element); /*Adds element in the data list*/
    float getMovingAverage(); /*Returns moving average*/
    public int getSize(); /*Returns size of the data list*/
}

/**
 * Title: DoubleDataStore
 * Description: Implementating FinalDataStructure for elements of any datatype.
 
 * @author George Oboh
*/
public class calcMovingAverage implements FinalDataStructure {
 
    private int n;
    private Queue<Float> queue;
    private float sum;
    
 
    public calcMovingAverage(int n) {
        queue = new LinkedList<>();
        this.n = n;
    }
 
    @Override
    public void addElement(float element) {

        /* Add the data element in the List */
        queue.add(element);

        if(n > 0)
		{
			/* Add the element to the sum */
			sum += element;


            /* If the number of elements in the Queue exceeds the N,
            remove first element*/
            if (queue.size() >= n) {
                float dataToRemove = queue.poll();
                sum -= dataToRemove;
            }
        } 
        
    }
 
    @Override
    public float getMovingAverage() {
        //return sum / n;
        /*If N is greater than zero and the list contains elements, return the average */
		if(n > 0 && queue.size() > 0)
		{
			return (sum / n);
		}
		
		/* Else */
		return 0; /*null;*/
    }
	
	/**
	 * Returns the size of the data list.
	 */
	public int getSize()
	{
		return queue.size();
	}
	
    public static void main(String[] args) {
        FinalDataStructure ma = new calcMovingAverage(4);
 
        ma.addElement(3);
        System.out.println(ma.getMovingAverage());
        ma.addElement(7);
        System.out.println(ma.getMovingAverage());
        ma.addElement(4);
        System.out.println(ma.getMovingAverage());
        ma.addElement(2);
        System.out.println(ma.getMovingAverage());
        ma.addElement(1);
        System.out.println(ma.getMovingAverage());
        ma.addElement(2);
        System.out.println(ma.getMovingAverage());
    }
}
