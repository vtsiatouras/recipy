export function smoothToTop(){
    const c = document.documentElement.scrollTop || document.body.scrollTop;
    if (c > 0) {
        window.requestAnimationFrame(smoothToTop);
        window.scrollTo(0, c - c / 8);
    }
}
