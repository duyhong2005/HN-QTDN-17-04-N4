# -*- coding: utf-8 -*-
import json
import requests
from odoo import http
from odoo.http import request

class OdooAiChatbotController(http.Controller):

    @http.route('/quan_ly_ai/ask', type='json', auth='user', cors='*')
    def ask_ai_chatbot(self, question, **kwargs):
        if not question:
            return {'status': 'error', 'message': 'Câu hỏi trống'}

        # Sử dụng API Key của bạn
        api_key = "YOUR_API_KEY_HERE"

        try:
            # ==========================================
            # 1. THU THẬP TOÀN BỘ DỮ LIỆU CHI TIẾT KHÁCH HÀNG (ĐÃ ĐỒNG BỘ FIELD)
            # ==========================================
            total_customers = request.env['customer'].sudo().search_count([]) if 'customer' in request.env else 0
            customer_list_str = "Không có"
            if 'customer' in request.env:
                customer_records = request.env['customer'].sudo().search([])
                customer_details = []
                for c in customer_records:
                    # Map chuẩn xác theo file cấu trúc model thực tế của bạn
                    c_code = c.customer_id if hasattr(c, 'customer_id') and c.customer_id else str(c.id)
                    c_name = c.customer_name if hasattr(c, 'customer_name') and c.customer_name else "Chưa có tên"
                    c_phone = c.phone if hasattr(c, 'phone') and c.phone else "Chưa cập nhật SĐT"
                    c_email = c.email if hasattr(c, 'email') and c.email else "Chưa có email"
                    c_address = c.address if hasattr(c, 'address') and c.address else "Chưa cập nhật địa chỉ"
                    
                    # Đọc nhãn hiển thị trực tiếp từ selection nếu cần hoặc trả về giá trị key
                    c_income = c.income_level if hasattr(c, 'income_level') and c.income_level else "Chưa rõ"
                    c_status = c.customer_status if hasattr(c, 'customer_status') and c.customer_status else "Mới"
                    
                    c_type = "Cá nhân"
                    if hasattr(c, 'customer_type') and c.customer_type == 'company':
                        c_type = "Công ty"
                        
                    c_orders = c.total_orders if hasattr(c, 'total_orders') else "0"

                    customer_details.append(
                        f"- Khách hàng: {c_name} (Mã: {c_code})\n"
                        f"  + Số điện thoại: {c_phone} | Email: {c_email}\n"
                        f"  + Địa chỉ: {c_address} | Loại khách hàng: {c_type}\n"
                        f"  + Mức thu nhập: {c_income} | Trạng thái: {c_status}"
                    )
                if customer_details:
                    customer_list_str = "\n\n".join(customer_details)

            # ==========================================
            # 2. THU THẬP TOÀN BỘ LÝ LỊCH NHÂN VIÊN
            # ==========================================
            total_employees = 0
            employee_list_str = "Không có"
            if 'nhan_vien' in request.env:
                total_employees = request.env['nhan_vien'].sudo().search_count([])
                employee_records = request.env['nhan_vien'].sudo().search([])
                employee_details = []
                
                for e in employee_records:
                    e_name = e.ho_ten if hasattr(e, 'ho_ten') and e.ho_ten else "Chưa rõ tên"
                    e_home = e.que_quan if hasattr(e, 'que_quan') and e.que_quan else "Chưa cập nhật"
                    e_mail = e.email if hasattr(e, 'email') and e.email else "Chưa có email"
                    e_phone = e.so_dien_thoai if hasattr(e, 'so_dien_thoai') and e.so_dien_thoai else "Chưa cập nhật SĐT"
                    e_birthday = str(e.ngay_sinh) if hasattr(e, 'ngay_sinh') and e.ngay_sinh else "Chưa cập nhật"
                    e_bhxh = e.so_bhxh if hasattr(e, 'so_bhxh') and e.so_bhxh else "Chưa cập nhật"
                    e_salary = f"{e.luong:,.0f}" if hasattr(e, 'luong') and e.luong else "0"
                    
                    p_ban = "Chưa xếp phòng"
                    if hasattr(e, 'phong_ban_ids') and e.phong_ban_ids:
                        p_ban = ", ".join([p.name if hasattr(p, 'name') else (p.ten_phong_ban if hasattr(p, 'ten_phong_ban') else str(p.id)) for p in e.phong_ban_ids])
                    
                    c_vu = "Chưa có chức vụ"
                    if hasattr(e, 'chuc_vu_id') and e.chuc_vu_id:
                        c_vu = e.chuc_vu_id.name if hasattr(e.chuc_vu_id, 'name') else (e.chuc_vu_id.ten_chuc_vu if hasattr(e.chuc_vu_id, 'ten_chuc_vu') else str(e.chuc_vu_id.id))

                    employee_details.append(
                        f"- Nhân viên: {e_name}\n"
                        f"  + Ngày sinh: {e_birthday} | Quê quán: {e_home}\n"
                        f"  + Số điện thoại: {e_phone} | Email: {e_mail}\n"
                        f"  + Số BHXH: {e_bhxh} | Lương định mức: {e_salary}\n"
                        f"  + Phòng ban: {p_ban} | Chức vụ: {c_vu}"
                    )
                if employee_details:
                    employee_list_str = "\n\n".join(employee_details)

            # ==========================================
            # 3. THU THẬP DỮ LIỆU QUẢN LÝ VĂN BẢN
            # ==========================================
            total_v_types = request.env['qlvn.loai_van_ban'].sudo().search_count([]) if 'qlvn.loai_van_ban' in request.env else 0
            total_v_in = request.env['van_ban_den'].sudo().search_count([]) if 'van_ban_den' in request.env else 0
            
            v_in_list_str = "Không có"
            if 'van_ban_den' in request.env:
                v_in_records = request.env['van_ban_den'].sudo().search([])
                v_in_details = []
                for v in v_in_records:
                    skh = v.so_ky_hieu if hasattr(v, 'so_ky_hieu') and v.so_ky_hieu else "Chưa có số"
                    tyieu = v.trich_yeu if hasattr(v, 'trich_yeu') and v.trich_yeu else "Không có trích yếu"
                    v_in_details.append(f"- Ký hiệu: {skh} | Trích yếu: {tyieu}")
                if v_in_details:
                    v_in_list_str = "\n".join(v_in_details)

            total_v_out = request.env['qlvn.van_ban_di'].sudo().search_count([]) if 'qlvn.van_ban_di' in request.env else 0
            v_out_list_str = "Không có"
            if 'qlvn.van_ban_di' in request.env:
                v_out_records = request.env['qlvn.van_ban_di'].sudo().search([])
                v_out_details = []
                for v in v_out_records:
                    v_name = v.name if hasattr(v, 'name') and v.name else "Chưa rõ tên VB"
                    svb = v.so_van_ban if hasattr(v, 'so_van_ban') and v.so_van_ban else "Chưa có số"
                    v_out_details.append(f"- Tên VB: {v_name} | Số VB: {svb}")
                if v_out_details:
                    v_out_list_str = "\n".join(v_out_details)

            # ==========================================
            # 4. XÂY DỰNG SYSTEM PROMPT GỬI CHO GEMINI (MỞ RỘNG KHẢ NĂNG TƯ VẤN)
            # ==========================================
            system_prompt = f"""
Bạn là Trợ lý ảo AI chuyên nghiệp tích hợp trên hệ thống Quản lý Khoa CNTT - Đại học Đại Nam.
DỮ LIỆU HỆ THỐNG THỜI GIAN THỰC:

[DANH SÁCH KHÁCH HÀNG CHI TIẾT]
{customer_list_str}

[HỒ SƠ LÝ LỊCH NHÂN VIÊN]
{employee_list_str}

[DANH SÁCH VĂN BẢN ĐẾN]
{v_in_list_str}

[DANH SÁCH VĂN BẢN ĐI]
{v_out_list_str}

NHIỆM VỤ VÀ NGUYÊN TẮC PHẢN HỒI:
1. ĐỐI VỚI CÂU HỎI TRA CỨU/HỎI ĐÁP DỮ LIỆU: Dựa hoàn toàn vào dữ liệu khách hàng, nhân viên và văn bản chi tiết được cung cấp ở trên (bao gồm tên, số điện thoại, email, địa chỉ, mức thu nhập, trạng thái...) để trả lời chính xác, trực tiếp. Tuyệt đối không bịa đặt thông tin không có trong hệ thống.
2. ĐỐI VỚI CÂU HỎI TƯ VẤN CHIẾN LƯỢC / PHÁT TRIỂN KINH DOANH (Ví dụ: "làm như nào để bán thêm hàng", "chiến lược tăng doanh thu là gì",...): Hãy đóng vai là một Chuyên gia phân tích dữ liệu và tư vấn kinh doanh cao cấp. Bạn hãy nhìn vào bức tranh dữ liệu tổng quan được cung cấp phía trên (ví dụ: số lượng khách hàng cá nhân/công ty là bao nhiêu, mức thu nhập của họ tập trung ở phân khúc nào, trạng thái khách hàng cũ/mới thế nào) để đưa ra các lời khuyên chiến lược, giải pháp thực tế, mang tính hành động cao nhằm giúp doanh nghiệp tăng trưởng bán hàng.
3. Trả lời bằng tiếng Việt lịch sự, định dạng rõ ràng, ngắn gọn, chia các đầu dòng rành mạch.
"""

            # ==========================================
            # 5. GỌI API GEMINI QUA HEADER AN TOÀN
            # ==========================================
            url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"
            
            headers = {
                'Content-Type': 'application/json',
                'x-goog-api-key': api_key
            }
            
            payload = {
                "contents": [
                    {
                        "parts": [
                            {"text": f"{system_prompt}\n\nCâu hỏi của người dùng: {question}"}
                        ]
                    }
                ]
            }
            
            response = requests.post(url, headers=headers, json=payload, timeout=30)
            
            if response.status_code == 200:
                res_json = response.json()
                ai_text = res_json['candidates'][0]['content']['parts'][0]['text']
                return {'status': 'success', 'reply': ai_text}
            else:
                return {'status': 'error', 'message': f'Lỗi API Google ({response.status_code}): {response.text}'}

        except Exception as e:
            return {'status': 'error', 'message': f'Lỗi hệ thống: {str(e)}'}