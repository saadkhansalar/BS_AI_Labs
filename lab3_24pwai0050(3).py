{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "a58d4f68-827b-429a-9094-4113fe9fef9d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to Python Programming Lab\n"
     ]
    }
   ],
   "source": [
    "# Task 1: Basic Function\n",
    "\n",
    "def welcome_message():\n",
    "    print(\"Welcome to Python Programming Lab\")\n",
    "\n",
    "# calling the function\n",
    "welcome_message()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "9d583eda-d9dd-4a23-85ff-fbf07898a421",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sum = 8\n"
     ]
    }
   ],
   "source": [
    "# Task 2: Function with Parameters\n",
    "\n",
    "def add_numbers(a, b):\n",
    "    return a + b\n",
    "\n",
    "# calling function\n",
    "result = add_numbers(5, 3)\n",
    "\n",
    "print(\"Sum =\", result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "884e146d-a96e-415c-9ae7-a7ee2ce28b3d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Inside Function A\n",
      "Inside Function B\n"
     ]
    }
   ],
   "source": [
    "# Task 3: Function Call Stack\n",
    "\n",
    "def functionB():\n",
    "    print(\"Inside Function B\")\n",
    "\n",
    "def functionA():\n",
    "    print(\"Inside Function A\")\n",
    "    functionB()   # calling functionB\n",
    "\n",
    "# start program\n",
    "functionA()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "78e30ef3-bae2-4f83-9a62-b7fe299396b5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello saad khan\n",
      "Hello Student\n"
     ]
    }
   ],
   "source": [
    "# Task 4: Default Parameters\n",
    "\n",
    "def greet(name=\"Student\"):\n",
    "    print(\"Hello\", name)\n",
    "\n",
    "# calling with name\n",
    "greet(\"saad khan\")\n",
    "\n",
    "# calling without name\n",
    "greet()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "9730f0f1-1a4b-45d7-bf23-6fa73ae6cbd6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Value of x inside function: 10\n",
      "Value of y inside function: 20\n"
     ]
    },
    {
     "ename": "NameError",
     "evalue": "name 'y' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[6], line 14\u001b[0m\n\u001b[1;32m     11\u001b[0m my_function()\n\u001b[1;32m     13\u001b[0m \u001b[38;5;66;03m# Trying to print y outside function\u001b[39;00m\n\u001b[0;32m---> 14\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[43my\u001b[49m)\n",
      "\u001b[0;31mNameError\u001b[0m: name 'y' is not defined"
     ]
    }
   ],
   "source": [
    "# Task 5: Variable Scope\n",
    "\n",
    "x = 10   # global variable\n",
    "\n",
    "def my_function():\n",
    "    print(\"Value of x inside function:\", x)\n",
    "    \n",
    "    y = 20  # local variable\n",
    "    print(\"Value of y inside function:\", y)\n",
    "\n",
    "my_function()\n",
    "\n",
    "# Trying to print y outside function\n",
    "print(y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "4d3f1eaf-861a-4050-99a2-20970b763f3e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total = 14\n"
     ]
    }
   ],
   "source": [
    "# Task 6: *args example\n",
    "\n",
    "def total_numbers(*numbers):\n",
    "    total = sum(numbers)\n",
    "    return total\n",
    "\n",
    "result = total_numbers(2,3,4,5)\n",
    "\n",
    "print(\"Total =\", result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "a745764a-a8da-4261-9c9d-8c71cd67f8e0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "name : saad khan jadoon\n",
      "age : 22\n",
      "course : Python\n"
     ]
    }
   ],
   "source": [
    "# Task 7: **kwargs example\n",
    "\n",
    "def student_info(**data):\n",
    "    for key, value in data.items():\n",
    "        print(key, \":\", value)\n",
    "\n",
    "student_info(name=\"saad khan jadoon\", age=22, course=\"Python\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "fd530877-3a7c-4669-93ae-f497e389e6b1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Square = 25\n"
     ]
    }
   ],
   "source": [
    "# Task 8: Lambda function\n",
    "\n",
    "square = lambda x: x * x\n",
    "\n",
    "print(\"Square =\", square(5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "d6b77f0d-cce3-46db-9b67-28da7befc7b5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Squares: [1, 4, 9, 16, 25]\n"
     ]
    }
   ],
   "source": [
    "# Task 9: Lambda with map\n",
    "\n",
    "numbers = [1,2,3,4,5]\n",
    "\n",
    "squares = list(map(lambda x: x*x, numbers))\n",
    "\n",
    "print(\"Squares:\", squares)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "170f6472-6123-443b-8e3d-edc641b72611",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "well come programming lab\n"
     ]
    }
   ],
   "source": [
    "def wellcome_message():\n",
    "    print(\"well come programming lab\")\n",
    "wellcome_message()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "2711c86d-44e5-45c0-a5bd-83d8f7efa83d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sum= 14\n"
     ]
    }
   ],
   "source": [
    "def add_numbers(a ,b):\n",
    "    return a + b\n",
    "result = add_numbers(10, 4)\n",
    "\n",
    "print(\"Sum=\", result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5f2f3c3f-2b45-46a5-8dc1-fe2a0d544f49",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "96690872-5af9-4a23-9209-21e1d6a6008f",
   "metadata": {},
   "outputs": [],
   "source": [
    "def functionB():\n",
    "    print(\"Inside function B\")\n",
    "def functionA():\n",
    "    print(\"Inside functin A\")\n",
    "    "
   ]
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
   "version": "3.10.15"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
