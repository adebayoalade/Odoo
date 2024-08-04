from odoo import http
from odoo.http import request

class ArticleController(http.Controller):
    
    @http.route('/api/articles', type='json', auth='user')
    def get_articles(self):
        articles = request.env['article'].search([])
        data = [{'id': article.id, 'title': article.title} for article in articles]
        return data

    @http.route('/api/article', type='json', auth='user')
    def get_article(self, id):
        article = request.env['article'].browse(id)
        if not article.exists():
            return {'error': 'Article not found'}, 404
        return {'id': article.id, 'title': article.title}

    @http.route('/api/articles/create', type='json', auth='user')
    def create_article(self, post):
        article = request.env['article'].create(post)
        return {'id': article.id, 'title': article.title}

    @http.route('/api/articles/update', type='json', auth='user')
    def update_article(self, id, post):
        article = request.env['article'].browse(id)
        if not article.exists():
            return {'error': 'Article not found'}, 404
        article.write(post)
        return {'id': article.id, 'title': article.title}

    @http.route('/api/articles/delete', type='json', auth='user')
    def delete_article(self, id):
        article = request.env['article'].browse(id)
        if not article.exists():
            return {'error': 'Article not found'}, 404
        article.unlink()
        return {'status': 'success'}
