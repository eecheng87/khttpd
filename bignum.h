#include <linux/kernel.h>
#include <linux/string.h>
#define MAXDIGITS 100 /* maximum length bignum */
#define PLUS 1        /* positive sign bit */
#define MINUS -1      /* negative sign bit */

typedef struct {
    char digits[MAXDIGITS]; /* represent the number */
    int signbit;            /* 1 if positive, -1 if negative */
    int lastdigit;          /* index of high-order digit */
} bignum;
void print_bignum(bignum *n);
void int_to_bignum(int s, bignum *n);
void initialize_bignum(bignum *n);
int add_bignum(bignum *a, bignum *b, bignum *c);
int subtract_bignum(bignum *a, bignum *b, bignum *c);
// zero_justify(bignum *n);
int compare_bignum(bignum *a, bignum *b);
void multiply_bignum(bignum *a, bignum *b, bignum *c);
void copy(bignum *a, bignum *b);
