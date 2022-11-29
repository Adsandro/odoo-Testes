# -*- coding: utf-8 -*-
from odoo import api, fields, models


class BancoCorrentista(models.Model):
    _name = "banco.correntista"
    _description = "descrição para o banco correntista, presente em models"

    correntista = fields.Char(string='Nome do correntista', required=True)
    idade = fields.Integer(string='Idade do correntista', required=True)


    sexo = fields.Selection([

        ('outros', 'Outros'),
        ('homem', 'Homem'),
        ('mulher', 'Mulher'),
    
    ],  required=True, default='outros' )


    observacao = fields.Text(string='Obs:')

    