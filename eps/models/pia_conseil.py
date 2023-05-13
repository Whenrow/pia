# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Conseil(models.Model):
    _inherit = 'pia.conseil'

    niv_fr = fields.Text('Niveau en français')
    niv_math = fields.Text('Niveau en math')
    rel = fields.Text('Relationnel')
    logo = fields.Text('Niveau en logo')
    gym = fields.Text('Niveau en gym')
    info = fields.Text('Niveau en informatique')
    trav_man = fields.Text('Niveau en travaux manuels')


class Pia(models.Model):
    _name = 'eps.pia'

    name = fields.Selection([
        ('premier', 'Premier PIA'),
        ('deuxieme', 'Deuxième PIA'),
        ('troisieme', 'Troisième PIA')
    ], required=True)
    date = fields.Date('Date', default=fields.Date.today)
    eleve_id = fields.Many2one('tipwit_base.eleve', 'Elève')
    implantation_id = fields.Many2one(related='eleve_id.implantation_id', string='Implantation')
    intervenant_ids = fields.Many2many(
        'res.partner',
        'pia_intervant_eps_pia_rel',
        'intervenant_id',
        'pia_id'
    )
    domaine = fields.Selection([
        ('rel', 'Relationnel / affectif'),
        ('moteur', 'Moteur / psyochomoteur'),
        ('auto', 'Autonomie'),
        ('attitude', 'Attitudes liées au travail'),
        ('peda', 'Pédagogique')], "Domaine")
    
    difficulte = fields.Text('Difficulté principale')
    force = fields.Text('Force de l\'élève')
    besoin = fields.Text('Besoins de l\'élève')
    objectif = fields.Text('Objectif PIA')
    report_name = fields.Char(compute='_compute_report_name')

    @api.depends('name')
    def _compute_report_name(self):
        for pia in self:
            if pia.name == 'premier':
                pia.report_name = '1 - '
            elif pia.name == 'deuxieme':
                pia.report_name = '2 - '
            elif pia.name == 'troisieme':
                pia.report_name = '3 - '
            else:
                pia.report_name = '(supp) - '
            pia.report_name += pia.eleve_id.name

