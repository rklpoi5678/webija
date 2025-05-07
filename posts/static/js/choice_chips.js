document.addEventListener('DOMContentLoaded', function() {
    const chips = document.querySelectorAll('.choice-chips li');
    // 페이지 URL 쿼리 받기
    const params = new URLSearchParams(window.location.search);
    const order = params.get('order') || 'new'; // default 'new'
    
    // 칩스 active 클래스 추가 & 삭제
    chips.forEach(function(chip){
        if (chip.getAttribute('data-order') === order) {
            chip.classList.add('active');
        } else {
            chip.classList.remove('active');
        }
    });

    // click event
    chips.forEach(function(chip){
        chip.addEventListener('click', function(){
            const selectedOrder = chip.getAttribute('data-order');

            // URL Query params
            const newParams = new URLSearchParams(window.location.search);
            newParams.set('order', selectedOrder);
            window.location.search = newParams.toString();
        });
    });

    // post 로직
    document.getElementById('loadMore').addEventListener('click', function(){
        // displayedPost는 style 디스플레이가 아닌 것들, allPosts는 모든 포스트 클래스
        
        let displayedPost = document.querySelectorAll('.posts-grid .post:not([style*="display: none"])').length;
        let allPosts = document.querySelectorAll('.posts-grid .post');
    
        // next 10
        for (let i = displayedPost; i < displayedPost + 10 && i < allPosts.length; i++) {
            allPosts[i].style.display = 'block';
        }
    
        if (displayedPost + 10 >= 10){
            allPosts[9].style.opacity = '1';
        }
    
        if (displayedPost + 10 >= allPosts.length){
            document.getElementById('loadMore').style.display = 'none';
        }
    });

    // 라이트/다크 모드 토글 버튼 로직
        //document.getElementById('ligthSwBtn').addEventListener('click', function() {
        // var body = document.body;
        // var button = document.getElementById('ligthSwBtn');
        let isDark = false;
        
        document.getElementById('ligthSwBtn').addEventListener('click', function() {
            if (isDark) {
                this.innerHTML = '<i class="fas fa-sun" style="color: gold;"></i>'; // 다크 모드에서 라이트 모드로 전환
                document.body.classList.remove('dark-mode');
                document.body.classList.add('light-mode');
                isDark = false;
            } else {
                this.innerHTML = '<i class="fas fa-moon" style="color: gold;"></i>'; // 라이트 모드에서 다크 모드로 전환
                document.body.classList.remove('light-mode');
                document.body.classList.add('dark-mode');
                isDark = true;
            }
        });
        // if (body.classList.contains('dark-mode')) {
        //     body.classList.remove('dark-mode');
        //     body.classList.add('light-mode');
        //     button.textContent = '다크 모드'; // 버튼 텍스트 변경
        // } else { // 그렇지 않으면 다크 모드로 설정
        //     body.classList.remove('light-mode');
        //     body.classList.add('dark-mode');
        //     button.textContent = '라이트 모드'; // 버튼 텍스트 변경
        // }
    
});
