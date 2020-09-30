# -*- coding: utf-8 -*-

from odoo import models, fields, api

from datetime import datetime


class BilanLogo(models.Model):
    _name = 'pia.bilan.logo'
    _description = 'Bilan Logopédique'

    def _get_default_date(self):
        months = [
            'Janvier',
            'Février',
            'Mars',
            'Avril',
            'Mai',
            'Juin',
            'Juillet',
            'Aout',
            'Septembre',
            'Octobre',
            'Novembre',
            'Décembre'
        ]
        return months[datetime.now().month - 1] + ' ' + str(datetime.now().year)

    name = fields.Char(related='eleve_id.name')
    date = fields.Char('Date', default=_get_default_date)
    eleve_id = fields.Many2one('pia.eleve', 'Elève')
    date_naissance = fields.Date(related='eleve_id.date_naissance')
    implantation_id = fields.Many2one(related='eleve_id.implantation_id',string='Implantation')
    annee_scolaire = fields.Selection([
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
       ('p6b', 'P6 bis')
    ], string='Année scolaire')

    bilan_type = fields.Selection([
        ('init_oral', 'initial en langage oral'),
        ('init_ecrit', 'initial en langage écrit'),
        ('init_math', 'initial en mathématique'),
        ('evo_oral', 'd\'évolution en langage oral'),
        ('evo_ecrit', 'd\'évolution en langage écrit'),
        ('evo_math', 'd\'évolution en mathématique')
    ], string='Bilan')

    test_ids = fields.Many2many('pia.bilan.test', string='Test(s) utilisé(s)')
    etalonnage_ids = fields.Many2many('pia.bilan.etalonnage', string='Étalonnage utilisés')

    anamnese = fields.Text('Anamnèse')
    comportement = fields.Text('Comportement durant le testing')

    # TODO: remove
    ana_quanti_ids = fields.One2many('pia.bilan.ana.quanti', 'bilan_id', 'Analyse quantitatif')
    ana_quali_ids = fields.One2many('pia.bilan.ana.quali', 'bilan_id', 'Analyse qualitatif')

    ana_ids = fields.One2many('pia.bilan.ana', 'bilan_id', 'Analyses')
    amenagement_ids = fields.Many2many('pia.amenagement', string='AR')

    conclusion = fields.Text('Conclusion')
    projet = fields.Text('Project thérapeutique')

class BilanTest(models.Model):
    _name = 'pia.bilan.test'
    _description = 'Test d\'un bilan logopédique'

    name = fields.Char('Nom', required=True)

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Ce test existe déjà"),
    ]


class BilanEtalonnage(models.Model):
    _name = 'pia.bilan.etalonnage'
    _description = 'Etalonnage d\'un bilan logopédique'

    name = fields.Char('Nom', required=True)

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Cet étalonnage existe déjà"),
    ]


# TODO: Remove
class BilanAnalyseQuantitatif(models.Model):
    _name = 'pia.bilan.ana.quanti'
    _description = 'Analyse quantitatif d\'un bilan logopédique'

    bilan_id = fields.Many2one('pia.bilan.logo', 'Bilan')
    test_id = fields.Many2one('pia.bilan.test', 'Epreuve')
    note = fields.Float('Note brute', digits=(2,1))
    note_pre = fields.Float('Note brute (année précédente)', digits=(2,1))
    ecart_type = fields.Float('Écart-type', digits=(1,2))
    ecart_type_pre = fields.Float('Écart-type (année précédente)', digits=(1,2))
    performance = fields.Selection([
        ('ex', 'Performance excellente'),
        ('tb', 'Très bonne performance'),
        ('mfo', 'Niveau moyen fort'),
        ('mfa', 'Niveau moyen faible'),
        ('f', 'Faible'),
        ('d', 'Déficitaire'),
        ('tf', 'Très faible')
    ], string='Performance')

# TODO: Remove
class BilanAnalyseQualitatif(models.Model):
    _name = 'pia.bilan.ana.quali'
    _description = 'Analyse qualitatif d\'un bilan logopédique'

    bilan_id = fields.Many2one('pia.bilan.logo', 'Bilan')
    test_id = fields.Many2one('pia.bilan.test', 'Test')
    epreuve_id = fields.Many2one('pia.bilan.test.epreuve', 'Epreuve')
    commentaire = fields.Text('Commentaire')
    allowed_epreuve_ids = fields.One2many('pia.bilan.test.epreuve', compute='_compute_allowed_epreuve_ids')

    @api.depends('bilan_id.test_ids')
    def _compute_allowed_epreuve_ids(self):
        for ana in self:
            ana.allowed_epreuve_ids = self.env['pia.bilan.test.epreuve'].search([
                ('test_id', 'in', ana.bilan_id.test_ids.ids)
            ])

class BilanAnalyse(models.Model):
    _name = 'pia.bilan.ana'
    _description = 'Analyse d\'un bilan logopédique'
    _order = 'test_id,epreuve_id'

    bilan_id = fields.Many2one('pia.bilan.logo', 'Bilan')
    test_id = fields.Many2one(related='epreuve_id.test_id')
    epreuve_id = fields.Many2one('pia.bilan.test.epreuve', 'Epreuve')
    note = fields.Char('Note brute')
    note_pre = fields.Char('Note brute (année précédente)')
    ecart_type = fields.Char('Écart-type')
    ecart_type_pre = fields.Char('Écart-type (année précédente)')
    commentaire = fields.Text('Commentaire')
    performance = fields.Selection([
        ('ex', 'Performance excellente'),
        ('tb', 'Très bonne performance'),
        ('mfo', 'Niveau moyen fort'),
        ('m', 'Niveau moyen'),
        ('mfa', 'Niveau moyen faible'),
        ('f', 'Faible'),
        ('d', 'Déficitaire')
    ], string='Performance')
    allowed_epreuve_ids = fields.One2many('pia.bilan.test.epreuve', compute='_compute_allowed_epreuve_ids')

    @api.depends('bilan_id.test_ids')
    def _compute_allowed_epreuve_ids(self):
        for ana in self:
            ana.allowed_epreuve_ids = self.env['pia.bilan.test.epreuve'].search([
                ('test_id', 'in', ana.bilan_id.test_ids.ids)
            ])


class BilanTestEpreuve(models.Model):
    _name = 'pia.bilan.test.epreuve'
    _description = 'Epreuve exalangue/examath d\'un bilan logopédique'
    _order = 'test_id, name'

    test_id = fields.Many2one('pia.bilan.test', 'Test')
    name = fields.Char('Titre')
    description = fields.Char('Description')

    _sql_constraints = [
        ('name_uniq', 'unique (name, test_id)', "Cette épreuve existe déjà"),
    ]
