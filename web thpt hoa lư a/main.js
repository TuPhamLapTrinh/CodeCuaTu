// Xử lý form đăng nhập
document.getElementById('login-form').addEventListener('submit', function(e) {
    e.preventDefault(); // Ngăn gửi form mặc định

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Giả định kiểm tra thông tin đăng nhập
    if (username === 'admin' && password === '123456') {
        alert('Đăng nhập thành công!');
        // Chuyển hướng đến trang chính hoặc thực hiện hành động khác
    } else {
        alert('Tài khoản hoặc mật khẩu không đúng. Vui lòng thử lại.');
    }

    // Reset form sau khi xử lý
    this.reset();
});
// Khởi tạo hiệu ứng AOS (Animate on Scroll)
document.addEventListener('DOMContentLoaded', function() {
    AOS.init({
        duration: 1000,  // Thời gian thực hiện animation
        once: true,      // Chỉ thực hiện hiệu ứng một lần khi cuộn trang
    });
});

// Preloader Animation
window.addEventListener('load', function() {
    const preloader = document.getElementById('preloader');
    preloader.style.display = 'none';
});

// Sticky Navigation
window.addEventListener('scroll', function() {
    const navbar = document.querySelector('nav');
    if (window.pageYOffset > 100) {
        navbar.classList.add('sticky');
    } else {
        navbar.classList.remove('sticky');
    }
});

// Modal Popup for News Details
const modal = document.querySelector('.modal');
const closeModalButton = document.querySelector('.modal .close');
const newsArticles = document.querySelectorAll('.news-grid article');

newsArticles.forEach(article => {
    article.addEventListener('click', function() {
        modal.style.display = 'flex';
        // Giả định dữ liệu tin tức được load qua AJAX hoặc API
        const modalContent = modal.querySelector('.modal-content');
        modalContent.innerHTML = `
            <h3>${article.querySelector('h3').textContent}</h3>
            <p>${article.querySelector('p').textContent}</p>
        `;
    });
});

// Đóng modal khi click vào nút X
closeModalButton.addEventListener('click', function() {
    modal.style.display = 'none';
});

// Đóng modal khi click ra ngoài vùng nội dung
window.addEventListener('click', function(e) {
    if (e.target === modal) {
        modal.style.display = 'none';
    }
});

// Lazy-load cho iframe (Google Maps)
document.addEventListener('DOMContentLoaded', function() {
    const mapIframe = document.querySelector('.map iframe');
    const lazyLoadMap = () => {
        if ('IntersectionObserver' in window) {
            const observer = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        mapIframe.src = mapIframe.dataset.src;
                        observer.disconnect();
                    }
                });
            });
            observer.observe(mapIframe);
        } else {
            // Trường hợp không hỗ trợ IntersectionObserver
            mapIframe.src = mapIframe.dataset.src;
        }
    };
    lazyLoadMap();
});

// Form Validation for Contact Form
document.querySelector('.contact-form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;

    // Kiểm tra định dạng email
    const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;

    if (name === '' || email === '' || message === '') {
        alert('Vui lòng điền đầy đủ thông tin.');
    } else if (!emailPattern.test(email)) {
        alert('Email không hợp lệ.');
    } else {
        alert('Gửi liên hệ thành công!');
        // Xử lý gửi form (giả định)
        this.reset();
    }
});

// Hiệu ứng scroll về đầu trang
const scrollToTopButton = document.createElement('button');
scrollToTopButton.textContent = '▲';
scrollToTopButton.classList.add('scroll-to-top');
document.body.appendChild(scrollToTopButton);

window.addEventListener('scroll', () => {
    if (window.pageYOffset > 200) {
        scrollToTopButton.classList.add('visible');
    } else {
        scrollToTopButton.classList.remove('visible');
    }
});

scrollToTopButton.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
});

// Progressive Web App (PWA) - Service Worker
if ('serviceWorker' in navigator) {
    window.addEventListener('load', function() {
        navigator.serviceWorker.register('/service-worker.js').then(function(registration) {
            console.log('Service Worker registered with scope:', registration.scope);
        }, function(err) {
            console.log('Service Worker registration failed:', err);
        });
    });
}