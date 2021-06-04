import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class DataStructureImpl implements DataStructure {

    private static int[] data;
    private int index=-1;

    public DataStructureImpl(int dataSize) {
        data = new int[dataSize];

    }

    @Override
    public Double averageOfLastNElementsAdded(int n) {
        if (n-1 <= index) {
            int index = this.index;
            int i = (index + 1) - n;
            double sum = 0.0;
            while (i <= index) {
                sum += data[i++];
            }
            return sum / n;
        } else {
            System.out.println("Last added size is not valid ");
            return null;
        }

    }

    @Override
    public void addElement(int element) {
        data[++index] = element;
        System.out.println("Element added "+element);
    }

    @Override
    public Integer getElement(int index) {
        if(this.index > -1 && this.index >= index-1){
            return data[index];
        }else{
            System.out.println("Invalid index "+index+" the size is "+this.index);
        }
        return null;
    }

    @Override
    public List<Integer> getAllElements() {
        AtomicInteger i = new AtomicInteger();
        return IntStream.of(data).filter(x -> i.getAndIncrement() <= index).boxed().collect(Collectors.toList());
    }
}
