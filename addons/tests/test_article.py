from odoo.tests.common import TransactionCase

class TestLibraryArticle(TransactionCase):

    def test_create_article(self):
        article = self.env['library.article'].create({
            'title': 'Test Article',
            'author_id': self.env.ref('base.partner_admin').id,
            'publish_date': '2024-01-01',
            'deadline': '2024-02-01',
            'assigned_to_id': self.env.ref('base.partner_admin').id,
            'content': 'Test content',
            'state': 'open'
        })
        self.assertEqual(article.title, 'Test Article')

