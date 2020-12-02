---
layout: post
filename: 2020-11-16-lab08-afterclass
title: Lab08 After Class
date: 2020-11-16 00:00:00 +0800
categories: post
tags:
  - CS171
  - Lab
mathjax: false
---

## 第1关：求x的n次方（改错题）

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

double p(double x, int n); // 1. 缺少函数声明

int main()
{
    int n;
    double x;

    cin >> x >> n;
    cout <<setprecision(2) << fixed << p(x,n);

    return 0;
}

double p(double x, int n)
{
    return n == 0 ? 1 : x * p(x, n-1); // 2. 缺少边界条件
}
```

## 第2关：只出现一次的数字
数字没有负数，且大小有限，可以直接用一个数组存储数字有没有出现。

```cpp
int findElement(int n, int arr[1000]) {
    int mask[10001] = {0};
    for (int i = 0; i < n; i++) {
        mask[arr[i]] += 1;
    }
    for (int i = 0; i < 10001; i++) {
        if (mask[i] == 1) return i;
    }
    return -1;
}
```

## 第3关：字母异位词
ASCII字符只有128个，只需要用两个长度128的数组记录下来每个字符出现几次，然后对比是否相等即可。

```cpp
bool isLike(char s[1000], char t[1000]) {
    int mask1[26] = {0};
    int mask2[26] = {0};
    int i = 0, j = 0;
    while (s[i] != '\0') {
        mask1[s[i] - 'a'] += 1;
        i++;
    }
    while (t[j] != '\0') {
        mask2[t[j] - 'a'] += 1;
        j++;
    }
    for (int i = 0; i < 26; i++) {
        if (mask1[i] != mask2[i]) {
            return false;
        }
    }
    return true;
}
```

## 第4关：最后一个单词的长度
```cpp
int lengthOfLastWord(char str[]) {
    char c;
    int i=0;
    int count = 0;
    int length = 0;
    while((c=str[i++])!='\0') {
        if(c==' ') {
            length = count;
            count = 0;
        } else {
            count++;
        }
    }
    return count > 0 ? count : length;
}
```

## 第5关：将每个元素替换为右侧最大元素
在从右往左遍历的情况下，可以只维护一个当前见过的最大元素，每遍历到一个元素，只需要判断最大元素是否需要更新，然后将元素替换掉即可。

```cpp
#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    /*** Your code here ***/
    int n, arr[1000];
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }


    int arr2[1000];
    int max = arr[n - 1];   // 见过的最大元素
    arr2[n - 1] = -1;       // 最右侧数字一定替换成-1
    for (int i = n - 2; i >= 0; i--) {
        int temp = max;
        max = arr[i] > max ? arr[i] : max;  // 检查遍历到的元素是不是比最大的还要大
        arr2[i] = temp;     // 注意赋的值是最大元素更新之前的值
    }

    // 输出
    for (int i = 0; i < n; i++) {
        cout << arr2[i] << " ";
    }
    /******** End *********/
    return 0;
}
```

## 第6关：买卖股票最佳时机
在从左往右遍历的情况下，能获得的最大利润只取决于当前股票的价格，和曾经出现过的股票最低价。所以只需要用一个变量维护出现过的最低价，然后计算当前最大利润，再与总最大利润比较即可。

```cpp
int maxProfit(int n, int prices[]) {
    if (n==0) {
        return 0;
    }
    int lowest = prices[0];
    int profit = 0;
    for(int i=1; i<n; i++) {
        profit = prices[i] - lowest > profit ? prices[i] - lowest : profit;
        lowest = prices[i] < lowest ? prices[i] : lowest;
    }
    return profit;
}
```

## 第7关：二进制加法

```cpp
void binarySum(int m, char a[10000], int n, char b[10000]) {
    int k = m > n ? m + 1 : n + 1;
    int sum[10000] = {0};
    int i = k - 1;
    m--;
    n--;
    while (m >= 0 && n >= 0) {
        sum[i--] = (a[m--] - '0') + (b[n--] - '0');
    }
    while (m >= 0) {
        sum[i--] = a[m--] - '0';
    }
    while (n >= 0) {
        sum[i--] = b[n--] - '0';
    }
    for (int j = k - 1; j > i; j--) {
        sum[j - 1] += sum[j] / 2;
        sum[j] &= 1;
    }
    for (int j = i; j < k; j++) {
        if (sum[j]) {
            for (; j < k; j++) {
                cout << sum[j];
            }
        }
    }
}
```