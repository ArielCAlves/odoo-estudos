from odoo import fields, models, api
import datetime
import time

class Monitor(models.Model):
    _name = 'lym_ariel.monitor'
    _description = 'Monitor'

    description = fields.Char('Description')

    running = fields.Boolean('Is running', default = True)
    start = fields.Datetime('Start', default = lambda self: fields.Datetime.now())
    finish = fields.Datetime('Finish')