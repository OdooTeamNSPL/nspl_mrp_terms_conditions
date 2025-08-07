from odoo import models, fields, api

class MrpTerms(models.Model):
    _name = 'mrp.terms'
    _description = 'MRP Terms and Conditions'

    name = fields.Char('Name', required=True)
    terms_text = fields.Text('Terms & Condition')


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    mrp_terms_id = fields.Many2one('mrp.terms', string="Terms & Condition")
    mrp_terms_text = fields.Text('Terms & Conditions Details')

    @api.onchange('mrp_terms_id')
    def onchange_mrp_terms_id(self):
        for rec in self:
            if rec.mrp_terms_id:
                rec.mrp_terms_text = rec.mrp_terms_id.terms_text or ''
            else:
                rec.mrp_terms_text = ''
