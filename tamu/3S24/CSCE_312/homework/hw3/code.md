## 3.5
```cpp
void decode1(long *xp, long *yp, long *zp) {
    // xp in %rdi, yp in %rsi, zp in %rdx
    long x = *xp;
    long y = *yp;
    long z = *zp;

    *yp = x;
    *zp = y;
    *xp = z;

    return;
}
```
## 3.6
Instruction | Result
--- | ---
leaq 9(%rdx), %rax | 
leaq (%rdx, %rbx), %rax | 
leaq (%rdx, %rbx, 3), %rax | 
leaq 2(%rbx, %rbx, 7), %rax | 
leaq 0xE(,%rdx, 3), %rax | 
leaq 6(%rbx, %rdx, 7), %rax | 