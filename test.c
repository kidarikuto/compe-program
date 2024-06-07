#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void sort_and_print_alternate(char *input) {
    int len = strlen(input);
    char *sorted = (char *)malloc(len + 1);
    strcpy(sorted, input);



    // シンプルなバブルソート
    for (int i = 0; i < len - 1; i++) {
        for (int j = 0; j < len - 1 - i; j++) {
            if (sorted[j] > sorted[j + 1]) {
                char temp = sorted[j];
                sorted[j] = sorted[j + 1];
                sorted[j + 1] = temp;
            }
        }
    }

    // 1個飛ばしで出力
    for (int i = 0; i < len; i += 2) {
        printf("%c", sorted[i]);
    }

    free(sorted);
}

int main() {
    char input[100];
    printf("文字列を入力してください: ");
    scanf("%99s", input);

    sort_and_print_alternate(input);

    return 0;
}
