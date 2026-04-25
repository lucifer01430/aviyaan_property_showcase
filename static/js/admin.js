document.addEventListener("DOMContentLoaded", () => {
    const revealItems = document.querySelectorAll("[data-reveal]");
    const sidebar = document.getElementById("adminSidebar");

    if (!("IntersectionObserver" in window) || !revealItems.length) {
        revealItems.forEach((item) => item.classList.add("is-visible"));
    } else {
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
                threshold: 0.1,
                rootMargin: "0px 0px -8% 0px",
            }
        );

        revealItems.forEach((item) => revealObserver.observe(item));
    }

    if (!sidebar || typeof bootstrap === "undefined") {
        return;
    }

    const links = sidebar.querySelectorAll(".admin-nav-link");
    links.forEach((link) => {
        link.addEventListener("click", () => {
            if (window.innerWidth >= 992) {
                return;
            }

            const offcanvas = bootstrap.Offcanvas.getInstance(sidebar);
            if (offcanvas) {
                offcanvas.hide();
            }
        });
    });
});
