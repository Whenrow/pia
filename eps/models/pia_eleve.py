# -*- coding: utf-8 -*-

from odoo import models, fields


class Eleve(models.Model):
    _inherit = 'tipwit_base.eleve'

    street_1 = fields.Char("street_1")
    ville_1 = fields.Char("ville_1")
    street_2 = fields.Char("street_2")
    ville_2 = fields.Char("ville_2")
    street_3 = fields.Char("street_3")
    ville_3 = fields.Char("ville_3")
    droit_image = fields.Boolean("Droit à l'image")

    job_1 = fields.Char("job_1")
    job_2 = fields.Char("job_2")

    nom_tuteur_3 = fields.Char()
    job_3 = fields.Char("job_3")
    statut_tuteur_3 = fields.Selection([
        ('pere', 'Père'),
        ('mere', 'Mère'),
        ('tuteur', 'Tuteur légal')
    ],)
    telephone_tuteur_3 = fields.Char()
    email_tuteur_3 = fields.Char()
    outil = fields.Selection([('rien', 'Rien'), ('pc', 'PC'), ('tab', 'Tablette')], string="Outil numérique")
    detail_ids = fields.One2many('eps.eleve.detail', 'eleve_id')
    pia_count = fields.Integer(compute='_compute_conseil_count')

    def _compute_conseil_count(self):
        for eleve in self:
            eleve.pia_count = self.env['eps.pia'].sudo().search_count([
                ('eleve_id', '=', eleve.id)
            ])
        super()._compute_conseil_count()
    
    def action_view_pia(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("eps.action_view_pia")
        action['domain'] = [('eleve_id', '=', self.id)]
        action['context'] = dict(self._context, default_eleve_id=self.id)
        return action

class EleveDetail(models.Model):
    _name = 'eps.eleve.detail'

    eleve_id = fields.Many2one('tipwit_base.eleve', "Eleve")
    annee_etude = fields.Selection([
        ('m1', 'M1'),
        ('m2', 'M2'),
        ('m3', 'M3'),
        ('p1', 'P1'),
        ('p1b', 'P1 bis'),
        ('p2', 'P2'),
        ('p2b', 'P2 bis'),
        ('p3', 'P3'),
        ('p3b', 'P3 bis'),
        ('p4', 'P4'),
        ('p4b', 'P4 bis'),
        ('p5', 'P5'),
        ('p5b', 'P5 bis'),
        ('p6', 'P6'),
        ('p6b', 'P6 bis'),
        ('s1', 'S1'),
        ('s2', 'S2'),
        ('s3', 'S3'),
        ('s4', 'S4'),
        ('s5', 'S5'),
        ('s6', 'S6'),
     ], string='Année scolaire')
    ecole = fields.Char("École")
    classe = fields.Char("Classe")
    prise = fields.Text("Prise en charge extérieure")
