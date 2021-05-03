from odoo import models, fields, api, exceptions
import requests
import re

import logging
_logger = logging.getLogger(__name__)

class ResPartner(models.Model):
    _inherit = 'res.partner'
    _name = 'res.partner' #talvez ñ precise desta linha

    cpf = fields.Char(string='CPF')





    @api.onchange('zip')
    def _compute_zip(self):
        for i in self:
            if i.zip and re.findall(r'^\d{8}$', i.zip):
                url = f'https://viacep.com.br/ws/{i.zip}/json/'
                resp = requests.get(url)
                
                if resp.status_code == 200:
                    if not resp.json().get('erro', False):                    
                        _json = resp.json()
                        i.street = _json.get('logradouro', None)
                        i.street2 = _json.get('complemento', None)
                        i.city = _json.get('localidade', None)
                        i.country_id = i.env['res.country'].search(
                            [
                                ('code','=','BR')
                            ], limit = 1
                        )
                        i.state_id = i.env['res.country.state'].search(
                            [
                                ('code','=',_json.get('uf', None)), 
                                ('country_id','=', i.country_id.id)
                            ], limit = 1
                        )
                        