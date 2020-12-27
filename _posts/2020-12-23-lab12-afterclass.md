---
layout: post
filename: 2020-12-23-lab12-afterclass
title: Lab12 After Class
date: 2020-12-23 00:00:00 +0800
categories: post
tags:
  - CS171
  - Lab
mathjax: false
---

## 第1关：有理数四则运算

```cpp
struct Rational {
    int num; // 分子
    int den; // 分母
};

/*** Your code here ***/
Rational add(const Rational &x, const Rational &y) {
    return Rational {
        .num = x.num * y.den + x.den * y.num,
        .den = x.den * y.den
    };
}

Rational sub(const Rational &x, const Rational &y) {
    return Rational {
        .num = x.num * y.den - x.den * y.num,
        .den = x.den * y.den
    };
}

Rational mul(const Rational &x, const Rational &y) {
    return Rational {
        .num = x.num * y.num,
        .den = x.den * y.den
    };
}

Rational div(const Rational &x, const Rational &y) {
    return Rational {
        .num = x.num * y.den,
        .den = x.den * y.num
    };
}
/******** End *********/
```

## 第2关：银行账户

```cpp
struct Account {
    char *password;  // 密码
    int balance; // 余额
};

/*** Your code here ***/
bool strEqual(const char *s1, const char *s2) {
    return *s1 == '\0' && *s2 == '\0' ? true : *s1 == *s2 && strEqual(s1 + 1, s2 + 1);
}

Account initAccount(char *password, int balance) {
    return Account {
        .password = password,
        .balance = balance
    };
}

int withdraw(Account &account, char *password, int amount) {
    if (!strEqual(password, account.password)) {
        return -1;
    }
    if (amount > account.balance) {
        return -1;
    } else {
        account.balance -= amount;
        return account.balance;
    }
}

int deposit(Account &account, char *password, int amount) {
    if (!strEqual(password, account.password)) {
        return -1;
    }
    account.balance += amount;
    return account.balance;
}
/******** End *********/
```

## 第3关：成绩单

```cpp
#include <iostream>
#include <algorithm>

using namespace std;

/*** Your code here ***/
struct Transcript {
    int math;
    int english;
    int cpp;
    int total;
};

bool compareM(const Transcript &a, const Transcript &b);
bool compareE(const Transcript &a, const Transcript &b);
bool compareC(const Transcript &a, const Transcript &b);
bool compareT(const Transcript &a, const Transcript &b);
/******** End *********/

int main(int argc, char const *argv[])
{
    /*** Your code here ***/
    int n;
    cin >> n;
    Transcript *p = new Transcript[n];
    for (int i = 0; i < n; i++) {
        cin >> p[i].math;
        cin >> p[i].english;
        cin >> p[i].cpp;
        p[i].total = p[i].math + p[i].english + p[i].cpp;
    }
    char c;
    int k;
    while (true) {
        cin >> c >> k;
        if (c == 'S' && k == 0) {
            break;
        }
        if (c == 'M') {
            sort(p, p + n, compareM);
            cout << p[k - 1].math << endl;
        } else if (c == 'E') {
            sort(p, p + n, compareE);
            cout << p[k - 1].english << endl;
        } else if (c == 'C') {
            sort(p, p + n, compareC);
            cout << p[k - 1].cpp << endl;
        } else if (c == 'T') {
            sort(p, p + n, compareT);
            cout << p[k - 1].total << endl;
        }
    }
    /******** End *********/
    return 0;
}

/*** Your code here ***/
bool compareM(const Transcript &a, const Transcript &b) {
    return a.math > b.math;
}

bool compareE(const Transcript &a, const Transcript &b) {
    return a.english > b.english;
}

bool compareC(const Transcript &a, const Transcript &b) {
    return a.cpp > b.cpp;
}

bool compareT(const Transcript &a, const Transcript &b) {
    return a.total > b.total;
}
/******** End *********/
```

## 第4关：生命游戏

```cpp
#include <iostream>

using namespace std;

struct Panel {
    int row;
    int col;
    bool status[30][30];
};

/*** Your code here ***/
bool getStatus(const Panel &panel, int i, int j) {
    if (i >= 0 && i < panel.row && j >= 0 && j < panel.col) {
        return panel.status[i][j];
    }
    return 0;
}

int getAroundAlives(const Panel &panel, int i, int j) {
    int count = 0;
    for (int m = i - 1; m <= i + 1; m++) {
        for (int n = j - 1; n <= j + 1; n++) {
            count += getStatus(panel, m, n);
        }
    }
    count -= getStatus(panel, i, j);
    return count;
}

void updateStatus(Panel &panel) {
    bool updated[30][30] {};
    for (int i = 0; i < panel.row; i++) {
        for (int j = 0; j < panel.col; j++) {
            int count = getAroundAlives(panel, i, j);
            if (getStatus(panel, i, j)) {
                if (count < 2) {
                    updated[i][j] = 0;
                } else if (count < 4) {
                    updated[i][j] = 1;
                } else {
                    updated[i][j] = 0;
                }
            } else {
                if (count == 3) {
                    updated[i][j] = 1;
                } else {
                    updated[i][j] = 0;
                }
            }
        }
    }
    for (int i = 0; i < panel.row; i++) {
        for (int j = 0; j < panel.col; j++) {
            panel.status[i][j] = updated[i][j];
        }
    }
}

void showStatus(const Panel &panel) {
    for (int i = 0; i < panel.row; i++) {
        for (int j = 0; j < panel.col; j++) {
            cout << panel.status[i][j];
            if (j < panel.col - 1) {
                cout << " ";
            }
        }
        cout << endl;
    }
}
/******** End *********/
```

## 第5关：通讯录结构体

```cpp
#include <iostream>
#include <algorithm>

using namespace std;

/*** Your code here ***/
struct Birth {
    int year;
    int month;
    int day;
};

struct Contact {
    char *name;
    Birth birth;
    char *phone;
    char *address;
};

bool compare(const Contact &c1, const Contact &c2) {
    if (c1.birth.year == c2.birth.year) {
        if (c1.birth.month == c2.birth.month) {
            return c1.birth.day > c2.birth.day;
        } else {
            return c1.birth.month > c2.birth.month;
        }
    } else {
        return c1.birth.year > c2.birth.year;
    }
}
/******** End *********/

int main(int argc, char const *argv[])
{
    /*** Your code here ***/
    int n;
    cin >> n;
    Contact *contact = new Contact[n];
    for (int i = 0; i < n; i++) {
        contact[i].name = new char[21] {};
        cin >> contact[i].name;
        cin >> contact[i].birth.year >> contact[i].birth.month >> contact[i].birth.day;
        contact[i].phone = new char[12] {};
        cin >> contact[i].phone;
        contact[i].address = new char[51] {};
        cin.get();
        cin.getline(contact[i].address, 51);
    }
    sort(contact, contact + n, compare);
    
    for (int i = 0; i < n; i++) {
        cout << contact[i].name << " ";
        cout << contact[i].birth.year << " " << contact[i].birth.month << " " << contact[i].birth.day << " ";
        cout << contact[i].phone << " ";
        cout << contact[i].address << endl;
    }
    /******** End *********/
    return 0;
}
```