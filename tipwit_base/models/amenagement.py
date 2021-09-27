# -*- coding: utf-8 -*-

from odoo import models, fields


class Amenagement(models.Model):
    _name = 'tipwit_base.amenagement'
    _description = 'Amènagements raisonable'
    _order = 'trouble'

    name = fields.Char(required=True, string="Aménagement")
    trouble = fields.Selection([
        ('asperger', 'Asperger'),
        ('dyscalculie', 'Dyscalculie'),
        ('dysexecutif', 'Dysexecutif'),
        ('dysgraphie', 'Dysgraphie'),
        ('dyslexie', 'Dyslexie'),
        ('dysorthographie', 'Dysorthographie'),
        ('dysphasie', 'Dysphasie'),
        ('dyspraxie', 'Dyspraxie'),
        ('HPI', 'HPI'),
        ('TDA', 'TDA')
    ], required=True)
    type = fields.Selection([
        ('comportement', 'Comportement à adopter'),
        ('travail', 'Travail en classe'),
        ('notes', 'Notes de cours'),
        ('evaluation', 'Evaluations')
    ], required=True)
    commentaire = fields.Text('Commentaire')
