{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "fa9326ad",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Interface:\n",
    "  def __init__(self,list_n_elements):\n",
    "    self.list_n_elements=list_n_elements\n",
    "  def show(self):\n",
    "    pass\n",
    "  def last_n_average(self,N):\n",
    "    pass\n",
    "  def add_n_elements(self,x):\n",
    "    pass\n",
    "  def getaccess(self):\n",
    "    pass"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "8ea84ea6",
   "metadata": {},
   "outputs": [],
   "source": [
    "class implementation(Interface):\n",
    "  def show(self):\n",
    "    print(self.list_n_elements)\n",
    "  def last_n_average(self,N):\n",
    "    return sum(self.list_n_elements[-N:])/N\n",
    "  def add_n_elements(self,x):\n",
    "    return self.list_n_elements.append(x)\n",
    "  def getaccess(self,index):\n",
    "    return self.list_n_elements[index]\n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "7ea40d5b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 3, 3, 3, 3, 31, 1, 2, -9]\n"
     ]
    }
   ],
   "source": [
    "list1=[2,3,3,3,3,31,1,2,-9]\n",
    "x=implementation(list1)\n",
    "x.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "358ef900",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5.6"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x.last_n_average(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "5305a9fb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 3, 3, 3, 3, 31, 1, 2, -9, 12, 12]\n"
     ]
    }
   ],
   "source": [
    "x.add_n_elements(12)\n",
    "x.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "3aa6f7ce",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "31\n"
     ]
    }
   ],
   "source": [
    "print(x.getaccess(5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "63658366",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
