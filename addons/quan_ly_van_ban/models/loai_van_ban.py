from odoo import models, fields, api
from datetime import date

from odoo.exceptions import ValidationError

class LoaiVanBan(models.Model):
    _name = 'qlvn.loai_van_ban'
    _description = 'Bảng chứa thông tin loại văn bản'
    _rec_name = 'ten_loai_van_ban'

    ma_loai_van_ban = fields.Char("Số hiệu văn bản", required=True)
    ten_loai_van_ban = fields.Char("Tên văn bản", required=True)
    
    # THÊM DÒNG NÀY (Đã có model nhan_vien rồi nên bạn dùng 'nhan_vien')
    nhan_vien_id = fields.Many2one('nhan_vien', string='Nhân viên phụ trách')