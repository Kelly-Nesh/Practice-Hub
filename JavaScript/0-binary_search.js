/* Binary seach in javascript */

const arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91];
const targ = 38;


function iterative_binary_search(arr, targ, l, r) {
    let m;

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

function recursive_binary_search(arr, targ, l, r) {
    const m = Math.floor((l + r) - 1)

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
        return -1;
}

let l = 0;
let r = arr.length - 1;

const idx = iterative_binary_search(arr, targ, l, r);
const ridx = recursive_binary_search(arr, targ, l, r);

if (idx == -1 || ridx == -1)
    console.log(404);
else
    console.log("Found at ", idx, ridx);
