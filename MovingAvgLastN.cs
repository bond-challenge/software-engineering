public static class MovingAvgLastN{
	int maxTotal;
	int total;
	double lastN[];
	double avg;
	int head;
// Define all the variables
	public MovingAvgLastN(int N){
		maxTotal = N;
		lastN = new double[N];
		avg = 0;
		head = 0;
		total = 0;
	}
// Define the sum function which will return the sum of n numbers in a queue
	public void sum(double val){
		double previous_sum_val = total*avg;
		
		if(total == maxTotal){
			previous_sum_val-=lastN[head];
			total--;
		}
		
		head = (head+1)%maxTotal;
		int emptyPos = (maxTotal+head-1)%maxTotal;
		lastN[emptyPos] = val;
		
		double newSum = previous_sum_val+val;
		total++;
		avg = newSum/total;
	}
// Define the average function which will return the average of n numbers in a queue
	public double getAvg(){
		return avg;
	}
}