# -*- coding: utf-8 -*-
{
    'name': 'DNU AI Assistant (Bản Tiếng Việt)',
    'summary': 'Trợ lý ảo AI hỗ trợ hỏi đáp hệ thống quản lý',
    'version': '1.0',
    'author': 'FIT-DNU Group 6',
    'category': 'Tools',
    'depends': [
        'base', 
        'web',  
        'nhan_su',    
        'quan_ly_khach_hang',  
        'quan_ly_van_ban'     
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/quan_ly_ai_view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'quan_ly_AI/static/src/css/chatbot.css',
            'quan_ly_AI/static/src/js/chatbot.js',
        ],
    },
    'installable': True,
    'application': True,
}