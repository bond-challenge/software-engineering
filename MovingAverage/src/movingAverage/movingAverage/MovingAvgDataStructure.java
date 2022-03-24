package movingAverage;

import java.util.Collection;
import java.util.LinkedList;
import java.util.Queue;

public class MovingAvgDataStructure implements MovingAvgInterface {
	private float sum;
	private int windowSize;
	private Queue<Float> queue;

	public MovingAvgDataStructure(int windowSize) {
		this.windowSize = windowSize;
		this.queue = new LinkedList<>();
	}

	@Override
	public float findAvg() {
		return sum / windowSize;
	}

	@Override
	public void addElem(float elem) {
		if (queue.size() >= windowSize) {
			float removeElem = queue.poll();
			sum = sum - removeElem;
		}
		queue.add(elem);
		sum = sum + elem;
	}

	@Override
	public void getFromQueue() {
		System.out.println("Elements in queue");
		for (Float item : queue) {
			Float element = (Float) item;
			System.out.print(element + " ");
		}
		System.out.println();
	}

	public static void main(String[] args) {
		MovingAvgDataStructure movingAvg = new MovingAvgDataStructure(4);
		movingAvg.addElem(1);
		movingAvg.getFromQueue();
		System.out.println("Average is " + movingAvg.findAvg());
		movingAvg.addElem(2);
		movingAvg.getFromQueue();
		System.out.println("Average is " + movingAvg.findAvg());
		movingAvg.addElem(3);
		movingAvg.getFromQueue();
		System.out.println("Average is " + movingAvg.findAvg());
		movingAvg.addElem(4);
		movingAvg.getFromQueue();
		System.out.println("Average is " + movingAvg.findAvg());
		movingAvg.addElem(5.5f);
		movingAvg.getFromQueue();
		System.out.println("Average is " + movingAvg.findAvg());
		movingAvg.addElem(6);
		movingAvg.getFromQueue();
		System.out.println("Average is " + movingAvg.findAvg());
	}
}
