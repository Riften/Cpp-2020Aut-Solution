---
layout: post
filename: 2020-12-23-lab13-afterclass
title: Lab13 After Class
date: 2020-12-23 00:00:00 +0800
categories: post
tags:
  - CS171
  - Lab
mathjax: false
---

## 第1关：字符串处理库

### my_string.h

```cpp
#ifndef _MY_STRING_H
#define _MY_STRING_H

/*** Your code here ***/
char* strcpy(char *dest, const char *src);

char* strcat(char *dest, const char *src);

int strcmp(const char *str1, const char *str2);

int strlen(const char *str);

char *substr(const char *str, int start, int end);
/******** End *********/

#endif
```

### my_string.cpp

```cpp
#include "my_string.h"

/*** Your code here ***/
char* strcpy(char *dest, const char *src) {
    int i = 0;
    while (*(src + i)) {
        *(dest + i) = *(src + i);
        i++;
    }
    *(dest + i) = '\0';
    return dest;
}

char* strcat(char *dest, const char *src) {
    int i = 0, j = 0;
    while (*(dest + i)) i++;
    while (*(src + j)) {
        *(dest + i) = *(src + j);
        i++;
        j++;
    }
    *(dest + i) = '\0';
    return dest;
}

int strcmp(const char *str1, const char *str2) {
    for (int i = 0; *(str1 + i) && *(str2 + i); i++) {
        if (*(str1 + i) < *(str2 + i)) {
            return -1;
        }
        if (*(str1 + i) > *(str2 + i)) {
            return 1;
        }
    }
    return 0;
}

int strlen(const char *str) {
    int i = 0;
    while (*(str + i)) i++;
    return i;
}

char *substr(const char *str, int start, int end) {
    int len = 0;
    while (*(str + len)) len++;
    if (end > len) end = len;
    char *ans = new char[end - start + 1] {};
    for (int i = start; i < end; i++) {
        *(ans + i - start) = *(str + i);
    }
    return ans;
}
/******** End *********/
```

## 第2关：海龟绘图（一）

```cpp
#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    /*** Your code here ***/
    int m, n;
    int r, c;
    bool running = true;
    cin >> m >> n;
    cin >> r >> c;
    char cmd;
    int step;
    while(running) {
        cin >> cmd >> step;
        switch(cmd) {
        case 'U':
            r = r-step < 0 ? 0 : r-step;
            break;
        case 'D':
            r = r+step > m-1 ? m-1 : r+step;
            break;
        case 'L':
            c = c-step < 0 ? 0 : c-step;
            break;
        case 'R':
            c = c+step > n-1 ? n-1 : c+step;
            break;
        default:
            running = false;
        }
    }
    cout << r << ' ' << c;
    /******** End *********/
    return 0;
}
```

## 第3关：海龟绘图（二）

### 写法一
```cpp
#include <iostream>

using namespace std;

/*** Your code here ***/
class Turtle {
    bool hourse[40][40]{};
    int m;
    int n;
    int dm[4] = { -1, 0, 1, 0 };
    int dn[4] = { 0, 1, 0, -1 };
    int dir;
    int r, c;
public:
    Turtle(int _m, int _n, int _r, int _c) {
        m = _m;
        n = _n;
        dir = 0;
        r = _r;
        c = _c;
        hourse[r][c] = 1;
    }
    void turnL() {
        dir = (dir + 3) % 4;
    }
    void turnR() {
        dir = (dir + 1) % 4;
    }
    void forWard(int step) {
        int tmpr, tmpc;
        for (int i = 0; i < step; i++) {
            tmpr = r + dm[dir];
            if (tmpr > m - 1) {
                r = m - 1;
            }
            else if (tmpr < 0) {
                r = 0;
            }
            else {
                r = tmpr;
            }

            tmpc = c + dn[dir];
            if (tmpc > n - 1) {
                c = n - 1;
            }
            else if (tmpc < 0) {
                c = 0;
            }
            else {
                c = tmpc;
            }

            hourse[r][c] = 1;
        }
    }

    void print() {
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                //cout << (hourse[i][j] ? '*':' ');
                if (hourse[i][j]) {
                    cout << '*';
                }
                else {
                    cout << ' ';
                }
            }
            cout << endl;
        }
    }

};

int main() {
    int m, n;
    int r, c;
    cin >> m >> n;
    cin >> r >> c;
    Turtle turtle(m, n, r, c);
    bool running = true;
    char cmd;
    int step;
    while (running) {
        cin >> cmd;
        switch (cmd) {
        case 'F':
            cin >> step;
            turtle.forWard(step);
            break;
        case 'L':
            turtle.turnL();
            break;
        case 'R':
            turtle.turnR();
            break;
        default:
            running = false;
        }
    }
    turtle.print();
    return 0;
}
/******** End *********/
```

### 写法二

```cpp
#include <iostream>

using namespace std;

/*** Your code here ***/

bool mask[100][100] {};

char changeOrient(char head, char orient) {
    if (head == 'U') {
        return orient == 'L' ? 'L' : 'R';
    } else if (head == 'D') {
        return orient == 'L' ? 'R' : 'L';
    } else if (head == 'L') {
        return orient == 'L' ? 'D' : 'U';
    } else {
        return orient == 'L' ? 'U' : 'D';
    }
}

void forward(int m, int n, int &i, int &j, char orient, int step) {
    if (orient == 'U') {
        while (step > 0 && i > 0) {
            mask[i--][j] = true;
            step--;
        }
    } else if (orient == 'D') {
        while (step > 0 && i < m - 1) {
            mask[i++][j] = true;
            step--;
        }
    } else if (orient == 'L') {
        while (step > 0 && j > 0) {
            mask[i][j--] = true;
            step--;
        }
    } else {
        while (step > 0 && j < n - 1) {
            mask[i][j++] = true;
            step--;
        }
    }
}

void showTrack(int m, int n) {
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (mask[i][j]) cout << "*";
            else cout << " ";
        }
        cout << endl;
    }
}

int main(int argc, char const *argv[])
{
    int m, n, i, j;
    cin >> m >> n >> i >> j;
    char head = 'U', action;
    int step;
    while (true) {
        cin >> action;
        if (action == 'F') {
            cin >> step;
            forward(m, n, i, j, head, step);
        } else if (action == 'E') {
            break;
        } else {
            head = changeOrient(head, action);
        }
    }
    mask[i][j] = true;
    showTrack(m, n);
    return 0;
}
/******** End *********/
```
