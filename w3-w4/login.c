#include <stdio.h>
#include <string.h>

int main() {
    char username[20];
    char password[20];
    int attempts = 3;

    while (attempts > 0) {
        printf("=== LOGIN SISTEM ===\n");

        printf("Username: ");
        fgets(username, sizeof(username), stdin);

        printf("Password: ");
        fgets(password, sizeof(password), stdin);

        // Menghapus newline dari fgets
        username[strcspn(username, "\n")] = 0;
        password[strcspn(password, "\n")] = 0;

        if (strcmp(username, "admin") == 0 && strcmp(password, "123") == 0) {
            printf("\nLogin berhasil!\n");
            return 0;
        } else {
            attempts--;
            printf("\nLogin gagal! Sisa percobaan: %d\n\n", attempts);
        }
    }

    printf("Akun diblokir karena terlalu banyak percobaan gagal.\n");

    return 0;
}