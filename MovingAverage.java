import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * The data structure used in this assignment is an ArrayList with a Circular Queue implemented using an Array.
 *
 * Circular Queue is used to get the moving average of last N elements inserted, as it adds a new element and discards
 * the oldest element. This takes O(1) time.
 *
 * ArrayList is used to maintain all the elements inserted in the data structure. Insert and get operation happen with
 * O(1) time complexity.
 *
 * Trade-off is space complexity, O(M+N), where M is the total number of elements inserted, N is the window size used
 * for calculating moving average.
 *
 * Alternately we can also use Double Ended Queue (Deque) to maintain the moving average, as it also provides us with O(1)
 * time complexity.
 */

public class MovingAverage implements MovingAverageInterface{

    private int windowSize;
    private List<Double> elementList;
    private Double[] circularQueue;
    private Double windowSum;
    private int head;
    private int numberofElements;

    public MovingAverage(int N){
        if(N <= 0)
            throw new IllegalArgumentException("Please provide size of N greater than 0.");
        this.windowSize = N;
        this.elementList = new ArrayList<>();
        this.circularQueue = new Double[windowSize];
        Arrays.fill(circularQueue, 0.0);
        this.windowSum = 0.0;
        this.head = 0;
        this.numberofElements = 0;
    }

    /**
     * Adding element in both ArrayList and Circular Queue
     * @param element
     */
    @Override
    public void addElement(Double element) {
        this.elementList.add(element);
        numberofElements++;
        int tail = (head + 1) % windowSize;
        windowSum = windowSum - circularQueue[tail] + element;
        head = (head + 1) % windowSize;
        circularQueue[head] = element;
    }

    /**
     * This method returns the element inserted in the specified index 'position', here 0 index signifies the 1st index
     * @param position
     * @return
     */
    @Override
    public Double getElement(int position) {
        if(position <= 0 || position >= elementList.size())
            throw new IllegalArgumentException("Please provide position > 0 and less than size of total elements inserted.");
        return elementList.get(position - 1);
    }

    /**
     * This method returns the moving average of last N elements inserted.
     * @return
     */
    @Override
    public Double getAverage() {
        return (windowSum * 1.0)/Math.min(windowSize, numberofElements);
    }

    /**
     * This helper method prints the elements inside circular queue
     */
    public void displayList(){
        for(Double i : circularQueue){
            System.out.print(i+ " ");
        }
        System.out.println();
    }
}
