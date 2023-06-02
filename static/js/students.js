        function openSidebar() {
            document.getElementById('sidebar').style.width = '250px';
        }

        function closeSidebar() {
            document.getElementById('sidebar').style.width = '0';
        }

                window.addEventListener('DOMContentLoaded', (event) => {
            closeSidebar(); // Закрыть боковую панель при загрузке страницы
        });

        // Оставьте ваш JavaScript-код здесь