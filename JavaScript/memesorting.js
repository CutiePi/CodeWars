const memesorting = (meme) => {
    const memers = ['Roma','Maxim', 'Danik'];
    let r = 'Vlad';

    const bugr = /b.*?u.*?g/;
    const boomr = /b.*?o.*?o.*?m/;
    const editsr = /e.*?d.*?i.*?t.*?s/;
    const m = meme.toLowerCase();


    let ir = Number.MAX_SAFE_INTEGER;

    [m.match(bugr),m.match(boomr), m.match(editsr)].forEach((match, i) => {
        if((match && (match.index + match[0].length)  < (ir))){
            ir = match.index + match[0].length;
            r = memers[i];
        }
    })

    return r;
}

/**
 * # Problem for the week of April 22nd
 *
 * [Meme sorting](https://www.codewars.com/kata/5b6183066d0db7bfac0000bb) (codewards kata level 6 kyu)
 *
 * ## Description
 *
 * Roma is programmer and he likes memes about IT,
 * Maxim is chemist and he likes memes about chemistry,
 * Danik is designer and he likes memes about design,
 * and Vlad likes all other memes.
 *
 * You will be given a meme (string), and your task is to identify its category, and send it to the right receiver: IT - 'Roma', chemistry - 'Maxim', design - 'Danik', or other - 'Vlad'.
 *
 * IT meme has letters b, u, g.
 * Chemistry meme has letters b, o, o, m.
 * Design meme has letters e, d, i, t, s.
 * If there is more than 1 possible answer, the earliest match should be chosen.
 *
 * Note: letters are case-insensetive and should come in the order specified above.
 *
 * ### Examples:
 *
 * (Matching letters are surrounded by curly braces for readability.)
 *
 * this is programmer meme {b}ecause it has b{ug}
 * this is also program{bu}r meme {g}ecause it has needed key word
 * this is {ed}s{i}gner meme cause i{t} ha{s} key word
 *
 * this could {b}e chemistry meme b{u}t our{g}Gey word 'boom' is too late
 *     instead of
 * this could {b}e chemistry meme but {o}ur gey w{o}rd 'boo{m}' is too late
 */
