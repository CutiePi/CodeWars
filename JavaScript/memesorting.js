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
