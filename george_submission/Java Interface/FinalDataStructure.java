package com.bondbrand.challenge.test;
 
/*
 * Title: FinalDataStructure
 * Description: A Data structure that allows adding elements 
 * and providing the moving average of the last N elements added. The N should be specified when 
 * creating an instance of the implementation class.
 
 * @author George Oboh
 */
public interface FinalDataStructure {
    void addElement(float data); /*Adds element in the data list*/
    float getMovingAverage(); /*Returns moving average*/
    public int getSize(); /*Returns size of the data list*/
}