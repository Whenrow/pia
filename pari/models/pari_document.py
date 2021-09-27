# -*- coding: utf-8 -*-

from odoo import models, fields


class TableRonde(models.Model):
    _name = 'pari.table.ronde'
    _description = 'Tables rondes'

    name = fields.Char(default='Nouveau', string='Nom')
    date = fields.Date('Date', default=fields.Date.today)
    eleve_id = fields.Many2one('tipwit_base.eleve', 'Elève')
    implantation_id = fields.Many2one(related='eleve_id.implantation_id',string='Implantation')

    intervenant_ids = fields.Many2many(
        'res.partner',
        'pia_intervant_pari_table_rel',
        'intervenant_id',
        'table_id'
    )
    intervenant_autres = fields.Text('Autres intervenants')
    compte_rendu = fields.Text('Compte rendu')


class ObservationPari(models.Model):
    _name = 'pari.observation'
    _description = 'Observations'

    name = fields.Char(default='Nouveau', string='Nom')
    date = fields.Date('Date', default=fields.Date.today)
    eleve_id = fields.Many2one('tipwit_base.eleve', 'Elève')
    observateur_id = fields.Many2one('res.partner', 'Observateur')

    compte_rendu = fields.Text('Compte rendu')


class ProtocoleAR(models.Model):
    _name = 'pari.protocole.ar'
    _description = 'Protocoles aménagements raisonable'

    name = fields.Char(default='Nouveau', string='Nom')
    date = fields.Date('Date', default=fields.Date.today)
    date_envoi = fields.Date('Date d\'envoi au PMS', default=fields.Date.today)
    eleve_id = fields.Many2one('tipwit_base.eleve', 'Elève')
    implantation_id = fields.Many2one(related='eleve_id.implantation_id',string='Implantation')

    #Partenariats
    logo = fields.Many2one(related='eleve_id.logo')
    ergo = fields.Many2one(related='eleve_id.ergo')
    kine = fields.Many2one(related='eleve_id.kine')
    psy = fields.Many2one(related='eleve_id.psy')
    neuropsy = fields.Many2one(related='eleve_id.neuropsy')
    pedopsy = fields.Many2one(related='eleve_id.pedopsy')
    orthoptiste = fields.Many2one(related='eleve_id.orthoptiste')
    neuroped = fields.Many2one(related='eleve_id.neuroped')
    orthopeda = fields.Many2one(related='eleve_id.orthopeda')
    kinesio = fields.Many2one(related='eleve_id.kinesio')
    osteo = fields.Many2one(related='eleve_id.osteo')
    autre = fields.Text(related='eleve_id.autre')

    amenagement_actuels_ids = fields.Many2many('tipwit_base.amenagement', 'pia_amenagement_pari_protocole_actuel_rel', 'amenagement_id', 'conseil_id')
    amenagement_actuels_autre = fields.Text('Autres aménagements actuels')
    amenagement_pari_ids = fields.Many2many('tipwit_base.amenagement', 'pia_amenagement_pari_protocole_pari_rel', 'amenagement_id', 'conseil_id')
    amenagement_pari_autre = fields.Text('Autres aménagements PARI')
    amenagement_finaux_ids = fields.Many2many('tipwit_base.amenagement', 'pia_amenagement_pari_protocole_finaux_rel', 'amenagement_id', 'conseil_id')
    amenagement_finaux_autre = fields.Text('Autres aménagements décidés')


class Dac(models.Model):
    _name = 'pari.dac'
    _description = 'DAC'

    name = fields.Char(default='Nouveau', string='Nom')
    date = fields.Date('Date', default=fields.Date.today)
    eleve_id = fields.Many2one('tipwit_base.eleve', 'Elève')

    ressource = fields.Text('Ressources')
    besoin = fields.Text('Dispositif de différenciation et d’accompagnement personnalisé de l’élève à besoins spécifiques')
    autre = fields.Text('Informations relayées au CdC')
    observation = fields.Text('Observations préalables au CdC')


