---
layout: post
filename: 2020-12-11-lab11-afterclass
title: Lab11 After Class
date: 2020-12-11 00:00:00 +0800
categories: post
tags:
  - CS171
  - Lab
mathjax: false
---

## 第1关：字符串拷贝（改错题）

```cpp
#include <iostream>
using namespace std;

char* strcpy( char* dest, const char* src );

int main()
{
    char *input = new char[101];             // 1. 括号使用错误
    char *copied = new char[101];
    char *returnValue;
    cin.getline(input, 100);
    
    returnValue = strcpy(copied, input);

    cout << copied << endl;
    cout << returnValue << endl;

    delete []input;                          // 2. delete 没加括号（不改可能也可以通过测评）
    return 0;
}

char* strcpy( char* dest, const char* src ){ // 3. 函数原型不一致
    int i=0;
    while(*(src+i)!='\0') {
        *(dest+i) = *(src + i);              // 4. 赋值方式错误
        i++;
    }
    *(dest+i) = '\0';                        // 5. 结尾没有加空字符
    return dest;                             // 6. 返回值类型错误
}
```

## 第2关：strncat函数
这里需要注意两个小问题
- 不需要对dest再次分配内存，这个工作是在调用`strncat`之前就需要完成的，也就是在`main`函数中。传入一个已经分配好内存的指针作为目的指针也是`strncat`函数的要求。
- 记得结尾加`\0`。

```cpp
#include <iostream>
using namespace std;

/*** Your code here ***/
char *strncat(char *dest, const char *src, unsigned count) {
    char *p = dest;
    while (*p != '\0') {
        p++;
    }
    unsigned i = 0;
    while (i < count && *(src + i) != '\0') {
        *p = *(src + i);
        p++;
        i++;
    }
    *p = '\0';

    return dest;
}
/******** End *********/
```

## 第3关：二维矩阵区域和

```cpp
#include <iostream>

using namespace std;

// 你需要自己写 main 函数
/*** Your code here ***/
int matrixSum(int **matrix, int r1, int c1, int r2, int c2) {
    int sum = 0;
    for (int i = r1; i <= r2; i++) {
        for (int j = c1; j <= c2; j++) {
            sum += matrix[i][j];
        }
    }
    return sum;
}

int main(int argc, char const *argv[])
{
    int m, n;
    cin >> m >> n;
    int **matrix = new int*[m];
    for (int i = 0; i < m; i++) {
        *(matrix + i) = new int[n];
    }
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            cin >> matrix[i][j];
        }
    }
    int r1, c1, r2, c2;
    while (true) {
        cin >> r1 >> c1 >> r2 >> c2;
        if (r1 == -1 && c1 == -1 && r2 == -1 && c2 == -1) {
            break;
        }
        cout << matrixSum(matrix, r1, c1, r2, c2) << endl;
    }
    return 0;
}
/******** End *********/
```

## 第4关：打家劫舍
递归关系见题目讲解讲义。本题实际上和菲波那切数列类似，如果使用递归求解需要注意避免重复计算。

### 非递归写法
```cpp
#include <iostream>
using namespace std;

/*** Your code here ***/
int Rob(int nums[], int n) {
    int Fi = 0;
    int Fi_1 = 0;
    int Fi_2 = 0;
    for(int i=0; i<n; i++) {
        Fi = nums[i] + Fi_2 > Fi_1 ? nums[i] + Fi_2 : Fi_1;
        Fi_2 = Fi_1;
        Fi_1 = Fi;
    }
    return Fi;
}
/******** End *********/
```

### 递归写法
```cpp
#include <iostream>
using namespace std;

int sum[200] {};
/*** Your code here ***/
int Rob(int nums[], int n){
    if(n<1){
        return 0;
    }
    if(sum[n] > 0) {
        return sum[n];
    }
    int res;
    int r1, r2;
    r1 = Rob(nums, n-1);
    r2 = Rob(nums, n-2) + nums[n-1];
    res = r1 > r2 ?  r1 : r2;
    sum[n] = res;
    return res;
}
/******** End *********/
```

## 第5关：最长回文子串
比较简单的解法是，用两层循环遍历每个子字符串的起始和结尾位置，然后判断每个子字符串是不是回文。

```cpp
bool isPlalindrome(char *str, int start, int end) {
    while(start < end) {
        if(str[start++] != str[end--]) return false;
    }
    return true;
}

char *plalindrome(char *str, int n) {
    char *res = str;
    int maxLength = 1;
    int len;
    for(int i=0; i<n-1; i++) {
        for(int j=i+1; j<n; j++) {
            len = j-i+1;
            if(len > maxLength) {
                if (isPlalindrome(str, i, j)) {
                    res = str + i;
                    maxLength = len;
                }
            }
        }
    }
    res[maxLength] = '\0';
    return res;
}
```

优化解法：用每个字符串的“中心位置”作为不同回文的标识，从一个中心位置只能得到唯一一个最长回文。
```cpp
/*** Your code here ***/

void findPla(char *str, int n, int midLeft, int midRight, int &start, int &length) {
    length = 0;

    if(midLeft == midRight) {
        length--;
    }

    while(midLeft > -1 && midRight < n && str[midLeft] == str[midRight]) {
        length += 2;
        midLeft--;
        midRight++;
    }

    start = midLeft + 1;
}

char* plalindrome(char *str, int n) {
    int start;
    int length;
    int maxLength = 1;
    int resStart = 0;
    for(int i=0; i<n; i++) {
        findPla(str, n, i, i, start, length);
        if(length > maxLength) {
            maxLength = length;
            resStart = start;
        }
        findPla(str, n, i, i+1, start, length);
        if(length > maxLength) {
            maxLength = length;
            resStart = start;
        }
    }
    str[resStart + maxLength] = '\0';
    return str + resStart;
}
/******** End *********/
```