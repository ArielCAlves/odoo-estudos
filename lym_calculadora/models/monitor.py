from odoo import fields, models, api
import datetime
import time

class Monitor(models.Model):
    _name = 'lym_calculadora.monitor'
    _description = 'Monitor'
    _soma = 'soma'
    _subtracao = 'subtração'
    _multiplicacao = 'multiplicação'
    _divisao = 'divisão'

    # description = fields.Char('Description')

    # start = fields.Datetime('Start', default = lambda self: fields.Datetime.now())
    # finish = fields.Datetime('Finish')

    first_number = fields.Integer('FirstNumber')
    second_number = fields.Integer('SecondNumber')


    soma = fields.Char(string = 'Soma', compute = '_compute_fields_soma')
    subtracao = fields.Char(string = 'Subtração', compute = '_compute_fields_subtracao')
    multiplicacao = fields.Char(string = 'Multiplicação', compute = '_compute_fields_multiplicacao')
    divisao = fields.Char(string = 'Divisão', compute = '_compute_fields_divisao')




    def _compute_fields_soma(self):
        for i in self:
            # i.soma = 'FirstNumber: %s + SecondNumber: %s' % (i.first_number, i.second_number)
            # i.soma = '%s + %s = 'i.first_number + i.second_number % (i.first_number, i.second_number)
            i.soma = i.first_number + i.second_number    

    def _compute_fields_subtracao(self):
        for i in self:
            i.subtracao = i.first_number - i.second_number
    def _compute_fields_multiplicacao(self):
        for i in self:      
            i.multiplicacao = i.first_number * i.second_number
    def _compute_fields_divisao(self):
        for i in self:
            # i.divisao = 'FirstNumber / SecondNumber = ', i.first_number / i.second_number            
            if i.second_number == 0:
                i.divisao = 0
            else:
                i.divisao = i.first_number / i.second_number
