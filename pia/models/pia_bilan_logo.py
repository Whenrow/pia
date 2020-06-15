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
        return months[datetime.now().month + 1] + ' ' + str(datetime.now().year)

    name = fields.Char(related='eleve_id.name')
    date = fields.Char('Date', default=_get_default_date)
    eleve_id = fields.Many2one('pia.eleve', 'Elève')
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

    test_ids = fields.Many2many('pia.bilan.test', compute='_compute_test_ids', inverse='_set_test_ids', string='Test(s) utilisé(s)')
    etalonnage_ids = fields.Many2many('pia.bilan.etalonnage', string='Étalonnage utilisés')

    anamnese = fields.Text('Anamnèse')
    comportement = fields.Text('Comportement durant le testing')

    ana_quanti_ids = fields.One2many('pia.bilan.ana.quanti', 'bilan_id', 'Analyse quantitatif')
    ana_quali_ids = fields.One2many('pia.bilan.ana.quali', 'bilan_id', 'Analyse qualitatif')
    amenagement_ids = fields.Many2many('pia.amenagement', string='AR')

    conclusion = fields.Text('Conclusion')
    projet = fields.Text('Project thérapeutique')

    @api.depends('ana_quali_ids.test_id', 'ana_quanti_ids.test_id')
    def _compute_test_ids(self):
        for bilan in self:
            bilan.test_ids = self.ana_quali_ids.test_id | self.ana_quanti_ids.test_id

    def _set_test_ids(self):
        for test in (self.test_ids - self.ana_quali_ids.test_id):
            self.ana_quali_ids = [(0, 0, {'test_id': test.id})]
        for test in (self.test_ids - self.ana_quanti_ids.test_id):
            self.ana_quanti_ids = [(0, 0, {'test_id': test.id})]


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


class BilanAnalyseQuantitatif(models.Model):
    _name = 'pia.bilan.ana.quanti'
    _description = 'Analyse quantitatif d\'un bilan logopédique'

    bilan_id = fields.Many2one('pia.bilan.logo', 'Bilan')
    test_id = fields.Many2one('pia.bilan.test', 'Epreuve')
    note = fields.Float('Note brute', digits=(2,1))
    ecart_type = fields.Float('Écart-type', digits=(1,2))
    performance = fields.Selection([
        ('ex', 'Performance excellente'),
        ('tb', 'Très bonne performance'),
        ('mfo', 'Niveau moyen fort'),
        ('mfa', 'Niveau moyen faible'),
        ('f', 'Faible'),
        ('d', 'Déficitaire')
    ], string='Performance')


class BilanAnalyseQualitatif(models.Model):
    _name = 'pia.bilan.ana.quali'
    _description = 'Analyse qualitatif d\'un bilan logopédique'

    bilan_id = fields.Many2one('pia.bilan.logo', 'Bilan')
    test_id = fields.Many2one('pia.bilan.test', 'Epreuve')
    commentaire = fields.Text('Commentaire')


