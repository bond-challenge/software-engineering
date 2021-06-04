public class Runner {

    public static void main(String... args) {
        DataStructure dataStructure=new DataStructureImpl(100);

        dataStructure.averageOfLastNElementsAdded(5);
        dataStructure.addElement(1);
        dataStructure.addElement(2);
        dataStructure.addElement(3);
        dataStructure.addElement(4);
        dataStructure.addElement(5);
        System.out.println("averageOfLastNElementsAdded : "+dataStructure.averageOfLastNElementsAdded(2));

        System.out.println("Get element : "+dataStructure.getElement(3));

        System.out.println("List of elements : "+dataStructure.getAllElements());



    }
}
