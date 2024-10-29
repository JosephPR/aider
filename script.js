// Form validation and submission handling
document.addEventListener('DOMContentLoaded', function() {
    // HubSpot forms are handled automatically, but you can add custom JavaScript here
    
    // Example: Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
});
