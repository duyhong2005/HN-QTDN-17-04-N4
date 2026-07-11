# -*- coding: utf-8 -*-
from odoo import models, fields, api


class VanBanDen(models.Model):
    _name = "van_ban_den"
    _description = "Văn bản đến"

    so_ky_hieu = fields.Char(string="Số ký hiệu", required=True)
    trich_yeu = fields.Text(string="Trích yếu")

    # 🔹 Cán bộ xử lý
    nhan_vien_xu_ly_id = fields.Many2one(
        comodel_name="nhan_vien",
        string="Cán bộ xử lý",
        required=True
    )

    # 🔹 Người ký
    nhan_vien_ky_id = fields.Many2one(
        comodel_name="nhan_vien",
        string="Người ký"
    )

    # 🔹 Người nhận / phối hợp (nhiều người)
    nhan_vien_phoi_hop_ids = fields.Many2many(
        comodel_name="nhan_vien",
        string="Người nhận / phối hợp"
    )

    # ==========================================
    # THÊM TRƯỜNG LIÊN KẾT ĐẾN MODULE QUẢN LÝ DỰ ÁN
    # ==========================================
    project_id = fields.Many2one(
        comodel_name="quan_ly_du_an.project",
        string="Thuộc dự án",
        ondelete="set null"
    )