function main() {
    let footer = document.querySelector('.footer')

    const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        let ratio = Math.min(1, Math.max(0, entry.intersectionRatio));
        footer.style.setProperty('--opacity-footer-after-before', ratio.toFixed(2));
        if (ratio != 0) {
            footer.style.setProperty('--visibility-footer-arter-before', 'visible')
        } else {
            footer.style.setProperty('--visibility-footer-arter-before', 'hidden')
        }
    });
    }, {
        threshold: Array.from({ length: 101 }, (_, i) => i / 100)
    });

    observer.observe(footer);
}

main()