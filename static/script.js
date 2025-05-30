function togglePassword() {
    const passwordInput = document.getElementById('password');
    const icon = document.getElementById('togglePassword');

    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
        icon.src = 'static/assets/eye-close.png';
    } else {
        passwordInput.type = 'password';
        icon.src = 'static/assets/eye-open.png';
    }
}
