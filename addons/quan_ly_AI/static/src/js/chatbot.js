odoo.define('quan_ly_AI.chatbot', function (require) {
    "use strict";

    // Sử dụng bộ gọi hàm ajax chuẩn của Odoo 15 thay cho ES6 import
    var ajax = require('web.ajax');

    document.addEventListener('DOMContentLoaded', function () {
        // 1. Tạo giao diện HTML cho Chatbot
        var chatbotHTML = `
            <div id="odoo-chatbot-toggle" style="position: fixed; bottom: 20px; right: 20px; width: 60px; height: 60px; background-color: #714B9E; color: white; border-radius: 50%; display: flex; justify-content: center; align-items: center; font-size: 24px; cursor: pointer; box-shadow: 0 4px 10px rgba(0,0,0,0.3); z-index: 999999;">
                <i class="fa fa-comments"></i>
            </div>

            <div id="odoo-chatbot-window" class="d-none" style="position: fixed; bottom: 90px; right: 20px; width: 350px; height: 450px; background-color: white; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.2); display: flex; flex-direction: column; z-index: 999999; overflow: hidden; font-family: sans-serif;">
                <div style="background-color: #714B9E; color: white; padding: 15px; font-weight: bold; display: flex; justify-content: space-between; align-items: center;">
                    <span>🤖 Trợ lý ảo AI - FIT DNU</span>
                    <button id="odoo-chatbot-close" style="background: none; border: none; color: white; font-size: 20px; cursor: pointer;">&times;</button>
                </div>
                <div id="odoo-chatbot-messages" style="flex: 1; padding: 15px; overflow-y: auto; background-color: #f8f9fa; display: flex; flex-direction: column; gap: 10px;">
                    <div style="background-color: #e9ecef; color: #212529; padding: 10px; border-radius: 8px; max-width: 85%; align-self: flex-start;">Xin chào! Tôi có thể giúp gì cho bạn về dữ liệu hệ thống hôm nay?</div>
                </div>
                <div style="padding: 10px; border-top: 1px solid #dee2e6; display: flex; gap: 5px; background-color: white;">
                    <input type="text" id="odoo-chatbot-input" placeholder="Nhập câu hỏi..." autocomplete="off" style="flex: 1; padding: 8px; border: 1px solid #ced4da; border-radius: 20px; outline: none;"/>
                    <button id="odoo-chatbot-send" style="background-color: #714B9E; color: white; border: none; padding: 8px 15px; border-radius: 20px; cursor: pointer;">Gửi</button>
                </div>
            </div>
        `;

        // Chèn vào body
        document.body.insertAdjacentHTML('beforeend', chatbotHTML);

        // Lấy các element
        var chatbotToggle = document.getElementById('odoo-chatbot-toggle');
        var chatbotWindow = document.getElementById('odoo-chatbot-window');
        var chatbotClose = document.getElementById('odoo-chatbot-close');
        var chatInput = document.getElementById('odoo-chatbot-input');
        var chatSend = document.getElementById('odoo-chatbot-send');
        var chatMessages = document.getElementById('odoo-chatbot-messages');

        // 2. Xử lý đóng mở an toàn chống lỗi di chuyển vùng chọn DOM
        document.addEventListener('click', function (event) {
            if (!event.target || !document.body.contains(event.target)) return;
            if (event.target.closest('.dropdown-toggle') || event.target.closest('.o_navbar_apps_menu') || event.target.closest('.dropdown-menu')) return;

            if (chatbotToggle && chatbotToggle.contains(event.target)) {
                chatbotWindow.classList.toggle('d-none');
                chatbotToggle.classList.toggle('d-none');
                chatInput.focus();
                return;
            }

            if (chatbotClose && chatbotClose.contains(event.target)) {
                chatbotWindow.classList.add('d-none');
                chatbotToggle.classList.remove('d-none');
                return;
            }
        });

        // 3. Xử lý gửi tin nhắn qua ajax.jsonRpc chuẩn Odoo 15
        function sendMessage() {
            var question = chatInput.value.trim();
            if (!question) return;

            appendMessage(question, 'user');
            chatInput.value = '';

            var loadingDiv = appendMessage('AI đang suy nghĩ...', 'loading');

            // Gọi hàm lên Backend Controller qua cổng RPC truyền thống công khai
            ajax.jsonRpc('/quan_ly_ai/ask', 'call', {
                'question': question
            }).then(function (result) {
                if (loadingDiv) loadingDiv.remove();

                if (result && result.status === 'success') {
                    appendMessage(result.reply, 'bot');
                } else {
                    appendMessage('Lỗi: ' + (result ? result.message : 'Không có phản hồi'), 'error');
                }
            }).catch(function (error) {
                if (loadingDiv) loadingDiv.remove();
                appendMessage('Lỗi kết nối hệ thống Backend!', 'error');
                console.error(error);
            });
        }

        function appendMessage(text, sender) {
            var msgDiv = document.createElement('div');
            if (sender === 'user') {
                msgDiv.style = "background-color: #714B9E; color: white; padding: 10px; border-radius: 8px; max-width: 85%; align-self: flex-end; word-break: break-word;";
            } else if (sender === 'bot') {
                msgDiv.style = "background-color: #e9ecef; color: #212529; padding: 10px; border-radius: 8px; max-width: 85%; align-self: flex-start; word-break: break-word;";
            } else if (sender === 'loading') {
                msgDiv.style = "background-color: #e9ecef; color: #6c757d; padding: 10px; border-radius: 8px; max-width: 85%; align-self: flex-start; font-style: italic;";
            } else {
                msgDiv.style = "background-color: #f8d7da; color: #721c24; padding: 10px; border-radius: 8px; max-width: 85%; align-self: flex-start;";
            }

            msgDiv.innerText = text;
            chatMessages.appendChild(msgDiv);
            chatMessages.scrollTop = chatMessages.scrollHeight;
            return msgDiv;
        }

        if (chatSend) chatSend.addEventListener('click', sendMessage);
        if (chatInput) {
            chatInput.addEventListener('keypress', function (e) {
                if (e.key === 'Enter') sendMessage();
            });
        }
    });
});