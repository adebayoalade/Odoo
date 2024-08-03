from odoo import models, fields, api
from odoo.exceptions import UserError


class Article(models.Model):
    _name = 'article.management'
    _description = 'Article Management'

    image = fields.Binary("Image")
    author_id = fields.Many2one('res.partner', string="Author")
    title = fields.Char("Title")
    publish_date = fields.Date("Publish Date")
    start_date = fields.Date("Start Date")
    finished_date = fields.Date("Finished Date")
    deadline = fields.Date("Deadline")
    assigned_to_id = fields.Many2one('res.partner', string="Assigned To")
    content = fields.Text("Content")
    state = fields.Selection([
        ('open', 'Open'),
        ('reading', 'Reading'),
        ('read', 'Read'),
        ('abandoned', 'Abandoned')
    ], string="State", default='open')
    
    @api.model
    def create(self, vals):
        article = super(Article, self).create(vals)
        self._send_notification(article)
        return article
    
    def write(self, vals):
        res = super(Article, self).write(vals)
        if 'state' in vals and vals['state'] == 'read':
            for record in self:
                self._send_notification(record)
        return res

    def _send_notification(self, article):
        if article.state == 'read':
            template = self.env.ref('your_module.email_template_article_read')
            if template:
                template.send_mail(article.id, force_send=True)
                
                


              

