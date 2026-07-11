# -*- coding: utf-8 -*-
{
    'name': "nhan_su",

    'summary': """
        Quản lý nhân sự và tích hợp báo cáo tổng hợp Dashboard""",

    'description': """
        Mô-đun quản lý thông tin nhân viên, phòng ban, chức vụ, chấm công và chứng chỉ.
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    'category': 'Human Resources',
    'version': '0.1',

    # Đã giữ nguyên board để hệ thống không bị lỗi thiếu mô hình board.board
    'depends': ['base', 'board'],

    # Sắp xếp lại thứ tự nạp: Menu/Security -> Dữ liệu gốc -> Dashboard
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',               # Đưa menu lên trước để làm điểm tựa parent cho các action/menu con
        'views/nhan_vien.xml',
        'views/phong_ban.xml',
        'views/chuc_vu.xml',
        'views/cham_cong.xml',
        'views/lich_su_cong_tac.xml',
        'views/chung_chi.xml',
        'views/nhan_vien_dashboard.xml', # Dashboard gọi đồ thị từ nhan_vien.xml và menu từ menu.xml nên xếp cuối là hoàn hảo
    ],

    'demo': [
        'demo/demo.xml',
    ],
    'license': 'LGPL-3', # Thêm dòng này để Terminal không bị bắn Warning Missing License Key nữa nhé!
}