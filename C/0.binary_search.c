#include <stdio.h>

/*
 * iterative_binary_search - Binary search with while loop.
 * @arr: sorted array to search
 * @targ: element to find
 * @r: array last index
 * Return; index of element if found else -1
 */
int iterative_binary_search(int arr[], int targ, int l, int r);
int recursive_binary_search(int arr[], int targ, int l, int r);


int main(void) {
    int arr[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
    int targ = 23;
    int r = sizeof(arr) / sizeof(arr[0]);
    int l = 0;

    int idx = iterative_binary_search(arr, targ, l, r);
    int ridx = recursive_binary_search(arr, targ, l, r);

    if (idx == -1 || ridx == -1)
        printf("%d\n", 404);
    else 
        printf("Found at %d %d\n", idx, ridx);
    return (1);
}

int iterative_binary_search(int arr[], int targ, int l, int r) {
    int m;

    while (l <= r) {
        m = (int) (l + r) / 2;

        if (arr[m] == targ)
            return (m);

        else if (arr[m] > targ)
            r = m - 1;

        else
            l = m + 1;
    }
    return (-1);
}

int recursive_binary_search(int arr[], int targ, int l, int r) {
    int m = (l + r) / 2;

    if (arr[m] == targ)
        return m;

    else if (arr[m] < targ) {
        l = m + 1;
        return recursive_binary_search(arr, targ, l, r);
    }
    else if (arr[m] > targ) {
        r = m - 1;
        return recursive_binary_search(arr, targ, l, r);
    }
    else
        return (-1);
}
