from odoo import http
from odoo.http import request, Response

class ArticleController(http.Controller):
    
    @http.route('/api/articles', type='json', auth='user')
    def get_articles(self):
        articles = request.env['library.article'].search([])
        data = [{'id': article.id, 'title': article.title} for article in articles]
        return data

    @http.route('/api/articles/<int:id>', type='json', auth='user')
    def get_article(self, id):
        article = request.env['library.article'].browse(id)
        return {'id': article.id, 'title': article.title}

    @http.route('/api/articles', type='json', methods=['POST'], auth='user')
    def create_article(self, **post):
        article = request.env['library.article'].create(post)
        return {'id': article.id, 'title': article.title}

    @http.route('/api/articles/<int:id>', type='json', methods=['PUT'], auth='user')
    def update_article(self, id, **post):
        article = request.env['library.article'].browse(id)
        article.write(post)
        return {'id': article.id, 'title': article.title}

    @http.route('/api/articles/<int:id>', type='json', methods=['DELETE'], auth='user')
    def delete_article(self, id):
        article = request.env['library.article'].browse(id)
        article.unlink()
        return {'status': 'success'}
