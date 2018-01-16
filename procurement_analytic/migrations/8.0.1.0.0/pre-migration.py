# -*- coding: utf-8 -*-
# Copyright 2017 Eficent
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openupgradelib import openupgrade

COLUMN_RENAMES = {
    'procurement_order': [
        ('account_analytic_id', 'analytic_account_id'),
    ]
}


@openupgrade.migrate(use_env=True)
def migrate(env, version):
    openupgrade.rename_columns(env.cr, COLUMN_RENAMES)
