public interface MovingAverageInterface {

    /**
     * add element to the data structure
     * @param element
     */
    public void addElement(Double element);

    /**
     * returns element present at the specified position
     * @param position
     * @return element
     */
    public Double getElement (int position);

    /**
     * calculates the average of the last N elements
     * @return average
     */
    public Double getAverage();
}
