# -*- coding: utf-8 -*-
# Part of Odoo,Flectra. See LICENSE file for full copyright and licensing details.

from flectra import fields, models


class ResPartnerBank(models.Model):
    _inherit = 'res.partner.bank'

    aba_routing = fields.Integer(string="ABA/Routing", help="American Bankers Association Routing Number")
