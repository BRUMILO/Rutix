document.addEventListener('DOMContentLoaded', function() {
    const flashAlerts = document.querySelectorAll('.flash-alert');
    
    flashAlerts.forEach(function(alert) {
        setTimeout(function() {
            alert.classList.add('fade-out');
            setTimeout(function() {
                if (alert.parentNode) {
                    alert.parentNode.removeChild(alert);
                }
            }, 500);
        }, 5000);
        
        const closeButton = alert.querySelector('.close');
        if (closeButton) {
            closeButton.addEventListener('click', function() {
                alert.classList.add('fade-out');
                setTimeout(function() {
                    if (alert.parentNode) {
                        alert.parentNode.removeChild(alert);
                    }
                }, 500);
            });
        }
    });
});