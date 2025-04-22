from odoo import models, fields, api

class ProjectProject(models.Model):
    _inherit = 'project.project'
    
    closed = fields.Boolean(string="Closed", help="If checked, timesheets cannot be logged to this project.")

    session_rate = fields.Integer(string='Session Rate')

    session_budget = fields.Integer(
        string='Session Budget',
        compute='_compute_session_budget',
        store=True,
        readonly=True,
    )

    remaining_session = fields.Integer(
        string='Remaining Session',
        compute='_compute_remaining_session',
        store=True,
        readonly=True,
    )
    
    @api.model
    def create(self, vals):
        project = super().create(vals)

        # Get default task stages
        default_stages = self.env['project.task.type'].search([('project_default_stage', '=', True)])

        # Set them on the new project
        if default_stages:
            project.write({'type_ids': [(6, 0, default_stages.ids)]})

        return project

    @api.depends('allocated_hours', 'session_rate')
    def _compute_session_budget(self):
        for record in self:
            if record.allocated_hours and record.session_rate:
                record.session_budget = record.allocated_hours * record.session_rate
            else:
                record.session_budget = 0

    @api.depends('session_budget', 'session_rate', 'effective_hours')
    def _compute_remaining_session(self):
        for record in self:
            if record.session_budget and record.effective_hours is not None and record.session_rate:
                record.remaining_session = record.session_budget - (record.effective_hours * record.session_rate)
            else:
                record.remaining_session = 0
