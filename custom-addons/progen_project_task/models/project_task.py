from odoo import models, fields, api

class ProjectTask(models.Model):
    _inherit = 'project.task'

    
    task_budget = fields.Integer(
        string="Task Budget ($)",
        compute='_compute_task_budget',
        store=True
    )

    task_remaining_budget = fields.Integer(
        string="Task Remaining Budget ($)",
        compute='_compute_task_remaining_budget',
        store=True
    )

    task_timesheet = fields.Boolean(
        string="Task Timesheet",
        compute='_compute_task_timesheet',
        store=True
    )

    @api.depends( 'allocated_hours','project_id.session_budget','project_id.allocated_hours')
    def _compute_task_budget(self):
        for record in self:
            if record.project_id and record.project_id.session_budget and record.project_id.allocated_hours:
                record.task_budget = (record.project_id.session_budget / record.project_id.allocated_hours) * record.allocated_hours
            else:
                record.task_budget = 0

    @api.depends('task_budget', 'allocated_hours', 'effective_hours')
    def _compute_task_remaining_budget(self):
        for record in self:
            if record.allocated_hours:
                cost_per_hour = record.task_budget / record.allocated_hours
                record.task_remaining_budget = record.task_budget - (record.effective_hours * cost_per_hour)
            else:
                record.task_remaining_budget = record.task_budget

    @api.depends('remaining_hours')
    def _compute_task_timesheet(self):
        for record in self:
            record.task_timesheet = record.remaining_hours == 0
