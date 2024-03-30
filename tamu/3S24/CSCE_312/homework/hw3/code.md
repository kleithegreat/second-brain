## 3.5
```c
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
`%rbx` holds $p$ and `%rdx` holds $q$.
Instruction | Result
--- | ---
`leaq 9(%rdx), %rax` | `%rax` $\leftarrow q + 9$
`leaq (%rdx, %rbx), %rax` | `%rax` $\leftarrow q + p$
`leaq (%rdx, %rbx, 3), %rax` | `%rax` $\leftarrow 3p + q$
`leaq 2(%rbx, %rbx, 7), %rax` | `%rax` $\leftarrow 7p + p + 2$
`leaq 0xE(,%rdx, 3), %rax` | `%rax` $\leftarrow 3q + 14$
`leaq 6(%rbx, %rdx, 7), %rax` | `%rax` $\leftarrow 7q + p + 6$
## 3.7
```asm
# short scale3(short x, short y, short z)
# x in %rdi, y in %rsi, z in %rdx
scale3:
    leaq (%rsi, %rsi, 9), %rbx       # rbx = 9y + y = 10y
    leaq (%rbx, %rdx), %rbx          # rbx = z + rbx = z + 10y
    leaq (%rbx, %rdi, %rsi), %rbx    # rbx = xy + rbx = xy + z + 10y
    ret
```
```c
short scale3(short x, short y, short z) {
    short t = x * y + z + 10 * y;
    return t;
}
```
## 3.8
Initial values:
Address | Value | Register | Value
--- | --- | --- | ---
`0x100` | 0xFF | `%rax` | 0x100
`0x108` | 0xAB | `%rcx` | 0x1
`0x110` | 0x13 | `%rdx` | 0x3
`0x118` | 0x11

Effects of the instructions:
Instruction | Destination | Value
--- | --- | ---
`addq %rcx, (%rax)` | $M[0x100]$ | 0x1
`subq %rdx, 8(%rax)` | $M[0x108]$ | 0xA8
`imulq $16, (%rax, %rdx, 8)` | $M[0x118]$ | 0x110
`incq 16(%rax)` | $M[0x110]$ | 0x14
`decq %rcx` | `%rcx` | 0x0
`subq %rdx, %rax` | `%rax` | 0xFD
## 3.18
```c
short test(short x, short y, short z) {
    short val = y + z - x;
    if (z > 5) {
        if (y > 2)
            val = x / z;
        else
            val = x / y;
    } else if (z < 3)
        val = z / y;
    return val;
}
```
## 3.20
```c
#define OP /* unknown operator */

short arith(short x) {
    return x OP 16;
}
```
```asm
# x in %rdi
arith:
    leaq 15(%rdi), %rax
    testq %rdi, %rdi
    cmovns %rdi, %rbx
    sarq $4, %rbx
    ret
```
## 3.24
## 3.25
## 3.32
## 3.35
## 3.37
## 3.38
## 3.41