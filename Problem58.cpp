#include <iostream>
using namespace std;

bool isPrime(unsigned long n) {
    if (n <= 3) {
        return n >= 2;
    }
    if (n % 2 == 0 || n % 3 == 0) {
        return false;
    }
    for (int i = 5; i * i <= n; i += 6) {
        if (n % i == 0 ||  n % (i + 2) == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    int count = 0;
    int currInt = 1;
    int interval = 2;
    int num_diags = 1;
    int diag_primes = 0;
    while (diag_primes * 1.0 / num_diags > 0.10 || diag_primes == 0) {
        currInt += interval;
        num_diags += 1;
        if (isPrime(currInt)) {
            diag_primes += 1;
        }
        count = (count + 1) % 4;
        if (count == 0) {
            interval += 2;
        }
    }
    cout << interval+1 << "\n" << diag_primes << " / " << num_diags << "\n";
}
