import unittest
from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

class TestArticle(TransactionCase):

    def setUp(self):
        super(TestArticle, self).setUp()
        self.Article = self.env['article.management.article']
        self.partner1 = self.env.ref('base.res_partner_1')
        self.partner2 = self.env.ref('base.res_partner_2')

    def test_article_creation(self):
        article = self.Article.create({
            'title': 'Test Article',
            'author_id': self.partner1.id,
            'publish_date': '2024-01-01',
            'assigned_to_id': self.partner2.id,
            'content': 'This is a test article.',
            'state': 'open',
        })
        self.assertTrue(article, "Article creation failed")
        self.assertEqual(article.title, 'Test Article', "Article title mismatch")
        self.assertEqual(article.state, 'open', "Article state mismatch")

    def test_article_state_transition(self):
        article = self.Article.create({
            'title': 'Test Article',
            'author_id': self.partner1.id,
            'publish_date': '2024-01-01',
            'assigned_to_id': self.partner2.id,
            'content': 'This is a test article.',
            'state': 'open',
        })
        article.write({'state': 'reading'})
        self.assertEqual(article.state, 'reading', "Failed to change state to reading")
        article.write({'state': 'read'})
        self.assertEqual(article.state, 'read', "Failed to change state to read")
        self.assertTrue(article.finished_date, "Finished date not set")

    def test_article_invalid_dates(self):
        with self.assertRaises(ValidationError):
            self.Article.create({
                'title': 'Invalid Date Article',
                'author_id': self.partner1.id,
                'publish_date': '2024-01-01',
                'start_date': '2024-03-01',
                'deadline': '2024-02-01',
                'assigned_to_id': self.partner2.id,
                'content': 'This article has invalid dates.',
                'state': 'open',
            })
