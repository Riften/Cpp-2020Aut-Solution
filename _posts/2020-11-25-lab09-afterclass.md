---
layout: post
filename: 2020-11-25-lab09-afterclass
title: Lab09 After Class
date: 2020-11-25 00:00:00 +0800
categories: post
tags:
  - CS171
  - Lab
mathjax: false
---

## 第1关：二分查找递归实现（改错题）

```cpp
#include <iostream>
using namespace std;

template <class T>  // 1. 缺少template关键字
int binarySearch(T arr[], int low, int high, T target) {    // 2. 返回值类型错误
    if (low > high) {
        return -1;
    }
    int mid = (low + high) / 2;
    T guess = arr[mid];
    if(guess == target) {
        return mid;
    }
    if(guess > target) {
        return binarySearch(arr, low, mid-1, target);
    }
    if(guess < target) {
        return binarySearch(arr, mid+1, high, target);      // 3. 递归错误
    }
}

int main() {
    int m, num;
    int n;
    char ch;

    int numArr[100];
    char chArr[100];

    cin >> m >> num;
    for(int i=0; i<m; i++) {
        cin >> numArr[i];
    }

    cin >> n >> ch;
    for(int i=0; i<n; i++) {    // 4. 变量没有重新置零
        cin >> chArr[i];
    }

    cout << binarySearch<int>(numArr, 0, m-1, num) << endl;
    cout << binarySearch<char>(chArr, 0, n-1, ch);
    return 0;
}
```

## 第2关：各位相加

```cpp
int addDigits(int num) {
    if(num < 10) {
        return num;
    }
    int newNum = 0;
    while(num) {
        newNum += num % 10;
        num /= 10;
    }
    return addDigits(newNum);
}
```

## 第3关：机器人路线数量
可以将原问题转化为两个子问题：

如果在(m, n)向右走，则变成了求解输入为(m,n-1)的子问题，即列数变少1单位。如果向下走，则变成了求解输入为(m-1,n)的子问题，即行数变少1单位。而原问题的答案就是两个子问题答案之和。

```cpp
int calRoutines(int m, int n) {
    if(m == 1 || n == 1) {
        return 1;
    }
    return calRoutines(m-1, n) + calRoutines(m, n-1);
}
```

上述代码可以通过测评，但是却存在着严重的重复计算问题。

我们把`m`行`n`列的路线记为`r(m,n)`，现在考虑计算`r(5,5)`。

按照上面的方法，`r(5,5)`被转变为`r(4,5)`和`r(5,4)`两个子问题，当问题进一步转化时，出现了一个有趣的现象，求解`r(4,5)`和`r(5,4)`的过程中都需要求解`r(4,4)`。

这也就意味着，我们在求解`r(5,4)`的时候就需要把`r(4,4)`求出来，这之后我们已经知道`r(4,4)`的结果了，却在求解`r(4,5)`的时候又计算了一遍`r(4,4)`。

随着行数和列数的增加，一些结果的重复计算次数也成指数增加，举个例子来说，如果按照这种方式计算`r(10,10)`，那么`r(5,5)`将会被计算252次，数字再大一点，程序就可能需要**数分钟**才能得出结果。

解决方法也很简单，用空间换时间，只需要每次计算出一个结果的时候，用一个数组将结果保存下来，之后只需要先检查这个数组，如果发现已经被计算过了，则不计算直接返回结果。代码如下

```cpp
int store[100][100] = {0};  // 用于存储计算结果，如果没有计算过，那么初始值是0
int calRoutines(int m, int n) {
    if(m == 1 || n == 1) {
        return 1;
    }
    if(store[m][n] > 0) {  // 之前已经计算过，直接返回结果
        return store[m][n];
    }
    int res = calRoutines(m-1, n) + calRoutines(m, n-1);
    store[m][n] = res;     // 在第一次计算该结果的时候存入数组，以备重复计算时使用
    return res;
}
```

在棋盘尺寸较大时，有中间结果的缓存可以极大降低代码的运行时间。

## 第4关：跳跃游戏
题目详解见题目讲解讲义或录屏。

```cpp
bool canJump(int arr[], int n) {
    if(n==1) {
        return true;
    }

    for(int i = n-2; i > -1; i--) {
        if(arr[i] + i >= n - 1) {
            return canJump(arr, i+1);
        }
    }
    return false;
}
```

## 第5关：数组乘法

```cpp
void arrayMul(int length, int arr[], int n) {
    for (int i = 0; i < length; i++) {
        cout << arr[i] * n << " ";
    }
}

void arrayMul(int length, char arr[], int n) {
    for (int i = 0; i < length; i++) {
        for (int j = 0; j < n; j++) {
            cout << arr[i];
        }
    }
}
```

## 第6关：向量

```cpp
int pow(int x, int n) {
    int ans = 1;
    while (n--) {
        ans *= x;
    }
    return ans;
}

void num2point(int num) {
    point[0] = 0;
    point[1] = 0;
    while (num % 2 == 0) {
        point[0]++;
        num /= 2;
    }
    while (num % 3 == 0) {
        point[1]++;
        num /= 3;
    }
}

int point2num(int a, int b) {
    return pow(2, a) * pow(3, b);
}
```

## 第7关：三点共线

```cpp
int point[2];
void num2point(int num) {
    point[0] = 0;
    point[1] = 0;
    while (num % 2 == 0) {
        point[0]++;
        num /= 2;
    }
    while (num % 3 == 0) {
        point[1]++;
        num /= 3;
    }
}

bool isCollinear(int x, int y, int z) {
    int p1[2], p2[2], p3[2];
    num2point(x);
    p1[0] = point[0];
    p1[1] = point[1];
    num2point(y);
    p2[0] = point[0];
    p2[1] = point[1];
    num2point(z);
    p3[0] = point[0];
    p3[1] = point[1];
    int v1[2] {};
    int v2[2] {};
    v1[0] = p2[0] - p1[0];
    v1[1] = p2[1] - p1[1];
    v2[0] = p3[0] - p2[0];
    v2[1] = p3[1] - p2[1];
    return v1[0] * v2[1] == v1[1] * v2[0];
}
```