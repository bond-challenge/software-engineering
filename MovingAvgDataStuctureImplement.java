import java.util.NoSuchElementException;
import QueueNode;

/* This class is implementation of interface "MovingAvgDataStructure" to calculate moving average of last N element. 
 * It calculates moving average with time complexity-> O(1) by keeping track of four things head & tail of queue , 
 * Size of current queue/buffer and queueTotal as sum of all elements from current queue/buffer
 */

class MovingAvgDataStructImplement<T> implements MovingAvgDataStructure {

	private QueueNode<Double> first;
	private QueueNode<Double> last;
	public Integer size = 0;
	public Double queueTotal = 0.0 ;

	
	@Override
	public Double movingAvgOfLastNElement(Double element, Integer N) {
	    QueueNode<Double> data = new QueueNode<Double> (element);
	    if(size >= N) {
		    queueTotal -= removeQueue();
	    }     
		if (last != null) {
			last.setNext(data);
		}

		last = data;
		if(first == null) {
			first = last;
		}
		size++;
		queueTotal += element;
	
	    return queueTotal/size;
	}

	
	/*
	 * Removes and return first element from FIFO queue(entered first in queue)
	 * This method removes element which entered in queue first in FIFO order
	 */
	 
	@Override
	public Double removeQueue() {
		if(first == null) throw new NoSuchElementException();
		Double data = first.getData();
		first = first.getNext();

		if(first == null) {
			last = null;
		}
		
		size-- ;
		return data;
	}

	/*
	 * Return first element from FIFO queue(entered first in queue) but doesn't remove element from queue
	 */
	
	@Override
	public Double peek() {
		if (first == null) throw new NoSuchElementException();
		return first.getData();
	}

   /*
    * Return array of object that contains all current element for given instance of queue. 
	* This can be used for toArray() function to print current queue elements. 
    */
	
	@Override
	public Object[] toArray() {
		Object[] al = new Object[size];
		QueueNode<Double> head = first;
		for(int i=0; i<=size-1; i++) {
			al[i] = head.getData();
			head = head.getNext();
		}
	
        return al;
    }
}