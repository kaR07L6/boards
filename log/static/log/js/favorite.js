<script>
    window.onload = function() {
        const starButtons = document.querySelectorAll('.star-btn');
        
        starButtons.forEach(button => {
            const boardId = button.getAttribute('data-board-id');
            
            // localStorageに保存された状態を確認
            const isFavorite = localStorage.getItem('favorite-' + boardId);
            if (isFavorite === 'true') {
                button.classList.add('filled'); // 塗りつぶし
            }
            
            // クリックイベント
            button.addEventListener('click', function() {
                // 状態をトグル（切り替え）
                if (button.classList.contains('filled')) {
                    button.classList.remove('filled');
                    localStorage.setItem('favorite-' + boardId, 'false'); // ステータスを更新
                } else {
                    button.classList.add('filled');
                    localStorage.setItem('favorite-' + boardId, 'true'); // ステータスを更新
                }
            });
        });
    };
</script>
