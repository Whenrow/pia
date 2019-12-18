-- From dest
Begin;
COPY res_partner(id,name,company_id,create_date,display_name,date,title,parent_id,ref,lang,tz,user_id,vat,website,comment,credit_limit,active,employee,function,type,street,street2,zip,city,state_id,country_id,partner_latitude,partner_longitude,email,phone,mobile,is_company,industry_id,color,partner_share,commercial_partner_id,commercial_company_name,company_name,create_uid,write_uid,write_date,message_main_attachment_id,email_normalized,message_bounce,signup_token,signup_type,signup_expiration,partner_gid,additional_info,phone_sanitized) FROM '/home/pia/partner.csv' DELIMITER ',' CSV;
alter table res_users add column oauth int4;
COPY res_users FROM '/home/pia/users.csv' DELIMITER ',' CSV;
alter table res_users drop column oauth;
update res_partner set name='Administrateur' where id=3;
update res_users set login='administrateur@eps-saintberthuin.be' where id=2;
COPY pia_implantation(id,create_uid,create_date,write_uid,write_date,name,fase,telephone,gsm,direction,reseau,email)
FROM '/home/pia/implantation.csv' DELIMITER ',' CSV;
insert into res_company_users_rel (cid, user_id) (select 1, id from res_users where id > 5);
insert INTO res_groups_users_rel (uid, gid) (select id, (select id from res_groups where name = 'Internal User') from res_users where id > 5);
COPY pia_eleve(id,create_date,write_uid,write_date,name,implantation_id,date_naissance,nom_tuteur_1,telephone_tuteur_1,email_tuteur_1,rue,parcours,objectif_integration,bilan_medical,situation_psycho_sociale,diagnostic,statut_tuteur_1,langue_maison,nom_tuteur_2,statut_tuteur_2,telephone_tuteur_2,email_tuteur_2,ville)
FROM '/home/pia/eleve.csv' DELIMITER ',' CSV;
UPDATE pia_eleve SET statut_tuteur_1 = REPLACE(statut_tuteur_1,'Père','pere');
UPDATE pia_eleve SET statut_tuteur_1 = REPLACE(statut_tuteur_1,'Mère','mere');
UPDATE pia_eleve SET statut_tuteur_2 = REPLACE(statut_tuteur_2,'Père','pere');
UPDATE pia_eleve SET statut_tuteur_2 = REPLACE(statut_tuteur_2,'Mère','mere');
COPY pia_amenagement(id,create_uid,create_date,write_uid,write_date,trouble,name,type,commentaire)
FROM '/home/pia/amenagement.csv' DELIMITER ',' CSV;

COPY pia_trouble(id,create_uid,create_date,write_uid,write_date,name)
FROM '/home/pia/trouble.csv' DELIMITER ',' CSV;

COPY pia_intervenant(id,create_uid,create_date,write_uid,write_date,name,fonction,telephone,email,implantation_id)
FROM '/home/pia/intervenant.csv' DELIMITER ',' CSV;
UPDATE pia_intervenant SET fonction = REPLACE(fonction,'institutrice','instit');
UPDATE pia_intervenant SET fonction = REPLACE(fonction,'logopède','logo');

COPY pia_conseil(id,create_uid,create_date,write_uid,write_date,name,date,eleve_id,ressource,responsable_id,autre,besoin,a_faire)
FROM '/home/pia/conseil.csv' DELIMITER ',' CSV;
UPDATE pia_conseil SET name = REPLACE(name,'Premier conseil de classe','premier');

COPY pia_objectif(id,create_uid,create_date,write_uid,write_date,evaluation,outil,moyen,commentaire,conseil_id,objectif,is_instit,is_logo)
FROM '/home/pia/objectif.csv' DELIMITER ',' CSV;

COPY pia_intervant_pia_conseil_rel(intervenant_id, conseil_id)
FROM '/home/pia/conseil_intervenant.csv' DELIMITER ',' CSV;

COPY pia_trouble_pia_conseil_rel(trouble_id,conseil_id)
FROM '/home/pia/conseil_trouble.csv' DELIMITER ',' CSV;

COPY pia_amenagement_pia_conseil_res(amenagement_id,conseil_id)
FROM '/home/pia/conseil_amenagement.csv' DELIMITER ',' CSV;
commit;
