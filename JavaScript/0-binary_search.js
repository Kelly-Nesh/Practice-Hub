/* Binary seach in javascript */

const arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91];
const targ = 38;


function iterative_binary_search(arr, targ) {
    let m;
    let l = 0;
    let r = arr.length - 1;

    while (l <= r) {
        m = parseInt((l + r) / 2);

        console.log(l, r,m, arr[m]);
        if (arr[m] === targ)
            return m;

        else if (arr[m] > targ)
            r = m - 1;

        else
            l = m + 1;
    }
    return -1;
}

const idx = iterative_binary_search(arr, targ);
if (idx == -1)
    console.log(404);
else
    console.log("Found at ", idx);
