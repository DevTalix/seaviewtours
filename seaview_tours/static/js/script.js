/* ======================================================
   GLOBAL HELPERS
====================================================== */
function $(selector, scope = document) {
    return scope.querySelector(selector);
}

function $all(selector, scope = document) {
    return scope.querySelectorAll(selector);
}

/* ======================================================
   MOBILE NAV MODULE
====================================================== */
function initMobileNav() {
    const hamburger = $('#hamburger');
    const nav = $('.nav');
    const overlay = $('#navOverlay');

    if (!hamburger || !nav || !overlay) return;

    function openMenu() {
        nav.classList.add('active');
        overlay.classList.add('active');
        document.body.style.overflow = 'hidden';
    }

    function closeMenu() {
        nav.classList.remove('active');
        overlay.classList.remove('active');
        document.body.style.overflow = '';
    }

    hamburger.addEventListener('click', (e) => {
        e.stopPropagation();
        nav.classList.contains('active') ? closeMenu() : openMenu();
    });

    overlay.addEventListener('click', closeMenu);

    $all('a', nav).forEach(link =>
        link.addEventListener('click', closeMenu)
    );
}

/* ======================================================
   FORMS MODULE
====================================================== */
function initForms() {

    // Booking Form
    const bookingForm = $('#simpleBookingForm');
    if (bookingForm) {
        bookingForm.addEventListener('submit', (e) => {
            e.preventDefault();
            console.log('Booking form submitted');
        });
    }

    // Contact Form
    const contactForm = $('#contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            console.log('Contact form submitted');
        });
    }
}

/* ======================================================
   SMOOTH SCROLL (ANCHOR LINKS)
====================================================== */
function initSmoothScroll() {
    $all('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const target = $(this.getAttribute('href'));
            if (!target) return;

            e.preventDefault();
            target.scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
}

/* ======================================================
   HEADER SCROLL EFFECT
====================================================== */
function initHeaderScroll() {
    const header = $('header');
    if (!header) return;

    window.addEventListener('scroll', () => {
        header.classList.toggle('scrolled', window.scrollY > 50);
    });
}

/* ======================================================
   FAQ / ACCORDION MODULE
====================================================== */
function initAccordions() {
    $all('.accordion-header').forEach(header => {
        header.addEventListener('click', () => {
            header.classList.toggle('active');
            const content = header.nextElementSibling;
            if (content) {
                content.style.maxHeight =
                    content.style.maxHeight ? null : content.scrollHeight + 'px';
            }
        });
    });
}

/* ======================================================
   MODALS (OPTIONAL)
====================================================== */
function initModals() {
    $all('[data-modal-open]').forEach(btn => {
        const targetId = btn.getAttribute('data-modal-open');
        const modal = $('#' + targetId);
        if (!modal) return;

        btn.addEventListener('click', () => {
            modal.classList.add('active');
            document.body.style.overflow = 'hidden';
        });
    });

    $all('[data-modal-close]').forEach(btn => {
        const modal = btn.closest('.modal');
        if (!modal) return;

        btn.addEventListener('click', () => {
            modal.classList.remove('active');
            document.body.style.overflow = '';
        });
    });
}

/* ======================================================
   ANIMATE ON SCROLL (LIGHTWEIGHT)
====================================================== */
function initScrollAnimations() {
    const items = $all('[data-animate]');
    if (!items.length) return;

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animated');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.2 });

    items.forEach(item => observer.observe(item));
}

/* ======================================================
   INIT EVERYTHING SAFELY
====================================================== */
document.addEventListener('DOMContentLoaded', () => {
    initMobileNav();
    initForms();
    initSmoothScroll();
    initHeaderScroll();
    initAccordions();
    initModals();
    initScrollAnimations();
});
if ('requestIdleCallback' in window) {
    window.requestIdleCallback(() => {
        // Load non-critical resources
    });
}
// script.js - optimized
document.addEventListener('DOMContentLoaded', function() {
    // Lazy load non-critical resources
    if ('requestIdleCallback' in window) {
        requestIdleCallback(loadNonCriticalResources);
    } else {
        setTimeout(loadNonCriticalResources, 3000);
    }
});

function loadNonCriticalResources() {
    // Load Font Awesome only when needed
    const fa = document.createElement('link');
    fa.rel = 'stylesheet';
    fa.href = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css';
    document.head.appendChild(fa);
}
// Add to your script.js for extra security
function sanitizeInput(input) {
    if (!input) return '';
    return input
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#x27;')
        .replace(/\//g, '&#x2F;');
}

// Use in form submission
const nameInput = document.getElementById('name');
const safeName = nameInput ? sanitizeInput(nameInput.value) : '';