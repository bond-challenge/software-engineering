import java.util.List;


public interface DataStructure {

    Double averageOfLastNElementsAdded(int n);

    void addElement(int element);

    Integer getElement(int index);

    List<Integer> getAllElements();
}
