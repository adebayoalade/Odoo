from odoo import models, fields, api
from odoo.exceptions import UserError

class LibraryArticle(models.Model):
    _name = 'library.article'
    _description = 'Article Management'
    
    image = fields.Binary("Image")
    author_id = fields.Many2one('res.partner', string='Author')
    title = fields.Char('Title', required=True)
    publish_date = fields.Date('Publish Date')
    start_date = fields.Date('Start Date')
    finished_date = fields.Date('Finished Date')
    deadline = fields.Date('Deadline')
    assigned_to_id = fields.Many2one('res.partner', string='Assigned To')
    content = fields.Text('Content')
    state = fields.Selection(
        [('open', 'Open'), ('reading', 'Reading'), ('read', 'Read'), ('abandoned', 'Abandoned')],
        string='State', default='open'
    )
    
    @api.model
    def create(self, vals):
        article = super(LibraryArticle, self).create(vals)
        self._send_notification(article)
        return article
    
    def write(self, vals):
        res = super(LibraryArticle, self).write(vals)
        if 'state' in vals and vals['state'] == 'read':
            self._send_notification(self)
        return res

    def _send_notification(self, article):
        if article.state == 'read':
            template = self.env.ref('your_module.email_template_article_read')
            self.env['mail.template'].browse(template.id).send_mail(article.id)
