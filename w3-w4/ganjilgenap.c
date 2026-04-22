#include <stdio.h>

int main() {
    int angka;

    // Meminta input dari pengguna
    printf("Masukkan sebuah bilangan: ");
    scanf("%d", &angka);

    // Mengecek ganjil atau genap
    if (angka % 2 == 0) {
        printf("Bilangan %d adalah GENAP\n", angka);
    } else {
        printf("Bilangan %d adalah GANJIL\n", angka);
    }

    return 0;
}