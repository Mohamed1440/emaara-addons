from odoo import models, fields

class StockMove(models.Model):
    _inherit = 'stock.move'

    sale_description = fields.Text(
        string="Description",
        compute="_compute_sale_description",
        store=False,
    )

    def _compute_sale_description(self):
        for move in self:
            # لو الحركة جاية من سطر بيع (Sales Order Line) خُد وصف السطر
            if move.sale_line_id:
                move.sale_description = move.sale_line_id.name
            else:
                # fallback: وصف البيع على المنتج
                move.sale_description = move.product_id.description_sale or ''
