---
layout: post
filename: 2020-12-06-lab10-afterclass
title: Lab10 After Class
date: 2020-12-06 00:00:00 +0800
categories: post
tags:
  - CS171
  - Lab
mathjax: false
---

## 第1关：最大最小值（改错题）

```cpp
#include <iostream>
using namespace std;

void maxmin(int n, int arr[], int *maximum, int *minimum);    // 1. 函数参数列表错误

int main() {
    int *maximum = new int;
    int *minimum = new int;
    int n, arr[10000];
    cin >> n;
    for(int i=0; i<n; i++) {
        cin >> arr[i];
    }
    maxmin(n, arr, maximum, minimum);
    cout << *minimum << " " << *maximum;
    return 0;
}

void maxmin(int n, int arr[], int *maximum, int *minimum) {
    *maximum = arr[0];                                          // 2. 修改指针指向的值，而非修改指针
    *minimum = arr[0];
    for(int i=1; i<n; i++) {
        if(arr[i] > *maximum){
            *maximum = arr[i];
        }
        if(arr[i] < *minimum) {
            *minimum = arr[i];
        }
    }
}
```

本题还可以通过将函数的参数类型从`int *`改成`int*&`，即指针的引用来解决。

## 第2关：敏感字符过滤

```cpp
#include <iostream>

/*** Your code here ***/
void delChar(char *str, int k) {
    while(str[k] != '\0') {
        str[k] = str[k+1];
        k++;
    }
}

void delSensitiveCh(char* str, char* sensitive) {
    bool isSen[128]{};
    while(*sensitive != '\0') {
        isSen[*sensitive] = true;
        sensitive ++;
    }

    int i=0;
    for(;str[i]!='\0'; i++) {
        if(isSen[str[i]]) {
            delChar(str, i);
            i--;
        }
    }
    return;
}
/******** End *********/
```

## 第3关：变换单词顺序
核心思路是通过两个数组，一个记录每个单词的起始位置，一个记录单词的长度，然后只需要按照order数组的信息，读出来每个单词的起始位置和长度，取出单词填入结果字符串即可。

```cpp
#include <iostream>
#include "func.h"
/*** Your code here ***/
char* shuffleWords(char* str, int* order){
    char* res = new char[1000];
    // index 记录每个单词的起始位置
    int index[100];
    // length 记录每个单词的长度
    int length[100];
    int n = 0;
    int curr = 0, begin = 0;
    while(str[curr] != '\0') {
        if(str[curr]==' ') {
            index[n] = begin;
            length[n] = curr - begin;
            begin = curr + 1;
            n++;
        }
        curr++;
    }
    // For last word
    index[n] = begin;
    length[n] = curr - begin;
    n++;
    
    curr = 0;
    for(int i=0; i<n; i++) {
        for(int j=index[order[i]]; j<index[order[i]]+length[order[i]]; j++) {
            res[curr++] = str[j];
        }
        res[curr++] = ' ';
    }
    res[curr-1] = '\0';
    return res;
}
/******** End *********/
```

## 第4关：Julian 历法
这里用一个数组记下来了每个月的天数，避免了大量分支语句的使用。

```cpp
#include <iostream>

/*** Your code here ***/
int days[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

int* julian(int year, int day) {
    if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
        days[1]++;
    }

    int month = 0;
    while (day > days[month]) {
        day -= days[month];
        month++;
        if (month == 12) {
            return NULL;
        }
    }

    return new int[2] {month + 1, day};
}
/******** End *********/
```

## 第5关：最长回文串
详见题目讲解讲义

```cpp
#include <iostream>

/*** Your code here ***/
int longestPalindrome(char *str) {
    int nums[128]{};
    while(*str != '\0') {
        nums[*str++] += 1;
    }
    int k=0;
    int res=0;
    for(int i=0; i<128; i++) {
        if(nums[i]%2) k=1;
        res += nums[i]/2*2;
    }
    res += k;
    return res;
}
/******** End *********/
```

## 第6关：和为0的三个数字
最简单的做法就是通过三层循环解决。

```cpp
/*** Your code here ***/
int threeSum(int *nums, int n) {
    //sort
    int res = 0;
    for(int i=0; i<n-2; i++) {
        for(int j=i+1; j<n-1; j++) {
            for(int k=j+1; k<n; k++) {
                if(nums[i]+nums[j]+nums[k]==0) {
                    res ++;
                }
            }
            
        }
    }
    return res;
}
/******** End *********/
```

优化解法见题目讲解讲义。

## 第7关：多数元素
第一种思路是，排序之后，中间的元素必定是多数元素。

但是这实际上并不是最优解法，下面的解法只需要遍历一遍数组，尝试把不相同的数字“两两抵消”，最后剩下的就是多数元素。

```cpp
#include <iostream>

/*** Your code here ***/
int findMajor(int nums[], int n) {
    int target=nums[0], counter=1;
    for(int i=1; i<n; i++){
        if(nums[i] == target){
            counter++;
        }else{
            if(counter)counter--;
            else{
                target=nums[i];
                counter=1;
            }
        }
    }
    return target;
}
/******** End *********/
```