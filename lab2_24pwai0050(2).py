{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f2d69c43-5301-4568-a42d-a80c2349cdf9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your full name: saad khan jadoon\n",
      "Enter your fovorite color: cream color\n",
      "Enter your birth date: 2002\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "wellcome , saad khan jadoon!\n",
      "Your favorte color is cream color - perfect for calm ai thinking.\n",
      "Your were born in 2002 - Your are currently 24 year old 2026.\n"
     ]
    }
   ],
   "source": [
    "name = input(\"Enter your full name:\")\n",
    "color = input(\"Enter your fovorite color:\")\n",
    "birth_year = int(input(\"Enter your birth date:\"))\n",
    "age = 2026 - birth_year\n",
    "print(f\"wellcome , {name}!\")\n",
    "print(f\"Your favorte color is {color} - perfect for calm ai thinking.\")\n",
    "print(f\"Your were born in {birth_year} - Your are currently {age} year old 2026.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "6f8ef736-92c7-4763-bdcc-847eb8524ed9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your first number: 48\n",
      "Enter your second number: 74\n",
      "Enter operation (+ ,- ,* , / ,**, %): +\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "48.0 + 74.0 = 122.0\n"
     ]
    }
   ],
   "source": [
    "# Ask for two numbers and convert them into flaot \n",
    "num1 = float(input(\"Enter your first number:\"))\n",
    "num2 = float(input(\"Enter your second number:\"))\n",
    "operator =input(\"Enter operation (+ ,- ,* , / ,**, %):\")\n",
    "#check which opeartion user perform\n",
    "if operator not in [\"+\", \"-\",\"*\",\"/\",\"**\",\"%\"]:\n",
    "    print(\"invalid operator!\")\n",
    "    #Addition\n",
    "elif operator == \"+\":\n",
    "    result = num1 + num2\n",
    "    print(f\"{num1} + {num2} = {result}\")\n",
    "    #substricton\n",
    "elif operator == \"-\":\n",
    "    result = num1 - num2\n",
    "    print(f\"{num1} -{num2} ={result}\")\n",
    "#Multiplicatin \n",
    "elif operator == \"*\":\n",
    "    result = num1  * num2\n",
    "    print(f\"{num1} * {num2} = {result}\")\n",
    "#Devision\n",
    "elif operator == \"/\":\n",
    "   if num2 == 0:\n",
    "      print(\"Cannot Divide by zero!\")\n",
    "   else: \n",
    "      result = num1 / num2\n",
    "      print(f\"{num1} / {num2} = {result:.2f}\")\n",
    "#Power\n",
    "elif operator == \"**\":\n",
    "    result = num1 ** num2\n",
    "    print(f\"{num1} ** {num2} = {result:.2f}\")\n",
    "\n",
    "#Moudlus\n",
    "elif operator == \"%\":\n",
    "    if num2 == 0:\n",
    "      print(\"Cannot divide by zero!\")\n",
    "    else:\n",
    "      result = num1 % num2\n",
    "      print(f\"{num1} %  {num2} ={result}\")\n",
    "\n",
    "\n",
    "\n",
    "      "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "75f695aa-7577-4d71-ab0f-b441d5eed86f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter starting number:  7\n",
      "Enter ending number:  9\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "8 → Even\n",
      "9\n"
     ]
    }
   ],
   "source": [
    "# Challenge A - Even/Odd & Multiple Checker\n",
    "\n",
    "start = int(input(\"Enter starting number: \"))\n",
    "end = int(input(\"Enter ending number: \"))\n",
    "\n",
    "# Start loop\n",
    "while start <= end:\n",
    "\n",
    "    # Skip numbers divisible by 7\n",
    "    if start % 7 == 0:\n",
    "        start += 1\n",
    "        continue\n",
    "\n",
    "    # Check if number is even and multiple of 5\n",
    "    if start % 2 == 0 and start % 5 == 0:\n",
    "        print(f\"{start} → Even & Multiple of 5!!\")\n",
    "\n",
    "    # Check only even\n",
    "    elif start % 2 == 0:\n",
    "        print(f\"{start} → Even\")\n",
    "\n",
    "    # Check multiple of 5\n",
    "    elif start % 5 == 0:\n",
    "        print(f\"{start} → Multiple of 5!\")\n",
    "\n",
    "    # If none\n",
    "    else:\n",
    "        print(start)\n",
    "\n",
    "    # Increase number\n",
    "    start += 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "b8526b3a-b356-4150-9eba-76bfa35f0d89",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your password:  Saadkhan10\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Strong password – good choice!\n"
     ]
    }
   ],
   "source": [
    "# Challenge B - Password Strength Checker\n",
    "\n",
    "password = input(\"Enter your password: \")\n",
    "\n",
    "# Check password length\n",
    "if len(password) < 6:\n",
    "    print(\"Too short!\")\n",
    "\n",
    "else:\n",
    "    has_digit = False\n",
    "    has_upper = False\n",
    "\n",
    "    # Check each character\n",
    "    for char in password:\n",
    "        if char.isdigit():\n",
    "            has_digit = True\n",
    "        if char.isupper():\n",
    "            has_upper = True\n",
    "\n",
    "    # Check conditions\n",
    "    if not has_digit:\n",
    "        print(\"Add at least one number\")\n",
    "\n",
    "    elif not has_upper:\n",
    "        print(\"Add at least one capital letter\")\n",
    "\n",
    "    else:\n",
    "        print(\"Strong password – good choice!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "79238591-3345-4615-8d3c-0f346358e7c9",
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
   "version": "3.10.15"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
