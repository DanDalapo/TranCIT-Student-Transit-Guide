document.addEventListener('DOMContentLoaded', function() {
    const authWrapper = document.getElementById('authWrapper');
    
    // Buttons that trigger the animation
    const showRegisterBtn = document.getElementById('showRegister');
    const showLoginBtn = document.getElementById('showLogin');
    const mobileShowRegisterBtn = document.getElementById('mobileShowRegister');
    const mobileShowLoginBtn = document.getElementById('mobileShowLogin');

    // Function to clear messages and reset form inputs
    function clearOppositeForm(isGoingToRegister) {
        let formToClear, messagesToClear;
        if (isGoingToRegister) {
            formToClear = document.querySelector('.login-panel form');
            messagesToClear = document.querySelector('.login-panel .form-messages');
        } else {
            formToClear = document.querySelector('.register-panel form');
            messagesToClear = document.querySelector('.register-panel .form-messages');
        }
        if (formToClear) formToClear.reset();
        if (messagesToClear) messagesToClear.innerHTML = '';
        
        const inputs = document.querySelectorAll('input[required]');
        inputs.forEach(input => {
            input.style.borderColor = '#ddd';
        });
    }

    // --- Event Listeners ---
    const addActive = () => {
        clearOppositeForm(true);
        authWrapper.classList.add('register-active');
    };
    
    const removeActive = () => {
        clearOppositeForm(false);
        authWrapper.classList.remove('register-active');
    };

    if (showRegisterBtn) showRegisterBtn.addEventListener('click', addActive);
    if (mobileShowRegisterBtn) mobileShowRegisterBtn.addEventListener('click', (e) => {
        e.preventDefault();
        addActive();
    });
    
    if (showLoginBtn) showLoginBtn.addEventListener('click', removeActive);
    if (mobileShowLoginBtn) mobileShowLoginBtn.addEventListener('click', (e) => {
        e.preventDefault();
        removeActive();
    });

    // --- Form Validation Styling ---
    const inputs = document.querySelectorAll('input[required]');
    inputs.forEach(function(input) {
        input.addEventListener('focus', function() {
            this.style.borderColor = '#4CAF50';
        });
        input.addEventListener('blur', function() {
            if (!this.value.trim()) {
                this.style.borderColor = '#dc3545';
            } else {
                this.style.borderColor = '#ddd';
            }
        });
    });
});