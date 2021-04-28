package com.codingchallenge.service;

import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.List;

public class MovingAverage implements MovingAverageInterface<Double> {
	
	//windowSize defined the last of "N" digits
	private int windowSize;
	
	//storing all added elements
	private List<Double> list;
	
	/**
	 * providing constructor to initial this instance
	 * @param size
	 */
	public MovingAverage(int size) {
		
		//we shouldn't allow window side less or equal than zero
		if(size <= 0) {
			throw new IllegalArgumentException("Window size should not less or equal than zero!");
		}
		this.windowSize = size;
		this.list = new ArrayList<Double>();
	}
	
	public void addElement(Double element) {
		list.add(element);
	}

	public List<Double> getElements() {
		return list;
	}

	public Double getAverage() {
		double avergae = 0d;
		
		if(windowSize <= list.size()) {
			double sum = 0;
			for(int i = list.size() - windowSize; i < list.size(); i++) {
				sum+=list.get(i);
			}
			avergae = new BigDecimal(sum/windowSize).doubleValue();
		}
		else {
			System.out.println("Couldn't find out average of the last " + windowSize 
					+ " elements since the size of the list is " + list.size());
		}
		
		return avergae;
	}

}
