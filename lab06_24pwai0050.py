{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "1d9d4078-5cc8-4af2-b400-6e24ace7890c",
   "metadata": {},
   "source": [
    "LAB_06"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3ae3bdf6-5215-4dac-877c-ed0d91660fe0",
   "metadata": {},
   "source": [
    "Task 1 — Creating Arrays"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "3ec17e02-9990-41eb-abd1-41a5845d3878",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1D Array:\n",
      " [ 1  2  3  4  5  6  7  8  9 10]\n",
      "\n",
      "2D Array:\n",
      " [[1 2 3]\n",
      " [4 5 6]\n",
      " [7 8 9]]\n",
      "\n",
      "Zeros Array:\n",
      " [[0. 0. 0. 0.]\n",
      " [0. 0. 0. 0.]\n",
      " [0. 0. 0. 0.]\n",
      " [0. 0. 0. 0.]]\n",
      "\n",
      "Ones Array:\n",
      " [[1. 1. 1. 1. 1.]\n",
      " [1. 1. 1. 1. 1.]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "# 1. 1D array from 1 to 10\n",
    "array1 = np.arange(1, 11)\n",
    "\n",
    "# 2. 3x3 2D array\n",
    "array2 = np.array([[1, 2, 3],\n",
    "                   [4, 5, 6],\n",
    "                   [7, 8, 9]])\n",
    "\n",
    "# 3. 4x4 zeros array\n",
    "zeros_array = np.zeros((4, 4))\n",
    "\n",
    "# 4. 2x5 ones array\n",
    "ones_array = np.ones((2, 5))\n",
    "\n",
    "# 5. Display arrays\n",
    "print(\"1D Array:\\n\", array1)\n",
    "print(\"\\n2D Array:\\n\", array2)\n",
    "print(\"\\nZeros Array:\\n\", zeros_array)\n",
    "print(\"\\nOnes Array:\\n\", ones_array)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d665a1fc-ee87-4eb2-b810-1a51bdde0b87",
   "metadata": {},
   "source": [
    "Task 2 — Array Properties"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "853f6239-f25c-4c2c-91c1-deaa3447bd1f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Shape: (2, 3)\n",
      "Total Elements: 6\n",
      "Data Type: int64\n",
      "Dimensions: 2\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "arr = np.array([[1, 2, 3],\n",
    "                [4, 5, 6]])\n",
    "\n",
    "# 1. Shape\n",
    "print(\"Shape:\", arr.shape)\n",
    "\n",
    "# 2. Total elements\n",
    "print(\"Total Elements:\", arr.size)\n",
    "\n",
    "# 3. Data type\n",
    "print(\"Data Type:\", arr.dtype)\n",
    "\n",
    "# 4. Number of dimensions\n",
    "print(\"Dimensions:\", arr.ndim)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6d27d8ea-98a8-4997-81d8-dc84d9437663",
   "metadata": {},
   "source": [
    "Task 3 — Indexing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "7eb8306f-1f61-4332-9156-f926d364e2be",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "First Element: 10\n",
      "Last Element: 60\n",
      "Third Element: 30\n",
      "Values greater than 30: [40 50 60]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "arr = np.array([10, 20, 30, 40, 50, 60])\n",
    "\n",
    "# Access elements\n",
    "print(\"First Element:\", arr[0])\n",
    "print(\"Last Element:\", arr[-1])\n",
    "print(\"Third Element:\", arr[2])\n",
    "\n",
    "# Values greater than 30\n",
    "print(\"Values greater than 30:\", arr[arr > 30])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9f100771-8088-49d9-b9fd-6887855f2c9d",
   "metadata": {},
   "source": [
    "Task 4 — Slicing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "bde9bd73-6cfc-4704-ab74-eb3c46bf92aa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Slice 1 to 4: [20 30 40 50]\n",
      "Reversed Array: [60 50 40 30 20 10]\n",
      "Alternate Elements: [10 30 50]\n",
      "First Row: [1 2 3]\n",
      "Second Column: [2 5 8]\n",
      "Last Two Rows:\n",
      " [[4 5 6]\n",
      " [7 8 9]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "arr = np.array([10, 20, 30, 40, 50, 60])\n",
    "\n",
    "# 1. Elements from index 1 to 4\n",
    "print(\"Slice 1 to 4:\", arr[1:5])\n",
    "\n",
    "# 2. Reverse array\n",
    "print(\"Reversed Array:\", arr[::-1])\n",
    "\n",
    "# 3. Alternate elements\n",
    "print(\"Alternate Elements:\", arr[::2])\n",
    "\n",
    "# 4. 3x3 matrix\n",
    "matrix = np.array([[1, 2, 3],\n",
    "                   [4, 5, 6],\n",
    "                   [7, 8, 9]])\n",
    "\n",
    "print(\"First Row:\", matrix[0])\n",
    "print(\"Second Column:\", matrix[:, 1])\n",
    "print(\"Last Two Rows:\\n\", matrix[1:])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1bb9621d-8d4a-40fe-9bce-2d123c2048cf",
   "metadata": {},
   "source": [
    "Task 5 — Vectorization"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "f4529470-99a7-44d4-a406-cad6b28e7418",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Multiply by 5: [ 5 10 15 20 25]\n",
      "Add 10: [11 12 13 14 15]\n",
      "Squared Values: [ 1  4  9 16 25]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "arr = np.array([1, 2, 3, 4, 5])\n",
    "\n",
    "# Multiply by 5\n",
    "print(\"Multiply by 5:\", arr * 5)\n",
    "\n",
    "# Add 10\n",
    "print(\"Add 10:\", arr + 10)\n",
    "\n",
    "# Square elements\n",
    "print(\"Squared Values:\", arr ** 2)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ee989981-b227-41ce-abe7-b1e713d26556",
   "metadata": {},
   "source": [
    "Task 6 — Broadcasting"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "64d888d8-9d7b-4caa-b698-bf1ec68fc699",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "After Adding 10:\n",
      " [[11 12 13]\n",
      " [14 15 16]]\n",
      "After Multiplying by 2:\n",
      " [[ 2  4  6]\n",
      " [ 8 10 12]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "arr = np.array([[1, 2, 3],\n",
    "                [4, 5, 6]])\n",
    "\n",
    "# Add 10\n",
    "print(\"After Adding 10:\\n\", arr + 10)\n",
    "\n",
    "# Multiply by 2\n",
    "print(\"After Multiplying by 2:\\n\", arr * 2)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5a9edea6-3b6e-4089-a0ae-f09a5f1286e7",
   "metadata": {},
   "source": [
    "Task 7 — Matrix Addition and Subtraction"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "b6b50e0b-a960-43b3-ba80-61cc6b64b707",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Addition:\n",
      " [[ 6  8]\n",
      " [10 12]]\n",
      "Subtraction:\n",
      " [[-4 -4]\n",
      " [-4 -4]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "A = np.array([[1, 2],\n",
    "              [3, 4]])\n",
    "\n",
    "B = np.array([[5, 6],\n",
    "              [7, 8]])\n",
    "\n",
    "# Addition\n",
    "print(\"Addition:\\n\", A + B)\n",
    "\n",
    "# Subtraction\n",
    "print(\"Subtraction:\\n\", A - B)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8f823872-fa81-4b86-bf85-11985c8a2250",
   "metadata": {},
   "source": [
    "Task 8 — Matrix Multiplication"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "6a5e1f9a-51ff-4ac1-8f42-19747d996c99",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Matrix Multiplication:\n",
      " [[19 22]\n",
      " [43 50]]\n",
      "Transpose of A:\n",
      " [[1 3]\n",
      " [2 4]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "A = np.array([[1, 2],\n",
    "              [3, 4]])\n",
    "\n",
    "B = np.array([[5, 6],\n",
    "              [7, 8]])\n",
    "\n",
    "# Matrix multiplication\n",
    "result = np.dot(A, B)\n",
    "\n",
    "print(\"Matrix Multiplication:\\n\", result)\n",
    "\n",
    "# Transpose\n",
    "print(\"Transpose of A:\\n\", A.T)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "45017880-09ad-4b2f-8a26-3768e1b6185e",
   "metadata": {},
   "source": [
    "Task 9 — Random Arrays"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "b6dd0494-7bdb-4e14-b1a9-73fa24b071f3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Random Integer Array:\n",
      " [[20 19 18 39]\n",
      " [81 65 49 21]\n",
      " [40 84 85  5]\n",
      " [45 30 49 34]]\n",
      "\n",
      "Random Decimal Array:\n",
      " [[0.92138892 0.48711139 0.43506184 0.24325663]\n",
      " [0.54251207 0.40622942 0.77417795 0.96758711]\n",
      " [0.40229721 0.27383225 0.22011595 0.05069499]\n",
      " [0.09675013 0.76713767 0.08624717 0.42478486]]\n",
      "\n",
      "Maximum Value: 85\n",
      "Minimum Value: 5\n",
      "Average Value: 42.75\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "# Random integers\n",
    "rand_int = np.random.randint(1, 101, (4, 4))\n",
    "\n",
    "# Random decimal values\n",
    "rand_float = np.random.rand(4, 4)\n",
    "\n",
    "print(\"Random Integer Array:\\n\", rand_int)\n",
    "print(\"\\nRandom Decimal Array:\\n\", rand_float)\n",
    "\n",
    "# Maximum, minimum, average\n",
    "print(\"\\nMaximum Value:\", rand_int.max())\n",
    "print(\"Minimum Value:\", rand_int.min())\n",
    "print(\"Average Value:\", rand_int.mean())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "04f9af23-2e78-4bcc-8990-6d79792f7482",
   "metadata": {},
   "source": [
    "Task 10 — Student Marks Analysis"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "26b7159d-b170-48c0-b6df-7dc6b51c8c94",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Average Marks: 74.3\n",
      "Highest Marks: 95\n",
      "Lowest Marks: 40\n",
      "Students scoring above 80: [85 90 82 95 88]\n",
      "Failed Students: [45 40]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "marks = np.array([78, 85, 90, 45, 67, 82, 95, 40, 73, 88])\n",
    "\n",
    "# Average, highest, lowest\n",
    "print(\"Average Marks:\", marks.mean())\n",
    "print(\"Highest Marks:\", marks.max())\n",
    "print(\"Lowest Marks:\", marks.min())\n",
    "\n",
    "# Students above 80\n",
    "print(\"Students scoring above 80:\", marks[marks > 80])\n",
    "\n",
    "# Failed students below 50\n",
    "print(\"Failed Students:\", marks[marks < 50])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "778021e2-8b4c-458c-bfce-70dac965e8e0",
   "metadata": {},
   "source": [
    "Task 11 — Image Pixel Simulation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "dea428aa-108e-49d0-bd46-15e665b9bbca",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Image Pixels:\n",
      " [[ 78  86 175 134 180]\n",
      " [226 180  45 178  50]\n",
      " [ 82  24 175  90 231]\n",
      " [ 53 182  20 108  90]\n",
      " [ 78 201 103  16  49]]\n",
      "Brightest Pixel: 231\n",
      "Darkest Pixel: 16\n",
      "Image Shape: (5, 5)\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "# Random 5x5 image pixels\n",
    "image = np.random.randint(0, 256, (5, 5))\n",
    "\n",
    "print(\"Image Pixels:\\n\", image)\n",
    "\n",
    "# Brightest and darkest pixels\n",
    "print(\"Brightest Pixel:\", image.max())\n",
    "print(\"Darkest Pixel:\", image.min())\n",
    "\n",
    "# Shape\n",
    "print(\"Image Shape:\", image.shape)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a86679c2-b34e-457e-9e54-0c0d7872937c",
   "metadata": {},
   "source": [
    "Task 12 — Data Normalization"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f3114eb2-2bb8-4b46-9bd2-8ec780e059ec",
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
