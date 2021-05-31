Coding Question:

As there was no specific programming language given, so I am supposing that I can implement this in any language. Also, reading the 2nd question where specifically mentioned that we have to provide a cloud based architecture so on basis of that Python is one of the option that can be used as it would integrate well in the cloud.

Since I have some experience with C# as well , so I want to show that capability and not going with Python or using any inbuilt function.

So, I have defined an interface and then used this as the basis of the implementation.

public interface MovingAverageN{
    public void sum(double val);
    public double getAvg();
}



Below is the logic which is the base of this code:
avg=(n*avg+new_element)/(n+1)

Also, below is the pseudocode for this approach, for n elements in a queue, this is the base logic for my program in C#:

Queue queue;
double avg;

def sum(val) :
    double
    if(queue.size() == N) then
         avg = (N*avg-queue.dequeue()+val)/N
    else
         avg = (queue.size()*avg+val)/(queue.size()+1)
         queue.sum(val);
    end
end

def getAvg() :
   return avg;
end
