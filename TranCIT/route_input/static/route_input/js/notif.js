function showNotification(message, duration = 3000) {
    let notification = document.getElementById('customNotification');
    
    if (!notification) {
        notification = document.createElement('div');
        notification.id = 'customNotification';
        notification.className = 'custom-notification';
        document.body.appendChild(notification);
    }

    notification.textContent = message;
    notification.classList.add('show');
    
    setTimeout(() => {
        notification.classList.remove('show');
    }, duration);
}