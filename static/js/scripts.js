    /*!
* Start Bootstrap - Business Casual v7.0.9 (https://startbootstrap.com/theme/business-casual)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-business-casual/blob/master/LICENSE)
*/
// Highlights current date on contact page

// 회원가입 생년월일 창
window.addEventListener('DOMContentLoaded', event => {
    const listHoursArray = document.body.querySelectorAll('.list-hours li');
    listHoursArray[new Date().getDay()].classList.add(('today'));
})

document.getElementById('loginBtn').addEventListener('submit', function(){
    if (document.getElementById('emailBox').value == ''){
        alert('이메일을 입력하세요.');
    }
});

// 메뉴판 모달창
function openModal() {
    var modalContainer = document.querySelector('.modal-container');
    modalContainer.style.display = 'flex';
}

function closeModal() {
    var modalContainer = document.querySelector('.modal-container');
    modalContainer.style.display = 'none';
}

// 좋아요 버튼 색상 유지

// 버튼 요소 가져오기
var button = document.getElementById("myButton");
var isActive = false; // 버튼 상태 초기값

// 버튼을 클릭할 때 이벤트 처리
button.addEventListener("click", function() {
    if (isActive) { // 버튼이 활성화 상태라면
        // 버튼에 활성화 클래스 제거
        button.classList.remove("bakery-active-btn");
    } else { // 버튼이 비활성화 상태라면
        // 버튼에 활성화 클래스 추가
        button.classList.add("bakery-active-btn");
    }
    isActive = !isActive; // 버튼 상태를 토글 (반전)
});
    
