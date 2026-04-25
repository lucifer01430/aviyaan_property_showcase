document.addEventListener("DOMContentLoaded", () => {
    const headerShell = document.querySelector(".site-header-shell");
    const revealItems = document.querySelectorAll("[data-reveal]");

    const syncHeader = () => {
        if (!headerShell) {
            return;
        }

        headerShell.classList.toggle("is-scrolled", window.scrollY > 12);
    };

    syncHeader();
    window.addEventListener("scroll", syncHeader, { passive: true });

    if (!("IntersectionObserver" in window) || !revealItems.length) {
        revealItems.forEach((item) => item.classList.add("is-visible"));
        return;
    }

    const revealObserver = new IntersectionObserver(
        (entries, observer) => {
            entries.forEach((entry) => {
                if (!entry.isIntersecting) {
                    return;
                }

                entry.target.classList.add("is-visible");
                observer.unobserve(entry.target);
            });
        },
        {
            threshold: 0.12,
            rootMargin: "0px 0px -8% 0px",
        }
    );

    revealItems.forEach((item) => revealObserver.observe(item));
});
